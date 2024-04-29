"""Memberikan list semua string yang dipisahkan separator

    Fungsi
        split(string, sep) -> [str] : memberikan substring yang dibatasi separator

"""

def split(string, sep=' '):
    substring = []

    placehold = ''
    for i in range(len(string)):
        if string[i]==sep:
            substring.append(placehold)
            placehold = ''
        else:
            placehold += placehold + string[i]
    substring.append(placehold)

    return substring