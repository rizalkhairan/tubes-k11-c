"""Menunjukkan inventory suatu user

    Fungsi
        get_monster_inventory(user_id, monsterInventoryTable, monsterTable)  -> [[str]] :
            mengembalikan list monster yang ada di inventory user
        get_item_inventory(user_id, itemInventoryTable) -> [[str]] :
            mengembalikan list item yang ada di inventory user

    Prosedur
        show_inventory(user_id, userTable, monsterInventoryTable, monsterTable, itemInventoryTable) -> [[str]] :
            menunjukkan inventory user
"""

import csvparse


def show_inventory(user_id, userTable, monsterInventoryTable, monsterTable, itemInventoryTable):

    print("==================== INVENTORY ====================")
    print("User ID : " + str(user_id))

    # Menunjukkan jumlah coin yang dimiliki user
    for i in range(1, len(userTable)):
        user = userTable[i]
        if int(user[0])==user_id:   # Cek user id yang sesuai
            coins = int(user[4])
            print("O.W.C.A Coin : " + str(coins))
    
    # Opsi untuk menunjukkan monster atau item
    print("Tunjukkan:")
    print("1. Monster      2. Item ")
    opsi = input()
    if opsi=="1" or opsi=="Monster":
        monsterTable = get_monster_inventory(user_id, monsterInventoryTable, monsterTable)
        for monster in monsterTable:
            print('|', end='')
            for field in monster[1:]:
                print("{:^16}".format(field), end='')
                print('|', end='')
            print('')

    elif opsi=="2" or opsi=="Item":
        item = get_item_inventory(user_id, itemInventoryTable)
        print(item)

    else:
        pass


def get_monster_inventory(user_id, monsterInventoryTable, monsterTable):
    table = []      
    table.append(monsterInventoryTable[0])

    # Filter monster berdasarkan kepemilikan user
    # Jika tidak memiliki monster, akan dikembalikan array yang hanya berisi judul (memiliki 1 baris)
    # Note: user Agent seharusnya sudah memiliki minimal satu monster
    for i in range(1, len(monsterInventoryTable)):
        monster = monsterInventoryTable[i]
        if int(monster[0])==user_id:
            table.append(monster)

    # Tambahkan data sesuai database monster(type, hp, atk_power, def_power)
    table[0].append("type")
    table[0].append("hp")
    table[0].append("atk_power")
    table[0].append("def_power")

    # Search index kolom monster id
    inventoryIndex = -1
    for i in range(len(table[0])):
        if table[0][i]=="monster_id":
            inventoryColIndex = i
    
    # Search monster dengan monster id tertentu
    for i in range(1, len(table)):
        monsterID = table[i][inventoryColIndex]
        for j in range(1, len(monsterTable)):   # Search monster di database dengan id yang sama
            if monsterTable[j][0]==monsterID:   # ID ada pada kolom indeks 0 pada database
                table[i].append(monsterTable[j][1])
                table[i].append(monsterTable[j][4])
                table[i].append(monsterTable[j][2])
                table[i].append(monsterTable[j][3])

    return table

def get_item_inventory(user_id, itemInventoryTable):
    return


# ==================== Test ====================

if __name__ == "__main__":
    # Loading data sementara. Akses file eksternal hanya pada proses load dan save (F14 dan F15)
    USER_ID = 2
    FILE_PATH = "../data/"
    with open(FILE_PATH + "user.csv") as userFile:
        userData = csvparse.parse_csv(userFile)
    with open(FILE_PATH + "monster_inventory.csv") as monsterFile:
        monsterInventoryData = csvparse.parse_csv(monsterFile)
    with open(FILE_PATH + "monster.csv") as monsterDatabaseFile:
        monsterData = csvparse.parse_csv(monsterDatabaseFile)
    with open(FILE_PATH + "item_inventory.csv") as itemFile:
        itemData = csvparse.parse_csv(itemFile)
    
    show_inventory(USER_ID, userData, monsterInventoryData, monsterData, itemData)