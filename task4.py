import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    new_dict = []
    new_rows = []
    with open(filename, 'r') as f:
        a = f.readlines()
        fields = a[0].rstrip(new_line).split(delimiter)
        for i in a[1:]:
            new_rows.append(i.rstrip().split(delimiter))
        for elements in new_rows:
            b = {k: v for k, v in zip(fields, elements)}
            new_dict.append(b)

    return new_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
