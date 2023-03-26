import json


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

import random
pk_count = 2
def create_fake_office(name):
    global pk_count
    pk_count += 1


    return {"model": "product_operation.office", "pk": pk_count,
            "fields": {"name": name,
                       "performance": pk_count}
            }
def create_fake_office_data():
    global pk_count
    return {"model": "product_operation.performancemetric", "pk": pk_count,
               "fields": {"sincere_count": random.randint(200,3000),
                          "reputable_count": random.randint(200,3000),
                          "powerful_count": random.randint(200,3000),
                          "competence_count": random.randint(200,3000),
                          "excitement_count": random.randint(200,3000)}
               }

subes = get_test_data()

result = []
for sube in subes:
    result.append(create_fake_office(sube))
    result.append(create_fake_office_data())

with open('fake_office.json','w+',encoding='utf-8') as fake_data:
    fake_data.write(json.dumps(result))

