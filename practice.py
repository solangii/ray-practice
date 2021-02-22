import numpy as np
import psutil
import ray
import time
import datetime
import scipy.signal

num_cpus = psutil.cpu_count(logical=False) #20

# 일반 함수 호출
def print_current_datetime():
    time.sleep(0.3)
    current_datetime = datetime.datetime.now()
    print(current_datetime)
    return current_datetime

print_current_datetime()

#ray 실행
ray.init(num_cpus=num_cpus)

#ray Task
#remote function

@ray.remote
def print_current_datetime_ray():
    time.sleep(0.3)
    current_datetime = datetime.datetime.now()
    print(current_datetime)
    return current_datetime

# print_current_datetime_ray() : type error
#print_current_datetime_ray.remote() #object ref
feature = print_current_datetime_ray.remote()
#print(feature) #ObjectRef
ray.get(feature)


features = [print_current_datetime_ray.remote() for i in range(4)]
#print(features)
ray.get(features)