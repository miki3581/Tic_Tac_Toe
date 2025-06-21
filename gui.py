import sys
import pygame
from game import TicTacToe
from opponent.easy import EasyAI
from opponent.medium import MediumAI
from opponent.hard import HardAI

pygame.init()

WIDTH, HEIGHT = 750, 750
CELL_SIZE = WIDTH // 3
LINE_WIDTH = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)

font = pygame.font.SysFont(None, 180)
small_font = pygame.font.SysFont(None, 72)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kółko i Krzyżyk")


def draw_lines():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, CELL_SIZE * i),
                         (WIDTH, CELL_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (CELL_SIZE * i, 0),
                         (CELL_SIZE * i, CELL_SIZE * 3), LINE_WIDTH)


def draw_symbols(game):
    for row in range(3):
        for col in range(3):
            symbol = game.board[row][col]
            if symbol != " ":
                text = font.render(symbol, True, BLACK)
                rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE//2,
                                             row * CELL_SIZE + CELL_SIZE//2))
                screen.blit(text, rect)


def draw_winning_line(game):
    if game.winner and game.winning_line:
        (start_row, start_col), (end_row, end_col) = game.winning_line
        x1 = start_col * CELL_SIZE + CELL_SIZE // 2
        y1 = start_row * CELL_SIZE + CELL_SIZE // 2
        x2 = end_col * CELL_SIZE + CELL_SIZE // 2
        y2 = end_row * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 10)


def draw_end_message(winner):
    if winner:
        msg = f"{winner} wygrał!"
    else:
        msg = "Remis!"

    text = small_font.render(msg, True, GREEN)
    outline_color = BLACK

    # Obramowanie tekstu
    for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3)]:
        outline = small_font.render(msg, True, outline_color)
        rect = outline.get_rect(center=(WIDTH//2, CELL_SIZE * 3 // 2 + dy))
        rect.centerx += dx
        screen.blit(outline, rect)

    rect = text.get_rect(center=(WIDTH//2, CELL_SIZE * 3 // 2))
    screen.blit(text, rect)


def draw_button(text, rect, active_color, inactive_color, mouse_pos):
    color = active_color if rect.collidepoint(mouse_pos) else inactive_color
    pygame.draw.rect(screen, color, rect, border_radius=12)
    btn_text = small_font.render(text, True, BLACK)
    btn_rect = btn_text.get_rect(center=rect.center)
    screen.blit(btn_text, btn_rect)


def show_menu():
    selecting = True
    btn_width, btn_height = 300, 80
    easy_btn_rect = pygame.Rect
    (WIDTH//2 - btn_width//2, 200, btn_width, btn_height)
    med_btn_rect = pygame.Rect
    (WIDTH//2 - btn_width//2, 320, btn_width, btn_height)
    hard_btn_rect = pygame.Rect
    (WIDTH//2 - btn_width//2, 440, btn_width, btn_height)

    while selecting:
        screen.fill(WHITE)
        title = small_font.render("Wybierz poziom trudności:", True, BLACK)
        screen.blit(title, title.get_rect(center=(WIDTH//2, 120)))

        mouse_pos = pygame.mouse.get_pos()

        draw_button("Łatwy", easy_btn_rect,
                    (170, 220, 170), (140, 200, 140), mouse_pos)
        draw_button("Średni", med_btn_rect,
                    (170, 170, 220), (140, 140, 200), mouse_pos)
        draw_button("Trudny", hard_btn_rect,
                    (220, 170, 170), (200, 140, 140), mouse_pos)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if easy_btn_rect.collidepoint(event.pos):
                    return "łatwy"
                elif med_btn_rect.collidepoint(event.pos):
                    return "średni"
                elif hard_btn_rect.collidepoint(event.pos):
                    return "trudny"


def draw_endgame_buttons(mouse_pos):
    btn_width, btn_height = 180, 60
    buttons_y = HEIGHT - 70 - btn_height  # 750 - 70 - 60 = 620

    reset_rect = pygame.Rect
    (WIDTH//4 - btn_width//2, buttons_y, btn_width, btn_height)
    quit_rect = pygame.Rect
    (3*WIDTH//4 - btn_width//2, buttons_y, btn_width, btn_height)

    draw_button("Resetuj", reset_rect,
                (180, 180, 255), (150, 150, 220), mouse_pos)
    draw_button("Wyjdź", quit_rect,
                (255, 180, 180), (220, 150, 150), mouse_pos)

    return reset_rect, quit_rect


def run_game():
    difficulty = show_menu()

    if difficulty == "łatwy":
        opponent = EasyAI("O")
    elif difficulty == "średni":
        opponent = MediumAI("O")
    else:
        opponent = HardAI("O")

    game = TicTacToe(opponent)
    game_over = False
    running = True

    while running:
        screen.fill(WHITE)
        draw_lines()
        draw_symbols(game)

        if game.winner:
            draw_winning_line(game)
            draw_end_message(game.winner)
            game_over = True
        elif game.is_draw():
            draw_end_message(None)
            game_over = True

        mouse_pos = pygame.mouse.get_pos()

        if game_over:
            reset_rect, quit_rect = draw_endgame_buttons(mouse_pos)
        else:
            reset_rect = quit_rect = None

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not game_over:
                    x, y = event.pos
                    row = y // CELL_SIZE
                    col = x // CELL_SIZE
                    if row < 3:
                        game.make_move(row, col)
                else:
                    if reset_rect and reset_rect.collidepoint(event.pos):
                        game.reset()
                        game_over = False
                    elif quit_rect and quit_rect.collidepoint(event.pos):
                        running = False

    pygame.quit()
    sys.exit()
