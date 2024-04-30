"""Melakukan parsing terhadap file csv dan mengembalikan dalam bentuk array

    Fungsi
        parse_csv(file) -> [[str]]  : memproses file csv dalam bentuk array dua dimensi
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

==================== Test ====================

# tab = open("../data/user.csv")
# print(parse_csv(tab))