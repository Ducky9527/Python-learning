工作忙起來，又耽誤了學習...

今天要記錄的心得是dictionary這個資料結構另外的妙用：Hash mapping

我本來也不知道這到底是什麼，是直到開始練習leetcode後，才發現原來dictionary可以這樣使用

在某些任務上，用hash mapping做，可以比用list一個一個暴力的推過去要快上非常多，快到多少的程度，容我留待介紹two sum這個任務再說明

--

在介紹hash mapping前，我們要先知道dictionary跟list一樣，都是可以增加新的資料進去的

list的做法是透過append這個method，如

```
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

```
dic = {}
dic['book'] = 'the lord of the ring'

print(dic['book'])
print(dic)

--
the lord of the ring
{'book': 'the lord of the ring'}
```

