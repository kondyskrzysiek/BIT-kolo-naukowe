def lista_zakupow_i_produkty_w_sklepie():
    products_need = []
    products_shop = []
    control_empty_line = 0
    with open('data.txt') as file:
        for line in file:
            if line == '\n':
                control_empty_line = 1
            elif control_empty_line == 0:
                for word in line.split(','):
                    products_need.append(word.strip())
            elif control_empty_line == 1:
                for word in line.split(','):
                    products_shop.append(word.strip())
    return set(products_shop),set(products_need)

if __name__ == "__main__":
    products_shop,products_need = lista_zakupow_i_produkty_w_sklepie()
    roznica_set = products_need.difference(products_shop)
    if  roznica_set == set():
        print('ok')
    else:
        print('tych produktów nie ma w tych sklepach : ',roznica_set)