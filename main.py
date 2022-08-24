from datetime import datetime
from pygame import mixer
from time import time

def musicloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break



def my_log(msg):
    with open("mylog.txt",'a') as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__=='__main__':
    # musicloop('water.mp3','stp')
    init_water=time()
    init_eyes=time()
    init_exec=time()
    watersecs=5
    eyssecs=10
    execsecs=15
    while True:
        if time()-init_water>watersecs:
            print("Water Drinking time. Enter 'done' to Stop the alarm")
            musicloop('water.mp3','done')
            init_water=time()
            my_log('done water time:')
        if time()-init_eyes>eyssecs:
            print("Eye Excersize time. Enter 'edone' to Stop the alarm")
            musicloop('eye.mp3','edone')
            init_eyes=time()
            my_log('done eyes excersize at time:')
        if time()-init_water>watersecs:
            print("Physical excersize time. Enter 'pdone' to Stop the alarm")
            musicloop('gym.mp3','pdone')
            init_exec=time()
            my_log('done physical excersize at time:')
        


