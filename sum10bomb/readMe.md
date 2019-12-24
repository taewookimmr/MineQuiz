# sum10bomb

## problem definition

```
숫자로만 구성된 문자열이 input으로 주어진다.
해당 문자열을 lower to higher of index 방향으로 순회하면서
연속된 두 숫자의 합이 10이면 그 두 숫자를 pop한다. 이러한 동작을 bomb이라고 한다.
해당 순회시 bombs하고 남은 나머지를 새로운 input으로 하여 위의 과정을 반복한다. (더 이상 bomb이 발생하지 않을 때까지 반복한다.)
최종적으로 남은 문자열을 반환하는 프로그램을 작성하여라.

```

## plausible solution?
```python
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
```

## plausible soluton2
```python
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
```
