import time

timeout = 3
start_time = time.time()

while time.time() < start_time + timeout:
    print('i')

print('done')
