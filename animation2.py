import pygame
import math
import random
pygame.init()
WIDTH = 1100
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("✨ Chethana - Magical Galaxy Garden ✨")
clock = pygame.time.Clock()
name_font = pygame.font.SysFont("segoescript", 105)
small_font = pygame.font.SysFont("arial", 22)
BLACK = (5, 3, 25)
PURPLE = (35, 10, 80)
PINK = (255, 100, 190)
WHITE = (255, 255, 255)
GREEN = (40, 150, 70)
stars = []
for i in range(220):
    stars.append({
        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT),
        "size": random.randint(1, 3),
        "phase": random.random() * 6.28
    })
butterflies = []
for i in range(9):
    butterflies.append({
        "angle": random.uniform(0, 6.28),
        "distance": random.randint(100, 300),
        "speed": random.uniform(0.01, 0.025),
        "color": random.choice([
            (255, 100, 180),
            (180, 100, 255),
            (100, 180, 255),
            (255, 180, 80),
            (255, 120, 220)
        ])
    })
flowers = []
for i in range(35):
    flowers.append({
        "x": random.randint(20, WIDTH - 20),
        "y": random.randint(610, 690),
        "size": random.randint(15, 30),
        "growth": random.uniform(0, 1),
        "color": random.choice([
            (255, 90, 160),
            (255, 150, 200),
            (180, 100, 255),
            (255, 210, 80)
        ])
    })
shooting_stars = []
for i in range(4):
    shooting_stars.append({
        "x": random.randint(-300, WIDTH),
        "y": random.randint(30, 250),
        "speed": random.uniform(4, 8)
    })
def draw_butterfly(x, y, size, color, animation):
    flap = abs(math.sin(animation))
    wing_width = 25 * size * (0.6 + flap * 0.4)
    pygame.draw.ellipse(
        screen,
        color,
        (
            x - wing_width * 2,
            y - 20 * size,
            wing_width * 1.5,
            wing_width * 1.5
        )
    )
    pygame.draw.ellipse(
        screen,
        color,
        (
            x + wing_width * 0.5,
            y - 20 * size,
            wing_width * 1.5,
            wing_width * 1.5
        )
    )
    pygame.draw.ellipse(
        screen,
        color,
        (
            x - wing_width * 1.4,
            y + 5 * size,
            wing_width,
            wing_width
        )
    )
    pygame.draw.ellipse(
        screen,
        color,
        (
            x + wing_width * 0.4,
            y + 5 * size,
            wing_width,
            wing_width
        )
    )
    pygame.draw.ellipse(
        screen,
        (30, 15, 30),
        (
            x - 4 * size,
            y - 10 * size,
            8 * size,
            30 * size
        )
    )
def draw_flower(x, y, size, growth, color):
    current = size * growth
    if current < 1:
        return
    pygame.draw.line(
        screen,
        GREEN,
        (x, y + 10),
        (x, y + 70),
        4
    )
    pygame.draw.ellipse(
        screen,
        GREEN,
        (
            x - current,
            y + 40,
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
            max(2, int(current * 0.6))
        )
    pygame.draw.circle(
        screen,
        (255, 220, 80),
        (x, y),
        max(2, int(current * 0.4))
    )
running = True
frame = 0
while running:
    frame += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(5 + 35 * ratio)
        g = int(3 + 8 * ratio)
        b = int(25 + 70 * ratio)
        pygame.draw.line(
            screen,
            (r, g, b),
            (0, y),
            (WIDTH, y)
        )
    for star in stars:
        brightness = int(
            130 +
            120 * abs(
                math.sin(
                    frame * 0.03 +
                    star["phase"]
                )
            )
        )
        pygame.draw.circle(
            screen,
            (brightness, brightness, brightness),
            (star["x"], star["y"]),
            star["size"]
        )
    pygame.draw.circle(
        screen,
        (255, 240, 180),
        (900, 110),
        55
    )
    pygame.draw.circle(
        screen,
        (15, 8, 45),
        (925, 90),
        55
    )
    for star in shooting_stars:
        star["x"] += star["speed"]
        star["y"] += star["speed"] * 0.35
        pygame.draw.line(
            screen,
            (255, 220, 255),
            (
                int(star["x"]),
                int(star["y"])
            ),
            (
                int(star["x"] - 80),
                int(star["y"] - 30)
            ),
            3
        )
        if star["x"] > WIDTH + 100:
            star["x"] = random.randint(-400, -100)
            star["y"] = random.randint(30, 250)
    center_x = WIDTH // 2
    center_y = 300
    for i in range(120):
        angle = i * 0.25 + frame * 0.015
        radius = 80 + i * 1.8
        x = center_x + math.cos(angle) * radius
        y = center_y + math.sin(angle) * radius * 0.45
        pygame.draw.circle(
            screen,
            (255, 150, 220),
            (int(x), int(y)),
            2
        )
    full_name = "CHETHANA"
    letters_to_show = int(
        frame / 12
    )
    if letters_to_show > len(full_name):
        letters_to_show = len(full_name)
    visible_name = full_name[:letters_to_show]
    name_surface = name_font.render(
        visible_name,
        True,
        (255, 245, 230)
    )
    name_rect = name_surface.get_rect(
        center=(center_x, center_y)
    )
    for glow in range(5):
        glow_surface = name_font.render(
            visible_name,
            True,
            (255, 70, 180)
        )
        glow_surface.set_alpha(
            35 - glow * 5
        )
        screen.blit(
            glow_surface,
            (
                name_rect.x - glow,
                name_rect.y - glow
            )
        )
    screen.blit(
        name_surface,
        name_rect
    )
    heart_size = 1 + 0.15 * math.sin(
        frame * 0.08
    )
    hx = center_x
    hy = center_y + 95
    points = [
        (
            hx,
            hy + int(35 * heart_size)
        ),
        (
            hx - int(35 * heart_size),
            hy - int(5 * heart_size)
        ),
        (
            hx - int(18 * heart_size),
            hy - int(25 * heart_size)
        ),
        (
            hx,
            hy - int(5 * heart_size)
        ),
        (
            hx + int(18 * heart_size),
            hy - int(25 * heart_size)
        ),
        (
            hx + int(35 * heart_size),
            hy - int(5 * heart_size)
        )
    ]
    pygame.draw.polygon(
        screen,
        (255, 80, 170),
        points
    )
    for butterfly in butterflies:
        butterfly["angle"] += butterfly["speed"]
        angle = butterfly["angle"]
        radius = butterfly["distance"] + \
                 math.sin(frame * 0.01) * 30
        bx = center_x + math.cos(angle) * radius
        by = center_y + math.sin(angle) * radius * 0.55
        draw_butterfly(
            bx,
            by,
            0.7,
            butterfly["color"],
            frame * 0.25
        )
    for flower in flowers:
        if flower["growth"] < 1:
            flower["growth"] += 0.004
        draw_flower(
            flower["x"],
            flower["y"],
            flower["size"],
            flower["growth"],
            flower["color"]
        )
    for i in range(35):
        x = (
            i * 97 +
            frame * 0.4
        ) % WIDTH
        y = 430 + math.sin(
            frame * 0.02 + i
        ) * 100
        glow = int(
            150 +
            100 *
            abs(
                math.sin(
                    frame * 0.08 + i
                )
            )
        )
        pygame.draw.circle(
            screen,
            (glow, 230, 120),
            (int(x), int(y)),
            3
        )
    for i in range(25):
        x = (
            i * 53 +
            frame * 0.7
        ) % WIDTH
        y = (
            350 +
            math.sin(
                frame * 0.02 + i
            ) * 150
        )
        pygame.draw.circle(
            screen,
            (255, 120, 190),
            (int(x), int(y)),
            3
        )
    subtitle = small_font.render(
        "✨ A little magical world made for Chethana ✨",
        True,
        (255, 200, 240)
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
