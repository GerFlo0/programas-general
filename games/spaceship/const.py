TEXTURES = {
    "screen":"imgs/bg.jpeg",
    "player":"imgs/player_ship.png",
    "player_1":"imgs/player_ship_1.png",
    "player_2":"imgs/player_ship_2.png",
    "player_3":"imgs/player_ship_3.png",
    "player_hurt":"imgs/player_ship_hurt.png",
    "boss":"imgs/boss.png",
    "boss_1":"imgs/boss_1.png",
    "boss_2":"imgs/boss_2.png",
    "boss_3":"imgs/boss_3.png",
    "boss_hurt":"imgs/boss_3.png",
    "player_bullet":"imgs/player_bullet.png",
    "boss_bullet":"imgs/enemy_bullet.png",
    "meteor":"imgs/meteor.png",
    "meteor_1":"imgs/meteor_1.png",
    "meteor_2":"imgs/meteor_2.png",
    "meteor_3":"imgs/meteor_3.png",
    "player_heart":"imgs/heart.png",
    "boss_heart":"imgs/boss_heart.png",
    "icon":"imgs/player_ship.png",
    "menu_txt":"imgs/txt/menu.png",
    "game_over_txt":"imgs/txt/game_over.png",
    "exit_txt":"imgs/txt/exit.png",
    "win_txt":"imgs/txt/win.png"
}

SIZES = {
    "screen":(800,600),
    "player":(40,40),
    "boss":(170,150),
    "boss_bullet":(20,40),
    "player_bullet":(10,20),
    "meteor":(60,60),
    "player_heart":(30,30),
    "boss_heart":(20,15),
    "menu_txt":(600,200),
    "exit_txt":(600,200),
    "game_over_txt":(600,200),
    "win_txt":(600,200)
}

VELS = {
    "player_vel":5,
    "boss_vel":3,
    "player_bullet_vel":-10,
    "player_bullet_cad":20,
    "boss_bullet_vel":5,
    "boss_bullet_cad":40,
    "meteor_vel":6,
    "meteor_cad_1":30,
    "meteor_cad_2":20,
    "meteor_cad_3":10
}

CANNONS = {
    "player":2,
    "boss":3
}

HEARTS = {
    "player":3,
    "boss":20
}

SOUNDS = {
    "boss_dead":"sounds/boss_dead.mp3",
    "player_dead":"sounds/player_dead.mp3",
    "laser":"sounds/laser.mp3",
    "player_damage":"sounds/player_damage.mp3",
    "meteor_dead":"sounds/meteor_dead.mp3",
    "boss_hit":"sounds/boss_hit.mp3"
}

MUSIC = {
    "ambient":"music/ambient.mp3",
    "boss_fight":"music/boss_fight.mp3",
    "menu":"music/menu.mp3"
}

BULLETS_SPAWN = (SIZES["screen"][0]+10, SIZES["screen"][1]+10)
BOSS_SPAWN = (-SIZES["boss"][0]-10, 30)
METEORS_SPAWN = (SIZES["screen"][0]+10, 0)
METEORS_POSS = [i for i in range(SIZES["screen"][0] - SIZES["meteor"][0]) if i%30 == 0]
METEORS_DYING_DURATION = 7
PLAYER_SPAWN = (380,540)
HEARTS_POS = [(15,555), (45,555), (75,555)]
BOSS_HEARTS_POS = [(i,10) for i in range(800) if i%20==0]
FPS = 60