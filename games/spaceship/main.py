import pygame, classes, const, random, math

def check_colision(obj1, obj2):
    return obj1.live and obj2.live and obj1.center[0]in range(obj2.x, obj2.x+obj2.size[0]) and obj1.y in range(obj2.y, obj2.y+obj2.size[1])

#pygame initialization
pygame.init()

#screen setup
screen = pygame.display.set_mode(const.SIZES["screen"])
GAME_BACKGROUND = pygame.image.load(const.TEXTURES["screen"]).convert()
screen.blit(GAME_BACKGROUND, (0, 0))
pygame.display.set_caption("Space ship by GigaGero with froggy04a")
pygame.display.set_icon(pygame.image.load(const.TEXTURES["icon"]).convert_alpha())
pygame.display.flip()

#sound efects
pygame.mixer.set_num_channels(10)

#sound efects: loads
sound_boss_dead = pygame.mixer.Sound(const.SOUNDS["boss_dead"])
sound_laser = pygame.mixer.Sound(const.SOUNDS["laser"])
sound_meteor_dead = pygame.mixer.Sound(const.SOUNDS["meteor_dead"])
sound_player_damage = pygame.mixer.Sound(const.SOUNDS["player_damage"])
sound_player_dead = pygame.mixer.Sound(const.SOUNDS["player_dead"])
sound_boss_hit = pygame.mixer.Sound(const.SOUNDS["boss_hit"])

#sound efects: volume
sound_boss_dead.set_volume(0.9)
sound_laser.set_volume(0.4)
sound_meteor_dead.set_volume(0.3)
sound_player_damage.set_volume(0.6)
sound_player_dead.set_volume(0.9)
sound_boss_hit.set_volume(1.0)

#txt loads
menu_txt = classes.Txt("menu_txt").img
exit_txt = classes.Txt("exit_txt").img
game_over_txt = classes.Txt("game_over_txt").img
win_txt = classes.Txt("win_txt").img

replay = True
menu = True

while replay:
    
    #vars
    #vars: whiles
    run = True
    end = True
    win = False
    
    screen.blit(GAME_BACKGROUND, (0,0))
    pygame.display.flip()
    
    #player stuff
    player = classes.Player_ship(const.PLAYER_SPAWN[0], const.PLAYER_SPAWN[1], "player")
    player_bullets = [classes.General(const.BULLETS_SPAWN[0], const.BULLETS_SPAWN[1], "player_bullet", False) for i in range(10)]
    player_hearts = [classes.Sprite(const.HEARTS_POS[i][0], const.HEARTS_POS[i][1], "player_heart") for i in range(const.HEARTS["player"])]
    
    #boss stuff
    boss = classes.Boss_ship(const.BOSS_SPAWN[0], const.BOSS_SPAWN[1], "boss")
    boss_bullets = [classes.General(const.BULLETS_SPAWN[0], const.BULLETS_SPAWN[1], "boss_bullet", False) for i in range(6)]
    boss_hearts = [classes.Sprite(const.BOSS_HEARTS_POS[i][0], const.BOSS_HEARTS_POS[i][1], "boss_heart") for i in range (2 * const.HEARTS["boss"])]
    
    #meteors
    meteors = [classes.Meteor(const.METEORS_SPAWN[0], const.METEORS_SPAWN[1], "meteor", False) for i in range(15)]
    
    #vars: misc
    boss_right = True
    boss_music = True
    boss_fase_2 = True
    boss_fase_3 = True
    og_boss_hearts = boss.hearts
    player_cannon = 0
    meteor_cad = 0
    ang = 0
    boss_y = boss.y
    
    #vars: time
    frame = 1
    sec = 0
    min = 0
    clock = pygame.time.Clock()
    
    #menu music
    pygame.mixer_music.load(const.MUSIC["menu"])
    pygame.mixer_music.play(-1,0,1000)
    
    #menu while
    while menu:
        screen.blit(menu_txt,(100,200))
        pygame.display.flip()
        
        #start playing
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]: 
            menu = False
        
        #exit menu/game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                menu = False
                run = False
                replay = False
                end = False
        
        clock.tick(const.FPS)
    
    #game music
    pygame.mixer_music.load(const.MUSIC["ambient"])
    pygame.mixer_music.play(-1,0,1000)
    
    #game while
    while run and not win:
        #refresing player/boss img
        if player.hearts > 2:
            player_img = player.img
        elif player.hearts > 1:
            player_img = player.img_damaged[0]
        else:
            player_img = player.img_damaged[1]
        
        if boss.hearts >= og_boss_hearts*.66:
            boss_img = boss.img
        elif boss.hearts >= og_boss_hearts*.33:
            boss_img = boss.img_damaged[0]
        else:
            boss_img = boss.img_damaged[1]
        
        #keys pressed and player: movement
        keys = pygame.key.get_pressed()
        player.move(keys)
        
        #exit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: 
                run = False
                replay = False
                end = False
        
        #player: shoot
        if not keys[pygame.K_RSHIFT]:
            shoot_frame = 1
        else:
            if shoot_frame == 1:
                #choosing cannon
                if player_cannon == 0: player_cannon = 1
                elif player_cannon == 1: player_cannon = 0
                
                #shooting
                player.shoot(player_bullets, player_cannon)
                pygame.mixer.find_channel(True).play(sound_laser)
            
            if shoot_frame < player.bull_cad:
                shoot_frame += 1
            else:
                shoot_frame = 1
        
        #meteors cadence
        if sec < 10: meteor_cad = const.VELS["meteor_cad_1"]
        elif sec < 20: meteor_cad = const.VELS["meteor_cad_2"]
        elif sec < 40: meteor_cad = const.VELS["meteor_cad_3"]
        else: meteor_cad = const.VELS["meteor_cad_2"]
        
        #cleaning screen
        screen.blit(GAME_BACKGROUND,(0,0))
        
        #player bullets
        for bullet in player_bullets:
            if bullet.live:
                #player bullets: moving
                bullet.move_to(bullet.x, bullet.y+bullet.vel)
                bullet.draw(bullet.img, screen)
                
                #player bulllets: collision with meteors
                for meteor in meteors:
                    if check_colision(bullet, meteor):
                        meteor.live = False
                        meteor.dying =  0
                        
                        bullet.move_to(const.METEORS_SPAWN[0], const.METEORS_SPAWN[1])
                        bullet.live = False
                        
                        pygame.mixer.find_channel(True).play(sound_meteor_dead)
                
                #player bulllets: collision with boss
                if check_colision(bullet, boss):
                        bullet.move_to(const.BULLETS_SPAWN[0], const.BULLETS_SPAWN[1])
                        bullet.live = False
                        boss.hearts -= 1
                        boss_img = boss.img_hurt
                        if boss.hearts > 0:
                            pygame.mixer.find_channel(True).play(sound_boss_hit)
                        else:
                            pygame.mixer.find_channel(True).play(sound_boss_dead)
            
            #player bullets: restart
            if bullet.y < 0:
                bullet.move_to(const.BULLETS_SPAWN[0], const.BULLETS_SPAWN[1])
                bullet.live = False
        
        #boss bullets
        for bullet in boss_bullets:
            #boss bullets: movement
            if bullet.live:
                bullet.move_to(bullet.x, bullet.y+bullet.vel)
                bullet.draw(bullet.img, screen)
            
            #boss bullets: restart
            if bullet.y > const.SIZES["screen"][1]:
                bullet.move_to(const.BULLETS_SPAWN[0], const.BULLETS_SPAWN[1])
                bullet.live = False
        
        #meteors spawning
        for meteor in meteors:
            if  frame%meteor_cad == 0 and not meteor.live:
                meteor.live = True
                meteor.move_to(random.choice(const.METEORS_POSS),-meteor.size[1])
                break
        
        #meteors
        for meteor in meteors:
            #meteors: movement
            if meteor.live:
                meteor.move_to(meteor.x, meteor.y+meteor.vel)
                meteor.draw(meteor.img, screen)
                
            elif meteor.dying < 3:
                meteor.draw(meteor.img_hurt[meteor.dying], screen)
                meteor.dying_counter += 1
                
                if meteor.dying_counter == const.METEORS_DYING_DURATION:
                    meteor.dying_counter = 0
                    meteor.dying +=1
                
            else:
                meteor.move_to(const.METEORS_SPAWN[0], const.METEORS_SPAWN[1])
                meteor.dying = -1
                
            #meteors: collision with player
            if check_colision(player, meteor):
                meteor.move_to(const.METEORS_SPAWN[0], const.METEORS_SPAWN[1])
                meteor.live = False
                player.hearts -= 1
                player_img = player.img_hurt
                
                if player.hearts > 0:
                    pygame.mixer.find_channel(True).play(sound_player_damage)
                else:
                    pygame.mixer.find_channel(True).play(sound_player_dead)
            
            #meteors: restart
            if meteor.y > const.SIZES["screen"][1]:
                meteor.move_to(const.METEORS_SPAWN[0], const.METEORS_SPAWN[1])
                meteor.live = False
        
        #boss
        if sec > 40:
            #boss: music start
            if boss_music:
                boss_music = False
                pygame.mixer_music.load(const.MUSIC["boss_fight"])
                pygame.mixer_music.play(-1,0,1000)
            
            #boss: movement: side to move
            if boss.x > const.SIZES["screen"][0]-boss.size[0]: boss_right=False
            elif boss.x < 0: boss_right=True
            
            #boss: movement: speed
            if boss.hearts < og_boss_hearts*0.66 and boss_fase_2:
                boss_fase_2 = False
                boss.vel += 2
            
            if boss.hearts < og_boss_hearts*0.33 and boss_fase_3:
                boss_fase_3 = False
                boss.vel += 2
            
            #boss: movement
            if boss_right:
                boss.move(boss.x+boss.vel, boss_y+int(50*math.sin(math.radians(ang))))
            else:
                boss.move(boss.x-boss.vel, boss_y+int(50*math.sin(math.radians(ang))))
            
            #boss: shooting
            if frame%boss.bull_cad == 0:
                boss.shoot(boss_bullets, 0)
                boss.shoot(boss_bullets, 1)
                boss.shoot(boss_bullets, 2)
            
            #boss: colision with player
            if check_colision(player, boss):
                player.hearts = 0
                pygame.mixer.find_channel(True).play(sound_player_dead)
            
            #boss: bullets
            for bullet in boss_bullets:
                #boss: bullets: movement
                if bullet.live:
                    bullet.draw(bullet.img, screen)
                    bullet.move_to(bullet.x, bullet.y+bullet.vel)
                    
                    #boss: bullet: colision with player
                    if check_colision(bullet, player):
                        bullet.move_to(const.BULLETS_SPAWN[0], const.BULLETS_SPAWN[1])
                        bullet.live = False
                        player.hearts-=1
                        player_img = player.img_hurt
                        if player.hearts > 0:
                            pygame.mixer.find_channel(True).play(sound_player_damage)
                        else:
                            pygame.mixer.find_channel(True).play(sound_player_dead)
                
                #boss: bullet: restart
                if bullet.y > const.SIZES["screen"][1]:
                    bullet.move_to(const.BULLETS_SPAWN[0], const.BULLETS_SPAWN[1])
                    bullet.live = False
            
            #boss: drawing
            if boss.hearts == 0:
                boss_img = boss.img_damaged[2]
            
            boss.draw(boss_img, screen)
            
            #boss: hearts
            for i in range(boss.hearts):
                boss_hearts[20+i].draw(boss_hearts[20+i].img, screen)
                boss_hearts[19-i].draw(boss_hearts[19-i].img, screen)
        
        #player: hearts
        for i in range(player.hearts):
            player_hearts[i].draw(player_hearts[i].img, screen)
        
        #player: drawing
        if player.hearts < 1:
            player_img = player.img_damaged[2]
        
        player.draw(player_img, screen)
        
        #screen update
        pygame.display.flip()
        
        if player_img == player.img_hurt:
            pygame.time.delay(200)
        
        #time: managment
        frame += 1
        if frame == 61:
            frame = 1
            sec += 1
        if sec == 300:
            run = False
        
        #player/boss: hearts managment
        if player.hearts < 1:
            run = False
        
        if boss.hearts < 1:
            win = True
        
        ang +=3
        if ang >360: ang = 1
        
        #screen: frames per second
        clock.tick(const.FPS)
    
    #menu music play
    pygame.mixer_music.load(const.MUSIC["menu"])
    pygame.mixer_music.play(-1, 0, 1000)
    
    #end: while
    while end:
        #win/lose: managment
        if win:
            screen.blit(win_txt, (100, 100))
        else:
            screen.blit(game_over_txt, (100,  100))
        
        screen.blit(pygame.transform.scale(exit_txt, (400, 200)), (0, 300))
        screen.blit(pygame.transform.scale(menu_txt, (400, 200)), (375, 300))
        
        keys = pygame.key.get_pressed()
        
        #exit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                end = False
                replay = False
        
        #replay
        if keys[pygame.K_RETURN]:
            end = False
            replay = True
        
        pygame.display.flip()
        clock.tick(const.FPS)

#pygame off
pygame.quit()