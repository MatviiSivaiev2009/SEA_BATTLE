
import pygame,  modules.settings as m_settings, modules.search_path as m_path, modules.data_base as m_data 

pygame.init()

# 1 = one deck ship - width = 32, heigth = 32
# 2 = two deck ship - width = 64, heigth = 32 
# 3 = three deck ship - width = 96, heigth = 32
# 4 = four deck ship - width = 128, heigth = 32
#def block():
     
class Ship():
    
      def __init__(self , x , y, cells = None):
          self.WIDTH = 27
          self.HEIGHT = 28
          self.X = x
          self.Y = y
          self.DIRECTION_L_R = False
          self.DIRECTION_U_D = False
          self.ROTATE=None
          self.CELLS = cells
      def load_image(self,rotate=None):
          #print(rotate,-98)
          if rotate==None:
              rotate=m_data.rotate_ships
          image_load = pygame.image.load(m_path.find_path('images/ships/one_deck_ship.png'))
          img_transform = pygame.transform.scale(image_load, (self.WIDTH, self.HEIGHT))
          #print(rotate,-999)
      #     if check_img:
      #       self.IMAGE = pygame.transform.flip(image_transform, flip_x= self.DIRECTION_L_R, flip_y= self.DIRECTION_U_D)
      #     else:
          return pygame.transform.rotate(img_transform, rotate) 
      
      def blit_sprite(self, screen_game, x, y):
            
          self.X = x
          
          self.Y = y
          
          screen_game.blit(self.load_image(self.ROTATE), (self.X, self.Y))

ship = Ship(x =139, y = 86)    


class Ship2():
   def __init__(self,width = 63,height = 31, x = 0 , y = 0, cells = None):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.CELLS = cells
   def load_image(self,rotate=None):
      if rotate==None:
              rotate=m_data.rotate_ships
      image_ship2 = pygame.image.load(m_path.find_path('images/ships/two_deck_ship.png'))

      img_transform = pygame.transform.scale(image_ship2, (self.WIDTH, self.HEIGHT))
      
      # pygame.transform.rotate(img_transform, m_data.rotate_ships) 

      return pygame.transform.rotate(img_transform, rotate) 
     
   def blit_sprite(self, screen_game, x, y):
         self.X = x
         self.Y = y
         screen_game.blit(self.load_image(), (self.X, self.Y))  
            
ship2 = Ship2(x = 139, y = 86)           
   
class Ship3:
   def __init__(self, width = 96, height = 32, x = 0 , y = 0, cells = None):
       self.WIDTH = width 
       self.HIGTH = height
       self.X = x
       self.Y = y
       self.CELLS = cells
   def load_image(self,rotate=None):
         if rotate==None:
              rotate=m_data.rotate_ships
         image_ship3 = pygame.image.load(
           m_path.find_path('images/ships/three_deck_ship_1.png')
           )
           
         img_transform = pygame.transform.scale(image_ship3, (self.WIDTH, self.HIGTH))
      #    pygame.transform.rotate(img_transform, m_data.rotate_ships) 
         return pygame.transform.rotate(img_transform, rotate) 
     
   def blit_sprite(self, screen_game, x, y):
         self.X = x
         self.Y = y
         screen_game.blit(self.load_image(), (self.X, self.Y))  
            
ship3 = Ship3(x = 139, y = 86)   
       
class Ship4():
   def __init__(self, height = 32, width = 128, x = 0 , y = 0, cells = None):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.CELLS = cells
   def load_image(self,rotate=None):
         if rotate==None:
              rotate=m_data.rotate_ships
         image_ship4 = pygame.image.load(m_path.find_path('images/ships/four_deck_ship.png'))
         img_transform = pygame.transform.scale(image_ship4, (self.WIDTH, self.HEIGHT))
      #    pygame.transform.rotate(img_transform, m_data.rotate_ships) 
         return pygame.transform.rotate(img_transform, rotate) 
     
   def blit_sprite(self, screen_game, x, y):
         self.X = x
         self.Y = y
         screen_game.blit(self.load_image(), (self.X, self.Y))  
            
ship4 = Ship4(x = 139, y = 86)            