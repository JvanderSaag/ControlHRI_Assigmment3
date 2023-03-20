import multiprocessing
import os

# Creating the tuple of all the processes
all_processes = ('Asteroids/Asteroids.py', 'haply_sim/haply.py')
python_path = 'C:/Users/jelme/anaconda3/envs/hri/python.exe'  # Put YOUR CONDA PATH or 'python' for default here


# This block of code enables us to call the script from command line.                                                                                
def execute(process):
    os.system(f'{python_path} {process}')


if __name__ == '__main__':
    process_pool = multiprocessing.Pool(processes=2)
    process_pool.map(execute, all_processes)