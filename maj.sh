#!/bin/bash
# Met à jour le numéro de version CSS/JS (pour que le navigateur recharge vraiment),
# régénère les pages, puis commit et push.   Usage :  ./maj.sh "message du commit"
cd "$(dirname "$0")" || exit 1
V=$(date +%Y%m%d-%H%M)
sed -i '' "s/^V = \".*\"/V = \"$V\"/" build.py
python3 build.py || exit 1
git add -A && git commit -q -m "${1:-mise à jour du site}" && echo "commit : $(git log --oneline -1)"
git remote get-url origin >/dev/null 2>&1 && git push -q origin main && echo "poussé"
