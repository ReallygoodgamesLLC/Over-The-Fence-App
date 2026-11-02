#!/usr/bin/env python3
"""Turn the game page (game-source.html) into the offline page the iOS app loads.

Run this whenever game-source.html changes:  python3 build_web.py
It swaps the internet-only bits (three.js from a CDN, Google Fonts) for the copies
bundled in OverTheFence/www, and adds the phone viewport settings.
"""
import pathlib, sys
root = pathlib.Path(__file__).resolve().parent
src = (root / "game-source.html").read_text(encoding="utf-8")
CDN = "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lilita+One&family=Fredoka:wght@500;600;700&display=swap">'
PRE = '<link rel="preconnect" href="https://fonts.googleapis.com">'
for needle in (CDN, FONTS):
    if needle not in src:
        sys.exit(f"build_web.py: expected to find {needle[:60]}... in game-source.html")
src = src.replace(CDN, "three.min.js").replace(FONTS, '<link rel="stylesheet" href="fonts/fonts.css">').replace(PRE, "")
if "__otf" in src:
    sys.exit("build_web.py: game-source.html still has test hooks (__otf) in it")
head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">\n'
        '<meta name="format-detection" content="telephone=no">\n'
        # the artifact page this game was built in hides [hidden] elements for it; do the same here
        '<style>[hidden]{display:none!important}body{margin:0}</style>\n</head>\n<body>\n')
(root / "OverTheFence/www/index.html").write_text(head + src + "\n</body>\n</html>\n", encoding="utf-8")
print("Wrote OverTheFence/www/index.html")
