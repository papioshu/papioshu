"""Rebuild assets/paperhand-mark.png and assets/paperhand-header.png from the untouched original.

The logo is only scaled (LANCZOS) and alpha-composited; geometry and colors are never edited.
Run from the repo root: python scripts/build_assets.py  (needs Pillow; fonts are Windows system fonts)
"""
from PIL import Image, ImageDraw, ImageFont

PURPLE = (143, 99, 236)          # #8F63EC, sampled from the original artwork
INK, PAPER, GRAY = (17, 17, 17), (250, 249, 246), (110, 110, 118)
LAVENDER = (238, 233, 251)
FONTS = "C:/Windows/Fonts/"
S = 2  # supersample, then downscale for clean edges

logo = Image.open("assets/paperhand-original.png").convert("RGBA")
assert logo.getpixel((0, 0))[3] == 0, "expected transparent original"


def font(name, size, variation=None):
    f = ImageFont.truetype(FONTS + name, size * S)
    if variation:
        f.set_variation_by_name(variation)
    return f


def fit(img, h):
    return img.resize((round(img.width * h / img.height), h), Image.LANCZOS)


def rounded(canvas, r):
    mask = Image.new("L", canvas.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, *canvas.size), r, fill=255)
    canvas.putalpha(mask)
    return canvas


# Mark: logo centred on off-white, rounded so it sits well on dark themes too.
W = 1024 * S
mark = Image.new("RGBA", (W, W), PAPER + (255,))
l = fit(logo, int(W * 0.72))
mark.alpha_composite(l, ((W - l.width) // 2, (W - l.height) // 2))
rounded(mark, 96 * S).resize((1024, 1024), Image.LANCZOS).save("assets/paperhand-mark.png", optimize=True)

# Header: 1600x420, logo left, type right, thin purple rules.
w, h = 1600 * S, 420 * S
hd = Image.new("RGBA", (w, h), PAPER + (255,))
d = ImageDraw.Draw(hd)
d.rectangle((0, 0, 28 * S, h), fill=LAVENDER)
d.rectangle((28 * S, 0, 32 * S, h), fill=PURPLE)
l = fit(logo, 300 * S)
hd.alpha_composite(l, (110 * S, (h - l.height) // 2))
x = 110 * S + l.width + 90 * S
d.text((x, 92 * S), "PAPERHAND", font=font("bahnschrift.ttf", 96, "Bold"), fill=INK)
d.text((x + 4 * S, 200 * S), "/ PAPiOSHU", font=font("bahnschrift.ttf", 34, "SemiBold"), fill=PURPLE)
d.line((x + 4 * S, 256 * S, x + 520 * S, 256 * S), fill=PURPLE, width=3 * S)
d.text((x + 4 * S, 274 * S), "Creative Technologist · Developer · Systems Architect · Worldbuilder",
       font=font("segoeui.ttf", 24), fill=GRAY)
d.text((x + 4 * S, 320 * S), "CREATE OR DIE.", font=font("bahnschrift.ttf", 28, "Bold"), fill=INK)
rounded(hd, 24 * S).resize((1600, 420), Image.LANCZOS).save("assets/paperhand-header.png", optimize=True)

# Self-check: original purple survives in the outputs.
for f in ("assets/paperhand-mark.png", "assets/paperhand-header.png"):
    colors = {c for _, c in Image.open(f).convert("RGB").getcolors(1 << 24)}
    assert PURPLE in colors, f
print("ok")
