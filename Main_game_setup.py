#!/usr/bin/env python
import time
import sys
import os
import consolemenu

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    """Main Menu Screen"""
    os.system('cls')
    print """
                      |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
                      |                                                  Welcome To EARTH-2086:                                              |
                      |                                                      A New Beginning                                                 |
                      |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
                      |                                                   (1) Start Your New Life                                            |
                      |                                                   (2) Load Your Save                                                 |
                      |                                                   (3) Help For Dummies                                               |
                      |                                                   (4) RAGE QUIT                                                      |
                      |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
                      |                                                     Pick a Number                                                    |
                      |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
                      |                                                Copyright 2018 Jakob Mceuen                                           |
                      |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"""
    option = raw_input('              -----> ')
    if option == '1':
        cutscene()
    elif option == '2':
        main_menu()
    elif option == '3':
        os.system('cls')
        help_menu()
    elif option == '4':
        rage_quit()
    else:
        main_menu()


def help_menu():
    """Help Menu"""
    os.system('cls')
    print"""
                      |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
                      |                                                Welcome To The                                                        |
                      |                                              Help Menu For Noobs                                                     |
                      |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
                      |01)                                                                                                                   |
                      |02)                                                                                                                   |
                      |03)                                                                                                                   |
                      |04)                                                                                                                   |
                      |05)                                                                                                                   |
                      |06)                                                                                                                   |
                      |07)                                                                                                                   |
                      |08)                                                                                                                   |
                      |09)                                                                                                                   |
                      |10)                                                                                                                   |
                      |11)                                                                                                                   |
                      |12)                                                                                                                   |
                      |13)                                                                                                                   |
                      |14)                                                                                                                   |
                      |15)                                                                                                                   |
                      |16)                                                                                                                   |
                      |17)                                                                                                                   |
                      |18)                                                                                                                   |
                      |19)                                                                                                                   |
                      |20)                                                                                                                   |
                      |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|==============================|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
                      |                                          |(1) Main Menu  (2) Extra Hints|                                            |
                      |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|==============================|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"""
    option = raw_input('              -----> ')
    if option == '1':
        main_menu()
    elif option == '2':
        hints()
    else:
        help_menu()


def rage_quit():
    """Quit Game"""
    os.system('cls')
    print """
                      |======================================================================================================================|
                      |                                                    |Rage Quit?|                                                      |
                      |======================================================================================================================|
                      |                                                      (1) YES?                                                        |
                      |                                                      (2) NO?                                                         |
                      |======================================================================================================================|"""
    option = raw_input('              -----> ')
    if option == '1':
        sys.exit()
    elif option == '2':
        main_menu()
    else:
        rage_quit()


def hints():
    """Extra Help Menu"""
    print """         |======================================================================================================================|
                      |                                                Welcome To The                                                        |
                      |                                                 Hints Section                                                        |
                      |======================================================================================================================|
                      |01)                                                                                                                   |
                      |02)                                                                                                                   |
                      |03)                                                                                                                   |
                      |04)                                                                                                                   |
                      |05)                                                                                                                   |
                      |06)                                                                                                                   |
                      |07)                                                                                                                   |
                      |08)                                                                                                                   |
                      |09)                                                                                                                   |
                      |10)                                                                                                                   |
                      |11)                                                                                                                   |
                      |12)                                                                                                                   |
                      |13)                                                                                                                   |
                      |14)                                                                                                                   |
                      |15)                                                                                                                   |
                      |16)                                                                                                                   |
                      |17)                                                                                                                   |
                      |18)                                                                                                                   |
                      |19)                                                                                                                   |
                      |20)                                                                                                                   |
                      |===============================================|=============|========================================================|
                      |                                               |(1) Main Menu|                                                        |
                      |===============================================|=============|========================================================|"""
    option = raw_input('              -----> ')
    if option == '1':
        main_menu()
    else:
        hints()


def load():
    """Load Save"""
    os.system('cls')
    print "hi"


def cutscene():
    """Story Start"""
    os.system('cls')
    story_pic_1()


def char_create():
    """Character Create"""
    print "      Are you a Male or a Female?"


def play():
    """Gameplay Start"""
    os.system('cls')
    print "WHATS UP DUDE! NOT FINISHED YET!"


def title_pic():
    """Title Text Picture"""
    os.system('cls')
    time.sleep(1.5)
    print """
             ___________________________________________________________________________________________________________________________________________________________
             |____|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|
             |                 EEEEEEEEEEEEEEEEEEEEEE               AAA               RRRRRRRRRRRRRRRRR   TTTTTTTTTTTTTTTTTTTTTTTHHHHHHHHH     HHHHHHHHH               |
             |                 E::::::::::::::::::::E              A:::A              R::::::::::::::::R  T:::::::::::::::::::::TH:::::::H     H:::::::H               |
             |                 E::::::::::::::::::::E             A:::::A             R::::::RRRRRR:::::R T:::::::::::::::::::::TH:::::::H     H:::::::H               |
             |                 EE::::::EEEEEEEEE::::E            A:::::::A            RR:::::R     R:::::RT:::::TT:::::::TT:::::THH::::::H     H::::::HH               |
             |                   E:::::E       EEEEEE           A:::::::::A             R::::R     R:::::RTTTTTT  T:::::T  TTTTTT  H:::::H     H:::::H                 |
             |                   E:::::E                       A:::::A:::::A            R::::R     R:::::R        T:::::T          H:::::H     H:::::H   ::::::        |
             |                   E::::::EEEEEEEEEE            A:::::A A:::::A           R::::RRRRRR:::::R         T:::::T          H::::::HHHHH::::::H   ::::::        |
             |                   E:::::::::::::::E           A:::::A   A:::::A          R:::::::::::::RR          T:::::T          H:::::::::::::::::H   ::::::        |
             |                   E:::::::::::::::E          A:::::A     A:::::A         R::::RRRRRR:::::R         T:::::T          H:::::::::::::::::H                 |
             |                   E::::::EEEEEEEEEE         A:::::AAAAAAAAA:::::A        R::::R     R:::::R        T:::::T          H::::::HHHHH::::::H                 |
             |                   E:::::E                  A:::::::::::::::::::::A       R::::R     R:::::R        T:::::T          H:::::H     H:::::H                 |
             |                   E:::::E       EEEEEE    A:::::AAAAAAAAAAAAA:::::A      R::::R     R:::::R        T:::::T          H:::::H     H:::::H   ::::::        |
             |                 EE::::::EEEEEEEE:::::E   A:::::A             A:::::A   RR:::::R     R:::::R      TT:::::::TT      HH::::::H     H::::::HH ::::::        |
             |                 E::::::::::::::::::::E  A:::::A               A:::::A  R::::::R     R:::::R      T:::::::::T      H:::::::H     H:::::::H ::::::        |
             |                 E::::::::::::::::::::E A:::::A                 A:::::A R::::::R     R:::::R      T:::::::::T      H:::::::H     H:::::::H               |
             |                 EEEEEEEEEEEEEEEEEEEEEEAAAAAAA                   AAAAAAARRRRRRRR     RRRRRRR      TTTTTTTTTTT      HHHHHHHHH     HHHHHHHHH               |
             |_________________________________________________________________________________________________________________________________________________________|
             |____|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|
             |                                         222222222222222         000000000          888888888             66666666                                       |
             |                                         2:::::::::::::::22     00:::::::::00      88:::::::::88          6::::::6                                       |
             |                                         2::::::222222:::::2  00:::::::::::::00  88:::::::::::::88       6::::::6                                        |
             |                                         2222222     2:::::2 0:::::::000:::::::08::::::88888::::::8     6::::::6                                         |
             |                                                     2:::::2 0::::::0   0::::::08:::::8     8:::::8    6::::::6                                          |
             |                                                     2:::::2 0:::::0     0:::::08:::::8     8:::::8   6::::::6                                           |
             |                                                  2222::::2  0:::::0     0:::::0 8:::::88888:::::8   6::::::6                                            |
             |                                             22222::::::22   0:::::0 000 0:::::0  8:::::::::::::8   6::::::::66666                                       |
             |                                           22::::::::222     0:::::0 000 0:::::0 8:::::88888:::::8 6::::::::::::::66                                     |
             |                                          2:::::22222        0:::::0     0:::::08:::::8     8:::::86::::::66666:::::6                                    |
             |                                         2:::::2             0:::::0     0:::::08:::::8     8:::::86:::::6     6:::::6                                   |
             |                                         2:::::2             0::::::0   0::::::08:::::8     8:::::86:::::6     6:::::6                                   |
             |                                         2:::::2       2222220:::::::000:::::::08::::::88888::::::86::::::66666::::::6                                   |
             |                                         2::::::2222222:::::2 00:::::::::::::00  88:::::::::::::88  66:::::::::::::66                                    |
             |                                         2::::::::::::::::::2   00:::::::::00      88:::::::::88      66:::::::::66                                      |
             |                                         22222222222222222222     000000000          888888888          666666666                                        |
             |_________________________________________________________________________________________________________________________________________________________|
             |____|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|
                                         |         /   |     / | / /__ _      __   / __ )___  ____ _(_)___  ____  (_)___  ____ _      |
                                         |        / /| |    /  |/ / _ \ | /| / /  / __  / _ \/ __ `/ / __ \/ __ \/ / __ \/ __ `/      |
                                         |       / ___ |   / /|  /  __/ |/ |/ /  / /_/ /  __/ /_/ / / / / / / / / / / / / /_/ /       |
                                         |      /_/  |_|  /_/ |_/\___/|__/|__/  /_____/\___/\__, /_/_/ /_/_/ /_/_/_/ /_/\__, /        |
                                         |                                                /____/                      /____/          |
                                         |____________________________________________________________________________________________|                                 """
    time.sleep(5.0)

#----------------------------------------Section#7--------------------------------------------------------------------------#
def story_pic_1():
    os.system('cls')
    time.sleep(0.8)
    print"""
         &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
         &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
         &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
         &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
         &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
         &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
         &&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&
         &&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&
         &&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(/###**#%%%#/*(#(//#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&
         &&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###(.         ...          (%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&
         &&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*.                                .(##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&
         &&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(                         .                 ./%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&
         &&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(,                   ...........         ......,/%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&
         &&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#.                       ..............................,(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&
         &&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(*                       .................................*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&
         &&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*                          .............,,,,,,,,,,,,......,....,*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&
         &&&&%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/.                       ................,,,,,,,,,,,,,,,.,,,,,,,,,/%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&
         &&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(                ................,,,,,,,,,,,.......,,,,,,,....,,,(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&
         &&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(,               ...............,,,,,,,,,,,..*******,,,,...,***,*(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&
         &&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(,.         ..............,,,,,,,,,,,,,,,,,.,**********************(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(       ...................,,,,,,,,,,,,,,,,.,*************************/(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###.     ..................,,,,,,,,,,,,,.....,**************************/*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%#/. .................,,,,,,,,,,....,*********////////////////***////**/#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&
         %%%%%%%%%%%%%%%%%%%(,..  ..,,/(#%%%%%%%%####%(, ...............,,,,,,,,,,,.,********//////////////////////////*//#%#%%%%%%%%%&@@@&&@&&@@@&&%%%%%%%%%%%%%%%%%%%&
         %%%%%%%%%%%%%%%%*,. .                .*(#####*................,,,,,,,,.,***********//////////////////////////**/######%%%%&@@@@@@@@@@@@@@@@@@@@@@&%%%%%%%%%%%%%
         %%%%%%%%%%%%%%%,...... .         .......*#####(*.............,,,,,,,,,************/////////////////////////////*########%&@@@@@@@@@@@&@@@@@@@@@@@@&%%%%%%%%%%%%
         %%%%%%%%%%%%%(,...**,,..........,,........./#####(,.......,,,,,,,,,,,,**********////////////**///////*///////**/########%@@@@@@@&%(//***//(#&@@@@@@@&%%%%%%%%%%
         %%%%%%%%%%%%%,...*/**********//(((((*.......(#####(,.....,,*,,,,,,((/**********////////****//(/*****/(//////*(##########%@@@@&(*,,,,,,,,,,,,,,*%@@@@@&%%%%%%%%%
         %%%%%%%%%%%%/...,*****************//(*,..,*########(**,,,*(#(/***(#((/******/**///**////((((#(##(((####(///(###########%%@@@&(*,,,,,,,,,,,,,,,,,/%@@@&%%%%%%%%%
         %%%%%%%%%%%#...*(/****/***/*/*******/(,,,#################(###((((((///***************/(((##(##########################%%@@@%/,,,,,,,,,,,,,,,,,,,/@@&&%%%%%%%%%
         %%%%%%%%%%%#,**/***////(((/*/((///((/(*,*#####################(#(((((//*************///(((((((#########################%%@&(/,,,,,,,,,,,,,,,,,,,,,*@&%%%%%%%%%%
         %%%%%%%%%%%(,,*/***//(/********/(/***(/**#####################(((((((/**************//*/(((((((#########################%%(//,(((###*,,,,,,/#%#(,,,/%%%%%%%%%%%
         %%%%%%%%%%(,,*******////******////***(/**/####################(((((((//**************///(((((((##########################((/*,,,,,,,//,,,,***,,,*,,*%%%%%%%%%%%
         %%%%%%%%%(***/(**********/**********/(/*,*/##################(((((((//****,....,******/((((((((#######################/**//(/,,,,/**,/*,,,*/#/,,,,,,*/%%%%%%%%%
         %%%%%%%%%%(*/((/*******//(((((/****/(((((*/##################(((((///****,,....,*****/(((((((((#######################/,,//(/,,,,,,,,/*,,,,,,,,,,,,,,*%%%%%%%%%
         %%%%%%%%%%%#/((/******/*********/**/((((/(###################(#((///****,......,*******//(#(((########################(,,///*,,,,,,,*/*,,,,,,,,,,,,,*/%%%%%%%%%
         %%%%%%%%%%%#/((/********///(///*****(((((####################(#((///***,..........,****///((###########################*,///*,,,,,,,,*,,,,,,,,,,,,,,/%%%%%%%%%%
         %%%%%%%%%%%#*///*********(((((/*****((//(######################((//***,,..........,,*****/(((##########################(////*,,,,,***///(/***,,,,,,,#%%%%%%%%%%
         %%%%%%%%%%%%(,,//******************/(/,*######################(//**,................,,,***///(###########################(//*,,,,,,,,,,*,,,,,,,,,,/%%%%%%%%%%%%
         %%%%%%%%%%%%%*,*((***//********///(((**(#####################(//***,...................,****//(######################%##%(///,,,,,,,/((((/*,,,,,,,#%%%%%%%%%%%%
         %%%%%%%%%%%%%%#(##((((((((((((((((((#(##(((######(///////((##(/*,....,*//((//*,...........,**///(###################((//////(/,,,,,,,*//*,,,,,,,,/%%%%%%%%%%%%%
         %%%%%###%%%%%%%#.,#(((((((####((((##,*//(//(((((/(//((////////****,,,/(/(//////*.,*////**..,**////################(//((((//(///,,,,,,,,,,,,,,,,*/(%%%%%%%%%%%%%
         #(//(//((##%%%%#   ,(##(((((((((#/   (%%%%#(((//////////////////(/////((/(((//((/(//////((////////###((////////((((////((#%/,*(///**,,,,,,,,,,,./(((%%#((((((#%
         /(####%%%%%%%%%%.     *(######(,.    #%%%%%%%%%#((/////////((((///////((%%%%%#(/(/((((((//(////////(///((((///(((//(##%%%%%#, .*/(((((((/****.  #&%%##((/((##((
         #%%%%%%%%%%%%%%%,        ..,.       .%%%%%&%%%%%%%%#((///((//////((((#%%%%%%%%%#%%%%%%%#((((((//(/(//((((((//(((#%%%%%%%%%%%(    .**/((///*.   .%%%%%%%%%%%%%%#
         %%%%%%%%%%&%%%%%(,    ./(%%%%#,     /%%%%%&%%%%%%%%%%%%%%#((#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##(/(#%%%###%%%%%%%%%%%%%%%%%.     .*(((*      *%%%%%%%%%%%%%%%
         %%%%%%%%%&&%%%%%%/  .*//#%%%%#//,   #%%%%%&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##%%%%%%%%%%%%%%%%%%%%%%%%%,   ,/(#####(/.   #%%%%&&%%%%%%%%%
         %%%%%%%%%&&%%%%%%%..    .#%%#.   ..*%%%%%%%&%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&%%%%%%%%%%%%%%&%%%%%%# ..   (###(   , ,%%%%%%&%%%%%%%%%
         %%%%%%%%%&%%%%%%%&*      /%%(     ,#%%%%%%%&&%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&%%%%%%%%%%%%%%&%%%%%%%.     .(#(.    .(%%%%%%%&%%%%%%%%
         %%%%%%%%%&&&%%%%%%#      #%%%.    #&%%%%%&&&%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&%%%%%%%%%%%%%&&&%%%%%%(     ,###,    (%%%%%%&&&%%%%%%%%
         %%%%%%%%%%%&&%%%%%%,    ,%%%%*   .%%%%%%&&%%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&%%%%%%%%%%%%%%%&&&%%%%%.    /###/   .%%%%%%&&&%%%%%%%%%
         %%%%%%%%%&&&%%%%%%%#   .(%%%%#   /%%%%%%%%&%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%&&%%%%%%/.  .(####.  /%%%%%%%&&%%%%%%%%% """
    time.sleep(1.0)
    print """    In 2018 President Donald Trump confronted Kim Jong Un, leader of North Korea about his nuclear program  """

#    print "                                         But then in may 9 2020 they started having major disagreements with certain topics about world domination.                                   "
    time.sleep(1.5)
    option = raw_input('Continue?[Yes/No]---> ')
    if option == 'yes':
        story_pic_2()
    elif option == 'Yes':
        story_pic_2()
    elif option == 'YES':
        story_pic_2()
    elif option == 'no':
        main_menu()
    elif option == 'No':
        main_menu()
    elif option == 'NO':
        main_menu()
    else:
        story_pic_1()

#-----------------------------------------------------------------------------------------------------------#
def story_pic_2():
    os.system('cls')
    time.sleep(0.5)
    print """
          yyyyyyyyyyyyyyyyyyyyyyyssssssoooo++++//////////////////////++++oooosssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssssooo++//:---......................................
          yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssssssssssyyyyyyyyyyyyyyyysyyyyyyyyssssyyyysyyyyyyyyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssoo+//::--.............................
          yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssyyyyyyyssssoo+/::--......................
          yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssyyyyyyyyyyyyyyysssyyyyyyssyyysyyyyyyhhddddmmmmmmmmmmddddddhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssyyyyyyyyyyyyyyyyyyyssssso+/:--................
          yyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyyyyysyyhddmNNNNNMMMMMMMMMMMMMMMMMMMMMNNNmmmddddhhyysyyyyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssoo/:--..........
          ossyssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyyyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssyyyyyyssyyso+/:-.....
          ``.-:+osyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmdyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssyyysysso+/:-
                `.:/osyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhdmNMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssyyyyyyyyyyyyysss
           `       `.-/osyyysyyysyysyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyhdNMMMMMMMMMMMNNNNNmmmmmmmmmmmmmmmmmmmmmNNNNNNNNMMMMMMMMMMMMMMMMMMMNmdhyyyyyyyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
           `          ``:+syysyysyyyyyyyyyyyyyyyyyyyyyyyyysyyyyyyhmNMMMMMMMMNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNMMMMMMMMMMMMMMMMMNNdhyyyyysyysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
          .              `-/syysyyyyyyyyyyyyyyyyyyyyyyyyyyssyyyydNMMMMMMMNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNMMMMMMMMMMMMMMMNmhyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
          -                `-+syyysyyyyyyyyyyyyyyyyyyyyyyyysysymMMMMNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNMMMMMMMMMMMMMNmhsyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
          /`                 `-oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhNMMMNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNMMMMMMMMMMMMNdysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
          o`                   ./syyyyyyyyyyyyyyyyyyyyyyyyyyysymMNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNMMMMMMMMMMMmhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
          s-                    `:syyyyyyyyyyyyyyyyyyyyyyysyyydmNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmddNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNMMMMMMMMMmysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
          s+                      -oyyyyyyyyyyyyyyyyyyyyyyyyhmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmddhhdmmmdssdmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNMMMMMMMMMmyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
          yo`                      -oyyyyyyyyyyyyyyyyyyyyysymMMNmmmmmmmmmmmmmmmmmmmmmmddddmmdddhssydmy+sdmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNMMMMMMMMNhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
          ys-                      `:syysyyyyyyyyyyyyyyyyyydMMNNmmmmmmmmmmmmmmmmmmmmmddddhyssoosyy+/+yy/ohhyymmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNMMMMMMMMmyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
          ys/                       `/syyysyyyyyyyyyyyyyyyhNMNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdhs+::---::::/-:sdmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNMMMMMMMMyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
          yyo.`                      .oysysyyyyyyyyyyyyyyydNNNmmmmmmmmmmmmmmmmmmmmmmmmmmddhyyysso/:-----------:/syhdmmmmmmmmmmmmmmmmmmmmmmmmmmNMMMMMMMhyyyssyyyyyyyyyyyyyyyyysyyyyyssysssoossyyyyyyyyyyyyyyy
          yyso:-``                   `/syyyyyyyyyyyyyyyyyyhmNmmmmmmmmmmmmmmmmmmmmmmmmdyo+/::::::::----------------::/+oyhmmmmmmmmmmmmmmmmmmmmmNMMMMMMMhyyyssyyyyyyyyyyyyyyyyyyyyyyyysoo++++syyyyyyyyyyyyyyyy
          yyyyyys+/-.`                -oyyyyyyyyyyyyyyyyyyhmmmmmmmmmmmmmmmmmmmmmmmmds:----------------------------------:sdyhmmmmmmmmmmmmmmmmmmNMMMMMMhssyyyyyyyyyyyyyyyyyyyyyyyysso+/:.:/osyyyyyyyyyyyyyyyy
          yyysyyyyyyso+:.`            .+syyyyyyyyyyyyyyyyyhmNmmmmmmmmmmmmmmmmmmmmmNs:-.----------------------------------/h+-+hmmmmmmmmmmmmmmmmNMMMMNNyssyyyyyyyyyyyyyyyyyyyysyyo++/-` `/+syyyyyyyyyyyyyyyyy
          yyyyyyyyyyyyysss+:.`        `/sysyyyyyyyyysyyyyydmmmmmmmmmmmmmmmmmmmmmmmNo:-------------------------------------yo--:odmNmNmmmmmmmmmmNMMMMdhyyyyyyyyyyyyyyyyysyyyysyo++/-`   -+osyyyyyyyyyyyyyyyyy
          yyyyyyyyyyyyyyyyyyyso/.` `   /syyyyyyyyyyysyyyyydmmmmmmmmmmmmmmmmmmmmmmmNy:-------------------------------------s+----/hmNmmmmmmmmmmmNMMMMhyyyyyyyyyyyyyyyyyyyysyso++:.     ./+ssyyyyyyyyyyyyyyyyy
          yyyyyyyyyyyysyyssysys+/.     /syyyyyyyyyyysyyyyhmmmmmmmmmdhsysyshhdmmmdyo:--------------------------------------o+------ymmmmmmmmmmNNNMMMNhyyyyyyyyyyyyyyyyysyysso+:.      `:+ossyyyyyyyyyyyyyyyyy
          yyyyyyyyyyssysyyso/.`       `/yyyyyyyyyyyyysyyydmmmmmdhhssososoo++/:--------------------------------------------o/-------hmmmmmmmmmNNMMMMNyyyyyysssyyyyyyyyyyyso+/.        .+osyyyyyyyyyyyyyyyyyyy
          yyyyyysyyyysso/-``          .oysyyyyyyyyyyssyyyhmmNmdhhyysyosooo+/:---------------------------------------------o/-------:dmmmmmmmmmNNNdmdysyso/../yyyyyssyyso+/.`        ./ossyyyyyyyyyyysyyyyyyy
          yyssyysyso/-.`              -syyyyyyyyyyyyssysshmmmdhhsysyosooo++/:--------------------------------------------/+:--------ommmmmmmmmmddyhyys/-` `.+yyyyyyyss+/-`         `:osyyyysyyyyyyyyysssyyyy
          yyyyso/-.``                `+syyyyyyyyyyyyyyysydNNmhhyhyyssooo++//---------------------------------------------/:---------/dmmmmmNNNdyyyso/.`   `:syyyyyyso/:`          `-+osssyyyyyyyyyyyyyyysssy
          sys+-``                    -oyssyyyyyyyyysyyyyydNmhdhhyysssoo++//----------------------------------------------::---------:hmdmNNNMMdyso/.`     .oyyssyss+:.            ./osyysyyyyssyysyyyysooosy
          sys-                      .+syysyyyyyyyyyyyhhyhhhyyhyyysssos+/::----------------------------------------------------------:dyyNMMMMMms/.`      `+yssyss+/.`            `/osyyyyyyysyyyyyssoo+/+oss
          yyo.                     `/yyyysyysyysydmNNNNNNhshhhyysssos+/-------------------------:/+oo/:----------------:------------+h//hMMMMMd:        `/yyysso+-`             `:osyyyyyyyyyyyyssso/-.:+oyy
          yy+`                    `:syssyyyyysshNMMMNNNMMhsyhhyssyoso+-----------------------------/+o/---------------::-----------/o:-:hMMMMMh-        :ysyys++:.`            `:osyyyyyyyyyyyysso/-` ./osyy
          ys/                    `/syyyyyssyyshNMMmh+//+yyshhyyyyssos:-----------------------------------------------::::::-------::---:hMMMMMh-       -syyso/-.-::-.`         -osyyyyyyyyyysyso+:.  `-+osyy
          ys-                  `./yyyyyyyyysyymMMh+:/:/oo+/+sysyssoo+:-------------------:////:--------------------/yhhys+:::----------:hMMMMMh-      .oyys+:.   `.-:::-`     .+yssyyyyyyysyyo+/.    `:+syyy
          yo`                 `-+sssyyyyyyyysyNMh::+----/o+:/oyssoos+------------------:+dmo/y-.-/+:-----:---------:::-----------------:yMMMMMh-     `+syo+-`        `.:::-.`.+yyyyssyyysyyso+:`     .+oyyyy
          y+                 `/syyyyyyyyyyyysymN/-:+-----/s+//++osoo/-------------------:ooss/.``.+s+::::+--------------:--------------:hMMMMMy.    `+yyo:.             `.-://syyyyyyyysyss+/-`     `:+syysy
          s/               `:+yyyysysyyyyysyyymm:--o:-::--++/:/:/o+o:--------------------:::::::---//:::o+----------/+syo::/:----------/dMMMMN+`   `/ss+:`                 :+syyyyssyysyso+:.`      .+ossssy
          s-          `  `:oyyssyysyysyyyysssshm:-:+---//:/::/::::/::---------------------------------::+/---------/hdydy-`.:o/--------+NMMMMh-   `/so/-                  -/syyyssyyyysso+:`       `:+syysyy
          s.          `.:ossyysssyyyysyyso+++syN+-//---:/+o+:/:::/:::--------------------------------::://---------:/osy/.```-yo:-----:yMMMMMy.  `:o+:.                  -+sysyyyssooss+/-`        -+oyyyyys
          /`       `.-+ssyyysssyyyyyyyso+/+++sydy-+/---:::+//::::/:/:--------------------------------:::/:---------::::::---..-/:-----/mMMMMMms-`-++-`                  -+oyyssso+++oo+/.         `/+syysyyy
                `.:/osysyyyysyyyyyyyso+/--/+oysyh/:o:--:/++//:::/:://:--------------------------------::/:----------------------------/sshNMMMN+-+/.                   -/sysso+/::/+++:`          -+ssyyyyyy
           ``.:/osyyyyyyyyyyysyysyso+/:``:+osyysyy::+sso:/o+/:::::://::-------------------------------:/::-------------------------------/dMMMmo/:`                   -/osoo+/-.`.++/-`          .++syyyyysy
          +osssyyyysyyyyyyyyyyyssso+:.` -/+ssysyydd/-::---:::::::/::::::---------------------------::::::-----------------------------/:-/dMMMh+-`                   ./os++/-`  `/+/-`           /+syyyyyyyy
          syyyyyyyyyyyyyyyyyysyso+/-`  `/+osysyymMNd/-----/o/::/:/::://:-------------------------:////::---------::------------------/+/:sNMMd+.                    -/+o+/-`   `-+/.            -+oyyyssyyyy
          yyyyyyyyyyyyyyyyyyysso/:. ` `:+ossysydMNmNds+//:+s/:/:::::://::----------------------::/:--------------+o-----------------:/:-+mMMmo`                    ./++/-`     .//-          ` .++syyyyyyyyy
          yyyyyyyyyyyyyyyyyyyo+/.     -/+syyyshNMmmmmd+///+s+://::::://::------------------------:::--::----------++-------------------/hMMd+`                    ./+/-`      `/+:`          ``:+sysyyyyyyyy
          yyyyyyyyyyyysyyyss++:`     ./+osysydNMNmmNmmo``-/s+://:::::://::------------------------://++o:-----//--+/------------------/hNNy:`                    .//:.        :+/`            :+oyssyyyyyyyy
          yyyyyyyyyysssyyso+/-    `.:+syhhhdmMMNmmmmmNd: .:oo/::://::://::-------------------------:::-------/yh+/:-----------------:odMNy.                     ./:.`        .++.            ./+sysyyyyyyyyy
          yyyyyyyyyyysyyso+/`    `+ydNNNNNNNNNmmmmmmmmms` .+s+/:/::::::::::------------------------------------::------------------yNNMMm:                     ./-`         `/+-            `/+ssyyyyyyyyyyy
          yyyyyyyyyyyyys++:`    `oNNNmNmmmmmmmmmmmmmmNmd/ `-oy+::::::::::::----------------------------::-------------------------/NMMMNy`                    -/-           /+:             -+syysyyyyyyyyyy
          yyyyyyyyyyyso+/-     `/NMNmmmmmmmmmmmmmmmmmmmmy. `-oh+::::::::::::-----------------------:osyhhyhdh/--------------------yMMMMm:                    -/-`          :+/`            ./+ssyssyyyyyyyyy
          yyyyyyyyyyso+/.      .dMNmmmmmmmmmmmmmmmmmmmmmmh-  .+y+/:::::::::::------------------:/oso++///+++oh/------------------/NMMMMh`                  `-/-`          -++`            `/+sysyssyyyyyyyyy
          yyyssyysss++:`      `sMMNmmmmmmmmmmmmmmmmmmmmmmmd/` `:s+/::::::::::----------------/+oooosyyyyyyo+/+s-----------------:dMMMMN+                   -/.           -++.            `:+syyyyyyyyyyyyyyy
          yyyyyyyyo+/-`      `oMMNmmmmmmmmmmmmmmmmmmmmmmmmmms- `-//////::/:::::----------------:://///+///+oo+o:----------------yNNMMMd.                 `-/.           ./+.             -/osyyyyyyyyyyyyyyy
          yyyyyyso+/.       `/NMNmmmmmmmmmmmmmmmmmmmmmmmmmmmNd/` .::::::://::/::----------------://///////////o/---------------yNMMMMm/                  :/.           ./+-             ./osyyyyyyyyyyyyyyyy
          yysssso+:.        /mMNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNmo. .://:::::::::::----------------/syysssoooso/:---------------sNMMMMNo`                `:/.           ./+-`            ./+syyyyyyyyyyyyyyyyy
          sssys++:`        :mMNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmy- .:///::///::::::-------------::/+oyhdmmmh+---------------:sNMMMMNo`                `:/.           `:+:`            `:+ssyyyyyyyyyyyyyyyyy
          syys+/-`     ```/mMMNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNh- .::///::://::::::-----------------:/oso:---------------:ymMMNMN+`                `:/`           `:+:`             -+osyyyyyyyyyyyyyyyyyy
          yso+/-`  `./oyhdNNNNMNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd:`.://///:///::::::::----------------------------------/hNMMMMN+                 `/:`           `:+:`             ./ossssyyyyyyyyyyyyyyyy
          yo+/.  .+hmNNNNmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd/`-:::/++//:::/:::::/:-------------------------------+hNNMMMm/`                ./:`           `:+:`             `/+syysyyyyyyyyyyyyyyyyy
          o+:.`:ymNNNmmmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm+`-::://////::::::/:/:::--------------------------/ymNmNMMMy-`               ./:`           `-+/.             `:+osysyyyyyyyyyyyyyyyyyy
          /:./hNNmmmmmmmmmmmmmmNmmmNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmms..:/:::///////:////++o+/:--------------------:/sdmmmmmNMMNNo`             ./-`           `-+/.             `-+oyyssyyyyyyyyyyyyyyyyyy
          +ohNNNmmmmmmmmmmmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNmy:.-::::////++///+oyhhddds/:---------------:ohmmmmmmmmmNNMMMy.           ./-`           `-+/.             `./osyysyyyyyyyyyyyyyyyyyyy
          mNNmmmmmmmmmmmmmmmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd+..:::/::///:///++osyhdmdhs+/::::-------ohmmmmmmmmmmmmNMMMMy.         -/-`           `-+/.`             ./+syyyyyyyyyyyyyyyyyyyyyyy
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmh/.-:::::::::::::::--://+oooo+//:----:sdmmmmmmmmmmmmmmNMMMNs`      `-/-`           `-//.              `/+osyyyyyyyyyyyyyyyyyyyyyyy
          mmNmmmmmmmmmmmmmmmmmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdy/.-:/::/::/::--------------------+hmmmmmmmmmmmmmmmmmNMMMN+     `:/.            `-//.              `:+oysyyyyyyyyyyyyyyysyyyssyy
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdy/.-://:::::::::------------:/ohmmmmmmmmmmmmmmmmmmmmNMMMm:   `:/.  `         `-//.              `-+oyysyyyyyyyyyyyyyyyyyyysyhh
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmy+--:/::::::://:::------:+ydmmmmmmmmmmmmmmmmmmmmmmNMMMMy` `::.             -+/.               -++sysyyyyyyyyyyyyyyyyyysyyhdh
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmho:--://:://://++//:--:hmmmmmmmmmmmmmmmmmmmmmmmmNMMMMm/.::.             -//.               ./+sysyyyyyyyyyyyyyyyyyysyyhdds
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmy+---::::::://+osyysymmmmmmmmmmmmmmmmmmmmmmmmmNMMMMh+:`             -+/.               `/+syysyyyyyyyyyyyyyyyyyysyhdds:
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdy/-``.--::::////oyhmNmmmmmmmmmmmmmmmmmmmmmmNMMMMNo`            `-+/.               `:+syyyyyyyyyyyyyyyyyyyyyyydddy:.
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNdy/-````.--:::::/hmmmmmmmmmmmmmmmmmmmmmmmmNMMMNy.            ://.                :+syyyyyyyyyyyyyyyyysyyyshdddy/..
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNMNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmy+:.`  ``..--+mmmmmmmmmmmmmmmmmmmmmmmmNMMMMd:          `://`                -+oyyyyyyyyyyyyyyyyyyysyyyhddh+...
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNMMNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmhs/.`     `smmNmmmmmmmmmmmmmmmmmmmmNNMMMNo`        `:+/.                .++syyyyyyyyyyyyyyyyyyyyyhdddh+....
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNMMNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdy+-`   :NmmmmmmmmmmmmmmmmmmmmmmmNMMMMh.       `:+/.                ./+syyyyyyyyyyyyyyyyyysyyhdddho-....
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNMMNNmmmmmmmmmmmmmmmmmmmmmmNNmmmmmmmmmmmmmmmmmmNmdho:`/mmmmmmmmmmmmmmmmmmmmmmmmmNMMMm/`     `:+/`                `/+syyyyyyyyyyyyyyyyyyssyhdddds-.....
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNMMNmmmmmmmmmmmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmdyhNmmmmmmmmmmmmmmmmmmmmmmmmmNMMMh-    `:+:`                `:+syyyyyyyyyyyyyyyyyyysydddddy-......
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNMMNmmmmmmmmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmNmmmmmmmmmmmmmmmmmmmmmmmmmmmNNMNy-  `:+:`                `:+oyyssyyyyyyyyyyyyyyyyhdddddh:.......
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNMMNNmmmmmmmmmmmmmmNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNMNh-./+:`                 -+osysyyyyyyyyyyyyyyyyyhdhdddh:........
          mNNMMNNNmmmmmmmmmmNMNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNMms+-`                 -/osyssyyyyyyyyyyysyyyyhdddddd/..........................................................."""
    time.sleep(1.0)
    print """  Things were going fine for a couple of years of the two leaders working together against Russia"""
    time.sleep(1.5)
    option = raw_input('Continue?[Yes/No]---> ')
    if option == 'yes':
        story_pic_10()
    elif option == 'Yes':
        story_pic_10()
    elif option == 'YES':
        story_pic_10()
    elif option == 'no':
        main_menu()
    elif option == 'No':
        main_menu()
    elif option == 'NO':
        main_menu()
    else:
        story_pic_2()


#-----------------------------------------------------------------------------------------------------------#
def story_pic_10():
    os.system('cls')
    time.sleep(0.5)
    print """
                                                        ...`
                                                      `:-....`
                                                     :.ss+`    .-+
                                                     .:/:o`  /oysy+`                                                                         .::--.
                                                     .+++`  `yooo+s.                                                                        ---:-:.. `:/-`
                                                   `/so/.    oo-+o/                                                                       `:+oo++/:-  /ho:o-`
                                                  `oyy+` `-.-oy//o:              `                                                       `-:+-./++/:` `.-`odyo+:-`` ``
                                                  oNddhsssyyyhmmsoo/    `..-`-``+o:.-.                                                   `.:+/yh++/+:.` `  hds.-::::.
                                                  `:shddddhhhmmNmyhddhhydsyyss/:so-..-                                                `.:odhyyysydhydmdhdhshmms
                                                      ```oNNNNNNNmmoooooo/+:`..o/-. ..                                     `.-:osyssyhhddhshdddmmddmmmyoossoo/.
                                                         `sNmmmmNNmo            ```                                      .oydsooooo/:---.`-mmddmmmddm+
                                                           ymmmNNNm/                           ``.````````               .:/-:/:-.        `sdmdmdddmo
                                                           -mmNmNmm`                         ```  ``  ``...`````                           .dddmmddh`
        .----`                                             oddmmNmh                        `.`  ``..````....---:``                          smNNmddh`
       `:o+/-.`    `/o++.                                 `++hmddmy...--``                 .` `..``` ``````````.--`.`                 ``    /dNNNNmds.
       .syddh:    -yhhddmy`                              .-.-:/:sd/:/+o/::.               .`` ``````        ``````.:-.`             `shhhyysydmmmmmdhy.                               .:/+/-`
       -ymmmNm/. :hdhmhhNd`                              :..-:::dy/+soo++/-             `-.```````````         ````..:--`           -mNdhdmmmmmmmmmmmdh:                             /dmmmmmy-
       -hdddddddo-hmmNddm/ :syso+/`                      :o//+++dhshdhoo/`           ` `-`. ``  ````  ```          ``.---`           :ohdmddmNNNNNNNmmdy                             omhhddNms
       oydh.-ohNd+dNMmhdmd/dNsoo//.                      oshhhhsyyhhhh+-```` ```.``..-.-.````     ```    ````         .:.``            `-ymmdmmNNNNmmdy+                             `yhhyhmd-  //-.
      -yhmhsydydNNNNNNNNdhdNNhsy+/+/////:/oo/:-..`   ```//odNNhhy++/--..-..`..`..`````-.`.```     ````     ```   `    .:-.```````````````.+dmmdmNNmmh+.`..`   `-.               `..`  -yhyhdh- :hyhys:.
      ohdmdNNmddddmmNNmNdsdmNNNmhhhhyhhhhdhysyo--...``-//oyNNmo..````````````````````````.``  ``     `     ```   ```   `:-`````````````````.odddmNNmys``````.-:+o/---:/+++///:::+o+o+::yhhhhhy+-+hoshyyo`
      -yhhddddNhsshhddNdmNNmdmmmdmmdhs/:+mmmdo-..``.://++oyNm+````````````````````````.``. ` ``````    `      ```````  `:--`                `-sdmmmmhh. ````-//+oo//++o/ooooo+oooo++++oyyyhhhys+hhhyhhhhy`
       `````.oNdhyhhdmmdmMNm:`.......    +hdy.    .ohs++.`.sm`.`.......-....`.````````.``.``  ``````      ``       `` `.:-.-```````````````````:ymmmmhy-`.```  `..````....`.-----/os++oyoyhhyo/+shhhhhhhho
         `..+NNNNmNNNNmmNddNh..`          ``     `/hhdy:    .          ````.`.`-.-.----.`````````           ``      ```:-.`                     `ommmdmy:                        .osooohhhhyo++oo+-:/osso:
       .oosyhmhyNmNNNmmNo./mdhyo+:              `-yyho.`                          ````..```.````               `      `-.                         :ydmmmh/                        :o+oyhhysooyyys.    ``
       -:-::::`.NNNmmmNN+  -://:-`            .-+yhy-.                                 ``...`````                     ``                           `ooydmd-                        -ohhysooyyhhh:
      +dhy/+ooshmmmmdddmm/                  `/dmmh+-                                    .-.`.`````    `     ``     ` ````                        `    .hdmy                         /hhyyyhhyyyy`
     `hddhhdmmmNMNmdyyhNNNo`               ..yNmh:                                      `......`````` `.      `  ``-.```                         :o:`  -hdd-                        +hhhyhhhyhh+
     -mdddhyhdmMMMmdyyNNmdho                /mms`                                         `.`--.```````..```  ..-:-.` ``                          odh+. -hds                       :oossyyyyyyy/----.``
      /dmmmdhhmMMMNdhmMmmdyy/               `om.                                           ```.````--...-````..--.`   `                           .dddh+`.ddyo:                   -yddysssososyhhhyyyysss+`
       .sdmmdhmmoo/..smNmdhhy                 .                                                ``-`...::.`   ```    ``                            -ddddhs`-hmmy                 .-+yddddddhhhddddddhhhhhdy`
         .omNdddo`    +mNmdhdy+                                                                   ``````.`````` ````                              ohhddhho .sdd/               `+oyhshdddddhddddmmmddddhs`
           ./hmddy:`   sNmdyhdd+                  `..`                                                   ``````  ``                              `dhhddhyh-  :hh               :ohhhyhdy//://ymmmmdhys:.
             `omddyyy: smmdhyhdd`                `sddhy-                                                                              ````       .dhhdhyyho   ..              `/hhsyddh.``-:ydhyo:...
              `hNNddmh..yNmhhhms                 :dmmmms                  `.-.`                                                       ......``   -dhdhhyyhs                     hyyhdhhdhhdhs:.
              .dMNmhdNd``omdhhms                 ymmdds:                 /yhhhho`                                         `    `       ````.-.`.+hddhhhhhd:                    .yyhddhNmhs+.`
               +dmmhmNo   /ddddo                 hhydd-     `.--.`      -dddddmm+                                        `` `.```     ` `   -..`-oddddhhs:                    -yhhhh+Nmh:`
                :NNNMMy    :hmds`                s+hMMm. ``:yhhddhs:`-:.+mmddddm/                                        `..-`..``-:+ssso+.`..````os/-.`                     :yyhdd:`ss-
                yMMdho.     sdNdy:              `ddMMMMhsssddddddddssdmdhmmmdddh                                         ``  .-..-odddhy:.......:+yy. `:+oo:`               +hhhhdo
                dNh-`..`    ddmdmdo              -dNNmmmdhhddmmmddNmNMNmdmmmmyy`                                          ``--..``/hhs:-::+ooosyhyyhhsyddddds`              ddhddh`
                //.``..     ymmdNNm`              :dmdmmmmmmNNmdmNmNMNyodNNmNo`                                           `/:.-soohh+```..:hddhhhhhdddddddddd+             -mddmmo
                  ..`..     -MNmmNNy-              ./---..--dNmdNNMNNm//hMMmh-                                     ``    `shh+shhhh+````../hhhhhhhhddddddddddy             :dhmmd`
                  `....      hNdhNNms.                     .ddmmmMMMMNNNMMNmdo                                   .....   +hysooosss`````../hhhhhhhhhhhhhddddd+             `hhdh.
                   `..`     :dNmdmNmMNo                 ``/hddmNNMNNMMMMNmdmdh      `                            ``..`   /:.``````` ``````.:ydddddddhddddddh/               yhh`
                     `     :NmmMMMhoso:              `.+shdmdmMMNNNNMNNNmmdmd:   -/sy/`                           `..`` `.`.-/o+.``````.````-yddddhhhhhhdds`               -hd/
                           .:.sMNNh..`             .oyyyohdmmNMMNNMNNdsmNmhdy    hdmddh.                           `-.``....-sdhs:``.`````.`../shddhhhhhdd.               `hdm-
                              `+/:-...           `.hs++oyhddysoomMNd/` sNNdmNyyy+mmmdd+                             `...``..`:hddho-``````.`.```./yhdddddd.               :ydm-
                               `..``.`          -so/:/oyyddyso:/sNNo-`  mNNMMMMmsyNd:.                                `....`  `/ys+.`..`...`-.`````:shhhdd+              `hdmN.
                                `....`      .syss///+yhmmmhsyhmmmh+/++- sNmNMMdso+/.                                     `    `.`````..--``.o/..````./hhddd.             `ymmy`
                                 `...`   `:sNMMd++shmNNmdddhdNMNmyo///o+/yddsso-                                            ``.```....-:/+shhhyo:.``..:shdds               ..
                                  `..` `:hhhdmNdsdNMNmy/:`/shdmNNmdhsoohmNmM-                                               ```.-.`...-/yhhhhhhhhyo-...../sh
                                    `:ymNNMNdhNmmmmy+-       .:/osyNMNMhdMyy                                                 ``.-..````../hhdhhhhddds/-.....``
                                   -yMMMNmNhyNMNy+-              +sNMMdymMm+                                                     ````````..syddhhddddhy-/-..````
                                  -mMMMMMMNmdys:                .hmdMMmmNMy`                                                           ```...:+shddddds   ``````.`
                                `+NMMMMNmNmdo                   `MdNMMMMMm:                                                                ```.`-+sdddo     `````.`
                              `+mMMMMNyos+-.                    `MdNMMMMs-                                                                    s/...odd+       `..```
                             .dMMMMNy:--`                       .dNMMMN/                                                                      /dhsohdd.          .`..`
                             yMMMmNd.                          -dmNMMM/                                                                        oddddy-             .``.
                           .yhdmNhso                           +mmMMMs`                                                                         .::.                .``.`
                          /yo:/sh-                            `ydMMNmy:                                                                                             `....
                         `do//ydm.                            -MMMds+/:+/-                                                                                            ``
                          ymddmd+                             `ohddmdysoyh`
                           `--.                                   `:+oso+.                                                                                                                  """
    time.sleep(1.0)
    print """ THIS PICTURE IS A SNEAK PEEK OF WHATS TO COME LATER ON IN THE STORY! IM NOT DONE WITH ALL THE CUTSCENE PICTURES YET!"""
    time.sleep(1.5)
    option = raw_input('Continue?[Yes/No]---> ')
    if option == 'yes':
        play()
    elif option == 'Yes':
        play()
    elif option == 'YES':
        play()
    elif option == 'no':
        main_menu()
    elif option == 'No':
        main_menu()
    elif option == 'NO':
        main_menu()
    else:
        story_pic_10()


##def story_pic_4():
##
#   time.sleep(1.5)
#   option = raw_input('Continue?[Yes/No]---> ')
#   if option == 'yes':
#       story_pic_2()
#   elif option == 'Yes':
#       story_pic_2()
#   elif option == 'YES':
#       story_pic_2()
#   elif option == 'no':
#       main_menu()
#   elif option == 'No':
#       main_menu()
#   elif option == 'NO':
#       main_menu()
#   else:
#       story_pic_1()
#
#
#def story_pic_5():
#
#   time.sleep(1.5)
#   option = raw_input('Continue?[Yes/No]---> ')
#   if option == 'yes':
#       story_pic_2()
#   elif option == 'Yes':
#       story_pic_2()
#   elif option == 'YES':
#       story_pic_2()
#   elif option == 'no':
#       main_menu()
#   elif option == 'No':
#       main_menu()
#   elif option == 'NO':
#       main_menu()
#   else:
#       story_pic_1()
#
#
#-----------------------------------Section#8----------------------------------------------------------------------#


title_pic()
clear_screen()
main_menu()
