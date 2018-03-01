import random,sys,time
import collections

class BingoGame():
    #最大値を指定して抽選機を作成
    def __init__(self,max_num):
        self.max_num = max_num
        self.lottery = [ i for i in range(max_num)]
    #カードの作成
    def gen_card(self,gyou_and_retu=5):
        #最大数値: max_num ビンゴカードの大きさ: gyou_and_retu
        #列ごとの要素個数
        retu_nums = round(self.max_num/gyou_and_retu)
        #指定された列長/最大数値を元に 順番に並んだ数値のリストを作る
        p_card = []
        for X in range(0,gyou_and_retu):
            p_card.append([i for i in range(1+(retu_nums*X),retu_nums*(X+1))])
        #要素の個数がgyou_and_retuになるまでランダムで要素を消してシャッフル
        for data in range(len(p_card)):
            while len(p_card[data]) > gyou_and_retu:
                p_card[data].remove(random.choice(p_card[data]))
            random.shuffle(p_card[data])
        #配列の中央をOPENにする
        p_card[int(gyou_and_retu/2)][int(gyou_and_retu/2)] = "O"
        #行列が逆なので逆にする(おまじない)
        p_card = list(map(list, zip(*p_card)))
        return p_card
    #抽選機を回す
    def roll(self):
        num = random.choice(self.lottery)
        self.lottery.remove(num)
        return num
    #カードを表示する
    def show_card(self,card):
        #行ごとに表示
        for line in card:
            text = ""
            for data in line:
                if len(str(data)) == 2:
                    text += str(data) + " "
                elif str(data) != "O":
                    text += "X" + str(data) + " "
                else:
                    text += "O" + str(data) + " "
            print(text)
    #カードを開ける
    def open_card(self,card,num):
        for x in range(len(card)):
            for y in range(len(card[x])):
                if card[x][y] == num:
                    card[x][y] = "O"
        return card
    
    #ビンゴとリーチの確認
    def check_card(self,card):
        bingo = 0
        riiti = 0
        #縦と横のBINGO確認
        for i in range(2):
            for data in card:
                if data.count("O") == 5: bingo +=1
                elif data.count("O") == 4: riiti += 1
            card = list(map(list, zip(*card)))
        #斜めのBINGO確認
        for i in range(2):
            cnt = 0
            for i,data in enumerate(card):
                if data[i] == "O": cnt += 1
            if cnt == 5: bingo += 1
            elif cnt == 4: riiti += 1
            card = list(map(list, zip(*card)))
        print("BINGO: %s RIITI: %s"%(bingo,riiti))
        return [bingo,riiti]
        
        
bingo = BingoGame(75)
card = bingo.gen_card()
bingo.show_card(card)

old_num = []
for i in range(1,50):
    print("")
    num = bingo.roll()
    print(num)
    card = bingo.open_card(card,num)
    bingo.show_card(card)
    riiti = bingo.check_card(card)
    if riiti != old_num:
        a = input()
        old_num = riiti