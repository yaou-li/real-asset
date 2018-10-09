import os
import time

times = int(os.argv[1])
sleep = int(os.argv[2])

path = 'test' * times

print 'sleeping', len(path)

time.sleep(sleep)
