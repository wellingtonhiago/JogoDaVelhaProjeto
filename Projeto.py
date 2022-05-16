cells = input("Enter cells: ")
cells_permitidas = ["O", "X", "_"]


line1 = cells[0:3].split()
line2 = cells[3:6].split()
line3 = cells[6:9].split()

line1 = " ".join(line1)
line2 = " ".join(line2)
line3 = " ".join(line3)

print(f'''---------
| {" ".join(line1)} |
| {" ".join(line2)} |
| {" ".join(line3)} |
---------''')



