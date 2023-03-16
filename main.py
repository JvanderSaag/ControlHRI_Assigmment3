import Asteroids.Asteroids
import haply_sim.haply
import subprocess


hap = subprocess.Popen(["haply.py"], shell=True)
ast = subprocess.Popen(["Asteroids.py"], shell=True)


while True:
    print("Running")


