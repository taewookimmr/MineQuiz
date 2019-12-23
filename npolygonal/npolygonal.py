
import matplotlib.pyplot as plt
import math

def calc():
    import math
    n = 1000000000
    answer = 1
    for i in range(1, n+1, 1):
        y = math.pi * i /(2*i +4)
        z = 1/math.sin(y)
        answer *= z
        if (i)%10000000 == 0:
            print(i, answer)
    print(n, answer)

def solution(n=1):
    r = [1 for _ in range(n+2)]
    for i in range(1, n+1):
        s = math.sin((i)*math.pi/(i+2)/2)
        r[i+1]=r[i]/s

    def drawCircle(n):
        radius = r[n]
        coord = [[0, radius]]
        
        theta = 2*math.pi/360
        accum = 0
        while accum < math.pi * 2:
            accum += theta
            px, py = coord[-1]
            nx = math.cos(theta) * px - math.sin(theta) * py
            ny = math.sin(theta) * px + math.cos(theta) * py
            coord.append([nx,ny])
        x,y = zip(*coord)
        plt.plot(x,y)    
    
    def drawOuter(n):
        radius = r[n+1]
        coord = [[0, radius]]
        
        theta = 2*math.pi/(n+2)
        accum = 0
        while accum < math.pi * 2:
            accum += theta
            px, py = coord[-1]
            nx = math.cos(theta) * px - math.sin(theta) * py
            ny = math.sin(theta) * px + math.cos(theta) * py
            coord.append([nx,ny])
        x,y = zip(*coord)
        plt.plot(x,y)

    plt.figure("hello world")
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    for i in range(1, n+1):
        print(i)
        drawCircle(i)
        plt.draw()
        plt.waitforbuttonpress()
        drawOuter(i)
        plt.draw()
        plt.waitforbuttonpress()
    # plt.show() 

    plt.figure()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    for i in range(1, n+1):
        drawCircle(i)
    plt.show() 

solution(n=20)

def fitting():
    pi = math.pi
    e = math.exp(1)
    uc = 8.70003664760304

    heap = []
    import heapq
    n = 30
    for i in range(-n, n+1, 1):
        for j in range(-n, n+1, 1):
            candi = (pi**i) / (e**j)
            print(candi, i, j)
            candi = abs(uc-candi)
            heapq.heappush(heap, [candi, i, j])
    error , i, j = heapq.heappop(heap)
    print(error, i, j)

    
# fitting()