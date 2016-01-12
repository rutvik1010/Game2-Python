__author__ = 'Rutvik'
import pygame
import time
import random
import os

screen_x = 200
screen_y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_x,screen_y)
pygame.init()
display_size = (1080,720)
game_display = pygame.display.set_mode(display_size)
pygame.display.set_caption("Copter Chase")
clock = pygame.time.Clock()
controls_image = pygame.image.load("wasd.png")
missile_image = pygame.image.load("missile-war-weapon_318-48046.png")
crash_sound = pygame.mixer.Sound("Smashing-Yuri_Santana-1233262689.wav")
pygame.mixer.music.load("Piano_Desire.wav")

#Copter Values
copter_image = pygame.image.load("copter2.png")
copter_width = 100
copter_height = 75

#Sound Files
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
wood = (139,35,35)
bg = (61,89,171)


def missile_display(x,y):
    game_display.blit(missile_image,(x,y))


def controls_display():
    game_display.blit(controls_image,(400,20))


def copter_display(image1, x ,y):
    game_display.blit(image1, (x, y))


def title_text_function(text, font, color):
    title_text_surface = font.render(text, True, color)
    return title_text_surface, title_text_surface.get_rect()


def button_text(text, font, color):
    buttontext_surf = font.render(text,True, color)
    return buttontext_surf, buttontext_surf.get_rect()


def title_screen(text, color):
    title_s_font = pygame.font.SysFont("comicsansms", 120)
    title_s_surf, title_s_rect = title_text_function(text, title_s_font, color)
    title_s_rect.center = ((display_size[0]/2), display_size[1]/2)
    game_display.blit(title_s_surf, title_s_rect)

def credits_object(text,font):
    cre_surf = font.render(text, True, white)
    return cre_surf, cre_surf.get_rect()

def game_credits(text):
    credits_font = pygame.font.SysFont("comicsansms", 15)
    credits_surf, credits_rect = credits_object(text, credits_font)
    credits_rect.center = (80, 10)
    game_display.blit(credits_surf, credits_rect)

def buttons(color_rect,x,y,w,h,button_font_size,text,color_font):
    pygame.draw.rect(game_display,color_rect,(x,y,w,h))
    button_font = pygame.font.Font("freesansbold.ttf", button_font_size)
    button_surf, button_rect = button_text(text,button_font,color_font)
    button_rect.center = (x+(w/2), y+(h/2))
    game_display.blit(button_surf, button_rect)


def score_text_function(text_sc, font, color):
    score_text_f = font.render("Score: " + text_sc, True,color )
    return score_text_f,score_text_f.get_rect()


def display_score(text_sc,font_sc,color):
    score_text = pygame.font.SysFont("comicsansms",20)
    score_text_surf, score_text_rect = score_text_function(text_sc,score_text, color)
    score_text_rect.center = (50,20)
    game_display.blit(score_text_surf,score_text_rect)

def crash_message():
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(crash_sound)
            game_display.fill(black)
            crash_text1 = pygame.font.SysFont("comnicsansms", 30)
            crash_text1_surf, crash_text1_rect = title_text_function("You Crashed :(", crash_text1, white)
            crash_text1_rect.center = (540, 620)
            game_display.blit(crash_text1_surf, crash_text1_rect)



def game_loop():
    pygame.mixer.music.play(-1)
    game_value = True
    copter_x = 100
    copter_y = 250
    altitude_change = 0
    horizontal_change =0
    score = 0
    top_obs_x = random.randrange(1100, 1400)
    top_obs_y = 110
    top_obs_height = random.randrange(110,260)
    bot_obs_x = random.randrange(1100, 1400)
    bot_obs_y = random.randrange(450,600)
    bot_obs_height = 600 - bot_obs_y
    obs_width = random.randrange(50,90)
    obs_speed = 4
    missile_x = 1200
    missile_y = random.randrange(220,580)
    missile_speed = 6
    missile_height = 100
    missile_width = 100
    copter_mis_x = copter_x+copter_width
    copter_mis_y = copter_y+copter_height
    missile_launch = False
    crash = False
    while game_value:
        copter_mouse_pos = pygame.mouse.get_pos()
        copter_mouse_click= pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    altitude_change -= 4
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    altitude_change += 4
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    horizontal_change += 5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    horizontal_change -= 5
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_v:
                        missile_launch = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    altitude_change = 0
                if event.key == pygame.K_s:
                    altitude_change = 0
                if event.key == pygame.K_d:
                    horizontal_change = 0
                if event.key == pygame.K_a:
                    horizontal_change = 0
                if event.key == pygame.K_v:
                    missile_launch = True
        copter_y += altitude_change
        copter_x += horizontal_change
        game_display.fill(bg)
#TOP OBSTACLES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        pygame.draw.rect(game_display, black, (0,0,1080, 110))
        pygame.draw.rect(game_display,wood, (top_obs_x,top_obs_y,obs_width, top_obs_height))
        top_obs_x -= obs_speed
#BOTTOM OBSTACLES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        pygame.draw.rect(game_display, black, (0, 600, 1080, 150))
        pygame.draw.rect(game_display,wood, (bot_obs_x,bot_obs_y,obs_width, bot_obs_height))
        bot_obs_x -= obs_speed
#GENERATING N OBSTACLES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if top_obs_x+obs_width < 0 :
            top_obs_x = random.randrange(1100, 1400)
            top_obs_height = random.randrange(110,240)
            score += 1
        if bot_obs_x + obs_width <0:
            bot_obs_x = random.randrange(1100, 1400)
            bot_obs_y = random.randrange(450,600)
            bot_obs_height = 600 - bot_obs_y
            score += 1
        score_str = str(score)
#GENERATING RECT BLOCKS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        missile_x = missile_x - missile_speed
        missile_display(missile_x, missile_y)
#GENERATING N RECT BLOCKS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if missile_x < 0:
            missile_x = 1200
            missile_y = random.randrange(220,580)
#GENERATE COPTER MISSILE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if missile_launch == True:
            pygame.draw.circle(game_display,black,(copter_mis_x,copter_mis_y),8,0)
            copter_mis_x +=6
        if copter_mis_x > 1080:
            missile_launch = False
            copter_mis_x = copter_x + copter_width
            copter_mis_y = copter_y + copter_height
#DETECTING COLLISIONS WITH WALL AND TOP/BOTTOM OBSTACLES~~~~~~~~~~~~~~~~~~~~~~~~
        if copter_x < 0:
            crash_message()
            game_value = False
        if copter_y + 50 < 110:
            crash_message()
            game_value = False
        if copter_y + 50 + copter_height > 600:
             crash_message()
             game_value = False
        if copter_y - 20 <= top_obs_height + 50 and top_obs_x-60 < copter_x + copter_width < top_obs_x + obs_width:
            crash_message()
            game_value = False
        if copter_y + copter_height + 30 >= bot_obs_y and bot_obs_x < copter_x + copter_width + 90 < bot_obs_x + obs_width:
             crash_message()
             game_value = False
#DETECTING COLLISION WITH THE MISSILE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if copter_x < missile_x < copter_x + copter_width and copter_y < missile_y < copter_y + copter_height:
            crash_message()
            game_value = False



        display_score(score_str,20, blue)
        copter_display(copter_image, copter_x, copter_y)
        controls_display()
        pygame.display.update()
        clock.tick(70)


def game_intro():
    intro_value = True
    while intro_value:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        title_screen("Copter Chase", red)
        game_credits("Created by: Rutvik")
        buttons(white,200,550,100,50,25,"Play!",red)
        buttons(white,800,550,100,50,25,"Quit",red)
        mouse_location = pygame.mouse.get_pos()
        mouse_clicks = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if 800 < mouse_location[0] < 900 and 550 < mouse_location[1] < 600:
                if mouse_clicks[0] == 1:
                    pygame.quit()
                    quit()
            if 200 < mouse_location[0] < 300 and 550 < mouse_location[1] < 600:
                if mouse_clicks[0] == 1:
                    game_loop()
        pygame.display.update()
game_intro()