# trial2 : 2중 반복문 접근법 (self-star : 1.1 of 5)


def solution(src):
    src = [int(e) for e in src]
    prevlength = len(src)
    initiate = True
    while initiate | prevlength != len(src):
        initiate=False
        preslength = len(src)
        
        for i in range(preslength-1):
            if int(src[i])+int(src[i+1]) == 10:
                src.pop(i+1)
                src.pop(i)
                break
        prevlength=preslength
    print("".join([str(e) for e in src]))
            
solution("113794") 




