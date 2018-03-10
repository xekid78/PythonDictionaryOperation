enemy_array = {"ザコ" : "スライム", "中ボス" : "ドラゴン", "ラスボス" : "魔王"}
print(enemy_array)
print("モンスターが" + str(len(enemy_array)) + "匹いる。")
print()

print("*** 追加 ***")
enemy_array["ザコ２"] = "ドラキー"
print(enemy_array)
print("モンスターが" + str(len(enemy_array)) + "匹いる。")
print()

print("*** 変更 ***")
enemy_array["ザコ"] = "メイジ"
print(enemy_array)
print("モンスターが" + str(len(enemy_array)) + "匹いる。")
print()

print("*** 削除 ***")
del enemy_array["ザコ"]
print(enemy_array)
print("モンスターが" + str(len(enemy_array)) + "匹いる。")
