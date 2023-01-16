
shopdict = {
    "pizza": 6.99,
    "shake": 4.99,
    "skittles": 0.99,
    "special ayylmao weed": 68.99
}

def snackshop():
    for key in shopdict:
        print(key, str(shopdict[key]),sep=" ---- ", end="\n  ")
    return
    

print(snackshop())