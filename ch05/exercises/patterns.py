def star_pyramid():
    rows = int(input(print("Enter the number of rows: ")))
    for i in range(1, rows+1):
        print('*' * i)


def rstar_pyramid():
    rows = int(input("Enter the number of rows: "))
    for i in range(rows, 0, -1):
        print('*' * i)
