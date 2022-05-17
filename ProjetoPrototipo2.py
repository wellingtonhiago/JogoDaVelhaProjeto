# Etapa 4/5
print((l := 9 * "-") + (3 * "\n| {} {} {} |").format(*(s := input("Enter cells: "))) + "\n" + l)
i = -1
while True:
    if len(a := input("Enter the coordinates: ").split()) != 2 or any([not e.isnumeric() for e in a]):
        print("You should enter numbers!")
    elif any([int(e) not in range(1, 4) for e in a]):
        print("Coordinates should be from 1 to 3!")
    elif s[i := 3 * (int(a[0]) - 1) + int(a[1]) - 1] == '_':
        break
    print("This cell is occupied! Choose another one!")
print((l := 9 * "-") + (3 * "\n| {} {} {} |").format(*(s[:i] + 'X' + s[i+1:])) + "\n" + l)