"""
Jackson Wolf (jtw3vhz) & Qasim Ali (qha4bh)

Game Details:
This is a platformer with two maps that you race against time to beat. We have two playable characters
(Sonic and Pikachu) with their own animations. The user will use the arrow keys to maneuver through the
maps. The maps are somewhat large and the camera moves with the user.

Optional Features:
    Multiple levels
    Scrolling levels
    Animations
    Timer

"""

import gamebox
import pygame

number_of_frames_run = 16
number_of_frames_fall = 4
camera = gamebox.Camera(800, 600)
sonic = gamebox.from_image(camera.x, camera.y, 'sonics.png')
sonic_run_sheet = gamebox.load_sprite_sheet("sonics_run.png", 1, 16)
sonic_run_sheet_left = gamebox.load_sprite_sheet('sonics_run_left.png', 1, 16)
sonic_idle_sheet = gamebox.load_sprite_sheet('sonics.png', 1, 1)
sonic_idle_sheet_left = gamebox.load_sprite_sheet('sonics_left.png', 1, 1)
sonic_jump_sheet = gamebox.load_sprite_sheet('sonic_jump.png', 1, 3)
sonic_jump_sheet_left = gamebox.load_sprite_sheet('sonic_jump_left.png', 1, 3)
sonic_in_air_sheet = gamebox.load_sprite_sheet('sonic_in_air.png', 1, 1)
sonic_in_air_sheet_left = gamebox.load_sprite_sheet('sonic_in_air_left.png', 1, 1)
sonic_fall = gamebox.load_sprite_sheet('sonic_fall.png', 1, 4)
sonic.scale_by(3)
temp_ground = gamebox.from_color(camera.x, camera.y + 200, 'green', 800, 100)
pikachu = gamebox.from_image(camera.x, camera.y, 'pikachus.png')
pikachu_idle_sheet = gamebox.load_sprite_sheet('pikachu_idle.png', 1, 1)
pikachu_idle_sheet_left = gamebox.load_sprite_sheet('pikachu_idle_left.png', 1, 1)
pikachu_in_air_sheet = gamebox.load_sprite_sheet('pikachu_in_air_right.png', 1, 4)
pikachu_in_air_sheet_left = gamebox.load_sprite_sheet('pikachu_in_air_left.png', 1, 4)
pikachu_run = gamebox.load_sprite_sheet('pikachu_run_right.png', 1, 4)
pikachu_run_left = gamebox.load_sprite_sheet('pikachu_run_left.png', 1, 4)
pikachu.scale_by(3)
coin = gamebox.from_image(5900, -850, 'coin.png')
coin2 = gamebox.from_image(1200, 20, 'coin.png')
coin_sheet = gamebox.load_sprite_sheet('coin_sheet.png', 1, 6)
coin_gone = False
coin.scale_by(1/2)
coin2.scale_by(1/2)
flag = gamebox.from_image(6900, -760, 'flag.png')
flag.scale_by(1/4)
flag2 = gamebox.from_image(1380, -500, 'flag.png')
flag2.scale_by(1/4)


timer = 360
timer_run = True

score_time = False


map_one_platformlist = [
    # Obstacles
    gamebox.from_color(2500, 240, 'blue', 50, 100),

    # Platforms
    gamebox.from_color(1000, 600, 'red', 600, 50),
    gamebox.from_color(800, 800, 'green', 800, 100),
    gamebox.from_color(2500, 300, 'red', 1500, 50),
    gamebox.from_color(3860, 300, 'purple', 800, 50),
    gamebox.from_color(3850, 500, 'purple', 1500, 50),
    gamebox.from_color(4500, 305, 'green', 100, 340),
    gamebox.from_color(4425, 320, 'blue', 50, 50),
    gamebox.from_color(5075, 160, 'red', 1250, 50),
    gamebox.from_color(6400, 160, 'red', 1050, 50),

    # Trap
    gamebox.from_color(5900, 430, 'red', 50, 540),
    gamebox.from_color(2950, 480, 'red', 50, 340),
    gamebox.from_color(4425, 675, 'blue', 3000, 50),

    # Parkour
    gamebox.from_color(5000, -25, 'blue', 150, 50),
    gamebox.from_color(5250, -150, 'blue', 50, 50),
    gamebox.from_color(5000, -250, 'blue', 50, 50),
    gamebox.from_color(5450, -400, 'blue', 450, 50),
    gamebox.from_color(5750, -600, 'blue', 20, 20),
    gamebox.from_color(5900, -760, 'blue', 20, 20),
    gamebox.from_color(6200, -550, 'blue', 20, 20),
    gamebox.from_color(6490, -550, 'blue', 100, 50),

    # Big boy Wall
    gamebox.from_color(6900, -240, 'orange', 100, 850),
    gamebox.from_color(6840, 0, 'blue', 20, 20),
    gamebox.from_color(6700, -150, 'blue', 20, 20),
    gamebox.from_color(6840, -300, 'blue', 20, 20),
    gamebox.from_color(6700, -450, 'blue', 20, 20),
    gamebox.from_color(6840, -600, 'blue', 20, 20),

    # Stairs
    gamebox.from_color(1450, 600, 'blue', 300, 50),
    gamebox.from_color(1500, 550, 'blue', 300, 50),
    gamebox.from_color(1550, 500, 'blue', 300, 50),
    gamebox.from_color(1600, 450, 'blue', 300, 50),
    gamebox.from_color(1650, 400, 'blue', 300, 50),
    gamebox.from_color(1700, 350, 'blue', 300, 50),
]

map_two_platformlist = [
    # Steps
    gamebox.from_color(700, 750, 'orange', 100, 100),
    gamebox.from_color(950, 700, 'orange', 75, 300),
    gamebox.from_color(1200, 550, 'orange', 75, 300),
    gamebox.from_color(1400, 400, 'orange', 75, 300),
    gamebox.from_color(1200, 150, 'orange', 75, 100),
    gamebox.from_color(950, 150, 'orange', 75, 450),
    gamebox.from_color(1200, -200, 'orange', 75, 100),
    gamebox.from_color(1400, -350, 'orange', 75, 100),

    # Platforms
    gamebox.from_color(400, 825, 'black', 400, 50),
    gamebox.from_color(800, 1000, 'black', 1600, 50),
    gamebox.from_color(25, 800, 'black', 50, 350),


]

s_input_list = [1]

s_frame_run = 0
s_frame_idle = 0
s_frame_fall = 0

p_input_list = [1]

p_frame_run = 0
p_frame_idle = 0
p_frame_fall = 0
coin_frame = 0
counter = 0
game_on = False
character_select = False
map_one = [gamebox.from_text(200, 400, 'Map 1', 70, 'white'), False]
map_two = [gamebox.from_text(600, 400, 'Map 2', 70, 'white'), False]
character_select_sonic = [gamebox.from_image(340, 500, 'sonics.png'), False]
character_select_pikachu = [gamebox.from_image(460, 500, 'pikachus.png'), False]
character_select_sonic[0].scale_by(3)
character_select_pikachu[0].scale_by(3)


def tick(keys):
    global s_frame_run
    global s_frame_idle
    global s_frame_fall
    global p_frame_run
    global p_frame_idle
    global p_frame_fall
    global counter
    global game_on
    global character_select
    global map_one
    global map_two
    global character_select_sonic
    global character_select_pikachu
    global coin_frame
    global timer
    global coin_gone
    global timer_run
    global score_time

    if not game_on:
        title = gamebox.from_text(400, 50, 'The Sonic and Pikachu ', 70, 'pink')
        title2 = gamebox.from_text(400, 110, "Tremondousnessly Ultimately Cool", 60, 'pink')
        title3 = gamebox.from_text(400, 175, "Gameplayer's Gigantic Gallopalooza", 60, 'pink')
        names = gamebox.from_text(400, 250, "By Qasim Ali (qha4bh) and Jackson Wolf (jtw3vhz)", 40, 'yellow')
        instructions = gamebox.from_text(400, 300, "The arrow keys are the only input required to play this game"
                                                   , 30, 'purple')
        instructions2 = gamebox.from_text(400, 325, "Using your mouse, Choose a map and then a character.", 30, 'purple')
        camera.draw(title), camera.draw(title2), camera.draw(title3),
        camera.draw(names), camera.draw(instructions), camera.draw(instructions2)
        if not character_select:
            if camera.mouseclick and 130 < camera.mousex < 270 and 360 < camera.mousey < 440:
                character_select = True
                map_one[1] = True
            if camera.mouseclick and 530 < camera.mousex < 670 and 360 < camera.mousey < 440:
                character_select = True
                map_two[1] = True

            camera.draw(map_one[0]), camera.draw(map_two[0])
            camera.display()

        if character_select:
            if camera.mouseclick and 300 < camera.mousex < 380 and 450 < camera.mousey < 600:
                game_on = True
                character_select_sonic[1] = True
            if camera.mouseclick and 420 < camera.mousex < 520 and 450 < camera.mousey < 600:
                game_on = True
                character_select_pikachu[1] = True

            camera.draw(character_select_sonic[0]), camera.draw(character_select_pikachu[0])
            camera.display()

    if map_one[1]:
        platformlist = map_one_platformlist
    if map_two[1]:
        platformlist = map_two_platformlist

    if game_on:
        for platform in platformlist:
            #sonic stuff
            if sonic.bottom_touches(platform):
                sonic.move_to_stop_overlapping(platform)
                sonic.yspeed = 0
                if pygame.K_RIGHT in keys:
                    sonic.xspeed = 5
                    sonic.move_speed()
                    if s_frame_run >= number_of_frames_run or s_frame_run < 0:
                        s_frame_run = 0
                    if counter % 3 == 0:
                        sonic.image = sonic_run_sheet[s_frame_run]
                    s_frame_run += 1
                    s_input_list.append(1)
                    s_input_list.reverse()
                    if pygame.K_UP in keys:
                        sonic.image = sonic_jump_sheet[2]
                        sonic.yspeed = -20
                elif pygame.K_LEFT in keys:
                    sonic.xspeed = -5
                    sonic.move_speed()
                    if s_frame_run <= 0 or s_frame_run > 15:
                        s_frame_run = 15
                    if counter % 3 == 0:
                        sonic.image = sonic_run_sheet_left[s_frame_run]
                    s_frame_run -= 1
                    s_input_list.append(0)
                    s_input_list.reverse()
                    if pygame.K_UP in keys:
                        sonic.image = sonic_jump_sheet_left[0]
                        sonic.yspeed = -20
                elif pygame.K_UP in keys:
                    if s_input_list.index(1) == 0:
                        sonic.image = sonic_jump_sheet[2]
                        sonic.yspeed = -20
                    else:
                        sonic.image = sonic_jump_sheet_left[0]
                        sonic.yspeed = -20
                elif s_input_list.index(1) == 0:
                    sonic.image = sonic_idle_sheet[0]
                    sonic.xspeed = 0
                else:
                    sonic.image = sonic_idle_sheet_left[0]
                    sonic.xspeed = 0
            #pikachu stuff
            if pikachu.bottom_touches(platform):
                pikachu.move_to_stop_overlapping(platform)
                pikachu.yspeed = 0
                if pygame.K_RIGHT in keys:
                    pikachu.xspeed = 5
                    pikachu.move_speed()
                    if p_frame_run >= 4 or p_frame_run < 0:
                        p_frame_run = 0
                    if counter % 5 == 0:
                        pikachu.image = pikachu_run[p_frame_run]
                    p_frame_run += 1
                    p_input_list.append(1)
                    p_input_list.reverse()
                    if pygame.K_UP in keys:
                        pikachu.image = pikachu_in_air_sheet[0]
                        pikachu.yspeed = -20
                elif pygame.K_LEFT in keys:
                    pikachu.xspeed = -5
                    pikachu.move_speed()
                    if p_frame_run <= 0 or p_frame_run > 3:
                        p_frame_run = 3
                    if counter % 5 == 0:
                        pikachu.image = pikachu_run_left[p_frame_run]
                    p_frame_run -= 1
                    p_input_list.append(0)
                    p_input_list.reverse()
                    if pygame.K_UP in keys:
                        pikachu.image = pikachu_in_air_sheet_left[3]
                        pikachu.yspeed = -20
                elif pygame.K_UP in keys:
                    if p_input_list.index(1) == 0:
                        pikachu.image = pikachu_in_air_sheet[0]
                        pikachu.yspeed = -20
                    else:
                        pikachu.image = pikachu_in_air_sheet_left[3]
                        pikachu.yspeed = -20
                elif p_input_list.index(1) == 0:
                    pikachu.image = pikachu_idle_sheet[0]
                    pikachu.xspeed = 0
                else:
                    pikachu.image = pikachu_idle_sheet_left[0]
                    pikachu.xspeed = 0
        #sonic air
        if sonic.yspeed < 0:
            if s_input_list.index(1) == 0:
                sonic.image = sonic_in_air_sheet[0]
            else:
                sonic.image = sonic_in_air_sheet_left[0]
            if pygame.K_LEFT in keys:
                sonic.xspeed = -5
            if pygame.K_RIGHT in keys:
                sonic.xspeed = 5

        if sonic.yspeed > 0:
            if s_frame_fall == number_of_frames_fall:
                s_frame_fall = 0
            if counter % 3 == 0:
                sonic.image = sonic_fall[s_frame_fall]
            s_frame_fall += 1
            if pygame.K_LEFT in keys:
                sonic.xspeed = -5
            if pygame.K_RIGHT in keys:
                sonic.xspeed = 5

        #pikachu air
        if pikachu.yspeed < 0:
            if p_input_list.index(1) == 0:
                pikachu.image = pikachu_in_air_sheet[0]
            else:
                pikachu.image = pikachu_in_air_sheet_left[3]
            if pygame.K_LEFT in keys:
                pikachu.xspeed = -5
            if pygame.K_RIGHT in keys:
                pikachu.xspeed = 5
        if pikachu.yspeed > 0:
            if p_frame_fall == 4:
                p_frame_fall = 0
            if counter % 3 == 0:
                pikachu.image = pikachu_in_air_sheet[p_frame_fall]
            p_frame_fall += 1
            if pygame.K_LEFT in keys:
                pikachu.xspeed = -5
            if pygame.K_RIGHT in keys:
                pikachu.xspeed = 5

        if character_select_sonic[1]:
            camera.x = sonic.x
            camera.y = sonic.y
        if character_select_pikachu[1]:
            camera.x = pikachu.x
            camera.y = pikachu.y

        if counter % 5 == 0:
            coin.image = coin_sheet[coin_frame]
            coin2.image = coin_sheet[coin_frame]
            coin_frame += 1
        if coin_frame > 5:
            coin_frame = 0
        if sonic.touches(coin) or pikachu.touches(coin):
            coin_gone = True
        if sonic.touches(coin2) or pikachu.touches(coin2):
            coin_gone = True

        if sonic.touches(flag) or pikachu.touches(flag):
            timer_run = False
            score_time = True

            score = timer
            if coin_gone:
                score = timer + 25
        if sonic.touches(flag2) or pikachu.touches(flag2):
            timer_run = False
            score_time = True

            score = timer
            if coin_gone:
                score = timer + 25

        counter += 1
        if timer_run:
            if counter % 60 == 0:
                timer -= 1
        if character_select_sonic[1]:
            timer_image = gamebox.from_text(sonic.x + 300, sonic.y - 250, str(timer), 40, 'black')
        if character_select_pikachu[1]:
            timer_image = gamebox.from_text(pikachu.x + 300, pikachu.y - 250, str(timer), 40, 'black')

        camera.clear('cyan')
        if character_select_sonic[1]:
            camera.draw(sonic)
        if character_select_pikachu[1]:
            camera.draw(pikachu)

        if map_one[1]:
            camera.draw(flag)
        if map_two[1]:
            camera.draw(flag2)

        if not coin_gone:
            if map_one[1]:
                camera.draw(coin)
            if map_two[1]:
                camera.draw(coin2)

        for platform in platformlist:
            camera.draw(platform)
            if sonic.right_touches(platform) or sonic.left_touches(platform):
                sonic.move_to_stop_overlapping(platform)
            if pikachu.right_touches(platform) or sonic.left_touches(platform):
                pikachu.move_to_stop_overlapping(platform)
            if sonic.top_touches(platform):
                sonic.yspeed = 0
            if pikachu.top_touches(platform):
                pikachu.yspeed = 0
        if score_time:
            if character_select_sonic[1]:
                score_back = gamebox.from_color(sonic.x, sonic.y, 'white', 325, 225)
                camera.draw(score_back)
                end_text = gamebox.from_text(sonic.x, sonic.y + 50, 'press ESC to quit', 40, 'black')
                score_show = gamebox.from_text(sonic.x, sonic.y, "Score: " + str(score), 60, 'black')
                camera.draw(end_text)
                camera.draw(score_show)
                gamebox.pause()
            if character_select_pikachu[1]:
                score_back = gamebox.from_color(pikachu.x, pikachu.y, 'white', 325, 225)
                camera.draw(score_back)
                end_text = gamebox.from_text(pikachu.x, pikachu.y + 50, 'press ESC to quit', 40, 'black')
                score_show = gamebox.from_text(pikachu.x, pikachu.y, "Score: " + str(score), 60, 'black')
                camera.draw(end_text)
                camera.draw(score_show)
                gamebox.pause()

        camera.draw(timer_image)
        pikachu.yspeed += 1
        sonic.yspeed += 1
        sonic.move_speed()
        pikachu.move_speed()
        camera.display()

ticks_per_second = 60

gamebox.timer_loop(ticks_per_second, tick)
