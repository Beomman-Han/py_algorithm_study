x,y,w,h = map(int,input().split(" "))

if (1 <= w and h <= 1000) and (x >= 1 and x <= w - 1 ) and (1 <= y and y <= h - 1) :
    print(min((h-y,w-x,x,y)))