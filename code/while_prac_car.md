while loop的小練習，天竺鼠車車

```python
#起始設定，車車是停的
car_start = False


print("""
天竺鼠車車pui pui
一起來玩ㄅ！！！
輸入help可以看到指令ㄛ！
""")
while True:
    print("")
    command = input("> ").lower()

    if command == "start":
        if car_start:
            print("天竺鼠車車已經哺哺哺ㄌ")
            print("")
        else:
            car_start = True
            print("天竺鼠車車哺哺！")
            print("")
    elif command == "stop":
        if not car_start:
            print("車車已經停好ㄌ辣！")
            print("")
        else:
            car_start = False
            print("天竺鼠車車停停")
            print("")
    elif command == "help":
        print("""
        =============
        start: 啟動天竺鼠車車
        stop: 停止天竺鼠車車
        quit: 終止天竺鼠車車小程式
        help: 你都知道要打help了還要我說嗎？
        =============
        """)
    elif command == "quit":
        print("天竺鼠車車說~掰~掰~")
        print("END")
        break
    else:
        print("聽不懂嗚嗚嗚")
```
