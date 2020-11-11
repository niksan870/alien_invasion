import pygame

from game_stats import GameStats
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    bullets = Group()
    aliens = Group()

    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while stats.game_active:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
