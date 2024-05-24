from collections import Counter

def solution(weights):
    answer = 0
    temp_list = Counter(weights)
    
    for i in temp_list:
        answer += temp_list[i] * (temp_list[i]-1) // 2
        answer += temp_list[i] * temp_list[i*(4/3)]
        answer += temp_list[i] * temp_list[i*(3/2)]
        answer += temp_list[i] * temp_list[i*2]
    return answer