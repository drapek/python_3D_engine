import pygame

from core import settings
from core.controller import keyboard_controller
from core.scenes.scene import Scene
from core.scenes.objects.cuboid import Cuboid


def main():
    pygame.init()
    screen = pygame.display.set_mode(settings.screen_size)
    scene = build_scene()

    while 1:
        keyboard_controller(scene)  # transform objects position in scene coordinate system
        screen.fill((255, 255, 255))
        scene.draw_scene_in_2d(screen)  # Translate scene coordinates to camera coordinates, and project it
        pygame.display.flip()
        pygame.time.wait(50)  # give the CPU to the other programs too! :)


def build_scene():

    scene = Scene()
    tower_1 = Cuboid(100, 300, 100, start_point=[-200, -50, 150])
    tower_2 = Cuboid(200, 0, 300, start_point=[-100, -50, 150])
    tower_3 = Cuboid(100, 200, 200, start_point=[100, -50, 250])

    scene.add_object(tower_1)
    scene.add_object(tower_2)
    scene.add_object(tower_3)

    return scene


if __name__ == '__main__':
    main()
