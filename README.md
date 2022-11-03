# PokeTracker

## Overview

PokeTracker is an back - end project that combains: Server (FastApi), SQL database (MySql) and External API.

PokeTracker allows the user to receive information and perform actions on pokemons.

## Run:

python ./server.py

## Technologies
<img align="left" alt="Pyton" width="50px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />
<img align="left" alt="Mysql" width="70px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/mysql/mysql.png" />
<br />
<br />

## Endpoints

Request:

```
GET http://localhost:8000/pokemons?trainer_name=Diantha
```

Response:

```
[
    {
        "id": 1,
        "name": "bulbasaur",
        "height": 7,
        "weight": 69,
        "type": [
            "grass",
            "poison"
        ],
        "ownedBy": [
            {
                "name": "Diantha",
                "town": "Little Italy"
            },
            {
                "name": "Roxie",
                "town": "Little Italy"
            },
            {
                "name": "Tierno",
                "town": "Cerulean City"
            }
        ]
    },
    ....
]
```

Request:

```
GET http://localhost:8000/pokemons?pokemon_type=grass
```

Response:

```
[
    {
        "id": 1,
        "name": "bulbasaur",
        "height": 7,
        "weight": 69,
        "type": [
            "grass",
            "poison"
        ],
        "ownedBy": [
            {
                "name": "Diantha",
                "town": "Little Italy"
            },
            {
                "name": "Roxie",
                "town": "Little Italy"
            },
            {
                "name": "Tierno",
                "town": "Cerulean City"
            }
        ]
    },
    ....
]
```

Request:

```
GET http://localhost:8000/trainers/bulbasaur
```

Response:

```
[
    {
        "name": "Archie",
        "town": "Little Italy"
    },
    {
        "name": "Ash",
        "town": "Little Italy"
    },
    {
        "name": "Bane",
        "town": "Cerulean City"
    },
    {
        "name": "Diantha",
        "town": "Cerulean City"
    }
    ...
]
```

Request:

```
POST http://localhost:8000/trainers?trainer_name=Or&trainer_town=tel-aviv
```

Response:

```
{
  "success": True,
  "payload": {
              Added Or to DB'
          }
}
```

Request:

```
DELETE http://localhost:8000/pokemons/{pokemon_name}/trainers/{trainer_name}

```

Response:

```

No Content

```

Request:

```
PATCH http://localhost:8000/evolve?pokemon_name=bulbasaur&trainer_name=Archie

```

Response:

```
{
  "success": True,
  "payload": {
              Envolved Archies bulbasaur to ivysaur'
          }
}
```

AND MORE....
