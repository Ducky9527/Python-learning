貓貓老師出題

用while loop做出一個可以把任意數字，按照下面的規則，逐漸收斂到一（而且必為一！）的小程式ㄅ～～

規則：
如果是奇數就乘以三再加一
如果是偶數就除以二

```python
import random
number = random.randint(1, 50)

print("""
Collatz conjecture
給定任一正整數，奇數則乘以三加一，偶數則直接除以二
按此原則反覆運算，最後必然會得到一

""")
print("選出的數字是！！！" +str(number))

print("")
while number > 1:
    if number % 2 != 0:
        number = (number * 3) + 1
        print(number)
    else:
        number = number // 2
        print(number)
else:
    print("萬法歸一🙏")
```
