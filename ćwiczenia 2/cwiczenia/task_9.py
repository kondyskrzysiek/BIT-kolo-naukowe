import json

def create_json_for_csv():
    result = []
    with open('task9.csv') as file:
        header = file.readline().split(',')
        key_names = []

        for key_name in header:
            key_names.append(key_name.strip())
        key_len = len(key_names)

        for line in file:
            line_dict = {}
            line_vals = line.split(',')
            for i in range(key_len):
                key_name = key_names[i]
                val = line_vals[i].strip()
                line_dict[key_name] = val
            result.append(line_dict)

    with open('convert.json','w') as file:
        json.dump(result,file,indent=2)

if __name__ == '__main__':
    create_json_for_csv()