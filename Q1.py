"""
ACPC 1
"""

__author__ = "SORENSHAMLOU"

__email__ = "sorenShamloo.programmer@gmail.com"

__mobile__ = "09932062665"

from numpy import (
    zeros,
    int32
)

try:
    home = int(input(f"Home Number >>> "))
except ValueError:
    print("ValueError")
    exit(0)

if 0 <= home <= 100:
    sum_bomb = 0
    array = zeros(home, int32)
    x = 1
    for i in range(home):
        x = i+1 # خانه بعدی
        y = i-1 # خانه قبلی
        if y < 0:
            y = home-1
        if x >= home:
            x = 0
        if array[i] == 2:
            continue
        array[i]+=2
        array[x]+=1
        array[y]+=1
        sum_bomb+=1
        if sum(array) >= 2 * home:
            break

print(f"sum bombs : {sum_bomb}")
