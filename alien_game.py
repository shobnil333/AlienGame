import pygame
from pygame.sprite import Group
from alien_setting import Setting
from alien_game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from alien_ship import Ship
import alien_game_function as agf


def run_game():

    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('Alien Hunter')
    play_button = Button(ai_setting, screen, "Play")
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()
    agf.create_fleet(ai_setting, screen, ship, aliens)

    while True:

        agf.check_events(ai_setting, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:

            ship.update()
            agf.update_bullet(ai_setting, screen, stats, sb, ship, aliens, bullets)
            agf.update_aliens(ai_setting, stats, sb, screen, ship, aliens, bullets)
        agf.update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()