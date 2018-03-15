import random
from collections import OrderedDict

class Poker():
    display_dict = {
        "11":"J",
        "12":"Q",
        "13":"K"
    }
    id_dict = {
        "ノーペア": 0,
        "ワンペア": 1,
        "ツーペア": 2,
        "スリーカード": 3,
        "ストレート": 4,
        "フラッシュ": 5,
        "フルハウス": 6,
        "フォーカード": 7,
        "ストレートフラッシュ": 8,
        "ロイヤルストレートフラッシュ": 9
    }

    def all_in(self,list,chk):
        for c in chk:
            if c not in list:
                return False
        return True
    
    #カード一覧表示
    def print_cards(self,cards):
        text = ""
        for l in cards:
            if l[0] in [11,12,13]: 
                text += "%s%s "%(l[1],Poker.display_dict[str(l[0])])
            else:
                text += "%s%s "%(l[1],l[0])
        return text
        
    #カード結果表示
    def show_down(self,P_or_D):
        if P_or_D == "P":
            cards = self.p_cards
        else:
            cards = self.d_cards
        cards.sort(reverse=True)
        return self.print_cards(cards) + "\n"+ list(self.check_cards(cards).keys())[0]
        
    #勝敗確認
    def check_win(self):
        d_res = self.check_cards(self.d_cards)
        p_res = self.check_cards(self.p_cards)
        d_res_id = list(d_res.keys())[0]
        p_res_id = list(p_res.keys())[0]
        
        if Poker.id_dict[d_res_id] > Poker.id_dict[p_res_id]:
            return -1
        elif Poker.id_dict[d_res_id] < Poker.id_dict[p_res_id]:
            return 1
        else:
            if d_res_id == -1 and p_res_id == -1: return 0
            elif list(d_res.values())[0] > list(p_res.values())[0]: return -1
            elif list(d_res.values())[0] < list(p_res.values())[0]: return 1
            else: return 0

    #カード確認本体
    def check_cards(self,cards):
        o_card = {}
        flash = 0
        straight = 1
        o_card_type = cards[0][1]
        o_card_num = o_card_ret = cards[0][0]
        for n_card in cards:
            #カード番号ごとの枚数辞書作成
            if n_card[0] not in o_card: o_card[n_card[0]] = 1
            else: o_card[n_card[0]] += 1
            #フラッシュかどうかのcntを増やしていく
            if o_card_type == n_card[1]: flash += 1
            #ストレートかどうかのcntを増やしていく
            if o_card_num - 1 == n_card[0]:
                o_card_num -= 1
                straight += 1
        #ストレート/ フラッシュなら ここで投げる
        if flash == 5 and self.all_in(o_card,[10,11,12,13,1]): return {"ロイヤルストレートフラッシュ": -1} 
        elif flash == 5 and straight == 5: return {"ストレートフラッシュ": o_card_ret}
        elif flash == 5: return {"フラッシュ": -1}
        elif straight == 5: return {"ストレート": o_card_ret}
        to_ret = {}
        #その他の確認
        for card in o_card:
            if o_card[card] == 4: return {"フォーカード":card}
            elif o_card[card] == 3: to_ret["スリーカード"] = card
            elif o_card[card] == 2:
                if "ワンペア" not in to_ret: to_ret["ワンペア"] = card
                else: to_ret["ペア2"] = card
        #フルハウスとツーペアはここで整形
        if self.all_in(to_ret,["ワンペア","スリーカード"]): return {"フルハウス":to_ret["ワンペア"]+to_ret["スリーカード"]}
        elif self.all_in(to_ret,["ワンペア","ペア2"]): return {"ツーペア":to_ret["ワンペア"]+to_ret["ペア2"]}
        elif to_ret != {}: return to_ret
        else: return {"ノーペア":-1}

    #カードを引く
    def draw(self,cnt):
        print(len(self.cards))
        cards = []
        if len(self.cards) != 0:
            for i in range(cnt):
                c = random.choice(self.cards)
                cards.append(c)
                self.cards.remove(c)
            cards.sort(reverse=True)
            return cards
        else:
            return False
        
    #カード一覧リセット
    def reset_cards(self):
        self.cards = [[n, m] for m in ['♣', '♦', '♥', '♠'] for n in range(1, 14)]
        self.d_cards = self.draw(5)
        self.p_cards = self.draw(5)
    
    #カードを入れ替える
    def change(self,id_text):
        for i in id_text:
            if i in ["1","2","3","4","5"]:
                dr = self.draw(1)
                if dr != False:
                    self.p_cards.pop(int(i)-1)
                    self.p_cards.insert(int(i),dr[0])
        
    #カードセットは インスタンスを作った時点で決めとく()
    def __init__(self):
        self.reset_cards()