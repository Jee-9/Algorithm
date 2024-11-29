import datetime

def work(left_time, stucks, success):
    del_list = []
    for i, stuck in enumerate(list(reversed(stucks))):
        if stuck[1] > left_time:
            stuck[1] = stuck[1] - left_time
            break
        elif stuck[1] == left_time:
            del_list.append(stuck[0])
            break
        else:
            del_list.append(stuck[0])
            left_time = left_time - stuck[1]
    
    for d in del_list:
        stucks.pop()
        success.append(d)
    
    return stucks, success

def solution(plans):
    dic = {}
    
    # sort
    for plan in plans:
        dic[plan[1]] = [plan[0], plan[2]]

    dic = dict(sorted(dic.items(), key=lambda x: x[0]))

    stuck = []
    success = []

    for idx, (time, plan) in enumerate(dic.items()):

        if idx == 0:
            before_end = datetime.datetime.strptime(time, "%H:%M") + datetime.timedelta(minutes=int(plan[1]))
            before_name = plan[0]
            continue;
        else: # 마지막에 before init 해주기
            start = datetime.datetime.strptime(time, "%H:%M")

            if start < before_end : # 만약 이전 일의 끝나는 시간이 현재 일의 시작보다 느리다면
                stuck.append([before_name, before_end - start])

            elif start == before_end : # 끝나는 시간과 시작 시간이 같다면
                success.append(before_name)

            else : # 이전 일의 끝나는 시간이 현재 일의 시작보다 빨라서 시간이 남는다면
                success.append(before_name)
                stuck, success = work(start - before_end, stuck, success)

            
            before_end = datetime.datetime.strptime(time, "%H:%M") + datetime.timedelta(minutes=int(plan[1]))
            before_name = plan[0]

            if idx == len(dic) - 1:
                success.append(plan[0])

    for st in list(reversed(stuck)):
        success.append(st[0])

    return success
