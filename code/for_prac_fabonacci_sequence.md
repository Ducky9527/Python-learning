2022/06/20

貓貓老師出題：

```
費波那契數列是一個從零與一開始，接下來之數值，則由前兩項之數加總而得，所構成之數列。
費波那契數列可以用下面的方式定義：
第零項 = 0
第一項 = 1
第n項 = 第n-1項 + 第n-2項

費波那契數列頭幾項為：0, 1, 1, 2, 3, 45, 8, 13, 21, 34....

你只要知道如何使用下面的工具，就可以寫出一個費波那契數列產生器嚕！！
1) if, elif, else
2) for loop
3) range
4) 基本的數學與邏輯運算
```


嗚嗚嗚，還好三小時內就做出來了，不然好丟臉...
(幹，誰在那邊說什麼搭配while loop，騙我！害我還在那邊東搞瞎搞，設定while loop停止的機制！)

```python
print("""
我是小費費～你想要產生費波那契數列產生到第幾項？我可以從第零項開始，一路往下列ㄛ！
""")
input = int(input("請輸入一個數字指定你想要列到第幾項～"))
step = 1 + input

real_compute_step = step - 2
fibo_even = 0
fibo_odd = 1

print(" ")
print(f"餔嚕餔嚕餔嚕～～～下面是從第零項開始到第{input}項的數列")
if step == 1:
    print(fibo_even)
elif step == 2:
    print(fibo_even)
    print(fibo_odd)
        
elif step > 2 and step % 2 == 1:
    print(fibo_even)
    print(fibo_odd)
    fibo_even += fibo_odd
    print(fibo_even)

    for iteration in range(int((real_compute_step - 1) / 2)):
        fibo_odd += fibo_even
        print(fibo_odd)
        fibo_even += fibo_odd
        print(fibo_even)

else:            
    print(fibo_even)
    print(fibo_odd)
    
    for iteration in range(int(real_compute_step / 2)):
        fibo_even += fibo_odd
        print(fibo_even)
        fibo_odd += fibo_even
        print(fibo_odd)
```


2020/06/25
大家看了我的解法後，嘖嘖稱奇，覺得思路怎能如此清奇
我自己也感到很意外呢！我這輩子從沒想到奇數跟偶數對我來說這麼重要！
乍看之下的一氣呵成，其實掩藏了我早早的奇偶分流！

看了G老師的`while loop`版本後，我才意識到自己是因為什麼原因所以必須把code寫成這樣
鄉親啊！`print`可以`print(fibo_even+fibo_odd)`啊！！！這樣就不用為了一定要把`fibo_even`跟`fibo_odd`兩兩一組印出來，搞這麼多功伕啊！！！

我...
我...我可以的!!!!

