# trial5 : trial4의 비재귀 version.

def solution(src):
    src = [int(e) for e in src] # 문자열을 숫자 리스트로 변환
    while True:
        stack=[]
        n = len(src)
        stack.append(src.pop(0))
        while len(src):
            if stack[-1] + src[0] == 10:
                stack.pop()
                src.pop(0)
            else :
                stack.append(src.pop(0))  
        if len(stack) != n:
            src = stack
        else :
            print("".join([str(e) for e in stack]))           
            break
    
solution("113794") 




