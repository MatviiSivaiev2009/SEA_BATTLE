# імпортуємо модуль кнопки
import modules.buttons as m_button
# імпортуємо pygame
import pygame
# імпортуємо модуль фону
import modules.background as m_background
# імпортуємо модуль карти
import modules.map as m_map
# імпортуємо сховище списків
import modules.data_base as m_data
import modules.ships as m_ships 
import modules.win_lose as m_win

# ініціюємо pygame
pygame.init()
pygame.display.set_caption("Sea_Battle")
# змінна game = 1
game = True
# ширина екрану
screen_width = 1000
# висота екрану
screen_height = 700
# створюємо та задаємо розмір екрану
screen_game = pygame.display.set_mode((screen_width, screen_height))

# створюємо оновлення екрану
FPS = pygame.time.Clock()
# відображення спрайту фона
m_background.background.blit_sprite(screen_game)
# відображення спрайту кнопки
m_button.button.blit_sprite(screen_game)
# створення карти номер 1
m_map.map1.create_map(m_data.list_map1)
# створення карти номер 2
m_map.map2.create_map(m_data.list_map2)
# перевірка довжини  рядку
import modules.bot as m_bot
m_bot.place()
#print(len(m_data.list_map1))
# цикл гри
m_ships.ship.blit_sprite(screen_game, x = 0, y = 0 )
m_ships.ship2.blit_sprite(screen_game, x = 100, y = 0 )
m_ships.ship3.blit_sprite(screen_game, x = 200, y = 0 )
m_ships.ship4.blit_sprite(screen_game, x = 300, y = 0 )
while game:
    if m_data.start_game == True:
        m_map.map1.check_attack(m_data.list_map1, screen_game, m_data.player_ships)
        m_map.map2.check_attack(m_data.list_map2, screen_game, m_data.enemy_ships)
    # для того щоб івент в pygame був полученням 
    for event in pygame.event.get():
        # keys = 
        if event.type == pygame.KEYDOWN:
            # print(9999)
            keys = pygame.key.get_pressed()
            #print(keys)
            if keys[pygame.K_UP]:
                m_data.rotate_ships = -90
                #print(99)
            elif keys[pygame.K_DOWN]:
                m_data.rotate_ships = 90
            elif keys[pygame.K_LEFT]:
                m_data.rotate_ships = 0
            elif keys[pygame.K_RIGHT]:
                m_data.rotate_ships = 180     
                 
        if m_data.turn and not m_data.win:
            m_bot.attack()
            
            check = m_win.win_lose(m_data.list_map1)
            check1 = m_win.win_lose(m_data.list_map2)
            if check or check1:
                    m_data.win = 1

        if m_data.count_ships == [4,3,2,1]:
            m_data.start_game = 1
        # якщо івент чітко дорівнює вихід 
            
        if event.type == pygame.QUIT:
            # тоді змінна game = 0 і віконце зачиняється 
            game = False
        # якщо івент чітко дорівнює натиску миші   
        if event.type == pygame.MOUSEBUTTONDOWN:

            # тоді х та у = івенту позиції
            x, y = event.pos 
            m_button.button.button_pressed(pos = event.pos, screen_game = screen_game )
        
            # написати координати х та у
            # print(m_data.)
            # функція яка робить натиск у клітинці карти номер 1 і пише ім'я клітинці
            if not m_data.win:
            
                if not m_data.start_game:
                    m_map.map1.get_pressed(x, y,  m_data.list_map1, screen_game)
                else:
                    m_map.map2.attack(x, y,m_data.list_map2)
                    
                    check = m_win.win_lose(m_data.list_map1)
                    check1 = m_win.win_lose(m_data.list_map2)
                    if check or check1:
                        m_data.win = 1
        #() - кортеж
        #[] - список
            # функція яка робить натиск у клітинці карти номер 2 і пише ім'я клітинці
           # m_map.map2.get_pressed(x, y, m_data.list_map2, screen_game)
    if m_data.win:
        for ship1 in m_data.enemy_ships[0]:
            m_data.rotate_ships = ship1[2]
            # m_ships.ship.load_image() /.
            m_ships.ship.blit_sprite(screen_game, ship1[0], ship1[1])
        for ship2 in m_data.enemy_ships[1]:
            m_data.rotate_ships = ship2[2]
            # m_ships.ship2.load_image().
            m_ships.ship2.blit_sprite(screen_game, ship2[0], ship2[1])
        for ship3 in m_data.enemy_ships[2]:
            m_data.rotate_ships = ship3[2]
            # m_ships.ship3.load_image()
            m_ships.ship3.blit_sprite(screen_game, ship3[0], ship3[1])
        m_data.rotate_ships = m_data.enemy_ships[3][2]
        #_ships.ship4.load_image() 
        m_ships.ship4.blit_sprite(screen_game,m_data.enemy_ships[3][0], m_data.enemy_ships[3][1])
        m_data.rotate_ships = 0
        # m_ships.ship.load_image()
        # m_ships.ship2.load_image()
        # m_ships.ship3.load_image()
        # m_ships.ship4.load_image()

    # m_ships.ship4.blit_sprite(screen_game,0,400)

    for cell in m_data.list_map2:
        if cell.ATTACKED:
            if cell.NAME != 5 and cell.NAME != 0:
                cell.draw_cross([255 ,25 ,25 ], screen_game)
            else:
                cell.draw_cross([25, 255, 25 ], screen_game)
    
    for cell in m_data.list_map1:
        if cell.ATTACKED:
            if cell.NAME != 5 and cell.NAME != 0:
                cell.draw_cross([255 ,25 ,25 ], screen_game)
            else:
                cell.draw_cross([25, 255, 25 ], screen_game)
    # задаємо значення для FPS       
    
    FPS.tick(60)
    # оновлення екрану
    pygame.display.flip()        
