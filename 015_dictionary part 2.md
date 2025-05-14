工作忙起來，又耽誤了學習...

今天要記錄的心得是dictionary這個資料結構另外的妙用：Hash mapping

我本來也不知道這到底是什麼，是直到開始練習leetcode後，才發現原來dictionary可以這樣使用

在某些任務上，用hash mapping做，可以比用list一個一個暴力的推過去要快上非常多，快到多少的程度，容我留待介紹two sum這個任務再說明

--

在介紹hash mapping前，我們要先知道dictionary跟list一樣，都是可以增加新的資料進去的

list的做法是透過append這個method，如

```python
l = []

l.append(1)
print (l)

--
[1]

```

那dictionary呢？

要新增資料進 dictionary 的話，因為dictionary有`key`又有儲存在`key`裡面的`value`

我們的做法跟更新list會不大一樣

以下面的例子來說，假設我們一開始的dictionary空空如也，我們想要新增一個叫做`book`的`key`，並且在book這個key下面儲存`the lord of the ring`
那我們實際的做法會是這樣：

```python
dic = {}
dic['book'] = 'the lord of the ring'

print(dic['book'])
print(dic)

--
the lord of the ring
{'book': 'the lord of the ring'}
```

聰明的小朋友看到這裡，一定就會想到，如果dictionary也可以新增資料，那是不是我們就可以透過for loop等loop，將表格資料、網頁資料用dictionary整理好

答案是！！！沒錯！！！事實上，這就是老Ｇ老師幫忙我把`中國哲學書電子計畫`這個網站上的資料dump下來的方式

因為把資料dump下來比較複雜，所以請容我用下面的簡單例子做範例


假設我們有一個`list`叫`fruits`
這個`list`中有`[‘banana', 'apple', 'watermelon']`

我們想要把這個水果清單轉成dictionary，並且，把每個水果都存到一個以他們在這個清單的次序而產生的key之下，我們可以這麼作

```python

fruit = [‘banana', 'apple', 'watermelon']

dic_fruit = {}
n = 0
for i in fruit:
    dic_fruit[n] = i
    n += 1
    print(dic_fruit)

---
{0: 'banana'}
{0: 'banana', 1: 'apple'}
{0: 'banana', 1: 'apple', 2: 'watermelon'}

``` 

這邊要千萬小心的地方在於，由於我們要讓`n`隨著每一次的loop都改變，所以`n`千萬不要寫成了 `'n'`

這是一個新手（也就是我）常犯的錯誤

因為`dictionary`的`key`如果是透過我們直接手動增加，那我們再增加的時候就需要特別加上引號才行（請參照之前的`book`範例）

但是！如果我們寫成了 `'n'`，那我們的意思就會變成每一次loop儲存的值都需要存在`'n'`這個key下面，最後就變成了'n'的值不斷地被覆寫

```python
fruit = [‘banana', 'apple', 'watermelon']

dic_fruit = {}
n = 0
for i in fruit:
    dic_fruit['n'] = i
    n += 1
    print(dic_fruit)

--
{'n': 'banana'}
{'n': 'apple'}
{'n': 'watermelon'}

```

如果真的是想要把資料都寫在'n'這個key下面，那也不是不行，但這個時候，我們做的事情其實是把一個list存在這個key下

所以我們要做的事情會是....`append` da list!
要做這件事情前，我們要先記得...要開好一個空空如也的list
不然python會吐出KeyError來

開好了之後，我們就可以開始append這個list啦～

```python
fruit = ['banana', 'apple', 'watermelon']

dic_fruit = {}
dic_fruit['n'] = []
for i in fruit:
    dic_fruit['n'].append(i)
    print(dic_fruit)

--
{'n': ['banana']}
{'n': ['banana', 'apple']}
{'n': ['banana', 'apple', 'watermelon']}

```

回到剛剛提的用index作為key，這邊需要稍微的離題一下，介紹一下利用很陽春的 `n += 1` 之術外，更佳簡潔的做法
也就是`enumerate` 這個`function`


`enumerate`這個`function`最基礎最基礎的用法，是用在一個長得跟`list`很像的、叫`tuple`（他婆）的東東上

他們兩個長得真的很像，一個用中括號，一個用小括號
```python
l = []
t = ()
```

`list`跟`tuple`最大的差別在於，`tuple`是`immutable`的
也就是說，當我們建立了一個`tuple`串後，我們無法增加、減少、改變任何存在這個`tuple`下的值
我們甚至無法對一個`tuple`直接使用`sort`這個`method`
如果我們對真的要他進行`sort`，我們要先建立一個新的變數來儲存sort完後獲得的`list`
是的，如果硬要，那我們會得到一個**全新的**、**不同的**類型的東東，原本的東東來是不變的tuple

```python
t = ('a', 'c', 'b')

sorted_t = sorted(t)

print(sorted_t)
print(type(sorted_t))

--
['a', 'b', 'c']
<class 'list'>

```
因為這些特性，所以如果我們要儲存的資料千千萬萬**不能夠被改動**的話，那我們就應該用`tuple`儲存，以防萬一


當我們對一個`tuple`使用`enumerate`這個function時，我們可以得到存在這個tuple下的各個值的index，以及相對應的資料
也就是說，我們會獲得index然後才是儲存在這個tuple的資料

```python
t = ('apple', 'banana', 'watermelon')

x = enumerate(t)

print(list(x))
--
[(0, 'apple'), (1, 'banana'), (2, 'watermelon')]

```



我們對這個`list`使用`enumerate`這個`function`後，我們就可以得到這個`list`內的東西的index還有對應到的東西
搭配for loop使用時，因為enumerate這個function會給我們index跟value，所以我們要記得寫兩個變數

```python
fruit = ['banana', 'apple', 'watermelon']
dic = {}
for i, v in enumerate(fruit):
    dic[i] = v
    print(dic)

--

{0: 'banana'}
{0: 'banana', 1: 'apple'}
{0: 'banana', 1: 'apple', 2: 'watermelon'}

```
