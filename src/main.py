import pygame

import settings
from controller import keyboard_controller
from scenes.light import Light
from scenes.objects.spheorid import Spheroid
from scenes.scene import Scene


def main():
    pygame.init()
    screen = pygame.display.set_mode(settings.screen_size)
    scene = build_scene()

    while 1:
        keyboard_controller(scene)  # transform objects position in scene coordinate system
        screen.fill(settings.background_color)
        scene.draw_scene_in_2d(screen)  # Translate scene coordinates to camera coordinates, and project it
        pygame.display.flip()
        pygame.time.wait(1)  # give the CPU to the other programs too! :)


def build_scene():
    scene = Scene(light_source=Light())
    sphere_1 = Spheroid(100, 100, 100, start_point=[0, 0, 200], resolution=40)

    scene.add_object(sphere_1)

    return scene


if __name__ == '__main__':
    main()
