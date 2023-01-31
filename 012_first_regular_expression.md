好久沒有寫小糞扣日誌惹

但，沒有關係，將軍不怕出身低，日記不怕富奸情（並沒有這種說法，而且這沒有押韻好嗎）

總之，今天真的是，爽辣！！！一天就把我想做的事情用剛學的regular expression做出來，真的很開心


事情是這樣的，現在這個網路時代，很多事情可以透過資訊分析抽取出一些有趣的訊息
最近我參加的一個線上學術活動的承辦人，因為寄信通知時沒有將報名參加的大家的信箱放到BCC
由於許多人是用自己任職（或是就學）的單位的信箱報名，我因此意外可以從收件人清單中分析一下，大概都是哪裡的人報名參加這個活動


要做這個分析，首先要做的就是把想辦法把複製貼上的清單弄乾淨



清單範例
```python
meow@gmail.com <meow@ncku.edu.tw>, quack <quack@gmail.com>, gurumeow@guru.com <gurumeow@guru.com>, furufuru@Gamil.com <furufuru@Gmail.com>
```

這邊可以看到，直接從收件人那邊複製貼上的話，我們得到的會是一長串的字串（string）
我想到的處理方式是先透過`split()`這個method，把這一大串長長的字串分割成一個收件人一個收件人的樣子

```python
mail = 'meow@gmail.com <meow@gmail.com>, quack <quack@ntu.edu.tw>, gurumeow@guru.com <gurumeow@guru.com>, furufuru@Gamil.com <furufuru@Gmail.com>'
mail_list = mail.split(',')
print(mail_list)
====
['meow@ncku.edu.tw <meow@ncku.edu.tw>', ' quack <quack@ntu.edu.tw>', ' gurumeow@guru.com <gurumeow@guru.com>', ' furufuru@Gamil.com <furufuru@Gmail.com>']

```
這邊這個做法的意思是，我先把這一串字串用mail這個變數存起來
然後我再新增一個叫做mail_list的變數，用這個變數來存取 `每看到一個逗號就切一刀下去` 切出來的收件人以及其收件信箱的清單(list)

`list` 在python中跟 `string`一樣，都是一種class，很多method可以對list做，但是不能對string做，反之亦然
這邊可以看到，print出的mail_list，收件人的名字跟信箱都用單引號括號起來（儲存的type為string）、並且用逗號隔開

這邊我之所以要先把這個字串切段，原因主要在於，當我把這些收件人資訊存成清單中的一個一個元素後
我就可以利用`for loop` 把他們一個一個抓出來，做一模模一樣樣的操作，也就是**把我不想要的資訊一個一個撥除掉**
以這邊來說，因為我有興趣的事情是其他人都來自哪些學術機構，所以我真正需要的資訊只有`@`之後的訊息
我只要有了小老鼠後面的字串，我就可以透過`count()`這個method來算哪個機構最多人報名參加了


那，接下來該怎麼做呢？
我首先注意到的是，清單中有些收件人的資訊跟信箱一樣，但是有些則是另外有名字（如quack <quack@ntu.edu.tw>這個)
但是，不管是哪個，信箱的部分都會用`<` 跟 `>` 夾起來
所以我的第一步便是想辦法截取出被夾起來的資訊（事後發現，其實是也不需要這一步...）

我採取的策略是`算算看`策略（！）
簡單的說就是，我先寫一段小糞扣，找出`<` 跟 `>` 在`quack <quack@ntu.edu.tw>`這個字串的位置（index）
然後再寫一段小糞扣說「把`<`出現的那個位置之後的字符(character)一個一個給我弄出來，弄到在`>`出現的位置之前的那個字符為止」

```python
clean_address = [ ]
sub1 = '<'
sub2 = '>'

for address in mail:
    idx1 = address.index(sub1)
    idx2 = address.index(sub2)
    res = ''

    for idx in range (idx1 + len(sub1), idx2):
        res = res + address[idx]
    
    clean_address.append(res.lower())
```
這邊有幾個或許（？）可以跟其他也是剛開始學習爬說嘴的同道們分享的技術小細節
我一開始先開的`clean_address`這個變數，等號後面的中括號表示這個變數是一個還沒有任何東東的list
我之所以要這麼做是因為，我之後要利用`append()`這個method，把小糞扣弄乾淨的電子信箱的地址一個一個丟進這個清單中
這邊的append可以理解為「更新」這個清單

第二個技術細小細節是`idx1 + len(sub1)`
之所以要這樣寫是因為，被用來當起點的東東，有可能有超過一個字符，所以我找到的`起點`，還不是真正的`起點`
我有興趣的，是`起點`加上`被用來當起點的東東的長度`後！開始出現的字符，所以我才要弄一個`len(sub1)`

以`quack <quack@ntu.edu.tw>`為例，我們可以
透過在`address`這個local variable後面加上中括號，指定地幾位數，這邊因為我有`idx`可以依序把字符抓出來，所以中括號中就用了他


實際的運作方式，可以透過下面這個有一點點點不一樣的小範例來理解
```python
ex = 'quack <quack@ntu.edu.tw>'

sub1 = '<'
sub2 = '>'

idx1 = ex.index(sub1)
idx2 = ex.index(sub2)
res = ''

for idx in range (idx1 + len(sub1), idx2):
    res = res + ex[idx]

    print(idx)
    print(res)
===
7
q
8
qu
9
qua
10
quac
11
quack
12
quack@
13
quack@n
14
quack@nt
15
quack@ntu
16
quack@ntu.
17
quack@ntu.e
18
quack@ntu.ed
19
quack@ntu.edu
20
quack@ntu.edu.
21
quack@ntu.edu.t
22
quack@ntu.edu.tw
    
```
在此再次感謝Ｇ惱絲傳授`print妖鏡`心法（！）
每次不是很懂我的`for loop`到底在幹嘛時，print一下，人都清爽了！

透過print妖鏡，相信大朋友小朋友們都很清楚這段小糞扣到底是怎麼把電子郵件的郵件地址抓出來的了～


最後一個可以說嘴之處在於，我這樣清乾淨後才發現，有些人的gmail是Gmail，有些人是gmail，這樣在計算時會被算成兩個不同的東東，不法喜
所以我把才在`append`那邊對`res`多使用了`lower()`這個method，讓所有可以有大小寫差異的字符通通都變成小寫


在清理乾淨後，接下來的工作就是利用regular expression來把小老鼠後面的資訊抓取出來了

regular expression的regular之處，講的是`結構上`的`規律`
以電子郵件的地址來說，一個正常的電子郵件地址的結構必然是`一串東東`加上`一個＠`然後是`一串東東`
另一個例子則是時間戳記（timestamp），好比說，`29 Jan 2023`跟`22 Feb 2023`這兩個日期寫法
觀察一下就會發現，他們的結構都是`兩個零到九的數字`加上`一個空白`加上`三個英文字母且第一個字母大寫剩下兩個小寫`加上`一個空白`再加上`四個零到九數字`

regular expression就是可以讓我們`一次`針對`符合我們感興趣的結構`的東東，做相關操弄的好幫手

但，從上面的簡單討論，我們不難發現，regular expression比較抽象（？）
為了要「簡明地」表記如`一串東東`、`三個英文字母且第一個字母大寫剩下兩個小寫`、`兩個零到九的數字`
爬說嘴的regular expression有一套速記（？）符碼要背，一開始接觸真的各種不知道自己到底在寫什麼

好比說，要表記`一個不是空白的東東`（也就是可以是數字也可以是文字，反正不要是空白的就好了），這邊要寫作`\S`
想要表記`一串東東`（我的`一串不是空白的東東`的略寫），則是在`\S`後面馬上加上一個`+`，寫成`\S+`
至於要表記一個空白，則是寫作`\s`


詳細的速記清單，可以參考我自己其實有看沒有懂的爬說嘴官網
https://docs.python.org/3/library/re.html

W3Schools的regular expression教學我比較看得懂在做什麼（然後，在發現findall後才意識到，自己之前幫收件人與電郵地址淨身這部根本可以省略...）
https://www.w3schools.com/python/python_regex.asp

Ｇ惱絲推薦的regex可以測試自己到底express了什麼（娃喔～才知道，自己的以為，都只是自以為呢！）
http://regexr.com/


好，總之，我們需要先匯入`re`這個`module`才能開始express自己
```python
import re


mail_type = []
for address in clean_address:
    x = re.findall('\@(\S+)', address)
    mail_type.append(x)
```
這邊的作法跟上面也很類似，就是先開一個空空如也的清單，等之後把清出來的東西丟進去
唯一特別要說明的是regular expression這邊的作法



這邊我的作法是按照Ｇ老師的提點去改的
Ｇ老師知道我對regular expression還是非常生疏，因此就直接教我用regular expression的`小括號挖挖術`
簡單說就是，regular expression可以透過小括號來挖出括號內的資料

比方說，如果我想要挖出小老鼠前以及小老鼠後的字串，我可以這樣寫，最後會回傳一個很像list但是另有名稱的東東，叫做tuple
```python
import re

ex = 'quack@ntu.edu.tw'
mail = re.findall('(\S+)@(\S+)', ex)

print(mail)
==
[('quack', 'ntu.edu.tw')]
```
這邊的意思就是，找出所有在ex裡面，符合(\S+)@(\S+)這個格式的東東，並且把小括號內的字串回傳回來到mail這個變數裡



但，以我的需求來說，我根本不在乎小老鼠前面的東東，所以我就改成了`@(\S+)`


做到這邊，最大的難關其實已經越過惹
接下來要做的事情就是算到底有「幾種」電子信箱結尾，以及每種結尾出現幾次

算到底有幾種電子信箱結尾，我的作法是先開一個空的list
如果我的for loop處理到的item沒有出現在那個空空的list過，就丟進去
這樣一來，我就可以確保我的清單都沒有重複的東東

```python
classify = []
for adr in mail_type:
    if adr not in classify:
        classify.append(adr)
```

最後一步，有點偷吃步就是...
該怎麼說呢，因為我想要讓我統計出來的東西可以用降冪的方式排列
但我又不想要另外再花時間研究要怎麼樣在不另外用pandas這個小畜生的情況下做sorting
所以我就...

```python
stat = []
for adr in classify:
    c = mail_type.count(adr)
    res = f'{c} from {adr}'
    stat.append(res)

stat.sort(reverse=True)

for i in stat:
    print(i)
    
 ===
 
2 from ['gmail.com']
1 from ['ntu.edu.tw']
1 from ['guru.com']
 ```
 
 
 (逃）
 
 ====
 ～～～完整糞扣，盡在github～～～
 https://github.com/Ducky9527/programming/blob/master/regular_expression_and_email_data_mining.py 
 
 
 ====
 後記中的後記，一直不斷反覆說regular expression很恐怖，能不要用就不要用的嗚喵老師在看了小糞扣後淡淡ㄉ縮
 
 「這不需要用到regular expression」

彈指間，一串連re都不需要import的咒文，就這樣從螢幕的另一端浮現...
```python
 prefix, suffix = s.strip("<>").split("@")
```


讚嘆。


===

後記中的後記中的後記


如是我聞，貓貓上師講經於龍眼樹下：

數學系教regular expression的方法：

1.先從 Kleene algebra開始教起，Kleene algebra的公理，然後推導出Kleene algebra的各種定理。

2.證明Kleene完備性定理。

3.證明Kleene algebra是有限可公理化的

4.用範疇論與代數語言開始定義automata，在此處已經有一半的學生被當掉了。

5.終於從Kleene algebra推出regular expression，證明 regular expression是一種Kleene algebra。而後從Kleene algebra與範疇論的角度證明regular expression與finite automata是等價的。此時只剩下1/3的學生存活。但真正搞懂regular expression的學生仍寥寥無幾。卻有少數的聰明學生掌握了regular expression的奧妙之處與各種性質。


.....我想我應該在步驟一就停修惹
