#功能：创建一个窗口，设置标题为"hello world"，并填充红色背景
import pygame
import sys


def setup():
    pygame.init()
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("hello world")
    screen.fill((255,0,0))
    return screen  

def main():
    screen = setup()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 0, 0))            
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()