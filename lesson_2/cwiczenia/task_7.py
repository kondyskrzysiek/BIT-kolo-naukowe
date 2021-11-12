def color_int(c_str):
    r, g, b = c_str.split()
    return int(r), int(g), int(b)


def load_colors():
    color_dict = {}
    with open('colors.txt') as file:
        for line in file:
            c_name, c_string_n = line.split(':')
            r, g, b = color_int(c_string_n)
            color_dict[(r, g, b)] = c_name
    return color_dict

# def search_early_color(r,g,b,color_dict):
#     i = 0
#     rgb = [b,g,r]
#     list_search_color = []
#     while not list_search_color:
#         i +=1
#         for index, n in enumerate(rgb):
#
#
#     return list_search_color




if __name__ == '__main__':
    color_dict = load_colors()
    print(color_dict)
    while True:
        try:
            user_number = input('> ')
            r, g, b = color_int(user_number)
            if (r, g, b) in color_dict:
                print('Color name: ', color_dict[(r, g, b)])
            else:
                # color_found_list = search_early_color(r,g,b,color_dict)
                # for number_color in color_found_list:
                #     print('Color not found, did you mean: ',number_color , ' ',color_dict[number_color])
                print('Color not found')
            break
        except:
            print('błąd wprowadź liczby jeszce raz , pamiętaj by było to 3 liczby')
