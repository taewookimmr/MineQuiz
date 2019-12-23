def solution(reversefraction=3, a4perbtn=4):
    n = int(input())
    atom = reversefraction*n
    btnClkCount = [0]
    def recur(atom):
        q = atom//reversefraction
        r = atom % reversefraction
        btnClkCount[0] += q
        realremain = q+r
        if realremain > reversefraction-1:
            recur(realremain)
    recur(atom)
    a4paper = a4perbtn*btnClkCount[0]
    print("when n : ", n, ", the f(n) : ", a4paper)
    

    
solution()