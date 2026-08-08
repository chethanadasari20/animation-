import pygame
import math
import random
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("❤️ Heartbeat & Sparkles")
clock = pygame.time.Clock()
BG = (10, 5, 30)
HEART = (255, 55, 120)
SPARKLE = (255, 210, 240)
GLOW = (255, 70, 150)
def heart_points(cx, cy, scale):
    points = []
    for i in range(200):
        t = i * 2 * math.pi / 200
        x = 16 * math.sin(t) ** 3
        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )
        points.append(
            (
                int(cx + x * scale),
                int(cy - y * scale)
            )
        )
    return points
sparkles = []
def create_sparkles():
    for i in range(45):
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(1.5, 5)
        sparkles.append({
            "x": WIDTH // 2,
            "y": HEIGHT // 2,
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed,
            "life": random.randint(30, 60),
            "size": random.randint(2, 5)
        })
beat_timer = 0
beat_number = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    beat_timer += 1
    screen.fill(BG)
    for i in range(100):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        pygame.draw.circle(
            screen,
            (70, 40, 90),
            (x, y),
            1
        )
    cycle = beat_timer % 90
    if cycle < 10:
        pulse = 1 + 0.25 * math.sin(
            cycle * math.pi / 10
        )
    elif 10 <= cycle < 20:
        pulse = 1.25 - (
            (cycle - 10) / 10
        ) * 0.25
    elif 20 <= cycle < 28:
        pulse = 1 + 0.15 * math.sin(
            (cycle - 20) * math.pi / 8
        )
    else:
        pulse = 1
    if cycle == 1 or cycle == 21:
        create_sparkles()
    glow_surface = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )
    glow_size = int(190 * pulse)
    pygame.draw.circle(
        glow_surface,
        (255, 50, 130, 25),
        (WIDTH // 2, HEIGHT // 2),
        glow_size
    )
    screen.blit(
        glow_surface,
        (0, 0)
    )
    points = heart_points(
        WIDTH // 2,
        HEIGHT // 2,
        13 * pulse
    )
    for thickness in [12, 8, 5]:
        pygame.draw.polygon(
            screen,
            (255, 40, 130),
            points,
            thickness
        )
    pygame.draw.polygon(
        screen,
        HEART,
        points
    )
    highlight = heart_points(
        WIDTH // 2 - 10,
        HEIGHT // 2 - 10,
        4 * pulse
    )
    pygame.draw.polygon(
        screen,
        (255, 130, 180),
        highlight
    )
    for sparkle in sparkles[:]:
        sparkle["x"] += sparkle["vx"]
        sparkle["y"] += sparkle["vy"]
        sparkle["life"] -= 1
        sparkle["vx"] *= 0.98
        sparkle["vy"] *= 0.98
        if sparkle["life"] <= 0:
            sparkles.remove(sparkle)
            continue
        x = int(sparkle["x"])
        y = int(sparkle["y"])
        size = sparkle["size"]
        pygame.draw.line(
            screen,
            SPARKLE,
            (x - size * 2, y),
            (x + size * 2, y),
            2
        )
        pygame.draw.line(
            screen,
            SPARKLE,
            (x, y - size * 2),
            (x, y + size * 2),
            2
        )
        pygame.draw.circle(
            screen,
            SPARKLE,
            (x, y),
            size // 2
        )
    for i in range(25):
        angle = (
            i * 2 * math.pi / 25
            + beat_timer * 0.01
        )
        radius = 230
        x = WIDTH // 2 + math.cos(angle) * radius
        y = HEIGHT // 2 + math.sin(angle) * radius
        sparkle_size = int(
            2 + 2 *
            abs(math.sin(
                beat_timer * 0.05 + i
            ))
        )
        pygame.draw.circle(
            screen,
            SPARKLE,
            (int(x), int(y)),
            sparkle_size
        )
    line_y = 590
    points = []
    for x in range(100, 900, 5):
        local = (x - 100) / 800
        if 0.45 < local < 0.50:
            y = line_y - 40
        elif 0.50 < local < 0.53:
            y = line_y + 45
        elif 0.53 < local < 0.58:
            y = line_y - 20
        else:
            y = line_y
        points.append((x, y))
    pygame.draw.lines(
        screen,
        (255, 100, 170),
        False,
        points,
        3
    )
    font = pygame.font.SysFont(
        "arial",
        28
    )
    text = font.render(
        "♥  LOVE BEATS  ♥",
        True,
        (255, 180, 220)
    )
    text_rect = text.get_rect(
        center=(WIDTH // 2, 650)
    )
    screen.blit(
        text,
        text_rect
    )
    pygame.display.flip()
    clock.tick(60)
pygame.mixer.music.stop()
pygame.quit()
