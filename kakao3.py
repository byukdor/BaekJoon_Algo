info = ["java backend junior pizza 150","python frontend senior chicken 210",\
    "python frontend senior chicken 150","cpp backend senior pizza 260",\
        "java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",\
    "cpp and - and senior and pizza 250","- and backend and senior and - 150",\
        "- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    candList = []
    candScore = []
    for i in info:
        temp = i.split(" ")
        candList.append(temp[:-1])
        candScore.append(int(temp[-1]))

    for j in range(len(query)):
        potenCand = 0
        temp = query[j].replace("and ","").replace("- ","").split(" ")
        if temp[0].isnumeric():
            answer.append(sum([k >= int(temp[0]) for k in candScore]))
        else:
            for l in range(len(candList)):
                if (set(temp[:-1]).issubset(set(candList[l]))) &\
                (candScore[l] >= int(temp[-1])):
                    potenCand += 1
            answer.append(potenCand)
    return answer




