#  Etapa 3/5

print((l := 9 * "-") + (3 * "\n| {} {} {} |").format(*(s := input("Enter cells: "))) + "\n" + l)

lines = [s[3 * i:3 * (i + 1)] for i in range(3)] + [s[i::3] for i in range(3)] + [s[0::4]] + [s[2:8:2]]
X_wins, O_wins = (3 * 'X') in lines, (3 * 'O') in lines
none_wins, both_wins = not (X_wins or O_wins), X_wins and O_wins
nX, nO = s.count('X'), s.count('O')
wrong_num = abs(nX - nO) > 1

print('Impossible' if both_wins or wrong_num else
      'Game not finished' if none_wins and '_' in s else
      'Draw' if none_wins and '_' not in s else
      'X wins' if X_wins else 'O wins' if O_wins else 'Unknown state!'
      )
