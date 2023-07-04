# імпортуємо pygame
import pygame
# імпортуємо модуль де створена функція для пошуку шляхів
import modules.search_path as m_path
import modules.restart as m_restart
# ініціюємо pygame
pygame.init()
# створюємо клас кнопки
class Button:
    # створюємо функцію для налаштування класу Button
    def __init__(self, x, y): 
      # параметр ширини
      self.WIDTH = 400
      # параметр висоти 
      self.HEIGHT = 100
      # параметр координату х
      self.X = x
      # параметр координату у
      self.Y = y
    # створюємо функцію завантаження зображення
    
    def load_image(self):
        # локальна змінна картинки яка завантажує картинку за допомогою функції load
        image_button = pygame.image.load(
          # за допомогою функції find_path показуємо шлях до нашої картинки
           m_path.find_path('images/buttons/button.png')
        )
        # трансформує картинку
        img_transform = pygame.transform.scale(image_button, (self.WIDTH, self.HEIGHT))
        # повертає значення img_transform у функцію
        return img_transform
    #  створюємо функцію для відображення спрайтів
    def blit_sprite(self, screen_game):
       # звертаємось до аргументу screen_game та функції blit щоб завантажити картинку 
       screen_game.blit(self.load_image(), (self.X, self.Y))
# створюємо об'єкт кнопки який зберігає в собі значення класу Button 
    def button_pressed(self, pos, screen_game):
       if self.X < pos[0] and self.Y < pos[1]:
          if self.X + self.WIDTH > pos[0] and self.Y + self.HEIGHT > pos[1]:
             m_restart.restart(screen_game, self)
       
button = Button(x = 300, y = 460)