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


## query 1

def heaviest_pokemon():
    try:
        with connection.cursor() as cursor:
            query = "SELECT *  \
                    FROM pokemon p \
                    WHERE p.weight = (SELECT MAX(p.weight) FROM pokemon p)"
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    except:
        print("Error")

# print(heaviest_pokemon())

## query 2

def find_by_type(type):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT pokemon.name  \
                    FROM pokemon JOIN type_of ON pokemon.id = type_of.pokemon_id \
                    WHERE type_of.type_name = '{type}'"
  
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    except:
        print("Error")

# print(find_by_type('water'))

## query 3

def find_owners(poke_name):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT owned_by.trainer_name  \
                    FROM pokemon JOIN owned_by ON pokemon.id = owned_by.pokemon_id \
                    WHERE pokemon.name = '{poke_name}'"
  
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except:
        print("Error")

# print(find_owners('gengar'))

## query 4

def find_roster(trainer_name):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT pokemon.name  \
                    FROM pokemon JOIN owned_by ON pokemon.id = owned_by.pokemon_id \
                    WHERE owned_by.trainer_name = '{trainer_name}'"
  
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except:
        print("Error")

# print(find_roster('Loga'))

## query 5

def most_owned():
    try:
        with connection.cursor() as cursor:
            query =  f"SELECT pokemon.name   \
                       FROM pokemon JOIN owned_by ON pokemon.id = owned_by.pokemon_id \
                       GROUP BY pokemon.name \
                       HAVING COUNT(pokemon.name) = (SELECT MAX(J.num) max_num   \
                                                     FROM ( SELECT pokemon.name name , COUNT(pokemon.name) num  \
                                                            FROM pokemon JOIN owned_by ON pokemon.id = owned_by.pokemon_id \
                                                            GROUP BY pokemon.name) J)"

            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except:
        print("Error")

# print(most_owned())