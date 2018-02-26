import random
from time import sleep
from collections import OrderedDict

#トランプセットを作る
numbers = range(1, 14)
marks = ['club', 'diamond', 'heart', 'spade']
cards = [[n, m] for m in marks for n in numbers]

display_dict = {
    "club":"♣",
    "diamond":"♦",
    "heart":"♥",
    "spade":"♠",
    "11":"J",
    "12":"Q",
    "13":"K"
}

#カード一覧表示
def print_cards(cards):
    text = ""
    for l in cards:
        if str(l[0]) in display_dict: 
            text += "%s%s "%(display_dict[l[1]],display_dict[str(l[0])])
        else:
            text += "%s%s "%(display_dict[l[1]],l[0])
    print(text)
    
#勝敗確認
def check_win(d_res,p_res):
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
    
    d_res_id = list(d_res.keys())[0]
    p_res_id = list(p_res.keys())[0]
    
    if id_dict[d_res_id] > id_dict[p_res_id]:
        print("私の勝ちです!")
    elif id_dict[d_res_id] < id_dict[p_res_id]:
        print("あなたの勝ちです...")
    else:
        if d_res_id == -1 and p_res_id == -1:
            print("ドローですね")
        elif list(d_res.values())[0] > list(p_res.values())[0]:
            print("私の勝ちです!")
        elif list(d_res.values())[0] < list(p_res.values())[0]:
            print("あなたの勝ちです...")
        else:
            print("ドローですね")

#カード確認本体
def check_cards(cards):
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
def draw(cnt):
    p_cards = []
    #プレイヤーの手札を引く
    for i in range(cnt):
        c = random.choice(cards)
        p_cards.append(c)
        cards.remove(c)
    p_cards.sort(reverse=True)
    return p_cards

print("私の手札を引きます...")
d_cards = draw(5)
print("プレイヤーの手札を引きます...")
p_cards = draw(5)
print("\nあなたの手札")
print_cards(p_cards)
print("\n交換しますか?")
print("(1,2,3,4,5 で指定して交換 交換しないなら0と入れてください)")
while True:
    tochg = input(">>")
    if len(tochg) < 6 and "0" not in tochg:
        break
    if tochg == "0":
        break
    
if tochg != "0":
    o_pcards = p_cards
    for i in tochg:
        p_cards.remove(o_pcards[int(i)-1])
        p_cards.insert(int(i)-1,draw(1)[0])
print_cards(p_cards)

print("\nショーダウン\n")
print("私")
d_cards.sort(reverse=True)
d_res = check_cards(d_cards)
print_cards(d_cards)
print(list(d_res.keys())[0])
print("")
p_cards.sort(reverse=True)
p_res = check_cards(p_cards)
print("あなた")
print_cards(p_cards)
print(list(p_res.keys())[0])
print("")
check_win(d_res,p_res)
