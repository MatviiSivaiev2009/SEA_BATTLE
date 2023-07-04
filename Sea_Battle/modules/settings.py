# імортуємо пай гейм 
import pygame
# імпортуємо модуль серч пас у якуму знаходиться функція файнд пас 
import modules.search_path as m_path
# створюємо класс налаштувань
class Settings:
    # функція для опису об'єкта класса 
    def __init__(self, width = 0, height = 0, x = 0, y = 0, name = None, screen_game = None):
        # парамтр ширини дорівнює ширині 
        self.WIDTH = width
        # парамтр висоти дорівнює висоті 
        self.HEIGHT = height
        # парамтр координати х дорінює х
        self.X = x
        # парамтр координати у дорівнює х
        self.Y = y
        # парамтр ім'я файлу дорівнює ім'ю 
        self.NAME_FILE = name
        self.DIRECTION_L_R = False
        self.DIRECTION_U_D = False
    # створюємо функцію для загрузки картинки 
    def load_image(self, check_img = True):
        image_load = pygame.image.load(m_path.find_path(self.NAME_FILE))
        image_transform = pygame.transform.scale(image_load, (self.WIDTH, self.HEIGHT))
        if check_img:
            self.IMAGE = pygame.transform.flip(image_transform, flip_x= self.DIRECTION_L_R, flip_y= self.DIRECTION_U_D)
        else:
            return pygame.transform.flip(image_transform, flip_x= self.DIRECTION_L_R, flip_y= self.DIRECTION_U_D)
     
    # створюємо функцію для того щоб відообразити спрайт (картину) на єкрані 
    def blit_sprite(self, screen_game):
        # відоображення картинки на єкрані та координати відоображення 
        screen_game.blit(self.IMG, (self.X, self.Y))