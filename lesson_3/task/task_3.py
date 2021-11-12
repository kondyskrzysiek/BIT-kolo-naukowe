import os


def read_text_files(dir_path, textall):
    texts = []
    for filename in os.listdir(dir_path):
        if filename.endswith('.txt'):
            filepath = os.path.join(dir_path, filename)
            with open(filepath) as file:
                text = file.read().strip()
                if not text == '':
                    texts.append(text)

    filepath = os.path.join(dir_path, textall)
    with open(filepath, 'w') as file:
        for line in texts:
            file.write(line + '\n')


if __name__ == '__main__':
    dir_path = input('dir path :> ')
    textall = input('name file where save :> ')
    # dir_path = ''
    read_text_files(dir_path, textall)
