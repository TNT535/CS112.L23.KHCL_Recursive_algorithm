# import random
# random.seed(19)
# z = 10000
# n = int(z)
# a = list([random.randint(1, 10) for x in range(1, z + 1)])
# m = int(z)
# b = list([random.randint(1, 10) for x in range(1, z + 1)])
# print(a, '\n', b)


n = int(input())
a = list(map(int, input().strip().split()))
m = int(input())
b = list(map(int, input().strip().split()))
# print(n, a, m, b)


# install binary search maxmi
def element(a):
    for x in a:
        yield x


def testmax(maxmin):
    pusher = element(b)
    for x in a:
        if x < maxmin:
            for y in pusher:
                if y + x >= maxmin:
                    break
            else:
                return False

    return True


def result(maxmin):
    pos = 0
    list_ans = []
    for i in range(n):
        if a[i] < maxmin:
            pick = False
            while pos < m and not pick:
                if (a[i] + b[pos]) >= maxmin:
                    pick = True
                else:
                    pick = False
                pos += 1
                if pick:
                    list_ans.append(str(i + 1) + ' ' + str(pos))
    return list_ans


left = min(a)
right = min(a) + max(b)

mid = (left + right) // 2
while left != mid and right != mid:
    if testmax(mid):
        left = mid
    else:
        right = mid
    mid = (left + right) // 2
# print(left, right, testmax(left), testmax(right))
if testmax(right):
    mid = right
else:
    mid = left
list_ans = result(mid)
print(mid, len(list_ans))
for kq in list_ans:
    print(kq)
