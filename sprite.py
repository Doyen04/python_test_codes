import pygame
 
 
SIZE = WIDTH, HEIGHT = 600, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 10 #Frames per second
 
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
 
        self.images = []
        self.images.append(pygame.image.load('images\walk1.jpg'))
        self.images.append(pygame.image.load('images\walk2.jpg'))
        self.images.append(pygame.image.load('images\walk3.jpg'))
        self.images.append(pygame.image.load('images\walk4.jpg'))
        self.images.append(pygame.image.load('images\walk5.jpg'))
        self.images.append(pygame.image.load('images\walk6.jpg'))
 
        self.index = 0
 
        self.image = self.images[self.index]
        self.rect = pygame.Rect(100, 50, 250, 298)
 
    def update(self):
        self.index += 1
 
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                quit()
 
        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)
 
if __name__ == '__main__':
    main()