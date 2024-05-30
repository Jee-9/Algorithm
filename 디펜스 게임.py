n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]

def solution(n, k, enemy):
    answer = 0
    check = []
    
    if k >= len(enemy):
        return k
    
    # k개만큼은 무조건
    for i in range(1000000):
        check = enemy[:k+1+i]
        # check.sort(reverse=True) 타임아웃남 ㅜ
        
        for num in range(k-1):
            check.remove(max(check))
        
        print(check)
        
        tmp = check[k:]
        if sum(tmp) > n:
            return k+i
    
    return 0

solution(n,k,enemy)