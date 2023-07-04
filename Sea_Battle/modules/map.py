# імпортуємо pygame
import pygame
# імпортуємо створюємо комірки 
import modules.cell as m_cell
# імпортуємо сховище списків
import modules.data_base as m_data
# імпортуємо сховище кораблів 
import modules.ships as m_ships 
# ініціюємо налаштування pygame
pygame.init()
# створюємо класс pygame 
# def turn(rotate):
#     if rotate % 180 == 0:
#         return
turn = lambda rotate: 1 if rotate % 180 == 0 else 10
class Map:
    # створюємо функцію ініт для налаштувань нашого класса Мап
    def __init__(self, x1 = 0, y1 = 0):
        # параметр кординати Х 
        self.X = x1
        # парамтр кординати У
        self.Y = y1
    # створюємо функцію для створювання карти 
    def create_map(self, list_map):
        #list_map = []
        # Локальна зманні х, яка дорівнює параматру кординати Х
        x = self.X
        # Локальна зманні у, яка дорівнює параматру кординати У
        y = self.Y
        # Локальна змінна сount_cell (лічільник клітинок) 
        count_cell = 0
        # list_map = []
        # створюємо цикл рядків який б
        for row in range(10):
            # створюємо лічільник комірок 
            for cell in range(10):
                # змінна count_cell кожен раз буде додавати одиницю сама у себе 
                count_cell = count_cell + 1
                # створюємо об'єкт клітинки який буде створювати клітинку і змащуватися по координаті Х та У на 31 піксель та вона буде записувати значення у count_cell (номер клітинки у лічільник клітинок)
                cell1 = m_cell.Cell(x1 = x, x2 = x + 30.6, y1 = y, y2 = y + 30.6, name = 0 , row = row )
                # список мап відправляє значення об'єкту клітинок у сховище списків, а точніше у список до якого будуть звертатися 
                list_map.append(cell1)
                # х кожен раз буде зростати на 31 піксель 
                x = x + 30.6
            #  у кожен раз буде зростати на 31 піксель   
            y = y + 30.6
            # х буде передавати значення у парамтр Х 
            x = self.X
    # Створюємо функцію для отримання натиску на будь-яку клавішу миші
    def check_attack(self, map, screen, list_ships):
        global turn
        rotate = 0
        #if list_ships == None:
            

        rotate += m_data.rotate_ships
        for cell1 in list_ships[0]:
           if map[cell1[3]].ATTACKED:
                m_data.rotate_ships = cell1[2]
                m_ships.ship.blit_sprite(screen, cell1[0], cell1[1])
                map[cell1[3]].block_cells(map, cell1[3], 1)
        for cell1 in list_ships[1]:
           
           if cell1[3] + turn(cell1[2]) < 100 and map[cell1[3]].ATTACKED and map[cell1[3] + turn(cell1[2])].ATTACKED:
                m_data.rotate_ships = cell1[2]
                m_ships.ship2.blit_sprite(screen, cell1[0], cell1[1])
                map[cell1[3]].block_cells(map, cell1[3], 1)
                map[cell1[3] + turn(cell1[2])].block_cells(map, cell1[3] + turn(cell1[2]), 1)
        for cell1 in list_ships[2]:
           
           if cell1[3] + turn(cell1[2]) + turn(cell1[2])  < 100 and map[cell1[3]].ATTACKED and map[cell1[3] + turn(cell1[2])].ATTACKED and map[cell1[3] + turn(cell1[2]) + turn(cell1[2])].ATTACKED:
                m_data.rotate_ships = cell1[2]
                m_ships.ship3.blit_sprite(screen, cell1[0], cell1[1])
                map[cell1[3]].block_cells(map, cell1[3], 1)
                map[cell1[3] + turn(cell1[2])].block_cells(map, cell1[3] + turn(cell1[2]), 1)
                # print(cell1[3]+ turn(cell1[2]), turn(cell1[2]))
                map[cell1[3] + turn(cell1[2]) + turn(cell1[2])].block_cells(map, cell1[3] + turn(cell1[2]) + turn(cell1[2]), 1)
        cell1 =list_ships[3]
        c = turn(cell1[2])
        if cell1[3] + c * 3 < 100 and map[cell1[3]].ATTACKED and map[cell1[3] + c].ATTACKED and map[cell1[3] + c * 2].ATTACKED and map[cell1[3] + c * 3].ATTACKED:
                m_data.rotate_ships = cell1[2]
                m_ships.ship4.blit_sprite(screen, cell1[0], cell1[1])
                map[cell1[3]].block_cells(map, cell1[3], 1)
                map[cell1[3] + c].block_cells(map, cell1[3] + c, 1)
                map[cell1[3] + c * 2].block_cells(map, cell1[3] + c * 2, 1)
                map[cell1[3] + c * 3].block_cells(map, cell1[3] + c * 3, 1)
        m_data.rotate_ships = rotate
    def attack(self, x = 0, y = 0, map = m_data.list_map2):
        for cell in map:
            if cell.X1 < x < cell.X2 and cell.Y1 < y < cell.Y2 and cell.ATTACKED != 1:
             cell.ATTACKED = 1
             if cell.NAME == 0 or cell.NAME == 5:
                m_data.turn = 1
             #print(cell.NAME, )
    def get_pressed(self, x, y, list_map, screen_game,): 
        # робимо цикл який буде рахувати клітинки у списку 
        if x  < 30 and y < 30:
            m_data.select_ship = 1
        if 100 < x < 160 and y < 30:
            m_data.select_ship = 2
        if 200 < x < 290 and y < 30:
            m_data.select_ship = 3
        if 300 < x < 420 and y < 30:
            m_data.select_ship = 4
        count = -1
        for cell in list_map: 
            count += 1
            # якщо клітинка по х1 менша за х та клітинка по х2 більша між х(Попадання в клітинку)
            plus = 1
            if m_data.rotate_ships % 180 != 0:
                plus = 10

            if cell.X1 < x and cell.X2 > x:
                # якщо клітинка по у1 менша за у та клітинка по у2 більша за у 
                check = 1
                if cell.Y1 < y and cell.Y2 > y:
                    for count1 in range(m_data.select_ship):
                        #print(count + (count1 * plus))
                        
                        if (count + (count1 * plus) > 99 or list_map[count + (count1 * plus)].NAME != 0) and plus == 10:
                            check = 0
                        elif (count + (count1 * plus) > 99 or list_map[count + (count1 * plus)].NAME != 0 or list_map[count + (count1 * plus)].ROW != list_map[count].ROW) and plus == 1:
                            check = 0
                    #тоді пишемо ім'я клітинки 
                            #print(cell.NAME) 
                    
                    if check:
                        if m_data.select_ship == 1 and m_data.count_ships[0] < 4:
                                cell.NAME = 1
                                m_data.count_ships[0] += 1
                                list_map[count + 0].block_cells(list_map, count + 0)
                                m_ships.ship.blit_sprite(screen_game, cell.X1, cell.Y1)
                                m_data.player_ships[0].append([cell.X1, cell.Y1, m_data.rotate_ships, count])
                                
                        if m_data.select_ship == 2  and m_data.count_ships[1] < 3:
                            if m_data.rotate_ships % 180 == 0:
                                cell.NAME = 2
                                m_data.count_ships[1] += 1
                                list_map[count + 1].NAME = 2
                                list_map[count + 1].block_cells(list_map, count + 1)
                                list_map[count + 0].block_cells(list_map, count + 0)
                                m_ships.ship2.blit_sprite(screen_game, cell.X1 , cell.Y1)
                            else:
                                cell.NAME = 2
                                m_data.count_ships[1] += 1
                                list_map[count + 1 * 10].NAME = 2
                                list_map[count + 1 * 10].block_cells(list_map, count + 1 * 10)
                                list_map[count + 0 * 10].block_cells(list_map, count + 0 * 10)
                                m_ships.ship2.blit_sprite(screen_game, cell.X1, cell.Y1)
                            m_data.player_ships[1].append([cell.X1, cell.Y1, m_data.rotate_ships, count])
                        if m_data.select_ship == 3 and m_data.count_ships[2] < 2:
                            m_data.count_ships[2] += 1
                            cell.NAME = 3 

                        

                            list_map[count + 1 * plus].NAME = 3
                            list_map[count + 2 * plus].NAME = 3
                            list_map[count + 2 * plus].block_cells(list_map, count + 2 * plus)
                            list_map[count + 1 * plus].block_cells(list_map, count + 1 * plus)
                            list_map[count + 0 * plus].block_cells(list_map, count + 0 * plus)
                            m_ships.ship3.blit_sprite(screen_game, cell.X1, cell.Y1)
                            m_data.player_ships[2].append([cell.X1, cell.Y1, m_data.rotate_ships, count])
                        if m_data.select_ship == 4 and m_data.count_ships[3] < 1:
                            cell.NAME = 4
                            m_data.count_ships[3] += 1
                            list_map[count + 1 * plus].NAME = 4
                            list_map[count + 2 * plus].NAME = 4 
                            list_map[count + 3 * plus].NAME = 4
                            list_map[count + 3 * plus].block_cells(list_map, count + 3 * plus)
                            list_map[count + 2 * plus].block_cells(list_map, count + 2 * plus)
                            list_map[count + 1 * plus].block_cells(list_map, count + 1 * plus)
                            list_map[count + 0 * plus].block_cells(list_map, count + 0 * plus)
                            m_ships.ship4.blit_sprite(screen_game, cell.X1, cell.Y1)
                            m_data.player_ships.append([cell.X1, cell.Y1, m_data.rotate_ships, count])
# створюємо об'єкт карти 1 з кординатами самої лівої клітинки таблиці 
map1 = Map(x1 = 139, y1 = 86)
# створюємо об'єкт карти 2 з кординатами самої лівої клітинки таблиці 
map2 = Map(x1 = 511, y1 = 87)


                    