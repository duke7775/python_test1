#功能：创建一个窗口，设置标题为"hello world"，并填充红色背景
import pygame


def setup():
    pygame.init()
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("hello world")
    screen.fill((255,0,0))
    return screen  

def main():
    screen = setup()
    pygame.display.flip()
    

if __name__ == "__main__":
    main()