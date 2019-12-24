# trial4 stack을 사용한 재귀 
# 불필요한 인덱싱이 없다.

def solution(src):
    src = [int(e) for e in src] # 문자열을 숫자 리스트로 변환
    def recur(source):
        stack=[]
        n = len(source)
        stack.append(source.pop(0))
        while len(source):
            if stack[-1] + source[0] == 10:
                stack.pop()
                source.pop(0)
            else :
                stack.append(source.pop(0))  
        if len(stack) != n:
            recur(stack)
        else :
            print("".join([str(e) for e in stack]))           

    recur(src)
    
solution("113794") 




