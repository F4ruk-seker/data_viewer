

def load_data_file() -> list:
    with open('kofte.txt','r',encoding='utf-8') as kofte_data:
        return kofte_data.readlines()


def clean_data(dry_data) -> list:
    clean_data = []
    for data in dry_data:
        data = data.replace("<li>",'')
        data = data.replace("\n",'')
        data = data.replace("</li>",'')
        clean_data.append(data)
    return clean_data


def get_test_data():
    dry_data = load_data_file()
    return clean_data(dry_data)

def get_test_data_status():
    data = get_test_data()
    print(f"\nTest Data Durum :{len(data)} adet\n{'*'*50}\nTEST DATA :")
    for _ in data:
        print(_)

get_test_data_status()