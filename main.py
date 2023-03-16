import haply_sim.haply
import Asteroids.Asteroids
import subprocess
import sys

sys.path.append("/Asteroids")
sys.path.append("/haply_sim")

subprocess.Popen(["python", "haply.py"])
subprocess.Popen(["python", "Asteroids.py"])

