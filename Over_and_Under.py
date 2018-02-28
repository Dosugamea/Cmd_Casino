import random,sys

print("-- オーバー&アンダー --")
money = 100

def gen_num():
    return random.randint(1,100)
    
    
while True:
    num = gen_num()
    print("\n所持金: %sクレジット"%(money))
    step = 0
    while True:
        step += 1
        print("\n数字を予想してください")
        while True:
            try:
                inp = int(input('>>'))
                if len(str(inp)) < 4:
                    break
            except:
                pass
        if inp == num: break
        elif inp < num: print("アンダー")
        else: print("オーバー")
    print("正解! 所要ステップ数: %s"%(step))
    if step < 5:
        print("5ステップ以内のクリア お見事!")
        print("50クレジット 獲得!")
        money += 50