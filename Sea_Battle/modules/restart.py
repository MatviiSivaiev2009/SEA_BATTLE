import pygame
import modules.background as m_background
import modules.data_base as m_data
import modules.map as m_map
import modules.ships as m_ships
import modules.bot as m_bot
pygame.init()
def restart(screen_game, button):
    m_data.win = False
    m_data.list_map1 = []
    m_data.list_map2 = []
    m_map.map1.create_map(m_data.list_map1)
    m_map.map2.create_map(m_data.list_map2)
    m_data.enemy_ships = [[],[],[]] 
    m_background.background.blit_sprite(screen_game)
    m_data.turn = 0
    m_data.count_ships = [0,0,0,0]
    m_data.start_game =  0 
    m_data.win = 0 
    m_bot.place()
    m_ships.ship.blit_sprite(screen_game, x = 0, y = 0 )
    m_ships.ship2.blit_sprite(screen_game, x = 100, y = 0 )
    m_ships.ship3.blit_sprite(screen_game, x = 200, y = 0 )
    m_ships.ship4.blit_sprite(screen_game, x = 300, y = 0 )
    # print(m_data.list_map1)
    # print(m_data.list_map2)
    
    button.blit_sprite(screen_game) 