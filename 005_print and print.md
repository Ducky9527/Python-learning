print 還有其他的用法，如：
```python
name = "Ducky"
print(name[0])
```

這個`name[0]`表示的是name這個variable暫存的第一個字元（因為python的計數是從0開始的），在這個case中，指涉到的就是D
所以print出來就會是D

如果用
```python
print(name[-1])
```
這邊的-1指的是從右邊算起來的第一個字元，在這個case中，指涉到的就是y
所以print出來就是y
依此類推

另外的用法則是
`print(name[0:3])`，這邊的`[0:3]`表示從name暫存的東東的第一個字元到第四個字元
在這個case中，就是Duck

同理
`print(name[1:])`這個[1:]指定從第二個字元開始，但是沒有指定在哪終止，所以就會一直下去，直到結束
在這個case中，print出來自然是ucky

`[:]`沒有指定開始，也沒有指定終止，所以會預設為從第一個字元開始，一直印到最後一個字元

`[1:-1]` 則表示是從第二個字元開始，然後到右邊數來第一個字元之前的那個字元結束
在這個case中，就是uck

**========**

要print一串包含不同variable的訊息時，可以用formated string來做，這樣好寫也好懂

比方說：
```python
name = "Ducky"
type = "pokemon"
```

如果要print出Ducky is a pokemon.

笨笨的做法可以寫成
```python
print(name + " is a " + type + ".")
```

這樣寫很煩，因為一邊寫一邊還要注意空格有沒有空好空滿

用formated string的話就不會有這個困擾
因為formated string可以直接打出一串句子，然後用`{}`把variable包起來，讓python知道哪邊是variable

寫成這樣
`print(f'{name} is a {type}.'`

好寫又好懂

**=======**

print搭配len()這個function可以計算string的長度

python也有一些針對string的"method"
好比說在name的屁屁後面加上`.upper()`

```python
name.upper()
```

這樣子在`print(name.upper())`時，本來的Ducky就會被輸出成DUCKY


```python
print(name.lower())
```
則會輸出ducky


```python
name.find("D")
```

則是會找在name中第一次出現D的位置是哪裡～
