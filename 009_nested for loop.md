nested for loop指的是在一個for loop裡面又塞了一個for loop的多重迴圈結構  
如果我們要同時處理兩個（或更多個）變項，我們就可以用nested for loop來讓python幫我們依次處理

比方說，如果我們想要印出一組座標系，我們就可以用nested for loop   
```python
for x in range(2):
    for y in range(2):
        print(f"{x}, {y}")
====
0, 0
0, 1
1, 0
1, 1
````
這邊的意思是，`x` 作為`range(2)` 也就是`[0, 1]` 這個list的元素   
1）第一次跑的時候，抓出的第一個`x`為`0`   
2) 然後進入到第二個`for loop`  
3) 而這個`for loop`是`y`作為`range(2`)也就是`[0, 1]`這個`list`的元素的`for loop`  
4) 在第一次跑的時候，抓出的第一個`y`元素`0`  
5) 印出目前抓出的的`x`與`y`的值`0, 0`  
6）因為目前進入到的`for loop`還有一個`y`元素還沒有抓出來用到（也就是`1`），所以繼續執行這個第二層的`for loop`  
7) 此時抓出來的`y`為`1`，但是`x`並未更動  
8) 印出沒有更動的`x`與有更新的`y`，也就是 `0,1`   
9) 因為第二層的`for loop`跑完了，所以可以到外層去，在執行一次`x`所屬的那層`for loop`，這次抓第二個元素`1`  
10) 接下來重複一樣的動作，直到所有的元素都操作過一輪結束

====

因為nested for loop這個的結構性質，我們也可以把它拿來印九九乘法表

```python
for item in range(1, 10):
    print(f"九九乘法表之 {item} 的表") # 每進來外環一次，印一次就好了
    for times in range(1, 10):
        result = item * times

        print(f"{item} X {times} = {result}") 
        # 因為每個乘數被乘數還有結果都要顯示，所以每執行一次這環就要印一次，不能擺到外環去
        # 如果少indent一次，就會只印出會後一次的結果喔！！  
      
```

在學`nested for loop`時，我碰到的困難其實主要是出在當`nested for loop`跟`range()`搭配時的變化  
比方說下面這題  

```
只用nested for loop與range()印出
xxxxx
xx
xxxx
xx
xx

限制：不能使用 x * number這種方式直接做圖
```

如果可以用x * number這種方式，這個其實很簡單，這樣寫就好了  

```python
number = [5, 2, 4, 2, 2]
for item in number:
  print("x" * item)
```

但如果不行的話，那就表示，要用increment讓他慢慢吐，可是，要怎麼一下子increment5次？一下2次？  
這邊我想超久都沒想出來  
看解答才知道，啊！range()可以一用再用啊！清單中的每個數字，也都可以成為range()作用的對象  
以這題來說，只要對number做range()我們就可以得到下面的數列  

```
[0, 1, 2, 3, 4]
[0, 1]
[0, 1, 2, 3,]
[0, 1]
[0, 1]
```
有了這些數列之後，我們就可以用它們來控制第二層的loop要跑幾次了！  
所以，整個解題關鍵，其實是在range()！！！  

```python
number = [5, 2, 4, 2, 2]
for item in number: # 依次執行，外層這個會執行五次
    output = " " # 畫畫要用的變數，先給一個空白
    for increment in range(item): # 這邊是重點！！！對外層的item做range控制要increment幾次
        output += "x"
    print(output) #這邊的print擺在外層的原因是因為我們只要印出最後increment完的結果即可
```


不過，我對range()的掌握，再之後做貓貓老師出的列印三角形習題時，還是看得出來我掌握得不夠好  
貓貓老師出的題目看起來很簡單，可是我想了很久才想出來...  

```
給定任意高度h，利用nested for loop列印像是下面這樣的直角三角形~
XXXXX
 XXXX
  XXX
   XX
    X

```
因為題目說給定任意高度，所以不能直接用偷吃步用數列去乘  
當下就有想到要用range()、同時做兩個同階層的for loop，然後把他們處理完的東西用print黏在一起印  
可是我一直卡在不大知道要怎麼樣一邊減少X一邊又增加空白之處  
一開始想到的是，既然X是逐行增加，那我是不是把可以透過一些手法，把數列的排列順序顛倒過來  
藉此印出這樣的直角三角形呢？  

所以我的第一次的嘗試長成這樣   
```python
h = 5


for height in range(h):
    space = ""
    dot = "X"
    for item in range(height):
        space += " "
    for iteration in reversed(range(height)):
        dot += "X"
    print(f"{space}{dot}")
====
X
 XX
  XXX
   XXXX
    XXXXX
```

答案是，不行...整個長得很歪，不知道發生什麼事情  
所以我使用了Ｇ老師傳授的print妖鏡來看看到底發生什麼事  

```python
h = 5


for height in range(h):
    space = " "
    dot = "X"
    for item in range(height):
        space += "Y" #我改成Y這樣比較好看出發生什麼事
        
    for iteration in reversed(range(height)):
        dot += "X"
        print(iteration) #print妖鏡
    print(f"{space}{dot}")
====
 X
0
 YXX
1
0
 YYXXX
2
1
0
 YYYXXXX
3
2
1
0
 YYYYXXXXX
```
..........
齁....  
洗安捏ㄏㄧㄡ   
我終於知道發生什麼事了...  
原來`reversed(range(height))`確實是有發生作用，只是他真正的作用跟我想的不大一樣  
他的作用是把`range(height)`裡的每個數列的排序顛倒過來排，所以最後每個數列有的元素的數目還是一樣多個  
跟我要的完全不一樣...

那、那、那到底要怎辦！！！！   
Ｇ老師此時好心的提點了  

```
range()裡，可不可以做基本的運算呢？
我們要的是一增一減，那是不是我們可以找一個定值進去
每當height增加了，我們就把那個定值減去height，這樣不就一增的同時也一減了?

```


鄉親啊！！！這實在是太睿智了！！！  
我到底在腦殘什麼呢！？我怎麼會都沒想到range內可以做基本的運算這件我根本就知道的事情！！！  
經過這個提示後，我馬上就把code修對了...  


```python
h = 5


for height in range(h):
    space = ""
    dot = ""
    for item in range(height):
        space += "Y"
        
    for iteration in (range(h-height)):
        dot += "X"
        
    print(f"{space}{dot}")
```
