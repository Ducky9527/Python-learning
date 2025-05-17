工作忙起來，又耽誤了學習...

今天要記錄的心得是dictionary這個資料結構另外的妙用：`Hash mapping`

我本來也不知道這到底是什麼，是直到開始練習leetcode後，才發現原來`dictionary`可以這樣使用

在某些任務上，用`hash mapping`做，可以比用`list`一個一個暴力的推過去要快上非常多，快到多少的程度，容我留待介紹`two sum`這個任務再說明

--

在介紹`hash mapping`前，我們要先知道`dictionary`跟`list`一樣，都是可以增加新的資料進去的

list的做法是透過append這個method，如

```python
l = []

l.append(1)
print (l)

--
[1]

```

那`dictionary`呢？

要新增資料進 `dictionary` 的話，因為`dictionary`有`key`又有儲存在`key`裡面的`value`

我們的做法跟更新`list`會不大一樣

以下面的例子來說，假設我們一開始的`dictionary`空空如也，我們想要新增一個叫做`book`的`key`，並且在book這個key下面儲存`the lord of the ring`
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

聰明的小朋友看到這裡，一定就會想到，如果`dictionary`也可以新增資料，那是不是我們就可以透過`for loop`等`loop`，將表格資料、網頁資料用`dictionary`整理好

答案是！！！沒錯！！！事實上，這就是老Ｇ老師幫忙我把`中國哲學書電子計畫`這個網站上的資料dump下來的方式

因為把資料dump下來比較複雜，所以請容我用下面的簡單例子做範例


假設我們有一個`list`叫`fruits`
這個`list`中有`[‘banana', 'apple', 'watermelon']`

我們想要把這個水果清單轉成`dictionary`，並且，把每個水果都存到一個以他們在這個清單的次序而產生的`key`之下，我們可以這麼作

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

如果真的是想要把資料都寫在`'n'`這個 `key`下面，那也不是不行，但這個時候，我們做的事情其實是把一個`list`存在這個`key`下

所以我們要做的事情會是....`append` da `list`!
要做這件事情前，我們要先記得...要開好一個空空如也的`list`
不然python會吐出`KeyError`來

開好了之後，我們就可以開始`append`這個`list`啦～

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

回到剛剛提的用`index`作為`key`，這邊需要稍微的離題一下，介紹一下利用很陽春的 `n += 1` 之術外，更佳簡潔的做法

也就是`enumerate` 這個`function`


`enumerate`這個`function`最基礎最基礎的用法，是用`list`跟`tuple`（他婆）

這邊又需要再離題一下...
`list`跟`tuple`他們兩個長得很像，一個用中括號，一個用小括號，但細部性質不大一樣
```python
l = []
t = ()
```

`list`跟`tuple`最大的差別在於，`tuple`是`immutable`的
也就是說，當我們建立了一個`tuple`串後，我們無法增加、減少、改變任何存在這個`tuple`下的值
我們甚至無法對一個`tuple`直接使用`sort`這個`method`
如果我們對真的要他進行`sorted()`，我們要先建立一個新的變數來儲存sort完後獲得的`list`
是的，如果硬要，那我們會得到一個**全新的**、**不同的**類型的東東，原本的東東還是不變的`tuple`

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


當我們對一個`tuple`使用`enumerate`這個`function`時，`enumerate`就會像是一個序數生產器一樣
以`tuple`中資料為基礎吐出該筆資料`index`以及該筆資料

這邊要小心的事情是，如果直接`print enumerate(t)`的話，我們會得到類似下面的資訊

```python
t = ('apple', 'banana', 'watermelon')

x = enumerate(t)
print(x)

--
<enumerate object at 0x10309a3e0>

```
會出現這個資訊的原因是因為，這邊的 `x` 實際上是一個`**(‘序數’, ‘資料’)tuple產生器**`，每叫他一次，他就生產一個`(‘序數’, ‘資料’)` 

`x` 指涉到的並不是下面這個完整的 `tuple list`

```python
[(0, 'apple'), (1, 'banana'), (2, 'watermelon')]
```

所以如果我們直接執行 `print(x)`

我們得到的資訊會是

```
<enumerate object at 0x10309a3e0>
這是一個 enumerate 產生的物件，它現在存在電腦記憶體裡的位置是 0x10309a3e0。
``

真的要看到我們想要看到的一個個的 `(‘序數’, ‘資料’)` 

我們需要再 `x` 這個 `iterator` （疊代器）上在施用`list()` 這個`function`

讓 `x` 可以按著存在`tuple`或是`list`中的所有資料從頭到尾執行一次

然後`list()`再把所有的`(‘序數’, ‘資料’) tuple` 給用`list`的方式存起來

得到下面這個東東

```python
[(0, 'apple'), (1, 'banana'), (2, 'watermelon')]
```


回過頭來說說如何搭配`for loop`
因為`enumerate`這個`function`會給我們一組有序數跟對應的儲存的值的`tuple`，所以我們要記得寫兩個變數

```python
fruit = ['banana', 'apple', 'watermelon']
dic = {}
for i, v in enumerate(fruit): #i = index, v = value
    dic[i] = v
    print(dic)

--

{0: 'banana'}
{0: 'banana', 1: 'apple'}
{0: 'banana', 1: 'apple', 2: 'watermelon'}

```

這樣使用`enumerate()`，就不用另外再可憐兮兮的手刻 `n+=1` 計數器了

如果要指定序數要從哪個數字開始，那也很簡單，在後面加上`start = x` 即可


```python
enumerate(iterable, start = 1)
```

是的，enumerate的完整語法是上面寫的這樣！

--
現在終於可以開始說`hash mapping`了！

`hash mapping`說穿了，其實就只是把資料轉成`dictionary`的格式儲存而已

他的優點在於，電腦在找`dictionary`裡的資料時，可以直接看到`dictionary`裡所有的`key`、`value`

所以，當一個`list`被轉換成`dictionary`時，電腦就不用苦命的每字都從`list`中的第一項開始查詢

比方說，我有一個`list = [1, 3, 7, 8]`

我想要知道，我這個`list`裡面儲存的數值中，哪兩個加總起來會是9

如果我用`for loop`直接對這個list做，我的邏輯就會是這樣

```python
"""
l = [1, 3, 7, 8]
target = 9
因為我不知道哪個加哪個會是9
所以我最保險的做法就是從第一個數值開始，讓他跟他之後的所有數值一個一個加加看
所以就是，先把 1 抓出來，然後開始把他跟3, 7, 8 分別加加看
"""
l = [1, 3, 7, 8]
target = 9
count = 0

found = False

for i in range(len(l)): # 用這樣的方式告訴程式要執行幾次
    for j in range(len(l)-1): # 記得要減一不然會out of range
        count+=1
        if l[i]+l[j+1] == target:
            print (f'the target is {target} and the combination is {l[i]} and {l[j+1]}')
            found = True
            break
    if found:
        print(f'It takes {count} times to find the combination')
        break
--
the target is 9 and the combination is 1 and 8.
It takes 3 search to find the combination.
```

在這個case中，我們很幸運的只在內層的 `for loop (J)` 做了三次loop就找到

也就是說，我們甚至沒有進入外層的 `for loop (I) `第二次、我們只掃過這個`list`一次而已

可是，如果，我們很衰，存在這個`list`的值雖然一模一樣，但是數值排序不一樣呢？

如果我們的list是下面這樣呢？？

```
l = [3, 7, 1, 8]
```

是的，以三為基準，掃過整個list一次，沒找到！
再來，以七為基準，掃過整個list一次，沒找到！
要直到以一為基準，做到最後一次，才真的找到1+8這個組合
總共要做九次！！
速度差很多啊！


對我們人類來說，不管這個 `list` 裡的東西是怎麼排的，我們都可以只掃過這個 `list` 一次就找到答案

這是因為，因為當我們看到三的時候，我們就知道等下要是看到六，那我們就找到組合了

但因為我們看到的不是六，是七，所以我們在無奈之餘，能做的就是先把三記在心裡，等等看會不會看到六

也就是說，我們會在心裡面偷偷開好一個記事板，等等隨時可以把暫時書寫在上面的三拿下來比對

接下來的七也是一樣的做法，我們看到七的時候，我們知道我們需要一個二才能跟湊出一個九

這個時候，我們可以再問自己，那剛剛有看到二嗎？沒有的話，那我們就先把七也寫進去，免得之後七馬上就可以跟人湊做對

一樣的操作方式操作下去，到最後的八的時候

我們可以問自己，剛剛有看到過一嗎？答案是有！bingo！


這個寫在心中的記事板的做法，其實就是先開一個dictionary，然後不斷地把新看到的、還沒派上用場的數值都記到記事板上

每一次的探問，我們都可以直接看到記事板上的所有資料

也就是說，我們不用從頭開始一個一個找，我們的做法是一次看所有的資料

這個做法基本上就是利用「記憶空間」來換取「時間」

因為我要能夠一次看到所有的資料，我就要花費記憶的空間來把所有我看到的、覺得可能有用的資料都先記下來

算是個無解的記憶空間與運算時間的trade-off

```python
l = [3, 7, 1, 8]
target = 9

for i, v in enumerate(l):
    com = target - v
    if com in dic:
        print(dic[com], i) # 找到了就印出兩個 index
        break
    dic[v] = i             # 沒有在裡面的話就 插入 hash map O(1) 
--
0 2
```

用資工人的語彙就是

用`hash mapping`來處理這個找出數字組合的問題的話，他的`時間複雜度(time complexity)`是 `O(n)`

這邊的 `O(n)` 的意思是說，每個數字只處理一次，每次查找或插入都是 `O(1)` (執行一次）

假若我們有n個數值，那我們就處理共 `（n*1）` 次

時間複雜度這個觀念在程式設計裡很重要，因為我們之所以會想要寫程式，往往是因為我們希望程式可以來幫我們重複執行某某動作很多很多次

這也是為什麼，我們會想知道，當要處理的檔案、資料變大時，不同策略所需的時間會以什麼方式增長


這個 `Big-O` 就是一個幫我們衡量`時間複雜度`的客觀標準

我一開始使用的`nested for loop`在最糟的狀況下，會需要把內外兩層都跑過一次

假設內外兩層都有 `n` 個東東，那我最糟最糟的狀況，就是要跑 `n*n` 次，也就是 `n^2` 次！！！

如果我的`list`只有2個東東，那最糟最糟，用`nested for loop`跑，就是跑 4 次

但如果我增長到 4 個東東呢？最糟最糟，要跑 16 次！

中間的增長是以平方的方式`（O (n^2)）`在增加，非常的可怕！！！

跟hash mapping這樣以線性的方式`(O(n))`增加不一樣


那...查字典在資料的大小改變下，會怎麼影響運算的速度呢？


答案就在剛剛說的「一目瞭然」

查字典的時間複雜度無論資料量的大小，通通都是操作一次就可以，也就是說，他的時間複雜度是 O(1)

這邊介紹的找出哪兩個數字加起來會是目標數字的任務，就是leetcode的TwoSum~
