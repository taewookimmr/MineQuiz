# sum10bomb

## problem definition

```
예를 들어, 113794가 input으로 주어졌을때, low index부터 요소별로 탐색을 했을 때, 
연속된 두 수의 합이 10이면 그 두 수를 pop한다.
이를 연속된 두 수의 합이 10인 경우가 없을 때까지 반복한다. 
과정 : 113794 -> 1194 -> 14, 즉 14가 최종적으로 남는다.

이러한 문제를 해결하는 일반화된 프로그램을 작성하여라
입력은 숫자로만 구성된 문자열이다.
```

## plausible solution?
```python
def solution(src):
    src = [int(e) for e in src] # 문자열을 숫자 리스트로 변환
    while True:
        indexlist = []
        for i in range(len(src)-1):
            if int(src[i])+int(src[i+1]) == 10:
                if i not in indexlist : indexlist += [i, i+1]                 
        src = [src[j] for j in range(preslength) if j not in indexlist]    
        if len(indexlist) == 0:
            break
    print("".join([str(e) for e in src])) # 숫자 리스트를 다시 문자열로 변환
solution("113794") 
```
