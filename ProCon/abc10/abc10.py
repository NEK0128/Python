import math
from Euclidean_distance import Euclidean_distance
if __name__ == "__main__" :

    tmp  = input().split(" ")
    start = (int(tmp[0]),int(tmp[1]))
    goal = (int(tmp[2]),int(tmp[3]))
    T = int(tmp[4])
    V = int(tmp[5])
    n = int(input())
    girls = []

    sw = 0
    for i in range(n):
        tmp = input().split(" ")
        tmp = (int(tmp[0]), int(tmp[1]))
        p1 = Euclidean_distance(start, tmp)
        p2 = Euclidean_distance(tmp, goal)
        distance = p1.calc_dist() + p2.calc_dist()
        if distance <= V*T :
            print("YES")
            sw = 1
            break;

    if sw == 0:
        print("NO")
