#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
import random
import pygame
import sys
from INTERNET.client import client
pygame.init() #вызываю все методы pygame

cli = client(host="localhost", port=9090)
cli.connect_server()
if cli == False:
    print("ou nou")
    sys.exit()




win = Tk() #создфю окно для ввода имени
win.title("okno")#делаю заголовок
win.geometry("500x500")#ширина и высота окна

#переменые для окна ввода имени-----

vvel_imja = False #эта переменая не будет давать несколько раз вводить имя

#конец переменых------------
    
def click():#функция по нажатию кнопки "жми"

    global vvel_imja
    try:
        vvod = vvod_imeni.get()
        if vvel_imja == False: #это нужно для того чтобы человек немог несколько раз написать имя
            vvel_imja = True
            file = open("fire_запись.txt","a")#открываю файл в который буду всё записовать
            file.write("\n\ngamer name: ")
            file.write(vvod)#и пишу в файл то что ввёл пользователь
            file.close()#закрываю файл
    except:
        file = open("fire_запись.txt","a")#открываю файл в который буду всё записовать
        file.write("\n\ngamer name: ")
        file.write("?????")# то что ввёл пользователь только знаками вопросов
        file.close()#закрываю файл
        
    

    

vvod_imeni = Entry(win,width=10)#делаю строку ввода
label_text = Label(text="впиши своё имя" )#делаю надпись "впиши своё имя"
label_opisanije = Label(text="описание и управление\nигрок движетсья по схеме клавиш(A,S,D,W), клавиша (P) включает музыку\nна клавишу (T) включаетсья окно где можно вписать команды\n(speed++, speed--, stop_kol(on), stop_kol(off), lose(on), lose(off))\nвсе ваши достижения в игрезаписываютсья в файл (fire_запись.txt)\nосле введения имени нажмите(готово)и закройте окно")
btn = Button(win , text="готово" , command=click)#делаю кнопку которая вызывает функцию "click"


label_text.pack()#выставляю надпись
vvod_imeni.pack()#выставляю строку ввода
btn.pack()#выставляю кнопку
label_opisanije.pack()#выставляю надпись

win.mainloop()# делаю окно бесконечным до того как пользователь нажмет на крестик

#работа с интернетом
cli = client(host="localhost", port=9090)
cli.connect_server()

#переменые:
text = pygame.font.SysFont('arial', 36) #размер и цвет основного текста
clock = pygame.time.Clock() #переменая для FPS я её использую на конце
pley = True #переменая отвечающая за главный цыкл

#переменые за окно---------------------
OSwin_visota = 700
OSwin_shirota = 1000
FPS = 60

#переменые за музыку
vkljucenije_muzika = False     #
perekljucenije_muzika = True #эти переменые нужны для того чтобы включать и выключать музыку
vstavljenije_muzika = True   # 
#переменые за картинки-----------------------


#цвета-------------------------------
MAGENTA = (255,0,255)
GOLDEN = (255,215,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GOLUBOJ = (0,255,255)
YELLOW = (255,255,0)
PURPLE = (128,0,128)

#переменые за игрока-----------------
x_igrok = 400
x_igrok2 = 400
y_igrok = 585
y_igrok2 = 585
shirota_igrok = 60
visota_igrok = 80
speed_igrok = 10
speed_igrok2 = 10
animacija_left_igrok = False
animacija_left_igrok2 = False
animacija_right_igrok = False
animacija_right_igrok2 = False
animacija_cislo = 0
animacija_cislo2 = 0
smerti_igrok = 0
smerti_igrok2 = 0
stop_smerti_igrok = False #эта переменая нужна чтобы останавливать прибовление смертей в методк кол
stop_smerti_igrok2 = False #эта переменая нужна чтобы останавливать прибовление смертей в методк кол
lose_igrok = False
lose_igrok2 = False
igrok_dont_lose = False
igrok_dont_lose2 = False
igrok = True
jump = 10 #высота прышка
jump2 = 10 #высота прышка
if_jump = False#проверка на прыжок
if_jump2 = False#проверка на прыжок
score = 0 # эта переменая служит для очков
score2 = 0 # эта переменая служит для очков

#переменые за кол падающий с верху-----------------------------

sozdanije_x_kola = True
shirota_kol = 40
visota_kol = 80
speed_kol = 20
animacija_kol = True
kolicestvo_kolov = 0 #количество еолов будет увеличаться с каждым новым колом
x_kol = 0 #x-kol пока будет 0, а потом в методе "kol" он станет рандомным
y_kol = 0

#конец переменых за кол падающий с верху---------------------------------

#переменые для звезды-------------
sozdanije_kordinat_zvezda = True
x_zvezda = 0 #x_zvezda пока будет 0, а потом в методе "score_zvezda" он станет рандомным
y_zvezda = 0 #y_zvezda пока будет 0, а потом в методе "score_zvezda" он станет рандомным
animacija_zvezda = True
kolicestvo_zvezda = 0
shirota_zvezda = 25
visota_zvezda = 25


#конец переменых для звезды-------
#-----------------------------------------------




OSwin = pygame.display.set_mode((OSwin_shirota,OSwin_visota))#создаю окно
pygame.display.set_caption("GREEN RUN")#имя окна
pygame.display.set_icon(pygame.image.load("common_images/tablicka_GR.ico"))

###загрузка--------------------
###загрузка звуков 
#fonovaja_muzika = pygame.mixer.Sound("muzika_ptic.wav")


### загрузка картинок----------------------

image_igrok = pygame.image.load("common_images/celovek_zeljonka0.png") #стоячий человек
image_igrok2 = pygame.image.load("common_images/celovek_sinij0.png") #стоячий человек
image_kol = pygame.image.load("common_images/raznocvetni_kol.png") #загружаю картинку кола
image_score = pygame.image.load("common_images/zvezda_s_rogami4.png")#загружаю картинку звезды
djungli1 = pygame.image.load("common_images/djungli3_fon.png") #фон



### конец загрузки звуков
#загружаю анимацию ходьбы----------------------



walk_left =[pygame.image.load("walkleft/celovek_zeljonka_left1.png"), # делаю список картинок движущихся в лево для персонажа
            pygame.image.load("walkleft/celovek_zeljonka_left2.png"),
            pygame.image.load("walkleft/celovek_zeljonka_left3.png"),
            pygame.image.load("walkleft/celovek_zeljonka_left4.png"),
            pygame.image.load("walkleft/celovek_zeljonka_left5.png")
            ]



walk_right =[pygame.image.load("walkright/celovek_zeljonka_right1.png"),#делаю список картинок движущихся в вправо для персонажа
             pygame.image.load("walkright/celovek_zeljonka_right2.png"),
             pygame.image.load("walkright/celovek_zeljonka_right3.png"),
             pygame.image.load("walkright/celovek_zeljonka_right4.png"),
             pygame.image.load("walkright/celovek_zeljonka_right5.png")
             ]
walk_left2 =[pygame.image.load("walkleft/celovek_sinij_left1.png"), # делаю список картинок движущихся в лево для персонажа
            pygame.image.load("walkleft/celovek_sinij_left2.png"),
            pygame.image.load("walkleft/celovek_sinij_left3.png"),
            pygame.image.load("walkleft/celovek_sinij_left4.png"),
            pygame.image.load("walkleft/celovek_sinij_left5.png")
            ]



walk_right2 =[pygame.image.load("walkright/celovek_sinij_right1.png"),#делаю список картинок движущихся в вправо для персонажа
             pygame.image.load("walkright/celovek_sinij_right2.png"),
             pygame.image.load("walkright/celovek_sinij_right3.png"),
             pygame.image.load("walkright/celovek_sinij_right4.png"),
             pygame.image.load("walkright/celovek_sinij_right5.png")
             ]

### конец загрузки анимации ходьбы
#конец загрузки картинок------------------

#ВСЕ def ------------------------------------------
def command_click(): #это для действий кнопки 
    command = vvod_command.get()
    dejstvija(command)

def dejstvija(command): #это читы
    global speed_igrok
    global speed_kol
    global igrok_dont_lose
    label_praviljno = Label(text="успешно введена команда")
    

    if command == "speed++":                        #
        speed_igrok += 30                            #
        label_praviljno.pack()                      #
    elif command == "speed--":                        #
        if speed_igrok >= 0:                        #
            speed_igrok -= 10                       #
            label_praviljno.pack()                   #
            
    elif command == "stop_kol(on)":                   #
        speed_kol = 0                               #
        label_praviljno.pack()                       #
    elif command == "stop_kol(off)":                  #
        
        speed_kol = 20                              #>>>>>>>>>>>>>> это всё читы 
        label_praviljno.pack()                        #
    elif command == "lose(off)":                      #
        
        igrok_dont_lose = True                      #
        label_praviljno.pack()                       #
        
    elif command == "lose(on)":                       #
        igrok_dont_lose = False                     #
        label_praviljno.pack() 
        
    else:
        label_oshibka = Label(text="несуществует такой команды!!!")
        label_oshibka.pack()






def draw_OSwin_hodjba():
    global animacija_cislo ######
    global walk_left            ###
    global walk_left2            ###
    global walk_right
    global walk_right2
    global x_igrok                  ###>>>>>>>>>> беру переменые из программы
    global y_igrok                ####
    global animacija_left_igrok ###
    global animacija_right_igrok#
    global animacija_cislo2 ######
    global x_igrok2                  ###>>>>>>>>>> беру переменые из программы
    global y_igrok2                ####
    global animacija_left_igrok2 ###
    global animacija_right_igrok2#
    OSwin.blit(djungli1, (0,0))#ставлю в экран картинку
                 
    if (animacija_cislo + 1) >= 25: #защищаю от ошибки, чтобы не вышло за рамки списка
        animacija_cislo = 0


    if animacija_left_igrok == True:          
        OSwin.blit(walk_left[animacija_cislo // 5],(x_igrok , y_igrok)) #выставляю картинку из списка "walk_left"
        animacija_left_igrok = False

    elif animacija_right_igrok == True:
        OSwin.blit(walk_right[animacija_cislo // 5],(x_igrok , y_igrok)) #выставляю картинку из списка "walk_right"
        animacija_right_igrok = False
         
    else:
        if igrok == True:
            OSwin.blit(image_igrok, (x_igrok , y_igrok)) #если он не идет ни на право ни налево то стоит

    if (animacija_cislo2 + 1) >= 25:  # защищаю от ошибки, чтобы не вышло за рамки списка
        animacija_cislo2 = 0

    if animacija_left_igrok2 == True:
        OSwin.blit(walk_left2[animacija_cislo2 // 5], (x_igrok2, y_igrok2))  # выставляю картинку из списка "walk_left"
        animacija_left_igrok2 = False

    elif animacija_right_igrok2 == True:
        OSwin.blit(walk_right2[animacija_cislo2 // 5], (x_igrok2, y_igrok2))  # выставляю картинку из списка "walk_right"
        animacija_right_igrok2 = False

    else:
        if igrok == True:
            OSwin.blit(image_igrok2, (x_igrok2, y_igrok2))  # если он не идет ни на право ни налево то стоит


def kol():
    global y_kol            #
    global image_kol         #
    global kolicestvo_kolov   #
    global sozdanije_x_kola    #
    global x_kol                #
    global speed_kol              #
    global shirota_igrok           #
    global shirota_kol              #>>> сабираю глобальные переменые из проограммы в метод "kol"
    global visota_igrok            #
    global visota_kol             #
    global y_igrok               #
    global x_igrok              #
    global lose_igrok          #
    global image_igrok        #
    global smerti_igrok      #
    global stop_smerti_igrok#
    global y_igrok2           #
    global x_igrok2             #
    global lose_igrok2          #
    global smerti_igrok2      #
    global stop_smerti_igrok2#
    global image_igrok2
    if kolicestvo_kolov >= 1: #останавливаю создание колов
        sozdanije_x_kola = False
        
    if sozdanije_x_kola == True: #создаю новый кол на новом месте
        x_kol = random.randint(0,1000)
        kolicestvo_kolov += 1 # прибавляю количество колов

        
   
    if animacija_kol == True: #выставляю кол
        OSwin.blit(image_kol,(x_kol,y_kol))
        y_kol += speed_kol
        
        
    if y_kol >= OSwin_visota: #если он дошёл до пола, то он появляетсья с верху на новом месте
        kolicestvo_kolov -= 1 #говорю что кола больше нет
        sozdanije_x_kola = True #говорю что можно создавать новый кол
        y_kol = 0 #ставлю кол на верх
    

    if igrok_dont_lose == False:
        if x_kol <= (x_igrok + 40) and x_kol + (shirota_kol - 25) >= x_igrok: #провераю совпадают ли x_igrok и x_kol
            if y_kol <= y_igrok and y_kol + visota_kol > y_igrok: #провераю совпадают ли y_igrok и y_kol
                speed_kol = 0 #если совпали x и y значит кол попал в человека, поэтому я кол не двигаю, игра проиграна
                lose_igrok = True

    if igrok_dont_lose2 == False:
        if x_kol <= (x_igrok2 + 40) and x_kol + (shirota_kol - 25) >= x_igrok2: #провераю совпадают ли x_igrok и x_kol
            if y_kol <= y_igrok2 and y_kol + visota_kol > y_igrok2: #провераю совпадают ли y_igrok и y_kol
                speed_kol = 0 #если совпали x и y значит кол попал в человека, поэтому я кол не двигаю, игра проиграна
                lose_igrok2 = True
    if lose_igrok == True:
        game_over = text.render("GAME OVER, press "'"SPEACE"'" to start game",True,(WHITE)) #пишу что человек проиграл и если хочет продолжить играть то пусть нажмет SPEASCE
        OSwin.blit(game_over,(90,350)) #выставляю надпись game over на показ
        image_igrok = pygame.image.load("common_images/celovek_zeljonka_placet0.png")#меняю человека на плачушего
        if stop_smerti_igrok == False:
            smerti_igrok += 1
            stop_smerti_igrok = True
    elif lose_igrok2 == True:
        game_over = text.render("GAME OVER, press "'"SPEACE"'" to start game",True,(WHITE)) #пишу что человек проиграл и если хочет продолжить играть то пусть нажмет SPEASCE
        OSwin.blit(game_over,(90,350)) #выставляю надпись game over на показ
        image_igrok2 = pygame.image.load("common_images/celovek_sinij_placet0.png")#меняю человека на плачушего
        if stop_smerti_igrok2 == False:
            smerti_igrok2 += 1
            stop_smerti_igrok2 = True
    else:
        image_igrok = pygame.image.load("common_images/celovek_zeljonka0.png") #востанавливаю картинку игрока, с плачущего на улыбающегося
        image_igrok2 = pygame.image.load("common_images/celovek_sinij0.png") #востанавливаю картинку игрока, с плачущего на улыбающегося

    pygame.display.update()  
            
def send_and_get_player():
    global cli
    global x_igrok
    global x_igrok2
    global y_igrok
    global y_igrok2
    Y_and_X = cli.send("x:{0}y:{1}".format(x_igrok,y_igrok))#получаю и отправляю данные о X и Y игроков

def score_zvezda():
    global shirota_igrok          #
    global visota_igrok            #
    global image_score              # 
    global sozdanije_kordinat_zvezda #
    global animacija_zvezda           #
    global kolicestvo_zvezda           #
    global x_zvezda                     #
    global y_zvezda                      #>>> сабираю глобальные переменые из проограммы в метод "score_zvezda"                                           
    global shirota_zvezda               #                      
    global visota_zvezda               #          
    global y_igrok                    #          
    global x_igrok                   #
    global score                    #
    global y_igrok2                #
    global x_igrok2               #


    if (x_igrok - 13) <= (x_zvezda) and (x_igrok ) + (shirota_igrok ) >= x_zvezda:# провераю не достиг ли
        if (y_igrok - 25)<= y_zvezda and y_igrok + visota_igrok > y_zvezda:       # игрок звезды
            kolicestvo_zvezda -= 1# если достиг то она пропадает
            score += 1 #+1 звезда
    if (x_igrok2 - 13) <= (x_zvezda) and (x_igrok2 ) + (shirota_igrok ) >= x_zvezda:# провераю не достиг ли
        if (y_igrok2 - 25)<= y_zvezda and y_igrok2 + visota_igrok > y_zvezda:       # игрок звезды
            kolicestvo_zvezda -= 1# если достиг то она пропадает
            score += 1 #+1 звезда
    if kolicestvo_zvezda >= 1:#не даю звездам слишком много появляться
        sozdanije_kordinat_zvezda = False
    else:
        sozdanije_kordinat_zvezda = True#иначе пусть появляется

    if sozdanije_kordinat_zvezda == True:
        kolicestvo_zvezda += 1
        y_zvezda = random.randint(400,630)
        x_zvezda = random.randint(10,990)

    if animacija_zvezda == True:
        OSwin.blit(image_score,(x_zvezda , y_zvezda))#ставлю звезду
        nadpis_score = text.render("SCORE: " , True , (MAGENTA))#делаю надпись "score" 
        score_nadpis_cifr = text.render(str(score), True , (GOLDEN))#делаю надпись самих очков и делаю "score" строкой чтобы "pygame" ее мог написсать 
        OSwin.blit(nadpis_score, (0,0))#выставляю надпись "score"
        OSwin.blit(score_nadpis_cifr , (150 , 0))#выставляю сами очки
        score = int(score)#вызвращаю переменую "score" в int чтобы ее можно было потом считать

        
 
   



#КОНЕЦ def----------------------------------------------------------------------



while pley == True:
    #if vkljucenije_muzika == True:
        #pygame.mixer.Sound.play(fonovaja_muzika)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #если нажмёт на крестик на окне, то окно закроеться
            file = open("fire_запись.txt","a")
            file.write("\nis ded: ")
            smerti_igrok = str(smerti_igrok)
            file.write(smerti_igrok)
            score = str(score)
            file.write("\nscore: ")
            file.write(score)
            file.write("\n:::::::::::::::::::::::::::::::::::::::::::::::::::")
            file.close()
            pley = False #выход из основного цыкла
            sys.exit() #выход из программы
     
            
    keys = pygame.key.get_pressed()# список в котором будет отслеживаться действия пользователя
    if keys[pygame.K_k]:
        console = Tk() #делаю окно
        console.geometry("250x250")#задаю размер
        console.title("console")#название        
        
        vvod_command = Entry(console, width=15)#это поле ввода
        command_button = Button(text="готово",command=command_click )#кнопка по которой будут исполнятся команды 
        vvod_command.pack() #
        command_button.pack()#все то что я зделал в окне "console" я выставляю
        
        console.mainloop()  #делаю окно бесконечным до того пока его не закройут
        
    if keys[pygame.K_p]:
        perekljucenije_muzika = vkljucenije_muzika #
        vkljucenije_muzika = vstavljenije_muzika      #переключение музыки
        vstavlenije_muzika = perekljucenije_muzika   #

              
              

        
    
    if keys[pygame.K_SPACE]: #если нажат пробел
        if lose_igrok == True: #если человек проиграл выполняй следующее
            speed_kol = 20 #востанавляю скорость кола
            stop_smerti_igrok = False#возвращаю, чтобы в методе "kol" смерти смогли записаться заново
            if lose_igrok == True:
                lose_igrok = False
            if x_kol > 400 and x_kol < 600: # если кол на середине...
                x_igrok = 200 #то игрок будет скраю
            else: #иначе
                x_igrok = 500 #игрок будет в середине
        
       
    if keys[pygame.K_d]:
        if x_igrok < OSwin_shirota - shirota_igrok - 5: #проверая не достиг ли персонаж конца карты
            if lose_igrok == False:
                if speed_igrok > 10:
                    speed_igrok -= 1
                x_igrok += speed_igrok #персонаж двигаеться вправо
                animacija_right_igrok = True #будет двигатсья вправо
                animacija_left_igrok = False #он теперь не будет двигатсья влево
                animacija_cislo += 4 #прибавляю, для того чтобы в списке walk_right происходили изменения кортинки

    elif keys[pygame.K_a] :
        if x_igrok > 10: #проверая не достиг ли персонаж конца карты
            if lose_igrok == False:
                if speed_igrok > 10:
                    speed_igrok -= 1
                x_igrok -= speed_igrok #персонаж двигаеться влево
                animacija_right_igrok = False #он теперь не будет двигатсья в право
                animacija_left_igrok = True #будет двигатсья влево
                animacija_cislo += 4 #прибавляю, для того чтобы в списке walk_left происходили изменения кортинки
    else:
        animacija_cislo = 0

    #анимация прышка--------------------------------------------------------------
    if lose_igrok == False:
        if not(if_jump):
            if keys[pygame.K_w] and y_igrok > 5:
                if_jump = True
        else:
            if speed_igrok >= 18:
                pass
                #speed_igrok -= 1

            else:
                speed_igrok += 1
            animacija_cislo = 0 #для того чтобы небыло анимации ходьбы во время прышка
            if jump >= -10:
                if jump < 0:
                    y_igrok += (jump ** 2) / 2 #опускаю игрока
                else:
                    y_igrok -= (jump ** 2) / 2 #поднимаю игрока
                jump -= 1

            else:
                if_jump = False #говорю что прыжок закончен и можно делать следующий
                jump = 10 #вызвращаю переменую отвечающую за прыжок на местоd

###################PLAYER2################################
    if keys[pygame.K_SPACE]:  # если нажат пробел
        if lose_igrok2 == True:  # если человек проиграл выполняй следующее
            speed_kol = 20  # востанавляю скорость кола
            stop_smerti_igrok = False  # возвращаю, чтобы в методе "kol" смерти смогли записаться заново
            if lose_igrok2 == True:
                lose_igrok2 = False
            if x_kol > 400 and x_kol < 600:  # если кол на середине...
                x_igrok2 = 200  # то игрок будет скраю
            else:  # иначе
                x_igrok2 = 500  # игрок будет в середине

    if keys[pygame.K_RIGHT]:
        if x_igrok2 < OSwin_shirota - shirota_igrok - 5:  # проверая не достиг ли персонаж конца карты
            if lose_igrok2 == False:
                if speed_igrok2 > 10:
                    speed_igrok2 -= 1
                x_igrok2 += speed_igrok2  # персонаж двигаеться вправо
                animacija_right_igrok2 = True  # будет двигатсья вправо
                animacija_left_igrok2 = False  # он теперь не будет двигатсья влево
                animacija_cislo2 += 4  # прибавляю, для того чтобы в списке walk_right происходили изменения кортинки

    elif keys[pygame.K_LEFT]:
        if x_igrok2 > 10:  # проверая не достиг ли персонаж конца карты
            if lose_igrok2 == False:
                if speed_igrok2 > 10:
                    speed_igrok2 -= 1
                x_igrok2 -= speed_igrok2  # персонаж двигаеться влево
                animacija_right_igrok2 = False  # он теперь не будет двигатсья в право
                animacija_left_igrok2 = True  # будет двигатсья влево
                animacija_cislo2 += 4  # прибавляю, для того чтобы в списке walk_left происходили изменения кортинки
    else:
        animacija_cislo2 = 0

    # анимация прышка--------------------------------------------------------------
    if lose_igrok2 == False:
        if not (if_jump2):
            if keys[pygame.K_UP] and y_igrok2 > 5:
                if_jump2 = True
        else:
            if speed_igrok2 >= 18:
                speed_igrok2 -= 1
            else:
                speed_igrok2 += 1
            animacija_cislo2 = 0  # для того чтобы небыло анимации ходьбы во время прышка
            if jump2 >= -10:
                if jump2 < 0:
                    y_igrok2 += (jump2 ** 2) / 2  # опускаю игрока
                else:
                    y_igrok2 -= (jump2 ** 2) / 2  # поднимаю игрока
                jump2 -= 1

            else:
                if_jump2 = False  # говорю что прыжок закончен и можно делать следующий
                jump2 = 10  # вызвращаю переменую отвечающую за прыжок на место

    #конец анимации прышка----------------
    draw_OSwin_hodjba() #вызываю метод заполнения экрана                
    score_zvezda()
    kol()

    
    
    
        

    clock.tick(FPS) #кадры в секунду



