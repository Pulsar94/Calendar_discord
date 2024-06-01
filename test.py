import json


def test():
    try:
        with open("test", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("La configuration des URL va commencer.")
        CONFIG = {'url': [0], 'prof': ['refgerfre']}
        with open("config.json", "w") as f:
            json.dump(CONFIG, f)


def test2():
    CONFIG = {'url': ['54546465465456', 'sfdgdsfgdfsgsd'], 'prof': '1456561615156'}

    with open("config.json", "r") as old_file:
        json_file = json.load(old_file)

    for key in CONFIG.keys():
        if key in json_file:
            print(type(CONFIG[key]))
            if isinstance(CONFIG[key], list):
                for element in CONFIG[key]:
                    json_file[key].append(element)
            else:
                json_file[key].append(CONFIG[key])

    with open("config.json", "w") as new_file:
        json.dump(json_file, new_file)

test()
test2()