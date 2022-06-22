在連續兩天的挫折後（我就草莓），我決定選擇比較沒有這麼挫折的方式繼續我的爬說嘴之旅

是的，我決定，來去youtube看教學、複習複習基礎先

我選的課程是Programming with Mosh這個youtuber的Python Tutorial - Python Full COurse for Beginners
https://youtu.be/_uQrJ0TkZlc



**Task 1 - Print Function**

Print name
把名字列印出來～
這個function某意義上來說真是重要到不行啊，沒有他根本不知道自己的糞code都做了什麼...
（沒有把print寫進程式的話，執行的話之後也不會顯示結果，因為「顯示結果」本身也是個需要被執行的事情啊！）

```python
print("Ducky9527")
```

easy peacey

python 3 的 print function語法跟python 2不大一樣，就只有這個要稍微注意一下而已

被 " " 或者是 ' ' 夾起來的東東叫做string(字串)

print這個function在python中可以有其他的變化，如

```python
print("*" * 10)
```

這個"*" 乘以10的意思是會生出十個 **********
惱絲縮，這不是每個語言都有的syntax sugar (之後會看到一些有這個syntax sugar的話人生會有多美好的例子）



**Task Two - Variable**

```python
price = 10
```

的price就是一個variable，這個「變數」可以用來表示不一樣的東東，現在暫時先說是10，但之後其實也可以變成其他的數值

比方說
```python
price = 10
print(price)
```python

就會這樣的話就會顯示出10
但如果多加了一行price = 20在下面

```python
price = 10
price = 20
```
因為python是逐行執行指令，在第42行這邊時，price這個variable的值就會被覆寫成20
所以在此後執行print的話，會print出20來


**Task Three - Type of Value**

在python的世界裡，變數可以暫存string, integer, flooting, 還有bolean value(True, False)等等的東東


**練習題**
we check in a patient named John Smith.
He's 20 years old and is a new patient.
```python
name = 'John Smith'
age = 20
existing_patient = False
```

**Task Four - Input Function**
input function可以用來輸入指令
利用 + 可以把兩個string黏起來一起print出來

```python
name = input('Who are you? ')
print('Hi!! ' + name)
```

**練習題**
```python
name = input("Who are you? ")
print("Hi! " + name)
colour = input("What's your favorite colour? ")
print("Oh, so you like " + colour + "!")
```

太無聊的話可以弄一個神奇寶貝fu的版本

```python
name = input("Who are you? ")
print = ("Gotcha! " + name + "!")
```

