## listelementcounter

### problem definition
```
Input으로 들어오는 리스트(src)를 구성하는 요소들에 대해 
특정 요소와 그 요소의 총 개수를 key-value로 묶어서 
모든 key-value로 이루어진 dictionary를 반환하는 프로그램을 작성하세요
```

### example
```
input : [a,a,b]
output(console 출력) : [a:2][b:1]
```

### 접근법_Sorting First
```python
def solution_trial_sorting_first(src):
    src.sort()
    temp = [[1, src.pop(0)]]
    while len(src):
        if temp[-1][-1] != src[0]:
            temp.append([1, src.pop(0)])
        else:
            temp[-1][0]+=1
            src.pop(0)  

    for count, word in temp:
        print("[", word, ":", count, "]", end="")

# 문제점은 src가 변한다는 점이다.
# src를 유지하고 싶다면, 복사를 해서 사용하면 된다.
# 메모리를 희생해서..
# src로 엄청 긴거 들어왔다? 알고리즘 대회에서는 메모리 초과 뜰지도..
```

### 접근법_그냥_있는_dictionary_사용
```python
def solution_trial_use_dic(src):
    dic = {}
    for e in src:
        if e in dic.keys():
            dic[e]+=1
        else:
            dic[e]=1
    temp = sorted(dic.keys())

    for k in temp:
        print("[", k, ":", dic[k], "]", end="")
```