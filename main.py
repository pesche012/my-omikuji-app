import random
import time

omikuji_list = ["大吉", "中吉", "凶"]
omikuji_aitem = ["ポテト", "じゃがりこ", "チョコレート"]
omikuji_calar = ["赤", "青", "黄色", "黒", "白"]

result = random.choice(omikuji_list)
result2 = random.choice(omikuji_aitem)
result3 = random.choice(omikuji_calar)
name = input("お名前を入力してください:")

print(f"{name}さんの今日の運勢を占います...")
print("お調べします10秒お待ち下さい...")
for i in range(10, 0, -1):
    print(f"解析中... あと{i}秒")
    time.sleep(1)


if result == "大吉":
    print("今日はとてもいい１日になるでしょう")
elif result == "中吉":
    print("いつも通りに過しましょう")
else:
    print("今日は、凶だけに静かにしてましょう")

print(f"あなたのラッキーアイテムは、{result2}です")
print(f"あなたのラッキーアイテムは、{result3}です")