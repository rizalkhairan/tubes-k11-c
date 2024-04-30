"""Melakukan parsing terhadap file csv dan mengembalikan dalam bentuk array

    Fungsi
        parse_csv(file) -> [[str]]  : memproses file csv dalam bentuk array dua dimensi
    
    Prosedur
        write_csv(table, file)      : menulis table menjadi file csv
"""

from split import split

def parse_csv(file):
    table = []
    lines = file.read()

    placehold = ''
    for char in lines:
        if char == '\n':
            table.append(split(placehold))
            placehold = ''
        else:
            placehold += char

    return table

def write_csv(table, file):
    for row in table:
        line = ''
        for column in row:
            line += column
            line += ';'
        line = line[:-1] + '\n'

        file.write(line)
            

# ==================== Test ====================

# with open("../data/user.csv") as file:
#   print(parse_csv(file))