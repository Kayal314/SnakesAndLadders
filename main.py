import pygame
from playerDes import Player
from boardDes import Board

pygame.init()

# Icons from "https://www.flaticon.com"
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Snakes and Ladders")
board = pygame.image.load("Sprites\\board.png")
pygame.display.set_icon(board)
board = pygame.transform.scale(board, (600, 600))
player1_img = pygame.image.load("Sprites\\ball1.png")
player2_img = pygame.image.load("Sprites\\ball2.png")
dice_faces = [pygame.image.load("Sprites\\faceone.png"), pygame.image.load("Sprites\\facetwo.png"),
              pygame.image.load("Sprites\\facethree.png"), pygame.image.load("Sprites\\facefour.png"),
              pygame.image.load("Sprites\\facefive.png"), pygame.image.load("Sprites\\facesix.png")]


def display_player(player: Player):
    screen.blit(player.image, (player.pos_x, player.pos_y))


# for drawing the dice-roll button
def draw_roll_button():
    rect = pygame.draw.rect(screen, (41, 55, 69), (25, 30, 60, 50), 0)
    text = pygame.font.SysFont("Arial", 20, True, False).render("ROLL!", True, (66, 203, 245), None)
    screen.blit(text, rect)


def draw_reset_button():
    rect = pygame.draw.rect(screen, (41, 55, 69), (722, 30, 60, 50), 0)
    text = pygame.font.SysFont("Arial", 20, True, False).render("RESET", True, (66, 203, 245), None)
    screen.blit(text, rect)


# for displaying the face of the dice which the player got
def display_dice(n: int):
    screen.blit(dice_faces[n - 1], (20, 100))


# for displaying message when player uses a ladder
def display_congrats():
    rect = pygame.draw.rect(screen, (41, 55, 69), (260, 635, 60, 30), 0)
    text = pygame.font.SysFont("Arial", 20, True, False).render("Congrats! You just used a ladder", True,
                                                                (66, 203, 245),
                                                                None)
    screen.blit(text, rect)


# for displaying a message when player gets poisoned by a snake
def display_consolation():
    rect = pygame.draw.rect(screen, (41, 55, 69), (260, 635, 60, 30), 0)
    text = pygame.font.SysFont("Arial", 20, True, False).render("Sorry, you were poisoned by a snake", True,
                                                                (66, 203, 245), None)
    screen.blit(text, rect)


# for displaying a message when a player wins the game
def display_win_msg():
    rect = pygame.draw.rect(screen, (41, 55, 69), (300, 630, 60, 30), 0)
    text = pygame.font.SysFont("Arial", 20, True, False).render("You've won the game!", True,
                                                                (66, 203, 245), None)
    rect2 = pygame.draw.rect(screen, (41, 55, 69), (340, 655, 60, 30), 0)
    text2 = pygame.font.SysFont("Arial", 20, True, False).render("Play Again?", True,
                                                                 (66, 203, 245), None)
    screen.blit(text, rect)
    screen.blit(text2, rect2)


# checks if the player's new position
# has a snake's mouth or a ladder's bottom
def check_snake_or_ladder(player: Player) -> int:
    new_pos_snake = BOARD.SNAKES.get(player.board_pos)
    new_pos_ladder = BOARD.LADDERS.get(player.board_pos)
    if new_pos_snake:
        make_move(player, new_pos_snake - player.board_pos)
        return 1
    elif new_pos_ladder:
        make_move(player, new_pos_ladder - player.board_pos)
        return 2
    return -1


"""
@:param: player (Player) -> the player who rolled the dice
@:param: dice (int) -> the number received by player on rolling the dice
@:returns: c ∈ {-1,1,2,100} -> whether player has played a normal move, been bitten by a snake, climbed a ladder,
                               or won the game
"""


def make_move(player: Player, dice: int) -> int:
    if player.board_pos + dice > 100:
        return -1
    player.board_pos += dice
    x, y = BOARD.get_coordinates(player.board_pos)
    player.change_coordinates(x, y)
    changed = check_snake_or_ladder(player)
    if player.board_pos == 100:
        return 100
    display_player(player)
    return changed


if __name__ == '__main__':
    running = True
    first = True  # player 1's turn
    BOARD = Board()  # the Board on which the game is played
    game_start = False  # the game has started
    game_over = False  # game is over i.e someone won
    p1 = Player(player1_img, 1)  # first player
    p2 = Player(player2_img, 2)  # second player
    dice_to_be_shown = -1  # the current dice of player
    current_player = p1
    pos_changed = -1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 25 <= pos[0] <= 85 and 30 <= pos[1] <= 80 and not game_over:
                    game_start = True
                    if first:
                        current_player = p1
                    else:
                        current_player = p2
                    dice_to_be_shown = current_player.roll_dice()
                    pos_changed = make_move(current_player, dice_to_be_shown)
                    first = not first
                elif 720 <= pos[0] <= 780 and 30 <= pos[1] <= 80:
                    game_start = False
                    game_over = False
                    first = True
                    dice_to_be_shown = -1
                    pos_changed = -1
                    current_player = p1
                    p1.reset()
                    p2.reset()
        screen.fill((41, 55, 69))
        screen.blit(board, (100, 0))
        if game_start:
            display_dice(dice_to_be_shown)
        if pos_changed == 1:
            display_consolation()
        elif pos_changed == 2:
            display_congrats()
        elif pos_changed == 100:
            display_win_msg()
            game_over = True
        display_player(p1)
        display_player(p2)
        draw_roll_button()
        draw_reset_button()
        pygame.display.update()
