"""Menunjukkan inventory suatu user

    Fungsi
        get_monster_inventory(user_id)  -> [[str]]  : mengembalikan list monster yang ada di inventory
        get_item_inventory(user_id) -> [[str]]      : mengembalikan list item yang ada di inventory
        get_inventory(user_id, file_path) -> [[str]]    : menunjukkan inventory 
"""

import csvparse

# Data sementara
USER_ID = 2
FILE_PATH = "../data/"

def get_inventory(user_id=USER_ID, file_path=FILE_PATH):
    print("==================== INVENTORY ====================")
    print("User ID : " + str(user_id))

    # Menunjukkan jumlah coin yang dimiliki user
    with open(file_path+"user.csv") as userFile:
        userTable = csvparse.parse_csv(userFile)
        for i in range(1,len(userTable)):
            user = userTable[i]
            if int(user[0])==user_id:
                coins = int(user[4])
                print("O.W.C.A Coin : " + str(coins))
    
    # Opsi untuk menunjukkan monster atau item
    print("Tunjukkan:")
    print("1. Monster")
    print("2. Item")
    opsi = input()
    if opsi=="1" or "Monster":
        get_monster_inventory(user_id)
    elif opsi=="2" or "Item":
        get_item_inventory(user_id)
    else:
        pass


def get_monster_inventory():
    return

def get_item_inventory():
    return


# ==================== Test ====================

get_inventory()

