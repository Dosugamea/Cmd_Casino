import random
from collections import OrderedDict

class Poker():
    cards = [[n, m] for m in ['club', 'diamond', 'heart', 'spade'] for n in range(1, 14)]
    display_dict = {
        "club":"♣",
        "diamond":"♦",
        "heart":"♥",
        "spade":"♠",
        "11":"J",
        "12":"Q",
        "13":"K"
    }
    jp_dict = {
        "NoPair": "ノーペア",
        "OnePair": "ワンペア",
        "TwoPair": "ツーペア",
        "ThreeCard": "スリーカード",
        "Straight": "ストレート",
        "Flash": "フラッシュ",
        "FullHouse": "フルハウス",
        "FourCard": "フォーカード",
        "StraightFlash": "ストレートフラッシュ",
        "RoyalStraightFlash": "ロイヤルストレートフラッシュ"
    }
    id_dict = {
        "NoPair": 0,
        "OnePair": 1,
        "TwoPair": 2,
        "ThreeCard": 3,
        "Straight": 4,
        "Flash": 5,
        "FullHouse": 6,
        "FourCard": 7,
        "StraightFlash": 8,
        "RoyalStraightFlash": 9
    }

    #カード一覧表示
    def print_cards(self,cards):
        text = ""
        for l in cards:
            if str(l[0]) in self.display_dict: 
                text += "%s%s "%(self.display_dict[l[1]],self.display_dict[str(l[0])])
            else:
                text += "%s%s "%(self.display_dict[l[1]],l[0])
        print(text)
        
    #カード結果表示
    def show_down(self,P_or_D):
        if P_or_D == "P":
            cards = self.p_cards
        else:
            cards = self.d_cards
        cards.sort(reverse=True)
        self.print_cards(cards)
        print(self.jp_dict[list(self.check_cards(cards).keys())[0]])
        
    #勝敗確認
    def check_win(self):
        d_res = self.check_cards(self.d_cards)
        p_res = self.check_cards(self.p_cards)
        d_res_id = list(d_res.keys())[0]
        p_res_id = list(p_res.keys())[0]
        
        if self.id_dict[d_res_id] > self.id_dict[p_res_id]:
            return -1
        elif self.id_dict[d_res_id] < self.id_dict[p_res_id]:
            return 1
        else:
            if d_res_id == -1 and p_res_id == -1:
                return 0
            elif list(d_res.values())[0] > list(p_res.values())[0]:
                return -1
            elif list(d_res.values())[0] < list(p_res.values())[0]:
                return 1
            else:
                return 0

    #カード確認本体
    def check_cards(self,cards):
        o_card = {}
        flash = 0
        straight = 1
        o_card_type = cards[0][1]
        o_card_num = o_card_ret = cards[0][0]
        for n_card in cards:
            #カード番号ごとの枚数辞書作成
            if n_card[0] not in o_card:
                o_card[n_card[0]] = 1
            else:
                o_card[n_card[0]] += 1
            #フラッシュかどうかのcntを増やしていく
            if o_card_type == n_card[1]:
                flash += 1
            #ストレートかどうかのcntを増やしていく
            if o_card_num - 1 == n_card[0]:
                o_card_num -= 1
                straight += 1
        #ストレート/ フラッシュなら ここで投げる(数字は?)
        if flash == 5 and 10 in o_card and 11 in o_card and 12 in o_card and 13 in o_card and 1 in o_card: return {"RoyalStraightFlash":"-1"} 
        if flash == 5 and straight == 5: return {"StraightFlash":"-1"}
        if flash == 5: return {"Flash":"-1"}
        if straight == 5: return {"Straight": o_card_ret}
        to_ret = {}
        #その他の確認
        for card in o_card:
            if o_card[card] == 4:
                to_ret["FourCard"] = card
            elif o_card[card] == 3:
                to_ret["ThreeCard"] = card
            elif o_card[card] == 2:
                if "PairCard" not in to_ret:
                    to_ret["PairCard"] = card
                else:
                    to_ret["2ndPairCard"] = card
        #フルハウス ツーペア ノーペア はここで整形
        if "PairCard" in to_ret and "ThreeCard" in to_ret:
            to_ret["FullHouse"] = to_ret["PairCard"] + to_ret["ThreeCard"]
            del to_ret["PairCard"]
            del to_ret["ThreeCard"]
        if "PairCard" in to_ret and "2ndPairCard" in to_ret:
            to_ret["TwoPair"] = to_ret["PairCard"] + to_ret["2ndPairCard"]
            del to_ret["PairCard"]
            del to_ret["2ndPairCard"]
        if "PairCard" in to_ret:
            to_ret["OnePair"] = to_ret["PairCard"]
            del to_ret["PairCard"]
        if to_ret == {}:
            return {"NoPair":"-1"}
        else:
            return to_ret

    #カードを引く
    def draw(self,cnt):
        cards = []
        #プレイヤーの手札を引く
        for i in range(cnt):
            c = random.choice(self.cards)
            cards.append(c)
            self.cards.remove(c)
        cards.sort(reverse=True)
        return cards
    
    #カードを入れ替える
    def change(self,id_text):
        if id_text != "0":
            o_pcards = self.p_cards
            for i in id_text:
                self.p_cards.remove(o_pcards[int(i)-1])
                self.p_cards.insert(int(i)-1,self.draw(1)[0])
        
    #カードセットは クラス作った時点で決めとく()
    def __init__(self):
        #ディーラーに引かせる
        self.d_cards = self.draw(5)
        self.p_cards = self.draw(5)

#TEST-PLAY
Pokerer = Poker()
print("\nあなたの手札")
Pokerer.print_cards(Pokerer.p_cards)
print("\n交換しますか?")
print("(1,2,3,4,5 で指定して交換 交換しないなら0と入れてください)")
#交換するカードの指定
while True:
    tochg = input(">>")
    if len(tochg) < 6 and "0" not in tochg:
        break
    if tochg == "0":
        break
Pokerer.change(tochg)
print("\nショーダウン\n")
print("私")
Pokerer.show_down("D")
print("")
print("あなた")
Pokerer.show_down("P")
print("")
print(Pokerer.check_win())