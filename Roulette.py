import random,sys
from time import sleep

class Roulette():
    #これでgroup_by 数毎に分けたグループが返ってくる(らしい)
    def get_group(self,group_by):
        #0～36のリストを作る
        li = list(range(37))
        del li[0]
        #1~36のリストになってるはず
        group = [li[i:i + group_by] for i in range(0, len(li), group_by)]
        return group
        
    def how_set(self):
        print("0,00,1~36 : 特定の数字にかける(36倍)")
        print("ふ1 ~ ふ18  : 2つの数字にかける(18倍)")
        print("み1 ~ み12  : 3つの数字にかける(12倍)")
        print("よ1 ~ よ9   : 4つの数字にかける(9倍)")
        print("む1 ~ む6   : 6つの数字にかける(6倍)")
        print("だ : 大 25~26 (3倍)")
        print("ち : 中 13~24 (3倍)")
        print("し : 小 01~12 (3倍) !!")
        print("ぜ : 前 01~18 (2倍)")
        print("ご : 後 19~36 (2倍)")
        print("ぐ : 偶 2,4.. (2倍)")
        print("き : 奇 1,3.. (2倍)")
        print("あ : 赤にかける(2倍)")
        print("く : 黒にかける(2倍)")

    def gen_TNTN(self,bet_to):
        type = None
        num = None
        # 処理が不安だからtypeを設定しておく
        #00はisdegitがTrueを返しちゃうので特別
        if bet_to == "00":
            type = 0
            num = -1
        #単純な数値
        elif bet_to.isdigit():
            type = 0
            num = int(bet_to)
        #範囲指定が要るもの
        elif bet_to[0] in ["ふ","み","よ","む"]:
            num = int(bet_to[1:])
            if bet_to[0]== "ふ": type = 1
            elif bet_to[0] == "み": type = 2
            elif bet_to[0] == "よ": type = 3
            elif bet_to[0] == "む": type = 4
        elif bet_to[0] == "だ": type = 6
        elif bet_to[0] == "ち": type = 7
        elif bet_to[0] == "ぜ": type = 8
        elif bet_to[0] == "ご": type = 9
        elif bet_to[0] == "ぐ": type = 10
        elif bet_to[0] == "き": type = 11
        elif bet_to[0] == "あ": type = 12
        else: type = 13
        return [type,num]
        
    def roll(self):
        return random.randint(-1,36)
        
    def result(self,roulette,type,num=0):
        atari = -1
        #数字の直接入力
        if type == 0:
            if (roulette == -1 and num == -1) or roulette == num:
                atari = 36
        #範囲指定が要るもの
        elif type in [1,2,3,4] and roulette not in [0,-1]:
            #数字をグループ分けする
            if type != 4:
                gr = self.get_group(type+1)
            else:
                gr = self.get_group(6)
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

#TEST-PLAY
Rouletter = Roulette()
Rouletter.how_set()
bet_to = input('どこにかけますか? >>')
datas = Rouletter.genTypes(bet_to)
roulette = Rouletter.roll()
if roulette == -1:
    print("結果: 00")
else:
    print("結果: %s"%(roulette))

if type in [0,1,2,3,4]:
    atari = Rouletter.result(roulette,type,num)
else:
    atari = Rouletter.result(roulette,type)
print(atari)