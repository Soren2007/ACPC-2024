"""
ACPC 1 Q1
"""
from numpy import (
    zeros,
    int32
)

try:
    n = int(input(f"n >>> "))
except ValueError:
    print("ValueError")
    exit(0)

if 0 <= n <= 100:
    sum_number = 0
    array = zeros(
        n,
        int32
    )

    i = 0
    while sum(array) < 2 * n:
        x = i+1 # خانه بعدی
        y = i-1 # خانه قبلی
        if y < 0:
            y = n-1
        if x >= n:
            x = 0
        if n <= i:
            i = n-1
        array[i]+=2
        array[x]+=1
        array[y]+=1
        sum_number+=1
        i+=2

print(f"{sum_number}")
