def names_processing(raw_names):
    new_list_names = []
    for raw_line in raw_names:
        name, surname = raw_line.split()
        name = name.capitalize()
        surname = surname.capitalize()
        new_list_names.append(name + " " + surname)

    return new_list_names


if __name__ == '__main__':
    names = []
    while True:
        name = input('> ')
        if not name:
            break
        else:
            names.append(name)
    new_names = names_processing(names)

    for name in new_names:
        print(name)