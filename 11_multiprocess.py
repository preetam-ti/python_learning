import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')



"""The platform.processor() function returns the processor name as a string.

>>> import platform
>>> platform.processor()
'Intel64 Family 6 Model 23 Stepping 6, GenuineIntel'
"""

"""NO of CPUs
import multiprocessing
>>> multiprocessing.cpu_count()
8

##python get cpu info
import cpuinfo
print('CPU =', cpuinfo.get_cpu_info()['brand_raw'])
"""