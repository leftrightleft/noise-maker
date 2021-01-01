import time, sys
import random
from pygame import mixer
import glob

mixer.init()

files = glob.glob("./sounds/*.wav")

sounds = []

for f in files:
    sounds.append(mixer.Sound(f))

random.choice(sounds).play()

time.sleep(1)