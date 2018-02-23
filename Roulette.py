import random,sys
from time import sleep

#これでgroup_by 数毎に分けたグループが返ってくる(らしい)
def get_group(group_by):
    #0～36のリストを作る
    li = list(range(37))
    del li[0]
    #1~36のリストになってるはず
    group = [li[i:i + group_by] for i in range(0, len(li), group_by)]
    print(group)
    return group

def roll():
    return random.randint(-1,36)
    
def new(roulette,type):
    #ひたすら確認する
    atari = -1

    #数字の直接入力
    if type == 0:
        if (roulette == -1 and num == -1) or roulette == num:
            atari = 36
    #範囲指定が要るもの
    elif type in [1,2,3,4] and roulette not in [0,-1]:
        #数字をグループ分けする
        if type != 4:
            gr = get_group(type+1)
        else:
            gr = get_group(6)
        #ルーレット結果がグループに入っているならatariにする
        if roulette in gr[num-1]:
            #1-2 3-4 5-6
            if type == 1: atari = 18
            #1-3 4-6 7-9
            elif type == 2: atari = 12
            #1-4 5-8 9-12
            elif type == 3: atari = 9
            #1-6 7-13 14-20
            else: atari = 6
    elif type == 6 and roulette > 0 and roulette < 13: atari = 3
    elif type == 7 and roulette > 12 and roulette < 25: atari = 3
    elif type == 5 and roulette > 24: atari = 3
    elif type == 8 and roulette < 19: atari = 2
    elif type == 9 and roulette > 18: atari = 2
    elif type == 10 and roulette%2 == 0: atari = 2
    elif type == 11 and roulette%2 == 1: atari = 2
    elif type == 12 and roulette in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]: atari = 2
    elif type == 13 and roulette in [2,4,6,7,10,11,13,15,17,20,22,24,26,28,29,31,33,35]: atari = 2
    return atari

money = 100
pay = 0
out = 0

while True:
    print("所持金: %sクレジット"%(money))
    if money <= 0:
        print("GAME OVER")
        sys.exit()
    while True:
        try:
            inp = input('いくらかけますか?>>')
            if inp == "ALL":
                inp = money
                break
            elif inp == "HALF":
                inp = int(money/2)
                break
            elif int(inp) > 0 and int(inp) <= money:
                inp = int(inp)
                break
        except:
            pass
    print(str(inp)+"クレジット かけます")
    money -= inp
    pay += inp

    print("0,00,1~36 : 特定の数字にかける(36倍)")
    print("D1 ~ D18  : 2つの数字にかける(18倍)")
    print("T1 ~ T12  : 3つの数字にかける(12倍)")
    print("Q1 ~ Q9   : 4つの数字にかける(9倍)")
    print("S1 ~ S6   : 6つの数字にかける(6倍)")
    print("L : 大 25~26 (3倍)")
    print("M : 中 13~24 (3倍)")
    print("S : 小 01~12 (3倍)")
    print("Z : 前 01~18 (2倍)")
    print("K : 後 19~36 (2倍)")
    print("E : 偶 2,4.. (2倍)")
    print("O : 奇 1,3.. (2倍)")
    print("R : 赤にかける(2倍)")
    print("B : 黒にかける(2倍)")

    while True:
        bet_to = input("どこにかけますか?>>")
        if bet_to[0] in ["D","T","Q","S","L","M","S","F","L","E","O","R","B"]:
            try:
                if bet_to[0] in ["L","M","Z","K","E","O","R","B"]: break
                if bet_to[0] == "D" and int(bet_to[1:]) > 0 and int(bet_to[1:]) < 19: break
                if bet_to[0] == "T" and int(bet_to[1:]) > 0 and int(bet_to[1:]) < 13: break
                if bet_to[0] == "Q" and int(bet_to[1:]) > 0 and int(bet_to[1:]) < 10: break
                if bet_to[0] == "S" and len(bet_to) == 1: break
                if bet_to[0] == "S" and int(bet_to[1:]) > 0 and int(bet_to[1:]) < 7: break
            except:
                pass
        elif bet_to == "00":
            break
        elif bet_to.isdigit():
            break
    # 処理が不安だからtypeを設定しておく
    #00はisdegitがTrueを返しちゃうので特別
    if bet_to == "00":
        type = 0
        num = -1
    #単純な数値
    elif bet_to.isdigit():
        type = 0
        num = int(bet_to)
    #Sは被っちゃってるので特殊処理
    elif bet_to[0] == "S" and len(bet_to) == 1: type = 5
    #範囲指定が要るもの
    elif bet_to[0] in ["D","T","Q","S"]:
        num = int(bet_to[1:])
        if bet_to[0]== "D": type = 1
        elif bet_to[0] == "T": type = 2
        elif bet_to[0] == "Q": type = 3
        elif bet_to[0] == "S": type = 4
    #大
    elif bet_to[0] == "L": type = 6
    #中
    elif bet_to[0] == "M": type = 7
    #前半
    elif bet_to[0] == "Z": type = 8
    #後半
    elif bet_to[0] == "K": type = 9
    #偶数
    elif bet_to[0] == "E": type = 10
    #奇数
    elif bet_to[0] == "O": type = 11
    #赤
    elif bet_to[0] == "R": type = 12
    #黒
    else: type = 13
    
    roulette = roll()
    atari = new(roulette,type)
    
    if (out/pay)*100 > 10 and atari != -1:
        print("もう一回!")
        roulette = roll()
        atari = new(roulette,type)
    if roulette == -1:
        print("結果: 00")
    else:
        print("結果: %s"%(roulette))
            
    if atari != -1:
        print("当たり %sx%s倍=%sゲット!"%(inp,atari,inp*atari))
        money += (inp * atari)
        out += (inp * atari)
    else:
        print("はずれ")
        
    print("P/O = %s"%((out/pay)*100))