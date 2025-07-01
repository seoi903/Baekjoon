lst = list(map(int,input()))

def check_alpsoo(lst):

    upside_downside = lst[1]-lst[0]
    slope = lst[1]-lst[0]
    
    if slope <=0: 
        print("NON ALPSOO")
        return 
    for i in range(1,len(lst)-1):
        if lst[i] == lst[i+1]:
            print('NON ALPSOO')
            return 
        upside_downside = (lst[i]-lst[i-1]) * (lst[i+1] - lst[i]) 
        if upside_downside > 0: 
            if slope != lst[i+1]-lst[i]:
                print("NON ALPSOO")
                return
        else:
            slope = lst[i+1]-lst[i]
    
    if slope<0:
        print("ALPSOO")
    else:
        print("NON ALPSOO")
    return 

check_alpsoo(lst)