def solution(food):
    answer = []
    for i, v in enumerate(food):
        if i != 0 :
            for k in range(v//2):
                answer.append(i)
    
    tmp = answer[::-1]
    answer.append(0)
    answer.extend(tmp)
    
    return ''.join(str(s) for s in answer)
