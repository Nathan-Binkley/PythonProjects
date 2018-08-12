import time
import random

random.seed(time.time())

for i in range(0,6):
    
    hour = random.randint(16,24)
    minute = random.randint(0,60)
    print(str(hour)+":"+str(minute))
