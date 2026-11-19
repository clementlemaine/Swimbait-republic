/* Swimbait Republic — interactions & scroll
   - défilement fluide (Lenis) + animations au scroll (GSAP ScrollTrigger)
   - tout reste lisible si les librairies ne chargent pas (repli IntersectionObserver)
*/
(function () {
  "use strict";
  var doc = document.documentElement;
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduced) doc.classList.add("reduced");
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  // ------------------------------------------------ page transition (curtain)
  var curtain = $(".curtain");
  function curtainOut() { if (curtain) { curtain.classList.remove("is-in", "is-gone"); curtain.classList.add("is-out"); } }
  window.addEventListener("pageshow", function () { requestAnimationFrame(curtainOut); });
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest("a[href]");
    if (ev.defaultPrevented || !a || !curtain || reduced) return;
    var href = a.getAttribute("href");
    if (!href || href.charAt(0) === "#" || a.target === "_blank" || /^(mailto:|tel:|https?:)/.test(href) || ev.metaKey || ev.ctrlKey || ev.shiftKey) return;
    if (href.split("#")[0] === "") return;
    ev.preventDefault();
    curtain.classList.add("is-gone");
    curtain.classList.remove("is-out");
    void curtain.offsetWidth;
    curtain.classList.remove("is-gone");
    curtain.classList.add("is-in");
    setTimeout(function () { window.location.href = href; }, 400);
  });

  // ------------------------------------------------ split headings into words
  $$("[data-split]").forEach(function (el) {
    var html = el.innerHTML.split(/<br\s*\/?>/i);
    el.innerHTML = html.map(function (line) {
      return line.trim().split(/\s+/).map(function (w) { return '<span class="w"><span>' + w + "</span></span>"; }).join(" ");
    }).join("<br>");
  });

  // ------------------------------------------------ nav + menu
  var nav = $("#nav"), burger = $(".burger"), menu = $("#menu");
  if (burger && menu) {
    burger.addEventListener("click", function () {
      var open = burger.getAttribute("aria-expanded") !== "true";
      burger.setAttribute("aria-expanded", String(open));
      if (open) { menu.hidden = false; requestAnimationFrame(function () { menu.classList.add("is-open"); }); }
      else { menu.classList.remove("is-open"); setTimeout(function () { menu.hidden = true; }, 500); }
      if (window.__lenis) open ? window.__lenis.stop() : window.__lenis.start();
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && menu.classList.contains("is-open")) burger.click(); });
  }

  // ------------------------------------------------ progress bar
  var bar = $(".progress span");
  function onScrollProgress(y) {
    if (!bar) return;
    var max = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.transform = "scaleX(" + (max > 0 ? Math.min(1, y / max) : 0) + ")";
  }

  // ------------------------------------------------ hero video: pause once fully covered
  var heroVideo = $(".hero-video");
  function onScrollHero(y) {
    if (!heroVideo) return;
    var covered = y > window.innerHeight * 1.3;
    if (covered && !heroVideo.paused) heroVideo.pause();
    else if (!covered && heroVideo.paused && !reduced) { var p = heroVideo.play(); if (p && p.catch) p.catch(function () {}); }
  }

  // ------------------------------------------------ counters
  function countUp(el) {
    if (el.dataset.done) return; el.dataset.done = "1";
    var raw = el.dataset.count, target = parseFloat(raw);
    if (isNaN(target) || /[–']/.test(raw) || reduced) return;
    var dec = (raw.split(".")[1] || "").length, t0 = null, dur = 1300;
    function step(t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / dur), ee = 1 - Math.pow(1 - k, 3);
      el.textContent = (target * ee).toFixed(dec);
      if (k < 1) requestAnimationFrame(step); else el.textContent = raw;
    }
    el.textContent = (0).toFixed(dec);
    requestAnimationFrame(step);
  }

  // ------------------------------------------------ depth modules (Lead Stickers)
  $$("[data-depth-module]").forEach(function (mod) {
    var lure = $(".depth-lure", mod), tag = $(".depth-tag", mod), btns = $$(".depth-btn", mod);
    function set(i, user) {
      btns.forEach(function (x, j) { x.classList.toggle("is-on", j === i); x.setAttribute("aria-pressed", String(j === i)); });
      lure.setAttribute("data-state", String(i));
      tag.textContent = $("strong", btns[i]).textContent;
      if (user) mod.dataset.touched = "1";
    }
    btns.forEach(function (b, i) { b.addEventListener("click", function () { set(i, true); }); });
    mod._set = function (i) { if (!mod.dataset.touched && !btns[i].classList.contains("is-on")) set(i, false); };
  });

  // ------------------------------------------------ range tabs (126 / 176 / 236)
  var range = $("[data-range]");
  if (range) {
    var tabs = $$(".rtab", range), panels = $$(".rpanel", range);
    function selectTab(k, focus) {
      tabs.forEach(function (t) {
        var on = t.dataset.k === k;
        t.classList.toggle("is-on", on); t.setAttribute("aria-selected", String(on)); t.tabIndex = on ? 0 : -1;
        if (on && focus) t.focus();
      });
      panels.forEach(function (p) { p.hidden = p.dataset.k !== k; });
    }
    tabs.forEach(function (t, i) {
      t.tabIndex = t.classList.contains("is-on") ? 0 : -1;
      t.addEventListener("click", function () { selectTab(t.dataset.k); t.parentNode.classList.add("touched"); });
      t.addEventListener("keydown", function (e) {
        var d = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
        if (d) { e.preventDefault(); selectTab(tabs[(i + d + tabs.length) % tabs.length].dataset.k, true); }
      });
    });
  }

  // ------------------------------------------------ colour carousel (home)
  var cv = $("[data-colours]");
  if (cv) {
    var data = JSON.parse($(".colours-data", cv).textContent);
    var strip = $(".cv-strip", cv), img = $(".cv-img", cv), nameEl = $(".cv-name", cv), ghost = $(".cv-ghost", cv);
    var modelEl = $(".cv-model", cv), countEl = $(".cv-count", cv), link = $(".cv-link", cv);
    var model = "176", current = -1, items = [], raf = null;
    var linkBase = link ? link.getAttribute("href").replace(/glideway-\d+/, "glideway-{k}") : "";

    function show(i) {
      if (i === current || !data[model][i]) return;
      current = i;
      var c = data[model][i];
      items.forEach(function (it, j) { it.classList.toggle("is-on", j === i); it.setAttribute("aria-pressed", String(j === i)); });
      img.classList.add("swap");
      var pre = new Image();
      pre.onload = pre.onerror = function () {
        setTimeout(function () { img.src = c[0]; img.alt = "Glideway " + model + " — " + c[1]; img.classList.remove("swap"); }, 150);
      };
      pre.src = c[0];
      nameEl.textContent = c[1]; ghost.textContent = c[1];
      countEl.textContent = (i + 1) + " / " + data[model].length;
    }
    function center(i, smooth) {
      var it = items[i]; if (!it) return;
      strip.scrollTo({ left: it.offsetLeft - (strip.clientWidth - it.offsetWidth) / 2, behavior: smooth ? "smooth" : "auto" });
    }
    function paint() {
      raf = null;
      var mid = strip.scrollLeft + strip.clientWidth / 2, best = 0, bestD = 1e9;
      items.forEach(function (it, j) {
        var c = it.offsetLeft + it.offsetWidth / 2, d = Math.abs(c - mid);
        var k = Math.max(0, 1 - d / (strip.clientWidth * 0.45));
        it.style.setProperty("--s", (0.72 + k * 0.5).toFixed(3));
        it.style.setProperty("--o", (0.35 + k * 0.65).toFixed(3));
        if (d < bestD) { bestD = d; best = j; }
      });
      show(best);
    }
    function build(m) {
      model = m; current = -1;
      strip.innerHTML = "";
      items = data[m].map(function (c, i) {
        var b = document.createElement("button");
        b.className = "cv-item"; b.type = "button";
        b.innerHTML = '<img src="' + c[0] + '" alt="" loading="lazy"><span>' + c[1] + "</span>";
        b.addEventListener("click", function () { if (!strip.dataset.moved) center(i, true); });
        strip.appendChild(b);
        return b;
      });
      modelEl.textContent = "Glideway " + m;
      if (link) link.setAttribute("href", linkBase.replace("{k}", m));
      var start = Math.min(3, items.length - 1);
      requestAnimationFrame(function () { center(start, false); paint(); });
    }
    strip.addEventListener("scroll", function () { if (!raf) raf = requestAnimationFrame(paint); }, { passive: true });
    $(".cv-prev", cv).addEventListener("click", function () { center(Math.max(0, current - 1), true); });
    $(".cv-next", cv).addEventListener("click", function () { center(Math.min(items.length - 1, current + 1), true); });
    strip.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { e.preventDefault(); center(Math.min(items.length - 1, current + 1), true); }
      if (e.key === "ArrowLeft") { e.preventDefault(); center(Math.max(0, current - 1), true); }
    });
    // drag with the mouse
    var drag = null;
    strip.addEventListener("pointerdown", function (e) {
      if (e.pointerType !== "mouse") return;
      drag = { x: e.clientX, left: strip.scrollLeft }; delete strip.dataset.moved;
    });
    window.addEventListener("pointermove", function (e) {
      if (!drag) return;
      var dx = e.clientX - drag.x;
      if (Math.abs(dx) > 4) { strip.dataset.moved = "1"; strip.classList.add("dragging"); }
      strip.scrollLeft = drag.left - dx;
    });
    window.addEventListener("pointerup", function () {
      if (!drag) return;
      drag = null; strip.classList.remove("dragging");
      if (strip.dataset.moved) { center(current, true); setTimeout(function () { delete strip.dataset.moved; }, 50); }
    });
    // stop Lenis from hijacking horizontal wheel/trackpad in the strip
    strip.setAttribute("data-lenis-prevent", "");
    $$(".ctab", cv).forEach(function (t) {
      t.addEventListener("click", function () {
        $$(".ctab", cv).forEach(function (x) { x.classList.toggle("is-on", x === t); x.setAttribute("aria-pressed", String(x === t)); });
        build(t.dataset.model);
      });
    });
    build(model);
    window.addEventListener("resize", function () { center(current, false); });
  }


  // ------------------------------------------------ product views (side / front / other side / top / bottom / back)
  $$("[data-views]").forEach(function (box) {
    var vtabs = $$(".vtab", box), views = $$(".view", box);
    function pick(key, focus) {
      vtabs.forEach(function (b) { var on = b.dataset.view === key; b.classList.toggle("is-on", on); b.setAttribute("aria-selected", String(on)); b.tabIndex = on ? 0 : -1; if (on && focus) b.focus(); });
      views.forEach(function (v) { v.hidden = v.dataset.view !== key; });
    }
    vtabs.forEach(function (b, i) {
      b.tabIndex = i === 0 ? 0 : -1;
      b.addEventListener("click", function () { pick(b.dataset.view); });
      b.addEventListener("keydown", function (e) {
        var d = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
        if (d) { e.preventDefault(); pick(vtabs[(i + d + vtabs.length) % vtabs.length].dataset.view, true); }
      });
    });
  });

  // ------------------------------------------------ colour charts (product pages)
  $$(".swatches").forEach(function (list) {
    var scope = list.closest("section");
    var vimg = $(".viewer-img", scope), vname = $(".viewer-name", scope);
    if (!vimg) return;
    $$(".swatch", list).forEach(function (s) {
      s.addEventListener("click", function () {
        $$(".swatch", list).forEach(function (x) { x.classList.remove("is-on"); x.setAttribute("aria-pressed", "false"); });
        s.classList.add("is-on"); s.setAttribute("aria-pressed", "true");
        vimg.classList.add("swap");
        var pre = new Image();
        pre.onload = pre.onerror = function () {
          setTimeout(function () {
            vimg.src = s.dataset.src;
            vimg.alt = (vimg.alt.split(" — ")[0] || "") + " — " + s.dataset.name;
            vname.textContent = s.dataset.name;
            vimg.classList.remove("swap");
          }, 160);
        };
        pre.src = s.dataset.src;
        if (scope.id === "colours") {
          var hero = $(".pd-lure img"); if (hero) hero.src = s.dataset.src;
          var th = $('.vtab[data-view="profil"] .vtab-thumb img'); if (th) th.src = s.dataset.src;
          var dl = $(".depth-lure img"); if (dl) dl.src = s.dataset.src;
        }
      });
    });
  });

  // ------------------------------------------------ films
  $$(".film").forEach(function (f) {
    var v = $("video", f), b = $(".film-play", f);
    if (!v || !b) return;
    b.addEventListener("click", function () {
      v.controls = true; v.muted = false;
      var p = v.play(); if (p && p.catch) p.catch(function () {});
      f.classList.add("is-playing");
    });
  });

  // ------------------------------------------------ contact form (prototype)
  var form = $(".cform");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var msg = $(".form-msg", form);
    if (!form.checkValidity()) { msg.textContent = form.dataset.msgBad; return; }
    msg.textContent = form.dataset.msgOk;
    form.reset();
  });


  // ------------------------------------------------ mobile preview (desktop only, not inside the preview itself)
  var mp = $("[data-mprev]");
  if (mp && window.self === window.top && window.innerWidth > 900) {
    mp.hidden = false;
    var mpBtn = $(".mprev-btn", mp), mpFrame = $("iframe", mp);
    function fit() {
      var s = Math.min(0.8, Math.max(0.5, (window.innerHeight - 130) / 866));
      mp.style.setProperty("--ms", s.toFixed(3));
    }
    mpBtn.addEventListener("click", function () {
      var open = !mp.classList.contains("is-open");
      mp.classList.toggle("is-open", open);
      mpBtn.setAttribute("aria-expanded", String(open));
      if (open) { fit(); if (!mpFrame.src) mpFrame.src = window.location.pathname.split("/").pop() || "index.html"; }
    });
    window.addEventListener("resize", fit);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && mp.classList.contains("is-open")) mpBtn.click(); });
  } else if (mp && window.self !== window.top) {
    mp.remove();
  }


  // ------------------------------------------------ "Volver" button on product pages
  $$("[data-back]").forEach(function (b) {
    b.addEventListener("click", function (e) {
      var fromSite = document.referrer && document.referrer.indexOf(location.host) !== -1;
      if (fromSite && history.length > 1) { e.preventDefault(); history.back(); }
    });
  });

  // ------------------------------------------------ main scroll loop
  function onScroll(y) { onScrollProgress(y); onScrollHero(y); }

  // ------------------------------------------------ boot
  function boot() {
    var hasGsap = window.gsap && window.ScrollTrigger;
    if (window.Lenis && !reduced) {
      var lenis = new window.Lenis({ duration: 1.1, easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); }, smoothWheel: true });
      window.__lenis = lenis;
      lenis.on("scroll", function (ev) { onScroll(ev.scroll); if (hasGsap) window.ScrollTrigger.update(); });
      if (hasGsap) { window.gsap.ticker.add(function (t) { lenis.raf(t * 1000); }); window.gsap.ticker.lagSmoothing(0); }
      else { (function raf(t) { lenis.raf(t); requestAnimationFrame(raf); })(0); }
      $$('a[href^="#"]').forEach(function (a) {
        a.addEventListener("click", function (e) {
          var id = a.getAttribute("href"); if (id.length < 2) return;
          var t = $(id); if (!t) return;
          e.preventDefault(); lenis.scrollTo(t, { offset: -72 });
        });
      });
    } else {
      window.addEventListener("scroll", function () { onScroll(window.scrollY); }, { passive: true });
    }
    // reload -> top of the page ; coming back (browser back or our "Volver" button) -> exactly where you were
    var KEY = "sr-pos:" + location.pathname;
    var navType = (performance.getEntriesByType && performance.getEntriesByType("navigation")[0] || {}).type;
    var saved = null;
    try { saved = JSON.parse(sessionStorage.getItem(KEY) || "null"); } catch (e) {}
    function goTo(y) { window.scrollTo(0, y); if (window.__lenis) window.__lenis.scrollTo(y, { immediate: true, force: true }); }
    if (navType === "back_forward" && saved) {
      if (saved.tab) { var tb = $('.rtab[data-k="' + saved.tab + '"]'); if (tb) tb.click(); }
      if (saved.model) { var cb = $('.ctab[data-model="' + saved.model + '"]'); if (cb && !cb.classList.contains("is-on")) cb.click(); }
      requestAnimationFrame(function () { goTo(saved.y); setTimeout(function () { goTo(saved.y); if (window.ScrollTrigger) window.ScrollTrigger.refresh(); }, 350); });
    } else {
      goTo(0);
    }
    function savePos() {
      var on = $(".rtab.is-on"), cm = $(".ctab.is-on");
      try { sessionStorage.setItem(KEY, JSON.stringify({ y: window.__lenis ? window.__lenis.scroll : window.scrollY, tab: on && on.dataset.k, model: cm && cm.dataset.model })); } catch (e) {}
    }
    window.addEventListener("pagehide", savePos);
    document.addEventListener("click", function (ev) { if (ev.target.closest && ev.target.closest("a[href]")) savePos(); }, true);
    onScroll(window.scrollY);
    if (hasGsap && !reduced) animateWithGsap(); else fallbackReveal();
  }

  function fallbackReveal() {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.style.transition = "opacity .8s ease, transform .8s ease";
        en.target.style.opacity = 1; en.target.style.transform = "none";
        $$("[data-count]", en.target).concat(en.target.matches("[data-count]") ? [en.target] : []).forEach(countUp);
        io.unobserve(en.target);
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    $$("[data-reveal], [data-count]").forEach(function (el) { io.observe(el); });
  }

  function animateWithGsap() {
    var gsap = window.gsap, ST = window.ScrollTrigger;
    gsap.registerPlugin(ST);

    ST.batch("[data-reveal]", {
      start: "top 90%",
      onEnter: function (els) {
        gsap.to(els, { opacity: 1, y: 0, duration: 0.9, ease: "power3.out", stagger: 0.07, overwrite: true });
        els.forEach(function (el) { $$("[data-count]", el).forEach(countUp); });
      }
    });
    $$("[data-split]").forEach(function (el) {
      var inHero = el.closest(".hero, .phero, .pd-hero");
      gsap.from($$(".w > span", el), {
        yPercent: 110, duration: 1, ease: "power4.out", stagger: 0.06, delay: inHero ? 0.3 : 0,
        scrollTrigger: inHero ? null : { trigger: el, start: "top 88%" }
      });
    });
    $$("[data-count]").forEach(function (el) {
      if (!el.closest("[data-reveal]")) ST.create({ trigger: el, start: "top 85%", once: true, onEnter: function () { countUp(el); } });
    });

    // HOME — transition: the range panel slides over the video, the real Glideway crosses on its edge
    var hero = $("[data-hero]");
    if (hero) {
      gsap.from(".hero-eyebrow, .hero .lede, .hero-ctas, .hero-cats", { opacity: 0, y: 24, duration: 1, delay: 0.5, ease: "power3.out", stagger: 0.1 });
      var rangeSec = $("[data-range]");
      gsap.to(".hero-shade", { opacity: 0.65, ease: "none", scrollTrigger: { trigger: rangeSec, start: "top bottom", end: "top top", scrub: true } });
      gsap.to(".hero-inner", { yPercent: -12, opacity: 0.3, ease: "none", scrollTrigger: { trigger: rangeSec, start: "top bottom", end: "top 20%", scrub: true } });
      gsap.to(".hero-media", { scale: 1.08, ease: "none", scrollTrigger: { trigger: rangeSec, start: "top bottom", end: "top top", scrub: true } });
      var rider = $(".rider");
      if (rider) {
        ST.create({
          trigger: rangeSec, start: "top bottom", end: "top 5%", scrub: 0.4,
          onUpdate: function (s) {
            var p = s.progress, vw = window.innerWidth, w = rider.offsetWidth;
            var x = -w * 1.1 + p * (vw + w * 1.3);
            var rot = Math.sin(p * Math.PI * 4) * 7;          // side-to-side glide while it crosses
            var y = Math.sin(p * Math.PI * 4) * 10;
            rider.style.transform = "translate(" + x + "px, calc(-62% + " + y + "px)) rotate(" + rot + "deg)";
          }
        });
      }
      // product cards rise in
      gsap.from(".pcard", { y: 50, opacity: 0, duration: 1, ease: "power3.out", stagger: 0.1, scrollTrigger: { trigger: ".pcards", start: "top 85%" } });
    }

    $$("[data-parallax]").forEach(function (el) {
      gsap.to(el, { yPercent: 12, ease: "none", scrollTrigger: { trigger: el.parentNode, start: "top top", end: "bottom top", scrub: true } });
    });
    $$("[data-parallax-img]").forEach(function (im) {
      gsap.fromTo(im, { yPercent: -8 }, { yPercent: 0, ease: "none", scrollTrigger: { trigger: im.parentNode, start: "top bottom", end: "bottom top", scrub: true } });
    });

    var pdl = $(".pd-lure img");
    if (pdl) gsap.from(pdl, { xPercent: -60, rotate: -12, opacity: 0, duration: 1.5, ease: "power3.out", delay: 0.2 });
    $$("[data-float]").forEach(function (im) {
      gsap.fromTo(im, { xPercent: -25, rotate: -8, opacity: 0 }, { xPercent: 0, rotate: 0, opacity: 1, duration: 1.3, ease: "power3.out", scrollTrigger: { trigger: im, start: "top 85%" } });
    });

    // depth tanks sink with the scroll until the visitor clicks
    $$("[data-depth-module]").forEach(function (mod) {
      ST.create({ trigger: mod, start: "top 65%", end: "bottom 35%",
        onUpdate: function (s) { if (mod._set && mod.offsetParent) mod._set(s.progress < 0.34 ? 0 : s.progress < 0.67 ? 1 : 2); } });
    });

    var rod = $("[data-rod]");
    if (rod) gsap.fromTo(rod, { xPercent: -6 }, { xPercent: 6, ease: "none", scrollTrigger: { trigger: rod, start: "top bottom", end: "bottom top", scrub: true } });

    window.addEventListener("load", function () { ST.refresh(); });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
