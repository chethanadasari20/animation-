import pygame
import math
import random
pygame.init()
WIDTH, HEIGHT = 1100, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("✨ Chethana's Magical Garden ✨")
clock = pygame.time.Clock()
font = pygame.font.SysFont("segoescript", 105, bold=False)
small_font = pygame.font.SysFont("arial", 22)
SKY = (18, 10, 55)
PINK = (255, 100, 180)
PURPLE = (170, 90, 255)
WHITE = (255, 245, 255)
GLOW = (255, 180, 220)
GREEN = (30, 100, 45)
stars = []
for i in range(180):
    stars.append({
        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT),
        "size": random.randint(1, 3),
        "speed": random.uniform(0.5, 2)
    })
flowers = []
for i in range(30):
    flowers.append({
        "x": random.randint(20, WIDTH - 20),
        "y": random.randint(580, 690),
        "size": random.randint(15, 35),
        "color": random.choice([
            (255, 100, 170),
            (255, 160, 200),
            (180, 100, 255),
            (255, 210, 100),
            (200, 80, 150)
        ]),
        "growth": 0
    })
butterflies = []
for i in range(7):
    butterflies.append({
        "angle": random.uniform(0, math.pi * 2),
        "radius_x": random.randint(300, 450),
        "radius_y": random.randint(150, 230),
        "speed": random.uniform(0.008, 0.018),
        "size": random.uniform(0.7, 1.2),
        "color": random.choice([
            (255, 100, 170),
            (170, 100, 255),
            (100, 180, 255),
            (255, 160, 70),
            (255, 120, 220)
        ])
    })
sparkles = []
for i in range(100):
    sparkles.append({
        "angle": random.uniform(0, math.pi * 2),
        "radius": random.uniform(300, 450),
        "speed": random.uniform(0.002, 0.008),
        "size": random.randint(1, 3)
    })
def draw_butterfly(x, y, scale, color, wing_animation):
    wing = 25 * scale
    # Wing movement
    wing_width = wing * (0.7 + 0.3 * abs(math.sin(wing_animation)))
    pygame.draw.ellipse(
        screen,
        color,
        (
            x - wing_width * 2,
            y - wing,
            wing_width * 1.5,
            wing * 1.5
        )
    )
    pygame.draw.ellipse(
        screen,
        color,
        (
            x + wing_width * 0.5,
            y - wing,
            wing_width * 1.5,
            wing * 1.5
        )
    )
    pygame.draw.ellipse(
        screen,
        color,
        (
            x - wing_width * 1.5,
            y,
            wing_width * 1.2,
            wing
        )
    )
    pygame.draw.ellipse(
        screen,
        color,
        (
            x + wing_width * 0.3,
            y,
            wing_width * 1.2,
            wing
        )
    )
    pygame.draw.ellipse(
        screen,
        (35, 15, 35),
        (
            x - 4 * scale,
            y - 12 * scale,
            8 * scale,
            30 * scale
        )
    )
    pygame.draw.line(
        screen,
        (30, 15, 30),
        (x, y - 10 * scale),
        (x - 10 * scale, y - 22 * scale),
        2
    )
    pygame.draw.line(
        screen,
        (30, 15, 30),
        (x, y - 10 * scale),
        (x + 10 * scale, y - 22 * scale),
        2
    )
def draw_flower(x, y, size, color, growth):
    current = size * growth
    if current <= 1:
        return
    pygame.draw.line(
        screen,
        GREEN,
        (x, y),
        (x, y + 70),
        4
    )
    pygame.draw.ellipse(
        screen,
        (40, 130, 55),
        (
            x - current,
            y + 35,
            current * 1.5,
            current / 2
        )
    )
    for i in range(6):
        angle = i * math.pi / 3
        px = x + math.cos(angle) * current
        py = y + math.sin(angle) * current
        pygame.draw.circle(
            screen,
            color,
            (int(px), int(py)),
            int(current * 0.65)
        )
    pygame.draw.circle(
        screen,
        (255, 220, 80),
        (int(x), int(y)),
        max(2, int(current * 0.4))
    )
running = True
frame = 0
while running:
    frame += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(SKY)
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(18 + 80 * ratio)
        g = int(10 + 15 * ratio)
        b = int(55 + 90 * ratio)
        pygame.draw.line(
            screen,
            (r, g, b),
            (0, y),
            (WIDTH, y)
        )
    for star in stars:
        brightness = int(
            150 + 100 *
            abs(math.sin(frame * 0.03 + star["x"]))
        )
        pygame.draw.circle(
            screen,
            (brightness, brightness, brightness),
            (star["x"], star["y"]),
            star["size"]
        )
    center_x = WIDTH // 2
    center_y = 300
    for radius in range(250, 80, -10):
        alpha = int(
            20 * (1 - radius / 250)
        )
        glow_surface = pygame.Surface(
            (WIDTH, HEIGHT),
            pygame.SRCALPHA
        )
        pygame.draw.ellipse(
            glow_surface,
            (255, 80, 180, alpha),
            (
                center_x - radius * 1.6,
                center_y - radius * 0.7,
                radius * 3.2,
                radius * 1.4
            )
        )
        screen.blit(
            glow_surface,
            (0, 0)
        )
    for sparkle in sparkles:
        sparkle["angle"] += sparkle["speed"]
        x = center_x + math.cos(
            sparkle["angle"]
        ) * sparkle["radius"]
        y = center_y + math.sin(
            sparkle["angle"]
        ) * sparkle["radius"] * 0.45
        pygame.draw.circle(
            screen,
            (255, 180, 220),
            (int(x), int(y)),
            sparkle["size"]
        )
    name = "Thulasi&Subbu"
    for glow_size in [8, 5, 3]:
        glow_font = pygame.font.SysFont(
            "segoescript",
            105,
            bold=False
        )
        glow_text = glow_font.render(
            name,
            True,
            (255, 80, 180)
        )
        glow_text.set_alpha(
            30 if glow_size == 8 else 60
        )
        glow_rect = glow_text.get_rect(
            center=(center_x, center_y)
        )
        screen.blit(
            glow_text,
            glow_rect
        )
    name_text = font.render(
        name,
        True,
        (255, 245, 235)
    )
    name_rect = name_text.get_rect(
        center=(center_x, center_y)
    )
    screen.blit(
        name_text,
        name_rect
    )
    heart_y = center_y + 80
    pygame.draw.arc(
        screen,
        (255, 150, 210),
        (
            center_x - 80,
            heart_y - 20,
            80,
            50
        ),
        math.pi,
        math.pi * 2,
        3
    )
    pygame.draw.arc(
        screen,
        (255, 150, 210),
        (
            center_x,
            heart_y - 20,
            80,
            50
        ),
        math.pi,
        math.pi * 2,
        3
    )
    pygame.draw.polygon(
        screen,
        (255, 120, 190),
        [
            (center_x, heart_y + 30),
            (center_x - 18, heart_y + 5),
            (center_x - 35, heart_y + 15),
            (center_x - 30, heart_y + 35),
            (center_x, heart_y + 65),
            (center_x + 30, heart_y + 35),
            (center_x + 35, heart_y + 15),
            (center_x + 18, heart_y + 5)
        ]
    )
    for butterfly in butterflies:
        butterfly["angle"] += butterfly["speed"]
        bx = center_x + math.cos(
            butterfly["angle"]
        ) * butterfly["radius_x"]
        by = center_y + math.sin(
            butterfly["angle"]
        ) * butterfly["radius_y"]
        by += math.sin(
            frame * 0.04 + butterfly["angle"]
        ) * 15
        draw_butterfly(
            bx,
            by,
            butterfly["size"],
            butterfly["color"],
            frame * 0.2
        )
    for flower in flowers:
        if flower["growth"] < 1:
            flower["growth"] += 0.003
        draw_flower(
            flower["x"],
            flower["y"],
            flower["size"],
            flower["color"],
            flower["growth"]
        )
    for i in range(20):
        x = (
            i * 57 +
            frame * 0.4
        ) % WIDTH
        y = (
            450 +
            math.sin(
                frame * 0.02 + i
            ) * 100
        )
        pygame.draw.circle(
            screen,
            (255, 130, 190),
            (int(x), int(y)),
            4
        )
    subtitle = small_font.render(
        "✨ Welcome to Chethana's Magical Garden ✨",
        True,
        (255, 210, 240)
    )
    subtitle_rect = subtitle.get_rect(
        center=(center_x, HEIGHT - 25)
    )
    screen.blit(
        subtitle,
        subtitle_rect
    )
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
