import pygame, sys
import random


def main():
    pygame.init()
    size = width, height = 1600, 800
    white = 255, 255, 255
    red = 255, 0, 0
    myfont = pygame.font.SysFont("monospace", 15)
    speed = 20

    screen = pygame.display.set_mode(size)

    line_1 = [(0, 0), (100, 100)]

    event_type = myfont.render("empty", 1, (255, 255, 0))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    event_type = myfont.render("Event type: Key UP", 1, (0, 0, 0))
                    line_1[0] = (line_1[0][0], line_1[0][1] - speed)
                    line_1[1] = (line_1[1][0], line_1[1][1] - speed)
                if event.key == pygame.K_DOWN:
                    event_type = myfont.render("Event type: Key DOWN", 1, (0, 0, 0))
                    line_1[0] = (line_1[0][0], line_1[0][1] + speed)
                    line_1[1] = (line_1[1][0], line_1[1][1] + speed)
                if event.key == pygame.K_RIGHT:
                    event_type = myfont.render("Event type: Key RIGHT", 1, (0, 0, 0))
                    line_1[0] = (line_1[0][0] + speed, line_1[0][1])
                    line_1[1] = (line_1[1][0] + speed, line_1[1][1])
                if event.key == pygame.K_LEFT:
                    event_type = myfont.render("Event type: Key LEFT", 1, (0, 0, 0))
                    line_1[0] = (line_1[0][0] - speed, line_1[0][1])
                    line_1[1] = (line_1[1][0] - speed, line_1[1][1])

        screen.fill(white)
        # draw line
        pygame.draw.line(screen, red, line_1[0], line_1[1], 5)
        screen.blit(event_type, (0, 0))
        pygame.display.flip()
        pygame.time.wait(50)  # give the CPU to the other programs too! :)


if __name__ == '__main__':
    main()
