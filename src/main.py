import pygame
from controller import keyboard_controller
from scenes.objects.cuboid import Cuboid

import settings
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
        pygame.time.wait(20)  # give the CPU to the other programs too! :)


def build_scene():
    scene = Scene()
    tower_1 = Cuboid(100, 300, 100, start_point=[-200, -50, 150], color=(128, 110, 74))
    sphere_1 = Spheroid(100, 100, 100, start_point=[100, 100, 100], resolution=20)

    scene.add_object(tower_1)
    scene.add_object(sphere_1)

    return scene


if __name__ == '__main__':
    main()
