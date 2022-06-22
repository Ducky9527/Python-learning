#calculation#

```python
birth_year = int(input("birth year: "))
age = 2022 - birth_year
print(age)
```

這邊要注意的是input function輸入的值預設為string
所以要做運算的話，要在input function外面在包一層int() function把東東的資料型態轉成可以做運算的「整數」
這種問題日後會以各種型態不斷跑出來，所以python有一個function叫做type()
把不是很確定到底是什麼樣的資料的東東用type()包起來就可以看到資料型態了

如
```python
print(type(age))
```
就會出現

```python
<class 'int'>
```

**練習題

**ask a user their weight in pounds and convert it to kilograms and print on the terminal

第一次的嘗試
```python
question = int(input("What is your weight in pounds? > "))
kilo = question * 0.45
print("so, that's " + kilo + " kg.")
```

跳出錯誤
```python
line 24, in <module>
    print("so, that's " + kilo + " kg.")
TypeError: can only concatenate str (not "float") to str
```
忘記了只有字串才可以黏在一起，要把kilo這個floating的小寶寶的性質改成字串

所以做第二次嘗試
```python
question = int(input("What is your weight in pounds? > "))
kilo = question * 0.45
print("so, that's " + str(kilo) + " kg.")
```
成功～

========

複習基本運算時，突然想到俗女養成記第二季時
陳嘉玲她弟說到自己用一個app去計算自己還有多少時間可以陪在父母身邊，才發現其實自己以為的還有很多時間，根本一點也不多
過去這十年來從台灣搬到英國，然後又搬到澳洲、荷蘭，一直到處飄泊，實際上跟家人相處的時間，不用算也知道少得嚇人
這也是為什麼現在對於是否要繼續玩以地球為尺度的學術大地遊戲感到遲疑
人生一轉眼就過了，這些學術名利，值得嗎？

所以我順手做了這個小程式，也當作是練習

```python
age = int(input("你現在幾歲？ "))
till_which_age = int(input("你想知道你到幾歲前，最多最多，大概還有多少天與親朋好友相處的時間？ 請輸入年齡： "))

max_day = (till_which_age - age) * 365
one_month = (till_which_age - age) * 30
print("你最多最多，大概還有" + str(max_day) + "天與親朋好友相處的時間喔～")
print ("不過，如果未來每年大概都只有一個月可以回家的話，你就只有" + str(one_month) + "天的時間了ㄛ")


你現在幾歲？ 32
你想知道你到幾歲前，最多最多，大概還有多少天與親朋好友相處的時間？ 請輸入年齡： 64
你最多最多，大概還有11680天與親朋好友相處的時間喔～
不過，如果未來每年大概都只有一個月可以回家的話，你就只有960天的時間了ㄛ
```

人蔘啊。


