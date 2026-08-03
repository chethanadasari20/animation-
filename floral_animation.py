from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio
import random
import math
# Canvas size
WIDTH = 900
HEIGHT = 600
TOTAL_FRAMES = 60
frames = []
# Load font
try:
    font = ImageFont.truetype("arial.ttf", 60)
    small_font = ImageFont.truetype("arial.ttf", 30)
except:
    font = ImageFont.load_default()
    small_font = ImageFont.load_default()
NAME = "Chethu Dasari"
def gradient_background():
    img = Image.new("RGB", (WIDTH, HEIGHT))
    px = img.load()
    top = (255, 220, 235)
    bottom = (210, 235, 255)
    for y in range(HEIGHT):
        r = int(top[0] + (bottom[0]-top[0])*y/HEIGHT)
        g = int(top[1] + (bottom[1]-top[1])*y/HEIGHT)
        b = int(top[2] + (bottom[2]-top[2])*y/HEIGHT)
        for x in range(WIDTH):
            px[x, y] = (r, g, b)
    return img
def draw_sparkles(draw):
    for _ in range(80):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.randint(2,5)
        draw.ellipse(
            (x-size,y-size,x+size,y+size),
            fill=(255,255,180)
        )
def draw_petals(draw, frame):
    petals = ["🌸","🌺","🌼"]
    for i in range(35):
        x = (i*40 + frame*5) % WIDTH
        y = (frame*12 + i*30) % HEIGHT
        draw.text(
            (x,y),
            random.choice(petals),
            font=small_font,
            fill="deeppink"
        )
def draw_butterflies(draw, frame):
    butterfly = "🦋"
    for i in range(6):
        x = (frame*12 + i*150) % WIDTH
        y = 120 + 40*math.sin(frame/6 + i)
        draw.text(
            (x,y),
            butterfly,
            font=small_font,
            fill="blue"
        )
flowers = ["🌸","🌺","🌷","🌼","🌹"]
def draw_border(draw):
    for x in range(0,WIDTH,35):
        draw.text((x,5),random.choice(flowers),font=small_font)
        draw.text((x,HEIGHT-35),random.choice(flowers),font=small_font)
    for y in range(0,HEIGHT,35):
        draw.text((5,y),random.choice(flowers),font=small_font)
        draw.text((WIDTH-35,y),random.choice(flowers),font=small_font)
def glowing_name(img):
    glow = Image.new("RGBA",(WIDTH,HEIGHT),(0,0,0,0))
    gdraw = ImageDraw.Draw(glow)
    bbox = gdraw.textbbox((0,0),NAME,font=font)
    w = bbox[2]-bbox[0]
    h = bbox[3]-bbox[1]
    x = (WIDTH-w)//2
    y = (HEIGHT-h)//2
    for r in range(8,0,-1):
        gdraw.text(
            (x,y),
            NAME,
            font=font,
            fill=(255,120,220,40)
        )
        glow = glow.filter(ImageFilter.GaussianBlur(2))
    img.paste(glow,(0,0),glow)
    draw = ImageDraw.Draw(img)
    draw.text(
        (x,y),
        NAME,
        font=font,
        fill="white"
    )
for frame in range(TOTAL_FRAMES):
    img = gradient_background()
    draw = ImageDraw.Draw(img)
    draw_border(draw)
    draw_sparkles(draw)
    draw_petals(draw,frame)
    draw_butterflies(draw,frame)
    glowing_name(img)
    frames.append(img)
# ==========================================
# Floral Name Animation - Part 2
# Continue below Part 1
# ==========================================

# Floating Hearts
def draw_hearts(draw, frame):
    hearts = ["💖", "💕", "💗"]

    for i in range(12):
        x = (i * 70 + frame * 4) % WIDTH
        y = HEIGHT - ((frame * 8 + i * 45) % HEIGHT)

        draw.text(
            (x, y),
            random.choice(hearts),
            font=small_font,
            fill="red"
        )
def blooming_flowers(draw, frame):
    flowers = ["🌸", "🌺", "🌼", "🌷", "🌹"]
    for i in range(20):
        angle = (frame * 6 + i * 18) % 360
        radius = 120 + 20 * math.sin(frame / 5 + i)
        x = WIDTH//2 + radius * math.cos(math.radians(angle))
        y = HEIGHT//2 + radius * math.sin(math.radians(angle))
        draw.text(
            (x, y),
            random.choice(flowers),
            font=small_font
        )
new_frames = []
for frame in range(TOTAL_FRAMES):
    img = gradient_background()
    draw = ImageDraw.Draw(img)
    draw_border(draw)
    draw_sparkles(draw)
    draw_petals(draw, frame)
    draw_butterflies(draw, frame)
    blooming_flowers(draw, frame)
    draw_hearts(draw, frame)
    glowing_name(img)
    draw.text(
        (WIDTH//2 - 120, HEIGHT - 60),
        "Bloom • Dream • Shine ✨",
        font=small_font,
        fill="purple"
    )
    new_frames.append(img)
imageio.mimsave(
    "chethu_floral.gif",
    new_frames,
    duration=0.08,
    loop=0
)
print("\n🌸 Animation Complete!")
print("Saved as: chethu_floral.gif")
