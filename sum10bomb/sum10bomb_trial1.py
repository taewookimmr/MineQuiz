# trial1 : 재귀를 사용한 접근법 (self-star : 1 of 5)

answer = []
def recur(src):
    n = len(src)
    i = 0
    count = 0
    while i < n-1:
        if int(src[i]) + int(src[i+1]) == 10:
            count+=1
            temp = []
            if i+1 < n-1:
                temp = src[:i] + src[i+2:]
            else:
                temp = src[:i]
            recur(temp)
            break
        i+=1
    if count == 0:
        answer.append("".join(src))    
            
recur("113794") 
print(answer[-1])

# 그렇지만 비효율적인 부분이 보인다. 
# 여기서 비효율적인 부분이란, src가 주어졌을 때, 첫번째로 sum10 조건을 만족시킨 부분이 디텍되자 마자 
# 재귀를 호출한다, 이럴 필요는 없다.

# (추가 코멘트 : 이런 방식으로 하면 결과가 달라질 수 있지 않을까?)
# 비교 대상, [주어진 리스트 순회 시  첫 sum10bomb 디텍되면 슬라이싱하고 바로 새로운 재귀 호출] vs [주어진 리스트 순회 시 모든 sum10bomb 처리하고 새로운 재귀 호출]
# 후자의 방식으로 구현을 해야 원하는 답이 정확하게 나올 것이다. 
# 그런데 전자의 방식으로도 후자의 방식과 같은 결과를 뱉어낸다면? 


