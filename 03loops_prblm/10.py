'''
Docstring for 03loops_prblm.10


exponetial backoff:
implement an expontial backoff strategy that double check the wait times between retries and stratring from 
1 second ,but stops after 5 retries


''' 

import time

wait_time=1 # initial wait time in seconds
max_retries=5
attempt=0

while attempt<max_retries:
    print('Attempt',attempt+1,'--Wait Time--',wait_time)
    time.sleep(wait_time) # simulate wait
    wait_time *=2 # double the wait time
    attempt +=1
    