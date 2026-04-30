import numpy as np
import pandas as pd
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time:", end - start)
    return wrapper

def generator():
    for i in range(5):
        yield i

@timer
def process():
    data = list(generator())
    arr = np.array(data)

    df = pd.DataFrame({"Numbers": arr})
    print(df)
    print("Mean:", np.mean(arr))

process()
