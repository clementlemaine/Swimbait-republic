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
    if (!a || !curtain || reduced) return;
    var href = a.getAttribute("href");
    if (!href || href.charAt(0) === "#" || a.target === "_blank" || /^(mailto:|tel:|https?:)/.test(href) || ev.metaKey || ev.ctrlKey || ev.shiftKey) return;
    if (href.split("#")[0] === "" ) return;
    ev.preventDefault();
    curtain.classList.add("is-gone");
    curtain.classList.remove("is-out");
    void curtain.offsetWidth;
    curtain.classList.remove("is-gone");
    curtain.classList.add("is-in");
    setTimeout(function () { window.location.href = href; }, 420);
  });

  // ------------------------------------------------ split headings into words
  $$("[data-split]").forEach(function (el) {
    var html = el.innerHTML.split(/<br\s*\/?>/i);
    el.innerHTML = html.map(function (line) {
      return line.trim().split(/\s+/).map(function (w) { return '<span class="w"><span>' + w + "</span></span>"; }).join(" ");
    }).join("<br>");
  });
  // words that light up with scroll (manifesto, product lede)
  $$("[data-words]").forEach(function (el) {
    el.innerHTML = el.textContent.trim().split(/\s+/).map(function (w) { return '<span class="mw">' + w + "</span>"; }).join(" ");
  });

  // ------------------------------------------------ nav + menu
  var nav = $("#nav"), burger = $(".burger"), menu = $("#menu");
  var lastY = 0;
  function onScrollNav(y) {
    if (!nav) return;
    nav.classList.toggle("is-solid", y > 40);
    var menuOpen = menu && menu.classList.contains("is-open");
    lastY = y;
  }
  if (burger && menu) {
    burger.addEventListener("click", function () {
      var open = burger.getAttribute("aria-expanded") !== "true";
      burger.setAttribute("aria-expanded", String(open));
      burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      if (open) { menu.hidden = false; requestAnimationFrame(function () { menu.classList.add("is-open"); }); }
      else { menu.classList.remove("is-open"); setTimeout(function () { menu.hidden = true; }, 600); }
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

  // ------------------------------------------------ word highlight on scroll
  var wordBlocks = $$("[data-words]");
  function onScrollWords() {
    var vh = window.innerHeight;
    wordBlocks.forEach(function (el) {
      var r = el.getBoundingClientRect();
      var p = (vh * 0.85 - r.top) / (r.height + vh * 0.35);
      p = Math.max(0, Math.min(1, p));
      var words = el.children, n = Math.round(p * words.length);
      for (var i = 0; i < words.length; i++) words[i].classList.toggle("on", i < n);
    });
  }

  // ------------------------------------------------ glide scene (home)
  var glide = $("[data-glide]");
  var glideLure = glide && $(".glide-lure", glide);
  var glideWords = glide ? $$(".glide-list span", glide) : [];
  function onScrollGlide() {
    if (!glide || !glideLure) return;
    var r = glide.getBoundingClientRect();
    var total = r.height - window.innerHeight;
    var p = Math.max(0, Math.min(1, -r.top / total));
    var vw = window.innerWidth, lw = glideLure.offsetWidth;
    var x = -lw + p * (vw + lw * 2) - lw * 0.5;
    // the S-curve of a glide bait: alternating headings while it crosses
    var phase = p * Math.PI * 5;
    var rot = Math.sin(phase) * 16;
    var y = Math.sin(phase) * 30;
    glideLure.style.transform = "translate(" + x + "px, calc(-50% + " + y + "px)) rotate(" + rot + "deg)";
    var n = Math.floor(p * (glideWords.length + 0.6));
    glideWords.forEach(function (w, i) { w.classList.toggle("on", i < n); w.classList.toggle("cur", i === n - 1); });
  }

  // ------------------------------------------------ counters
  function countUp(el) {
    if (el.dataset.done) return; el.dataset.done = "1";
    var raw = el.dataset.count;
    var target = parseFloat(raw);
    if (isNaN(target) || /[–']/.test(raw) || reduced) return;
    var dec = (raw.split(".")[1] || "").length, t0 = null, dur = 1400;
    function step(t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = (target * e).toFixed(dec);
      if (k < 1) requestAnimationFrame(step); else el.textContent = raw;
    }
    el.textContent = (0).toFixed(dec);
    requestAnimationFrame(step);
  }

  // ------------------------------------------------ depth module
  $$("[data-depth-module]").forEach(function (mod) {
    var lure = $(".depth-lure", mod), tag = $(".depth-tag", mod), btns = $$(".depth-btn", mod);
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        btns.forEach(function (x) { x.classList.remove("is-on"); x.setAttribute("aria-pressed", "false"); });
        b.classList.add("is-on"); b.setAttribute("aria-pressed", "true");
        lure.setAttribute("data-state", b.dataset.depth);
        tag.textContent = $("strong", b).textContent;
        mod.dataset.touched = "1";
      });
    });
    mod._set = function (i) { if (!mod.dataset.touched && btns[i] && !btns[i].classList.contains("is-on")) { btns[i].click(); delete mod.dataset.touched; } };
  });

  // ------------------------------------------------ colour viewers
  $$(".swatches").forEach(function (list) {
    var scope = list.closest("section");
    var img = $(".viewer-img", scope), name = $(".viewer-name", scope);
    if (!img) return;
    $$(".swatch", list).forEach(function (s) {
      s.addEventListener("click", function () {
        $$(".swatch", list).forEach(function (x) { x.classList.remove("is-on"); x.setAttribute("aria-pressed", "false"); });
        s.classList.add("is-on"); s.setAttribute("aria-pressed", "true");
        img.classList.add("swap");
        var next = new Image();
        next.onload = next.onerror = function () {
          setTimeout(function () {
            img.src = s.dataset.src;
            img.alt = (img.alt.split(" — ")[0] || "") + " — " + s.dataset.name;
            name.textContent = s.dataset.name;
            img.classList.remove("swap");
          }, 180);
        };
        next.src = s.dataset.src;
        // also update the product hero lure so the choice follows you
        var hero = $(".pd-lure img");
        if (hero && scope.id === "colours") hero.src = s.dataset.src;
        var dl = $(".depth-lure img");
        if (dl && scope.id === "colours") dl.src = s.dataset.src;
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
    v.addEventListener("pause", function () { if (v.currentTime < 0.2) f.classList.remove("is-playing"); });
  });

  // ------------------------------------------------ contact form (prototype)
  var form = $(".cform");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var msg = $(".form-msg", form);
    if (!form.checkValidity()) { msg.textContent = "Please fill in your name, a valid email and your message."; return; }
    msg.textContent = "Thanks! (Prototype: the form still has to be connected to Swimbait Republic's mailbox.)";
    form.reset();
  });

  // ------------------------------------------------ parade rows: speed follows scroll
  var parade = $$(".parade-track");
  var paradeX = [0, 0], velocity = 0;
  function tickParade() {
    parade.forEach(function (t, i) {
      var dir = parseInt(t.parentNode.dataset.dir, 10) || 1;
      var half = t.scrollWidth / 2;
      paradeX[i] = (paradeX[i] - (0.45 + Math.min(Math.abs(velocity) * 0.08, 6)) * dir);
      if (paradeX[i] <= -half) paradeX[i] += half;
      if (paradeX[i] > 0) paradeX[i] -= half;
      t.style.transform = "translate3d(" + paradeX[i] + "px,0,0)";
    });
    velocity *= 0.92;
    requestAnimationFrame(tickParade);
  }
  if (parade.length && !reduced) requestAnimationFrame(tickParade);

  // ------------------------------------------------ main scroll loop
  function onScroll(y) {
    onScrollNav(y); onScrollProgress(y); onScrollWords(); onScrollGlide();
  }

  // ------------------------------------------------ boot
  function boot() {
    var hasGsap = window.gsap && window.ScrollTrigger;
    var lenis = null;
    if (window.Lenis && !reduced) {
      lenis = new window.Lenis({ duration: 1.15, easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); }, smoothWheel: true });
      window.__lenis = lenis;
      lenis.on("scroll", function (e) { velocity = e.velocity || 0; onScroll(e.scroll); if (hasGsap) window.ScrollTrigger.update(); });
      if (hasGsap) {
        window.gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
        window.gsap.ticker.lagSmoothing(0);
      } else {
        (function raf(t) { lenis.raf(t); requestAnimationFrame(raf); })(0);
      }
      // anchor links through Lenis
      $$('a[href^="#"]').forEach(function (a) {
        a.addEventListener("click", function (e) {
          var id = a.getAttribute("href"); if (id.length < 2) return;
          var t = $(id); if (!t) return;
          e.preventDefault(); lenis.scrollTo(t, { offset: -60 });
        });
      });
    } else {
      window.addEventListener("scroll", function () { onScroll(window.scrollY); }, { passive: true });
    }
    onScroll(window.scrollY);
    window.addEventListener("resize", function () { onScroll(window.scrollY); });

    if (hasGsap && !reduced) animateWithGsap(); else fallbackReveal();
  }

  function fallbackReveal() {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.style.transition = "opacity .9s cubic-bezier(.2,.7,.1,1), transform .9s cubic-bezier(.2,.7,.1,1)";
        en.target.style.opacity = 1; en.target.style.transform = "none";
        $$("[data-count]", en.target).concat(en.target.matches("[data-count]") ? [en.target] : []).forEach(countUp);
        io.unobserve(en.target);
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    $$("[data-reveal]").forEach(function (el) { io.observe(el); });
    $$("[data-count]").forEach(function (el) { io.observe(el); });
  }

  function animateWithGsap() {
    var gsap = window.gsap, ST = window.ScrollTrigger;
    gsap.registerPlugin(ST);

    // reveals
    ST.batch("[data-reveal]", {
      start: "top 90%",
      onEnter: function (els) {
        gsap.to(els, { opacity: 1, y: 0, duration: 1, ease: "power3.out", stagger: 0.08, overwrite: true });
        els.forEach(function (el) { $$("[data-count]", el).forEach(countUp); });
      }
    });
    // split headings: words rise from a mask
    $$("[data-split]").forEach(function (el) {
      var words = $$(".w > span", el);
      var inHero = el.closest(".hero, .phero, .pd-hero");
      gsap.from(words, {
        yPercent: 110, duration: inHero ? 1.2 : 1, ease: "power4.out", stagger: 0.06, delay: inHero ? 0.35 : 0,
        scrollTrigger: inHero ? null : { trigger: el, start: "top 88%" }
      });
    });
    $$("[data-count]").forEach(function (el) {
      if (!el.closest("[data-reveal]")) ST.create({ trigger: el, start: "top 85%", once: true, onEnter: function () { countUp(el); } });
    });

    // home hero: video frame shrinks into a card, title drifts up
    var hero = $("[data-hero]");
    if (hero) {
      gsap.from(".hero-eyebrow, .hero .lede, .hero-ctas", { opacity: 0, y: 24, duration: 1, delay: 0.6, ease: "power3.out", stagger: 0.1 });
      gsap.to(".hero-media", { yPercent: 18, ease: "none", scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true } });
    }

    // inner heroes: parallax background
    $$("[data-parallax]").forEach(function (el) {
      gsap.to(el, { yPercent: 12, ease: "none", scrollTrigger: { trigger: el.parentNode, start: "top top", end: "bottom top", scrub: true } });
    });
    $$("[data-parallax-img]").forEach(function (img) {
      gsap.fromTo(img, { yPercent: -8 }, { yPercent: 0, ease: "none", scrollTrigger: { trigger: img.parentNode, start: "top bottom", end: "bottom top", scrub: true } });
    });
    // image reveal: clip from bottom
    $$(".ph-clip").forEach(function (c) {
      gsap.from(c, { clipPath: "inset(100% 0 0 0)", duration: 1.3, ease: "power4.inOut", scrollTrigger: { trigger: c, start: "top 85%" } });
    });

    // product hero: lure swims in, ghost number drifts
    var pdl = $(".pd-lure img");
    if (pdl) {
      gsap.from(pdl, { xPercent: -60, rotate: -12, opacity: 0, duration: 1.6, ease: "power3.out", delay: 0.3 });
      gsap.to(".pd-lure", { yPercent: 12, ease: "none", scrollTrigger: { trigger: ".pd-hero", start: "top top", end: "bottom top", scrub: true } });
    }
    // swimbaits list: lures float into place
    $$("[data-float]").forEach(function (img) {
      gsap.fromTo(img, { xPercent: -25, rotate: -8, opacity: 0 }, { xPercent: 0, rotate: 0, opacity: 1, duration: 1.4, ease: "power3.out", scrollTrigger: { trigger: img, start: "top 85%" } });
    });
    // family to scale: each lure swims in from the left
    $$(".fam-lure img").forEach(function (img, i) {
      gsap.from(img, { x: -120, opacity: 0, duration: 1.3, ease: "power3.out", delay: i * 0.08, scrollTrigger: { trigger: img, start: "top 88%" } });
    });

    // depth module (home + product pages): sinks with the scroll until the user clicks
    $$("[data-depth-module]").forEach(function (mod) {
      ST.create({
        trigger: mod, start: "top 60%", end: "bottom 40%",
        onUpdate: function (s) { if (mod._set) mod._set(s.progress < 0.34 ? 0 : s.progress < 0.67 ? 1 : 2); }
      });
    });

    // rod strip slides with scroll
    var rod = $("[data-rod]");
    if (rod) gsap.fromTo(rod, { xPercent: -8 }, { xPercent: 8, ease: "none", scrollTrigger: { trigger: rod, start: "top bottom", end: "bottom top", scrub: true } });

    // process: horizontal scroll pinned (desktop)
    var proc = $("[data-hscroll]");
    if (proc) {
      ST.matchMedia({
        "(min-width: 901px)": function () {
          var track = $(".process-track", proc);
          var view = $(".process-view", proc);
          var dist = function () { return Math.max(0, track.scrollWidth - view.clientWidth); };
          gsap.to(track, {
            x: function () { return -dist(); }, ease: "none",
            scrollTrigger: { trigger: proc, start: "top top", end: function () { return "+=" + dist(); }, pin: ".process-pin", scrub: 0.6, invalidateOnRefresh: true }
          });
        }
      });
    }

    // footer giant word

    window.addEventListener("load", function () { ST.refresh(); });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
