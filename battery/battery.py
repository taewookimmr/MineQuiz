def solution(battery_needs, battery_list):
    import heapq
    mylist = []
    for b in battery_list:
        mylist += [ [b[1]/b[0], b[0], b[1]] ] # 개당 가격
    
    mylist.sort()
    remain = battery_needs
    answer = 0
    
    while remain != 0:
        heap = [] 
        for _, pack, price in mylist :
            q = remain // pack
            r = remain % pack 
            if q == 0 : 
                q = 1
                r = 0
            heapq.heappush(heap, [q * price, r])
        purchased_price, remain = heapq.heappop(heap)
        answer += purchased_price
        
    print(answer)
        
       
battery_needs = 96
battery_list=[[10,100], [5,55], [1, 54]]
solution(battery_needs, battery_list)
