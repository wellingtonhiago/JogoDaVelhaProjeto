s, sym, other_sym = '_' * 9, 'X', 'O'

while True:
    print((l := 9 * "-") + (3 * "\n| {} {} {} |").format(*(s.replace('_', ' '))) + "\n" + l)
    lines = [s[3 * i:3 * (i + 1)] for i in range(3)] + [s[i::3] for i in range(3)] + [s[0::4]] + [s[2:8:2]]
    X_wins, O_wins = (3 * 'X') in lines, (3 * 'O') in lines
    none_wins, both_wins = not (X_wins or O_wins), X_wins and O_wins
    nX, nO = s.count('X'), s.count('O')
    wrong_num = abs(nX - nO) > 1
    print('Impossible' if both_wins or wrong_num else 'Draw' if none_wins and '_' not in s else
          'X wins' if X_wins else 'O wins' if O_wins else "", end="")
    if X_wins or O_wins or wrong_num or '_' not in s: break
    i = -1

    while True:
        if len(a := input("Enter the coordinates: ").split()) != 2 or any([not e.isnumeric() for e in a]):
            print("You should enter numbers!")
        elif any([int(e) not in range(1, 4) for e in a]):
            print("Coordinates should be from 1 to 3!")
        elif s[i := 3 * (int(a[0]) - 1) + int(a[1]) - 1] == '_':
            break
        print("This cell is occupied! Choose another one!")
    s = s[:i] + sym + s[i+1:]
    sym, other_sym = other_sym, sym


