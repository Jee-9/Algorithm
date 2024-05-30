def solution(brown, yellow):
    answer = []
    
    if yellow == 1:
        answer = [3,3]
        
    for hor in range(2, yellow+1):
        if (yellow%hor == 0):
            ver = int(yellow/hor)
            print(hor,"X",ver)
            if (hor>=ver) & (2*hor+2*ver+4 == brown):
                print("answer:", hor, "X", ver)
                answer = [hor+2, ver+2]
            
    return answer