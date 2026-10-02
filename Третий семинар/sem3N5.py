import numpy as np

N, M = map(int, input().split())

def spiral_matrix(N, M):
    left, right, bottom, top = 0, M, N, 0
    res = np.zeros((N, M))
    num = 1

    while left < right and top < bottom:

        res[top, left:right] = np.arange(num, num + right - left)
        top += 1
        num += right - left

        if top < bottom:
            res[top:bottom, right - 1] = np.arange(num, num + bottom - top)
            right -= 1
            num += bottom - top
        else:
            break

        if left < right:
            res[bottom - 1, left:right][::-1] = np.arange(num, num + right - left)
            bottom -= 1
            num += right - left
        else:
            break

        if top < bottom:
            res[top:bottom, left][::-1] = np.arange(num, num + bottom - top)
            left += 1
            num += bottom - top
        else:
            break

    return res

A = spiral_matrix(N, M)

B = np.arange(N).reshape(-1,1)

print(A*B)
