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
        monsterList = get_monster_inventory(user_id, monsterInventoryTable, monsterTable)

        # Setiap monster akan ditunjukkan atribut sesuai urutan array attr
        # Array attr berisi triplet atribut yang ditunjukkan, nama header di monsterList, dan indeks di mosterList
        attr = [["MonsterID", "monster_id", -1], ["Name", "type", -1], ["Level", "level", -1],
                ["HP", "hp", -1], ["ATK", "atk_power", -1], ["DEF", "def_power", -1]]
        for i in range(len(attr)):
            header = attr[i][1]
            for j in range(len(monsterList[0])):
                if header==monsterList[0][j]:
                    attr[i][2] = j
        
        # Tunjukkan data setiap monster
        for i in range(1, len(monsterList)):
            print('')
            print('Monster ke-{}'.format(i))

            monster = monsterList[i]
            for elem in attr:
                print('{:<10}'.format(elem[0]), end=': ')
                print('{}'.format(monster[elem[2]]))

    elif opsi=="2" or opsi=="Item":
        item = get_item_inventory(user_id, itemInventoryTable)
        print(item)

    else:
        pass


def get_monster_inventory(user_id, monsterInventoryTable, monsterTable):
    # Filter monster berdasarkan kepemilikan user
    # Jika tidak memiliki monster, akan dikembalikan array yang hanya berisi judul (memiliki 1 baris)
    # Note: user Agent seharusnya sudah memiliki minimal satu monster
    table = []      
    table.append(monsterInventoryTable[0])
    for i in range(1, len(monsterInventoryTable)):
        monster = monsterInventoryTable[i]
        if int(monster[0])==user_id:
            table.append(monster)

    # Tambahkan data sesuai database monster(type, hp, atk_power, def_power)
    # Urutan penambahan atribut sesuai array attr
    # Array attr berisi pasangan atribut dan indeks di monsterTable
    attr = [["type", -1], ["hp", -1], ["atk_power", -1], ["def_power", -1]]
    for i in range(len(attr)):
        header = attr[i][0]
        for j in range(len(monsterTable[0])):
            if header==monsterTable[0][j]:
                attr[i][1] = j

    for elem in attr:
        table[0].append(elem[0])

    # Search index kolom monster id
    inventoryColIndex = -1
    for i in range(len(table[0])):
        if table[0][i]=="monster_id":
            inventoryColIndex = i
    
    # Search monster dengan monster id tertentu
    for i in range(1, len(table)):
        monsterID = table[i][inventoryColIndex]

        for j in range(1, len(monsterTable)):   # Search monster di database dengan id yang sama
            if monsterTable[j][0]==monsterID:   # Note: ID ada pada kolom indeks 0 pada database
                # Tambah atribut
                for elem in attr:
                    table[i].append(monsterTable[j][elem[1]])

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