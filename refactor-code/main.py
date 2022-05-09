import sys
import pygame


def play_game(screen, player, game):
    game_over = False
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and player.x > 0:
                    player.x -= player.size
                elif event.key == pygame.K_RIGHT and player.x < (screen.width - player.size):
                    player.x += player.size

        game.drop_enemies(screen.width)
        game.update_enemy_positions(screen.height)
        game.set_level()

        screen.update_screen(game.enemy_list, player, game.score)

        if game.collision_check(player):
            game_over = True
            break

