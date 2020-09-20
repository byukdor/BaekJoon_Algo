N = int(input())

for i in range(N):
    HP, MP, ATK, DEF, HP_P, MP_P, ATK_P, DEF_P = list(map(int,input().split()))
    if HP + HP_P < 1:
        HP = 1
    else:
        HP = HP + HP_P 
    
    if MP + MP_P < 1:
        MP = 5
    else:
        MP = 5 * (MP + MP_P)
    
    if ATK + ATK_P < 0:
        ATK = 0
    else:
        ATK = 2 * (ATK + ATK_P)
    DEF = 2 * (DEF + DEF_P)

    print( HP + MP + ATK + DEF)
