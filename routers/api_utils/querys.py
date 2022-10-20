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