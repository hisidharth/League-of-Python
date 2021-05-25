from art import *
import time
tprint("Welcome to League of Python")
tprint("You can check builds, runes, and more")
build={
    "Irelia":"BoTRK, Stride Breaker, Plated Steecaps, Titanic Hydra, Deaths Dance, Guardian Angel",
    "Akali":"Rift Maker, Sorcerors Shoes, Demonic Embrace, Lich Bane, Void Staff, Zhonyas Hour Glass",
    "Pyke":"Prowlers Claw, Ubral Glaive, Edge of Night, Yommus Ghost Blade, Mobility Boots, Guardian Angel"
    }
runes={
    "Irelia":"Conqueror, Presence of Mind, Tenacity, Last Stand, Taste of Blood, Raveous Hunter",
    "Akali":"Electrocute, Sudden Impact, Eyeball Collection, Raveous Hunter, Presence of Mind, Coup de Grace",
    "Pyke":"Hail of Blades, Cheap Shot, Eyeball Collection, Ultimate Hunter, Second Wind, Unflinching"
    }
team_comp={
    "Knockup":["Top:Malphite","Jg:Nunu","Mid:Yasuo","ADC:Kalista","Supp:Alistar"],
    "Funnel":["Top:Lulu","Jg:Master Yi","Mid:Taric","ADC:Soraka","Supp:Seraphine"]
    }
    

champion_confirmation={}
def ask_runes():
    print(runes[rchampion])
def ask_build():
    print(build[bchampion])
def add_champ():
    build[addchampion]=addbuild
def add_runes():
    runes[addchampion]=addrunes
def full_setup():
    print("build:",build[setupchampion],"runes",runes[setupchampion])
def add_teamcomp():
    team_comp[compname]=["Top:"+toplaner,"Jg:"+jungler,"Mid:"+midlaner,"ADC:"+adc,"Supp:"+supp]

index=0
while index<1:
    check=input("What do you want to do?")
    check=check.lower()
    if check=="build":
        bchampion=input("Which champion?")
        ask_build()
    if check=="runes":
        rchampion=input("Which champion?")
        ask_runes()
    if check=="add":
        addchampion=input("Which champion do you want to add?")
        addbuild=input("What items will you build?")
        addrunes=input("what runes will you take?")
        add_runes()
        add_champ()
        champion_confirmation[addchampion]=[addrunes, addbuild]
        print(champion_confirmation)
    if check=="full setup":
        setupchampion=input("which champion?")
        full_setup()
    if check=="team comp":
        for x in team_comp:
            print(x,team_comp[x])
    if check=="add teamcomp":
        compname=input("what is this team compositions name?")
        toplaner=input("what toplaner do you want to add?")
        jungler=input("what jungler do you want to add?")
        midlaner=input("what midlaner do you want to add?")
        adc=input("what ADC do you want to add?")
        supp=input("what support do you want to add?")
        add_teamcomp()
        for x in team_comp:
            print(x,team_comp[x])
    if check=="help":
        print("You can do the following: build, runes, add, full setup, team comp, add teamcomp, help(capitalize champion names and team compositions:Irelia, or for team comp:Funnel")
    if check=="close":
        tprint("BYE","rnd-xlarge")
        time.sleep(2)
        index+=1

        

