#Alisha Rhodes
#12/7/2025
#15.1 Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between zero and one, print the current time, and then exit.

import multiprocessing as mp
import random
import time
from datetime import datetime

def process(name: str):
    random.seed(mp.current_process().pid + time.time()) #random number generator function
    delay = random.uniform(0,1)
    time.sleep(delay)

    now = datetime.now().strftime("%Y-%m-%d %H:%M") #pull local time and converting to string 
    print(f"[{name}] Slept {delay:.3f}s | Time: {now}")

if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)
    
    processes = [
        mp.Process(target=process, args=("Process-1",)),
        mp.Process(target=process, args=("Process-2",)),
        mp.Process(target=process, args=("Process-3",)),
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("All processes completed.")
