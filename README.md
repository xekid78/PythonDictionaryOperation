# PythonDictionaryOperation
辞書（連想配列）操作

## 処理
配列の内容を追加、変更、削除を行います。

## コード
```
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

```

## 出力結果  
```
{'ザコ': 'スライム', '中ボス': 'ドラゴン', 'ラスボス': '魔王'}
モンスターが3匹いる。

*** 追加 ***
{'ザコ': 'スライム', '中ボス': 'ドラゴン', 'ラスボス': '魔王', 'ザコ２': 'ドラキー'}
モンスターが4匹いる。

*** 変更 ***
{'ザコ': 'メイジ', '中ボス': 'ドラゴン', 'ラスボス': '魔王', 'ザコ２': 'ドラキー'}
モンスターが4匹いる。

*** 削除 ***
{'中ボス': 'ドラゴン', 'ラスボス': '魔王', 'ザコ２': 'ドラキー'}
モンスターが3匹いる。
```
  
## 開発環境
| 開発ツール |  |
|:-|:-|
| OS | Windows10 |
| 仮想化ソフト | Oracle VM VirtualBox 5.2 |
| 構築ソフト | Vagrant 2.0.2 |
| 仮想化上OS | CentOS 6.9 |
| SSHクライアント | PuTTY 0.6.8 |
| FTPクライアント | Cyberduck 6.3.5 |
| エディタ | Atom 1.24.0 |
| 開発言語 | Python 3.6.4 |
