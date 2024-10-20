"""
ACPC 2
"""


n = int(input("n >>> "))
a = list(map(int, input("a >>> ").split()))

# تعیین جایگشت متناظر با خصیصه‌ی ارزش‌معنوی
permutation = [-1] * n
print(permutation)
for i in range(n):
    for j in range(n):
        if a[i] + a[j] == i + j + 2 and permutation[j] == -1:
            permutation[j] = i + 1
            break

if -1 in permutation:
    print(-1)
else:
    print(' '.join(map(str, permutation)))
