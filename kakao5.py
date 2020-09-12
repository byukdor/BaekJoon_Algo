def convtime(time):
    total = 0
    time = list(map(int,time.split(":")))
    for i in range(3):
        total += time[i] * (60 ** (2 - i))
    return(total)

def convtime2(time):
    hour = time // 3600
    minute = ((time % 3600) // 60)
    second = (time % 3600) % 60
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)
    if second < 10:
        second = "0" + str(second)
    else:
        second = str(second)

    return("".join([hour,":",minute,":",second]))

def solution(play_time, adv_time, logs):
                        
    play_time = convtime(play_time)
    adv_time = convtime(adv_time)
    view = [0] * play_time
    maximum = 0
    maximum_point = 86400
    start = [0]
    end = [play_time]
    
    for i in logs:
        temp = i.split("-")
        temp[0] = convtime(temp[0])
        temp[1] = convtime(temp[1])
        
        start.append(temp[0])
        end.append(temp[1])

        view[temp[0]:(temp[1] + 1)] = [x + 1 for x in view[temp[0]:(temp[1] + 1)]]
    
    for j in start:
        if j + adv_time <= play_time:
            if maximum < sum(view[j:j+adv_time+1]):
                maximum = sum(view[j:j+adv_time+1])
                maximum_point = j
            if maximum == sum(view[j:j+adv_time+1]):
                maximum_point = min(maximum_point,j)


    for k in end:
        if k - adv_time >= 0:
            if maximum <= sum(view[k-adv_time:k+1]):
                maximum = sum(view[k-adv_time:k+1])
                maximum_point = min(maximum_point,k - adv_time)

    return convtime2(maximum_point)


play_time = "02:03:55"
adv_time = "00:14:15"

logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))