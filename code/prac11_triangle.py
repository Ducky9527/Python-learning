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