這是一個while loop 練習

從前從前有一隻無主家庭小精靈到處流浪，一直找不到主人
直到有一天....

```python
question_attempt = 0
question_limit = 3 

while question_attempt < question_limit:
  answer = input('Do you like little elf? ').upper()
  question_attempt += 1
  if answer == "Y":
    print("He likes you too!")
    break
  if answer == "N":
    print('But...he likes you!')
    print(" ")
  else:
    print("This is a yes or no question!")
    print(" ")
else:
    print("不管辣！你要愛我辣！")
```
