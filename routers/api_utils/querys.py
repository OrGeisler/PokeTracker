sql_insert_type =    """
                           INSERT IGNORE into type (name) 
                           values (%s)
                           """

sql_get_pokemon_id =    """
                        SELECT p.id
                        FROM pokemon p
                        WHERE p.name = %s
                        """

sql_insert_type_of = """
                            INSERT IGNORE into type_of (type_name,pokemon_id)
                            values (%s , %s)
                            """


sql_get_pokemon_by_name =   """
                            SELECT *
                            FROM pokemon p
                            WHERE p.name = %s
                            """

sql_get_pokemon_type_by_id = """
                                SELECT t.type_name
                                FROM type_of t
                                WHERE t.pokemon_id = %s
                                """
sql_get_all_pokemons = """
                        SELECT *
                        FROM pokemon
                        """
sql_get_pokemon_by_type = """
                            SELECT p.id , p.name , p.height, p.weight
                            FROM pokemon p JOIN type_of t ON p.id = t.pokemon_id
                            WHERE t.type_name = %s
                            """

sql_get_pokemon_by_trainer = """
                            SELECT p.id , p.name , p.height, p.weight
                            FROM pokemon p JOIN owned_by o ON p.id = o.pokemon_id
                            WHERE o.trainer_name = %s
                            """

sql_get_pokemon_by_trainer_and_type = """
                                        SELECT p.id , p.name , p.height, p.weight
                                        FROM pokemon p JOIN owned_by o ON p.id = o.pokemon_id JOIN type_of t ON p.id = t.pokemon_id
                                        WHERE o.trainer_name = %s
                                        AND t.type_name = %s
                                        """
sql_get_trainers_of_pokemon = """
                                SELECT t.name , t.town
                                FROM trainer t JOIN owned_by o ON t.name = o.trainer_name
                                WHERE o.pokemon_id = %s
                                """
sql_insert_trainer = """
                        INSERT IGNORE into trainer (name,town) 
                        values (%s,%s)
                        """
sql_insert_pokemon_to_trainer = """
                                INSERT IGNORE into owned_by (trainer_name,pokemon_id) 
                                values (%s,%s)
                                """

sql_delete_pokemon_of_trainer = """
                                DELETE FROM owned_by 
                                WHERE trainer_name = %s
                                AND pokemon_id = %s
                                """

