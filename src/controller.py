import sys
import pygame
import settings


def keyboard_controller(scene):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed = pygame.key.get_pressed()

    # moving on scene
    if pressed[pygame.K_w] and not pressed[pygame.K_RSHIFT]:
        scene.move_objects_on_scene([0, 0, -settings.move_step])

    if pressed[pygame.K_s] and not pressed[pygame.K_RSHIFT]:
        scene.move_objects_on_scene([0, 0, settings.move_step])

    if pressed[pygame.K_a] and not pressed[pygame.K_RSHIFT]:
        scene.move_objects_on_scene([settings.move_step, 0, 0])

    if pressed[pygame.K_d] and not pressed[pygame.K_RSHIFT]:
        scene.move_objects_on_scene([-settings.move_step, 0, 0])

    # flying mode - go up and down
    if pressed[pygame.K_p]:
        scene.move_objects_on_scene([0, -settings.move_step, 0])

    if pressed[pygame.K_l]:
        scene.move_objects_on_scene([0, settings.move_step, 0])

    # scene rotating
    if pressed[pygame.K_UP]:
        scene.rotate_x_objects_on_scene(-settings.camera_tilt_angle_step)

    if pressed[pygame.K_DOWN]:
        scene.rotate_x_objects_on_scene(settings.camera_tilt_angle_step)

    if pressed[pygame.K_LEFT]:
        scene.rotate_y_objects_on_scene(settings.camera_tilt_angle_step)

    if pressed[pygame.K_RIGHT]:
        scene.rotate_y_objects_on_scene(-settings.camera_tilt_angle_step)

    if pressed[pygame.K_q]:
        scene.rotate_z_objects_on_scene(-settings.camera_tilt_angle_step)

    if pressed[pygame.K_e]:
        scene.rotate_z_objects_on_scene(settings.camera_tilt_angle_step)

    # Change the camera focus
    if pressed[pygame.K_m]:
        scene.change_camera_zoom(settings.camera_zoom_step)

    if pressed[pygame.K_n]:
        scene.change_camera_zoom(-settings.camera_zoom_step)

    # Change position of the light
    if pressed[pygame.K_w] and pressed[pygame.K_RSHIFT]:
        scene.rotate_light_x(settings.light_tilt_angle_step)

    if pressed[pygame.K_s] and pressed[pygame.K_RSHIFT]:
        scene.rotate_light_x(-settings.light_tilt_angle_step)

    if pressed[pygame.K_a] and pressed[pygame.K_RSHIFT]:
        scene.rotate_light_y(settings.light_tilt_angle_step)

    if pressed[pygame.K_d] and pressed[pygame.K_RSHIFT]:
        scene.rotate_light_y(-settings.light_tilt_angle_step)

    # Show / Hide the triangular boundary lines
    if pressed[pygame.K_o]:
        settings.sub_triangs_line_visible = not settings.sub_triangs_line_visible

    if pressed[pygame.K_i]:
        scene.light_source.actual_material.next()

