"""Menunjukkan inventory suatu user

    Fungsi
        get_monster_inventory(user_id, monsterInventoryTable)  -> [[str]] :
            mengembalikan list monster yang ada di inventory user
        get_item_inventory(user_id, itemInventoryTable) -> [[str]] :
            mengembalikan list item yang ada di inventory user

    Prosedur
        show_inventory(user_id, userTable, monsterInventoryTable, itemInventoryTable) -> [[str]] :
            menunjukkan inventory user
"""

import csvparse

# Loading data sementara. Akses file eksternal hanya pada proses load dan save (F14 dan F15)
USER_ID = 2
FILE_PATH = "../data/"
userData = None
monsterData = None
itemData = None
with open(FILE_PATH + "user.csv") as userFile:
    userData = csvparse.parse_csv(userFile)
with open(FILE_PATH + "monster_inventory.csv") as monsterFile:
    monsterData = csvparse.parse_csv(monsterFile)
with open(FILE_PATH + "item_inventory.csv") as itemFile:
    itemData = csvparse.parse_csv(itemFile)

def show_inventory(user_id=USER_ID, userTable=userData, monsterInventoryTable=monsterData,
                   itemInventoryTable=itemData):

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
    print("1. Monster")
    print("2. Item")
    opsi = input()
    if opsi=="1" or "Monster":
        table = get_monster_inventory(user_id, monsterInventoryTable)
        print(table)

    elif opsi=="2" or "Item":
        item = get_item_inventory(user_id, itemInventoryTable)
        print(item)

    else:
        pass


def get_monster_inventory(user_id, monsterInventoryTable):
    table = []      
    table.append(monsterInventoryTable[0])

    # Filter monster berdasarkan kepemilikan user
    # Jika tidak memiliki monster, akan dikembalikan array yang hanya berisi judul (memiliki 1 baris)
    # Note: user Agent seharusnya sudah memiliki minimal satu monster
    for i in range(1, len(monsterInventoryTable)):
        monster = monsterInventoryTable[i]
        if int(monster[0])==user_id:
            table.append(monster)

    return table

def get_item_inventory(user_id, itemInventoryTable):
    return


# ==================== Test ====================

show_inventory()

