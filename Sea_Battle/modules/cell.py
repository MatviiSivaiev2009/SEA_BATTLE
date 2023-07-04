#імпортує пайгейм
import pygame 
#імпортує модуль сетінгс 
import modules.settings as m_settings
#імпортує модуль серч пас
import modules.search_path as m_path
#імпорткє модуль дата бейс
import modules.data_base as m_data

#створює класс селл
class Cell:
#задає значченя ініту
    def __init__(self, x1 , x2,  y1 , y2, name, row = 0):
#задає значення селф х1
        self.X1 = x1
#задає значення селф х2
        self.X2 = x2
#задає значення селф у1
        self.Y1 = y1
#задає значення селф у2
        self.Y2 = y2
#задає значення селф нейм
        self.ATTACKED = 0
        self.NAME = name
        self.ROW =  row
    def draw_cross(self, color, screen_game):
        pygame.draw.line(screen_game, color, [self.X1, self.Y1], [self.X2, self.Y2], width = 5)
        pygame.draw.line(screen_game, color, [self.X2, self.Y1], [self.X1, self.Y2], width = 5)
    def block_cells(self, list_map, count, att = 0):
        if not att:
            if count > 0 and list_map[count - 1].ROW == self.ROW and list_map[count - 1].NAME == 0:
                list_map[count - 1].NAME = 5
            if count + 1 < 100 and list_map[count + 1].ROW == self.ROW and list_map[count + 1].NAME == 0:
                list_map[count + 1].NAME = 5
            count -= 11
            for count1 in range(3):
                if -1 < count + count1 < 100 and list_map[count + count1].ROW == self.ROW - 1 and list_map[count + count1].NAME == 0:
                    list_map[count + count1].NAME = 5
            count += 20
            
            for count1 in range(3):
                #print(list_map[count + count1].ROW, self.ROW + 1)
                if -1 < count + count1 < 100 and list_map[count + count1].ROW == self.ROW + 1 and list_map[count + count1].NAME == 0:
                    list_map[count + count1].NAME = 5
        else:
            #print(count - 1, len(list_map))
            if count > 0 and list_map[count - 1].ROW == self.ROW and list_map[count - 1].ATTACKED == 0:
                list_map[count - 1].ATTACKED = 1
            if count + 1 < 100 and list_map[count + 1].ROW == self.ROW and list_map[count + 1].ATTACKED == 0:
                list_map[count + 1].ATTACKED = 1
            count -= 11
            for count1 in range(3):
                if -1 < count + count1 < 100 and list_map[count + count1].ROW == self.ROW - 1 and list_map[count + count1].ATTACKED == 0:
                    list_map[count + count1].ATTACKED = 1
            count += 20
            
            for count1 in range(3):
                #print(list_map[count + count1].ROW, self.ROW + 1)
                if -1 < count + count1 < 100 and list_map[count + count1].ROW == self.ROW + 1 and list_map[count + count1].ATTACKED == 0:
                    list_map[count + count1].ATTACKED = 1
                          