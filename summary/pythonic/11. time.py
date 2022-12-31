import time

start_time = int(round(time.time() * 1000))

time.sleep(2)

end_time = int(round(time.time() * 1000))

print(end_time - start_time)
