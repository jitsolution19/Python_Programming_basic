'''
Created on 25-Mar-2024

@author: jeete
'''
import time
for j in range(10):
    for i in range(1, 10):
        print(i, end="")
    for i in range(1, 10):
        print(i, end="")
    time.sleep(2)
    print()