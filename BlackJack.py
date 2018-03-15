import random

class BlackJack():
    num_dict = {
        11:"J",
        12:"Q",
        13:"K"
    }

    #カードを数える(10以上は10として数える)
    def cnt_cards(self,P_or_D,SB=False):
        if P_or_D == "P": cards = self.p_cards
        else: cards = self.d_cards
        tt = 0
        for card in cards:
            if card[1] < 11: tt += card[1]
            else: tt += 10
        if SB == False: return tt
        else:
            if tt == 21: return "ブラックジャック"
            elif tt > 21: return "%s バスト"%(tt)
            else: return str(tt)
    #カード一覧リセット
    def reset_cards(self):
        self.cards = [[m, n] for m in ['♣', '♦', '♥', '♠'] for n in range(1, 14)]
        self.d_cards = self.draw()
        self.p_cards = self.draw()
        #ディーラーは17以上になるまで引く
        while True:
            if self.cnt_cards("D") < 18: self.d_cards.append(self.draw(1)[0])
            else: break
        
    #カードを引く
    def draw(self,cnt=2):
        cards = []
        for i in range(cnt):
            c = random.choice(self.cards)
            cards.append(c)
            self.cards.remove(c)
        return cards
    
    #判定 引き分けなら 0 負けなら -1 勝ちなら 1が返る
    def decision(self):
        pcnt = self.cnt_cards("P")
        dcnt = self.cnt_cards("D")
        if pcnt == dcnt or (pcnt > 21 and dcnt > 21): return 0
        if (dcnt > 21 or pcnt > dcnt) and pcnt <= 21: return 1
        else: return -1
    
    #カードを追加する 21以下なら1 それ以外なら -1が返る
    def hit(self):
        self.p_cards.append(self.draw(1)[0])
        if self.cnt_cards("P") < 22: return 1
        else: return -1
    
    #一覧をそれぞれテキストで返す
    def conv_txt(self):
        toret = ["",""]
        for card in self.p_cards:
            if card[1] in self.num_dict: toret[0] += "%s%s "%(card[0],self.num_dict[card[1]])
            else: toret[0] += "%s%s "%(card[0],card[1])
        for card in self.d_cards:
            if card[1] in self.num_dict: toret[1] += "%s%s "%(card[0],self.num_dict[card[1]])
            else: toret[1] += "%s%s "%(card[0],card[1])
        toret = [ret[:len(ret)-1] for ret in toret]
        return toret

    #カードセットは クラス作った時点で決めとく()
    def __init__(self):
        self.reset_cards()


#blackjacker = BlackJack()
'''
print("あなたの手札")
print(blackjacker.conv_txt()[0])
while True:
    print("ヒットしますか? y/n")
    yn = input('>>')
    if yn == "y":
        gohit = blackjacker.hit()
        print("あなたの手札")
        print(blackjacker.conv_txt()[0])
        if gohit == -1: break
    elif yn == "n":
        break
print("\nショーダウン\n")
datas = blackjacker.conv_txt()
print("私 [%s] :"%(blackjacker.cnt_cards("D")))
print(datas[1])
print("あなた [%s] :"%(blackjacker.cnt_cards("P")))
print(datas[0])
print("")
print(blackjacker.decision())
'''