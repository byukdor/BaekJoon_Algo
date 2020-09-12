new_id = "=.="

def solution(new_id):

    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = "".join(list([x for x in new_id if  x.isalpha() or \
                       x.isnumeric() or x == "-" or x == "_" or x == "."]))
    # 3단계
    while (new_id.count("..") != 0 ) :
        new_id = new_id.replace("..",".")
    # 4단계
    if new_id != "":
        if new_id[0] == ".":
            new_id = new_id[1:]
    if new_id != "":
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    # 5단계
    else:
        new_id = "a"
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    # 7단계
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]
    
    return new_id