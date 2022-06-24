while loop是一個可以指定什麼時候要開車，開到什麼時候要停車的語法

好比說，設定一個在氣溫15度以下會自動執行增溫，直到氣溫達到十五度的小程式，可以寫成這樣

```python
temp = int(input("現在氣溫幾度？"))


while temp < 15:
    temp += 1
    print (temp)
print("Target Temp Hit!")
==
現在氣溫幾度？13
14
15
Target Temp Hit!
```

整個概念是這樣
當輸入的氣溫是`13`度時，符合`while loop`啟動的條件，所以依次
1)執行了更新`temp`這個變數為`14`，然後將更新的`temp`印出來
2)重新再比對是否新的`temp`依舊符合氣溫低於15度這個條件
3)因為符合，所以再執行一次 `temp += 1` 將 `temp` 儲存的數值改為`15`，然後再執行印出的指令
4)此時，`while loop`比對最新的`temp`的數值，發現`temp`現在已經不再小於`15`，不符合執行的條件了，因此不再執行（打破輪迴～～）
5)不再一直轉呀轉後，程式就可以繼續往下走，執行 `print("Target Temp Hit!")` 


在設定while loop時，要非常非常注意indention，一個沒有indent好，從屬關係就跑掉了，意思就整個不一樣了！
這件事情用畫的來表達比較清楚

好比說，我們想要透過python的while loop的重複執行來畫出一個高為五的三角形好了
我們可以簡單寫成這樣

```python
dot = 1

while dot <=5:
    triangle = "X" * dot
    dot += 1 
    print(triangle)
    
    
===
X
XX
XXX
XXXX
XXXXX
```

這樣子的意思是，當dot小於等於五的時候
1) `dot` 小於五，執行`while loop`中的`triangle`變數中暫存的 `"X" * dot` (這邊的乘號的意思比較是X出現的次數由後面的dot所暫存的數值決定，而不是數值運算時的乘法的用法）
2) 更新`dot`的數值 (2)
3) 印出`triangle`的`string` (X)
4) 再比對一次`dot`的數值，發現依舊小於五，繼續執行`while loop`
5) 執行`triangle`
6) 更新dot (3)
7) 印出`triangle`(XX)
8) ....
dot大於五，停止

但如果，這個print(triangle)沒有indent好，就會不會被視為是`while loop`的一部分

```python
dot = 1

while dot <=5:
    triangle = "X" * dot
    dot += 1 
print(triangle)
===
XXXXX
```

這是因為，沒有indent時，python的理解方式是這樣：
1) `dot` 小於五，執行`while loop`中的`triangle`變數中暫存的 `"X" * dot`
2) 更新`dot`的數值 (2)
3) 再比對一次`dot`的數值，發現依舊小於五，繼續執行`while loop`
4) 執行`triangle`
5) 更新dot (3)
6) ....dot大於五，停止while loop
7) 執行下一行的`print(triangle)` 印出XXXXX


====
利用while loop跟increment operator (就是 `=+`、`-=`、`*=`、`**=` 這些孩子)可以設計一些互動式小程式
比方說，三次內要猜到數字不然就算輸的小遊戲，這個「三次」的條件，就可以用increment operator去做，邏輯跟上面的一模一樣

```python
import random

guess_time = 0
guess_max_time = 3
answer = random.randint(0,9)
print(answer)


while guess_time < guess_max_time:
    guess = int(input("Let's guess! Type in a number from 0 to 9! "))
    guess_time += 1

    if guess == answer:
        print(f"That's correct! The anwer is {answer}!")
        break
    elif guess < answer:
        print("That's wrong. Higher.")
    else:
        print("That's wrong. Lower.")

print("Sorry. You fail.")
```
這個小程式唯二兩個跟之前的小東東不大一樣的只有
1) 為了增添趣味性，匯入了random，這樣才能使用亂數產生器這些平常未必會用到的功能
2) 因為猜對了就不用再猜了，所以在猜對這邊有下一個叫做`break`的斷開迴圈的指令，其餘的狀況則可以繼續猜，猜到次數用完為止

====
因為我太無聊了，所以又做了一個稍稍有變化的版本
就，如果第一次猜錯，要再猜的時候，程式顯示的訊息會變成```Try again!```，以示鼓勵...

```python
import random

guess_time = 0

answer = random.randint(0,9)
print(answer)


while guess_time < 1:
    guess = int(input("Let's guess! Type in a number from 0 to 9! "))
    guess_time += 1

    if guess == answer:
        print(f"That's correct! The anwer is {answer}!")
        break
    elif guess < answer:
        print("That's wrong. Higher.")
    else:
        print("That's wrong. Lower.")

while guess_time < 3:
    guess = int(input("Try again!"))
    guess_time += 1

    if guess == answer:
        print(f"That's correct! The anwer is {answer}!")
        break
    elif guess < answer:
        print("That's wrong. Higher.")
    else:
        print("That's wrong. Lower.")

if guess_time == 3:
    print("Sorry. You fail.")
```
