import os
from PIL import Image, ImageDraw, ImageFont

# Canvas: Pinterest Standard 1000x1500
W, H = 1000, 1500
img = Image.new("RGB", (W, H), "#0b0f19")
draw = ImageDraw.Draw(img)

# Try loading standard clean fonts
try:
    font_cat = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 54)
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    font_head = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    font_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    font_badge = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    font_footer = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
except:
    font_cat = font_title = font_sub = font_head = font_body = font_bold = font_badge = font_footer = ImageFont.load_default()

# 1. Top Category Pill
draw.rounded_rectangle([320, 50, 680, 100], radius=25, fill="#be123c")
draw.text((500, 75), "SKIN BIOHACKING 2026", fill="#ffffff", font=font_cat, anchor="mm")

# 2. Main Title
draw.text((500, 155), "ASTAXANTHIN 12MG", fill="#f43f5e", font=font_title, anchor="mm")
draw.text((500, 225), "Natural Tanning & Sun Defense", fill="#ffffff", font=font_title, anchor="mm")
draw.text((500, 285), "Which Brand Delivers the Best Carotenoid Glow?", fill="#94a3b8", font=font_sub, anchor="mm")

# Divider line
draw.line([(80, 330), (920, 330)], fill="#1e293b", width=2)

# 3. Micro Ingredients Card (Winner)
draw.rounded_rectangle([70, 360, 930, 820], radius=24, fill="#111827", outline="#e11d48", width=3)
# Winner Badge
draw.rounded_rectangle([100, 385, 330, 425], radius=12, fill="#e11d48")
draw.text((215, 405), "#1 TOP CHOICE", fill="#ffffff", font=font_badge, anchor="mm")

draw.text((100, 470), "Micro Ingredients 12mg Softgels", fill="#ffffff", font=font_head)
draw.text((100, 515), "Pure Microalgae (H. Pluvialis) + MCT Oil", fill="#fda4af", font=font_body)

items_mi = [
    ("• 120 Softgels", "4-Month Protocol Supply"),
    ("• Daily Cost:", "~$0.26 / day (High Value)"),
    ("• Formulation:", "Targeted Carotenoid Tanning & UV Shield"),
    ("• Lab Verification:", "USA 3rd-Party ISO Certified"),
]
y_offset = 570
for k, v in items_mi:
    draw.text((110, y_offset), k, fill="#f43f5e", font=font_bold)
    draw.text((330, y_offset), v, fill="#e2e8f0", font=font_body)
    y_offset += 48

# Price tag box inside card
draw.rounded_rectangle([100, 750, 900, 800], radius=12, fill="#1e1b4b")
draw.text((500, 775), "Use Code: MICROCHOPSREVIEW for 10% Off Direct", fill="#38bdf8", font=font_bold, anchor="mm")

# 4. Sports Research Card (Comparison)
draw.rounded_rectangle([70, 850, 930, 1260], radius=24, fill="#0f172a", outline="#334155", width=2)
# Runner Up Badge
draw.rounded_rectangle([100, 875, 320, 915], radius=12, fill="#334155")
draw.text((210, 895), "RUNNER UP", fill="#cbd5e1", font=font_badge, anchor="mm")

draw.text((100, 955), "Sports Research Astaxanthin 12mg", fill="#e2e8f0", font=font_head)
draw.text((100, 1000), "AstaReal Extract + Virgin Coconut Oil", fill="#94a3b8", font=font_body)

items_sr = [
    ("• 60 Softgels", "2-Month Supply Only"),
    ("• Daily Cost:", "~$0.46 / day (More Expensive)"),
    ("• Formulation:", "Generic Antioxidant & Joint Health"),
    ("• Note:", "Contains Coconut (Tree Nut Allergen)"),
]
y_offset = 1050
for k, v in items_sr:
    draw.text((110, y_offset), k, fill="#64748b", font=font_bold)
    draw.text((330, y_offset), v, fill="#94a3b8", font=font_body)
    y_offset += 46

# 5. Bottom Call To Action Banner
draw.rounded_rectangle([70, 1300, 930, 1440], radius=20, fill="#e11d48")
draw.text((500, 1345), "READ FULL CLINICAL BREAKDOWN", fill="#ffffff", font=font_footer, anchor="mm")
draw.text((500, 1395), "lab.chopsreview.com/astaxanthin-vs-sports-research", fill="#ffe4e6", font=font_body, anchor="mm")

output_path = "/home/long-npl/aff-landing-pages/astaxanthin-pinterest-pin.png"
img.save(output_path, "PNG")
print(f"DONE:{output_path}")
