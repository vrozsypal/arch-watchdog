import psutil
import time

psutil.cpu_percent(interval=None)

while True:
    cpu = psutil.cpu_percent(interval=None)
    mem = psutil.virtual_memory()
    # print('CPU, MEM')
    print(f"{cpu} %, {((mem.available)/1024**3):.2f} GiB")
    time.sleep(1)
