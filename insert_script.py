import pymysql
import json
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

def pokemon_insert():
    file = open('poke_data.json')
    data = json.load(file)
    for pokemon in data:
        try:
            with connection.cursor() as cursor:
                query = f'INSERT into pokemon (name,height,weight) values ("{pokemon["name"]}","{pokemon["height"]}",{pokemon["weight"]})'
                cursor.execute(query)
                connection.commit()
        except:
            print("Error")
    file.close()

# pokemon_insert()

def trainer_insert():
    trainer_list = []
    file = open('poke_data.json')
    data = json.load(file)
    for pokemon in data:
        for trainer in pokemon["ownedBy"]:
            if trainer["name"] not in trainer_list:
                try:
                    with connection.cursor() as cursor:
                        query = f'INSERT into trainer (name,town) values ("{trainer["name"]}","{trainer["town"]}")'
                        cursor.execute(query)
                        connection.commit()
                except:
                    print("Error")
                trainer_list.append(trainer["name"])
    file.close()

# trainer_insert()


def owned_by_insert():
    file = open('poke_data.json')
    data = json.load(file)
    for pokemon in data:
        for trainer in pokemon["ownedBy"]:
            try:
                with connection.cursor() as cursor:
                    query = f'INSERT into owned_by (trainer_name,pokemon_id) values ("{trainer["name"]}","{pokemon["id"]}")'
                    cursor.execute(query)
                    connection.commit()
            except:
                print("Error")
    file.close()

# owned_by_insert()

def type_insert():
    type_list = []
    file = open('poke_data.json')
    data = json.load(file)
    for pokemon in data:
        if pokemon["type"] not in type_list:
            try:
                with connection.cursor() as cursor:
                    query = f'INSERT into type (name) values ("{pokemon["type"]}")'
                    cursor.execute(query)
                    connection.commit()
            except:
                print("Error")
            type_list.append(pokemon["type"])
    file.close()

# type_insert()

def type_of_insert():
    file = open('poke_data.json')
    data = json.load(file)
    for pokemon in data:
        try:
            with connection.cursor() as cursor:
                query = f'INSERT into type_of (type_name,pokemon_id) values ("{pokemon["type"]}",{pokemon["id"]})'
                cursor.execute(query)
                connection.commit()
        except:
            print("Error")
    file.close()

# type_of_insert()