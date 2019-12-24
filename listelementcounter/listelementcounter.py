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

x = ["a", "b", "c", "a" , "a", "b"]
solution_trial_use_dic(x)
solution_trial_sorting_first(x)