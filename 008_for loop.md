for loop跟while loop一樣適用於會需要反覆操作的情境
不過for loop的條件設定跟while loop不大一樣
for loop 的想法比較像是

```
給定一坨東西，對這坨東西含的每個元素進行圈圈叉叉
```
這坨東西，可以是一個清單（[1, 2, 3, 4] 或者是["陽光"、"空氣"、"水"、"wifi"]）可以以是一個字串（"Ducky9527"）
而確切的元素，以["陽光"、"空氣"、"水"、"wifi"]這個生活必需清單來說，"陽光"就是其中一個元素

如果我們想要印出生活必需清單中的所有東西，在沒有for loop的時候，我們可以這樣笨笨的寫

```python
essential = ["陽光", "空氣", "水", "wifi"]

print(essential[0])
print(essential[1])
print(essential[2])
print(essential[3])
====
陽光
空氣
水
wifi

```

這樣超笨，而且很浪費時間
我們知道我們要做的就是是依序從第一個元素開始一個一個印而已
這麼repetitive的事情，實在不值得多敲幾次鍵盤，這樣鍵帽會油得很快
這個時候，for loop就可以派上用場了！！！


```python
essential = ["陽光", "空氣", "水", "wifi"]

for element in essential:
#對於essential的這坨東東的element，我們依序對這些element執行下面的動作
    print(element)
====
陽光
空氣
水
wifi
```

如果我們的清單是一個數列，如[5, 7, 8, 10]
我們也可以把這個數列中的一個一個數值抓出來，一一進行運算
```python
for number in [5, 7, 8, 10]:
    compute = number * 10
    print(compute)
====
50
70
80
100
```

如果我們有一個花費的清單，我們想要知道總共花了多少錢，我們也可以用for loop來做
```python
price = [10, 20, 30]
total = 0 #起始值是零
for item in price:
    total += item #開始按照順序，從第一個物件的價錢加總上total這個變項，更新total暫存的數值
    
print(total) #因為我不想要看到每一次loop把item的價錢加總到total後更新total暫存的數值的過程，所以我把print拉到for loop外，等他loop完、更新完total後，我在印最後的總價
```



我覺得這邊比較需要一點時間來理解的，是跟`range()`的搭配
`range()`可以用來產生`一串`數字
所以看到`range(3)`的時候，心中要想到，這其實是一個數列（[0, 1, 2]），而不是一個數字
這也是為什麼，`range()`常常拿來控制for loop要loop幾次

比方說這樣
```python
for item in range(3):
    print (f"鴨鴨說你好～第{item}次") # 這邊搭配item可以很明確的看到印了幾次，每一次他都做了什麼
====
鴨鴨說你好～第0次
鴨鴨說你好～第1次
鴨鴨說你好～第2次
```

搭配increment也可以很輕鬆的印出直角三角形
```python
tri = " "
for item in range(3):
    tri += "X" #每次執行時對tri這個變數做更新，每次增加一個X
    print (f"{item}{tri}") 
    #前面一樣放一個item，方便我們知道發生什麼事，然後印出更新完後的tri
```

`range()`還可以明確指定數列的數字要從哪邊開始產生、哪邊結束、公差多少等等等的
從剛剛的鴨鴨說你好～例子也可看出，如果只給定一個數字`3`，那`range(3)`就會被預設成從`0`開始，一路列到第十個數字，也就是`2`
（所以如果要輸出成符合人類世界主流的計數方式的話，`{item}`可以改寫成{`item+1}`）

如果寫成`range(3, 5)`
那python就會產生一組從`3`開始，到`5`就停的數列，也就是`[3, 4]`

寫成`range(3, 10, 2)`則是產生一組從`3`開始，到`10`停止，以2為公差的數列，也就是`[3, 5, 7, 9]`


======


在參考這篇教學（https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-4990a5757aa6）時看到了一個不是很了解的用法
為什麼要先對先對theBeatles取len()然後才下for loop呢？

```python
theBeatles = ['John Lennon', 'Paul McCartney', 'Ringo Starr', 'George Harrison']
for i in range(len(theBeatles)):
    print(theBeatles[i])
====
John Lennon
Paul McCartney
Ringo Starr
George Harrison
```

實在無法自己參悟，就用了就用了Ｇ老師說的，不知道發生什麼事的時候，就找個地方用print當照妖鏡，讓他現出原形

```python
theBeatles = ['John Lennon', 'Paul McCartney', 'Ringo Starr', 'George Harrison']
print(len(theBeatles))

for i in range(len(theBeatles)):
    print(theBeatles[i])
====
4
John Lennon
Paul McCartney
Ringo Starr
George Harrison
```

這樣終於看懂了，原來用`len()`去取的，是theBeatles這個變數目前暫存的清單的長度（因為有四個東東，所以長度為四）
所以`range(len(theBeatles))`其實就只是利用這個清單的長度去設定loop要loop四次，依次把theBeatles裡的每個東東印出來而已
實在是感恩Ｇ老師！讚嘆Ｇ老師！
有什麼問題，print他一print，人生的困惑，就解開了至少一半了！

4
