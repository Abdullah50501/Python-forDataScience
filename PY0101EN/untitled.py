squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = ['a']
i = 0
while squares[i]=='orange':
    new_squares.append(squares[i])
    if i == (len(squares)-1):
        break
    i = i+1
print(new_squares)
print('hi')