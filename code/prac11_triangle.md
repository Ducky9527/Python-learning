貓貓老師出題

`給定行高為h，用for loop列印出一個底也為h的三角形ㄅ！`


```python
height = input("the height of the triangle is > ")
triangle = int(height)

for h in range(triangle):
    triangle_body = 'X'
    space = ''
    for iterate in range(2 * h):
        triangle_body +='X'
    for iterate in range(triangle - h):
        space += ' '
        
    print(f"{space}{triangle_body}")
 ```
 
這題真的是乍看簡單，但實在折磨死初學者的難題...
我想了兩天，最後才在Ｇ老師的提醒下，發現癥結點在於腦筋打結，沒有意識到可以用`range()`內還可以`triagngle - h`這樣子逐行縮減
 
也就是說，我卡住的地方根本不是for loop，而是range...
