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
fibo_start = 0
fibo_add = 1

print(" ")
print(f"餔嚕餔嚕餔嚕～～～下面是從第零項開始到第{input}項的數列")

if step == 1:
    print(fibo_start)
    
elif step == 2:
    print(fibo_start)
    print(fibo_add)
        
elif step > 2 and step % 2 == 1:
    print(fibo_start)
    print(fibo_add)
    fibo_start += fibo_add
    print(fibo_start)

    for iteration in range(int((real_compute_step - 1) / 2)):
        fibo_add += fibo_start
        print(fibo_add)
        fibo_start += fibo_add
        print(fibo_start)

else:            
    print(fibo_start)
    print(fibo_add)
    
    for iteration in range(int(real_compute_step / 2)):
        fibo_start += fibo_add
        print(fibo_start)
        fibo_add += fibo_start
        print(fibo_add)
```
