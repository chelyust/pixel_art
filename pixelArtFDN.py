import pygame
import sys

#настройки
COLS = 32
ROWS = 32
CELL_SIZE = 20

PALETTE = [
    (255, 0, 0),      #красный
    (0, 100, 255),    #синий
    (0, 200, 0),      #зелёный
    (255, 255, 255),  #белый
]

BG_COLOR = (255, 255, 255)
UI_HEIGHT = 40


#инициализация кода
pygame.init()

pygame.display.set_caption("Pixel Art Editor")

screen = pygame.display.set_mode(
    (COLS * CELL_SIZE, ROWS * CELL_SIZE + UI_HEIGHT)
)

clock = pygame.time.Clock()


#холст
canvas = []

for y in range(ROWS):
    row = []

    for x in range(COLS):
        row.append(BG_COLOR)

    canvas.append(row)


current_color = PALETTE[0]
drawing = False


def get_palette_rects():
    rects = []
    x = 5

    for color in PALETTE:
        rect = pygame.Rect(x, 7, 26, 26)
        rects.append((rect, color))
        x += 30

    return rects


running = True

while running:

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        #клик
        elif event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = event.pos

            if mouse_y < UI_HEIGHT:

                for rect, color in get_palette_rects():

                    if rect.collidepoint(mouse_x, mouse_y):
                        current_color = color

            else:

                if event.button == 1:
                    drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:
                drawing = False


    if drawing and mouse_pressed[0]:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if mouse_y >= UI_HEIGHT:

            # Переводим координаты мыши
            # в координаты клетки
            grid_x = mouse_x // CELL_SIZE
            grid_y = (mouse_y - UI_HEIGHT) // CELL_SIZE

            if 0 <= grid_x < COLS and 0 <= grid_y < ROWS:
                canvas[grid_y][grid_x] = current_color


    screen.fill((240, 240, 240))

    for y in range(ROWS):

        for x in range(COLS):

            pygame.draw.rect(
                screen,
                canvas[y][x],
                (
                    x * CELL_SIZE,
                    y * CELL_SIZE + UI_HEIGHT,
                    CELL_SIZE,
                    CELL_SIZE
                )
            )


    pygame.draw.rect(
        screen,
        (220, 220, 220),
        (0, 0, screen.get_width(), UI_HEIGHT)
    )

    pygame.draw.line(
        screen,
        (150, 150, 150),
        (0, UI_HEIGHT),
        (screen.get_width(), UI_HEIGHT),
        2
    )

    for rect, color in get_palette_rects():

        pygame.draw.rect(screen, color, rect)

        if color == current_color:
            border = (255, 0, 255)
        else:
            border = (80, 80, 80)

        pygame.draw.rect(screen, border, rect, 2)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()