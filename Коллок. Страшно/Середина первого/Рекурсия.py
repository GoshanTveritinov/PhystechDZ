#Первый - третий билет

def fib1(N): #Рекурсия без меморизации
    if N == 0:
        ans = 0
    if N == 1:
        ans = 1
    else:
        ans = fib1(N-1) + fib1(N-2)
    return ans

def BinSearch(a, N):
    if not a:
        return "Список ПУСТ((("
    left = 0
    right = len(a)-1
    
    while left <= right:
        half  = (left + right)//2
        if a[half] == N:
            return f'Мы нашли! Твое число {N} в списке под номером {half}'
        elif a[half] > N:
            right = half-1
        else:
            left = half + 1

    return "Мы с питоном ничего не нашли("
#асимптотика О(logN)

def BSR(a, N):
    if not a:
            return "Список ПУСТ((("
    left = 0
    right = len(a)-1
    half  = (left + right)//2
    if a[half] == N:
        return f'Мы нашли! Твое число {N} в списке под номером {half}'
    elif a[half] > N:
        right = half-1
        return(a[left:right], N)
    elif a[half] < N:
        left = half + 1
        return(a[left:right], N)

    return "Мы с питоном ничего не нашли("
#асимптотика О(logN)



def fib2(N, cache = {0:0, 1:1} ):  #Рекурсия с меморизацией
    if N in cache:
        return cache[N]
    else:
        cache[N] = fib2(N-1, cache) + fib2(N-2, cache)
        return cache[N]


