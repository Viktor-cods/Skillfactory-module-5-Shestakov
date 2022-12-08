#Приветствие и правила игры:
def head_piece():
    print("*****************")
    print("Добро пожаловать в игру")
    print("Крестики-Нолики")
    print("-----------------")
    print("Формат игры:")
    print("Вводятся координаты ячейки в таблице")
    print("Х- это строка,а У- это столбец")
    print("#################")


#Создаем поле:
def pole():
    print(f"  0 1 2")
    print("  --------------- ")
    spis = [[""] * 3 for i in range(3)]
    for i in range(3):
        print(f"{i} {spis[i][0]} {spis[i][1]} {spis[i][2]}")


#Данные от игроков:
def dan():
    while True:
      hod = input("         Ваш ход: ").split()

      if len(hod) != 2:
          print(" Введите 2 координаты! ")
          continue

      x,y=hod


      if not (x.isdigit()) or not (y.isdigit()):
          print(" Введите числа! ")
          continue

      x,y=int(x),int(y)

      if 0 > x or x < 2 and 0 > y or y > 2:
          print("Вы вышли за пределы игрового поля!")
          continue

      if spis[x][y] != " ":
          print("Клетка занята!")
          continue

      return x,y


# Выигрышные комбинации:
def win():
    wincomb=(((0,0),(0,1),(0,2),
              (1,0),(1,1),(1,2),
              (2,0),(2,1),(2,2),
              (0,0),(0,1),(0,2),
              (1,0),(1,1),(1,2),
              (2,2),(2,1),(2,0),
              (0,0),(1,1),(2,2),
              (0,2),(1,1),(2,0)))
    for i in wincomb:
        chi=[]
        for c in i:
            chi.append(spis[c[0]][c[1]])
        if chi==["X","X","X"]:
            print("Выиграл X!!!")
            return True
        if chi==["0","0","0"]:
            print("Выиграл 0!!!")
            return True
    return False

head_piece()
spis=[[" "] * 3 for i in range(3)]
defcho = 0
while True:
    defcho += 1
    pole()
    if defcho % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = dan()

    if defcho % 2 == 1:
        spis[x][y] = "X"
    else:
        spis[x][y] = "0"

    if win():
        break

    if defcho == 9:
        print("Ничья!!!")
        break
