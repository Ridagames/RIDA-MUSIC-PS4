from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

out = Path("sce_sys/icon0.png")
out.parent.mkdir(parents=True, exist_ok=True)
size = 512
im = Image.new("RGB", (size, size), (12, 16, 14))
d = ImageDraw.Draw(im)

for inset in range(0, 220, 4):
    shade = max(18, 42 - inset // 10)
    d.rounded_rectangle((inset, inset, size-inset, size-inset),
                        radius=72, outline=(12, shade, 28), width=3)

d.ellipse((118, 92, 394, 368), fill=(29, 185, 84))
d.ellipse((154, 128, 358, 332), fill=(12, 16, 14))
d.ellipse((226, 200, 286, 260), fill=(29, 185, 84))
d.rounded_rectangle((242, 155, 270, 240), radius=14, fill=(29, 185, 84))
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 43)
except OSError:
    font = ImageFont.load_default()
label = "RIDA MUSIC"
bbox = d.textbbox((0, 0), label, font=font)
d.text(((size-(bbox[2]-bbox[0]))/2, 408), label, font=font, fill=(245, 248, 246))
im.save(out, "PNG")
