# trial3 : trial2과 비슷, bombIndex라는 리스트 추가 (self-star : 2.5 of 5)
# bombIndex라는 리스트를 이용하여 터트릴 녀석들 index 저장해서 한꺼번에 터트려, 이게 while의 body
# 그나마 괜찮은 방법 

def solution(src):
    src = [int(e) for e in src] # 문자열을 숫자 리스트로 변환
    while True:
        indexlist = []
        n = len(src)
        for i in range(n-1):
            if int(src[i])+int(src[i+1]) == 10:
                if i not in indexlist : indexlist += [i, i+1]   
        if len(indexlist) == 0: break                              
        src = [src[j] for j in range(n) if j not in indexlist]    
    print("".join([str(e) for e in src])) # 숫자 리스트를 다시 문자열로 변환
    
solution("113794") 




