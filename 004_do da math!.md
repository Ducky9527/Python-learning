**calculation**

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

**練習題**

**ask a user their weight in pounds and convert it to kilograms and print on the terminal**

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


===========

繼續延續算數學的話題

python的基本運算跟學校學到的沒有什麼不一樣，也是先乘除後加減，然後該加就加（`+`）、該減就減（`-`）、該乘就乘（`*`），唯一要注意的是除法（`/`）


因為除法可能會除出除不盡的東東，或者是有小數點的東東，這些有小數點的孩子，在python中有特別的地位，叫做floating number，跟一般的整數不一樣

這些有小數點的數值（好比說十除以三得到的數）其實不會如實地被python存起來，python就存到小數點後16位而已，所以嚴格說起來，有些「浮點數」其實只是近似值而已

這些浮點數，常常會在出其不意之處造成各種八阿哥（bug）...所以能避免使用到他們就最好避免使用到他們



簡單的民國紀年換算（在國外久了真的會不知道今年是民國幾年...此糞code有其實用之處！！）
```python
this_year = 2022
revolution = 1911
this_ROC_year = this_year - revolution
print(this_ROC_year)
```

除了基本的四則運算，python還有 `//`這個東東，這個東東基本上跟除法沒有太大差異，就是會將小數點後的數值全部捨去，只保留整數部分

如果用搭配`type()`去看，就會發現，`//`運算出來的值是的性質是整數

至於用`/`運算的值，即便是整除，python也會直接看待成floating number


```python
print(type(10//3))
<class 'int'>

print(type(6/3))
<class 'float'>

```

另一個很好用的運算符號是`%`，這個運算符號可以吐出餘數來，在判斷一個數是奇數還是偶數等等等的很方便

比方說
```python
print(10 % 3)
```
就會吐出1來

最後一個常用的運算符號是`**`，這是指數的意思

比方說
```python
print(10**3)
```
就會吐出1000（十的三次方）


==========

遠古時代第一次嘗試學爬說嘴時，覺得最神秘的運算符號，是`-=`跟`+=`

這兩個運算符號都可以直接用來動態更新variable的數值

比方說
```python
x = 10
```

要更新這個變數的數值，把它變成13，可以笨笨的寫成
```python
x = 10
x = x + 3
```
（爬說嘴允許不另外下一個新的變數，直接動態更新x的值，但這樣寫要小心，有的時候會寫到忘記，然後動態更新後糞code就炸了）

也可以寫成
```python
x = 10
x += 3
```
這邊的`x += 3` 跟 `x = x + 3`意思完全一樣，`-=`的用法也完全一樣

========

`round()`這個function可以做四捨五入，他會直接把浮點數變成最靠近該浮點數的整數

比方說
```python
print(round(-2.2))
-2

print(round(2.9))
3
```

`abs()`這個function則是可以取絕對值

=========

這些運算都是直接就可以使用的，如果要用到更複雜的（或說是進階的）運算，可以另外在一開始就利用`import math`叫匯入相關的指令，這樣就可以使用像是三角函數之類的東東

如，要求arc sine時，就可以這樣：
```python
import math

x = 0
print(math.asin(x))

0.0
```

如果沒有`import math`，會print出下面的訊息
```python
in <module>
    print(math.asin(x))
NameError: name 'math' is not defined
```
因為太多小幫手可以用了，想到什麼爬說嘴應該要有的小幫手，就直接去看math module的documentation看要怎麼召喚這些小幫手

完整的documentation在這邊：https://docs.python.org/3/library/math.html
