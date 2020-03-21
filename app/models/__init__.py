
# email regex: 	^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$

FIELD_LENGTHS = {
    "username": {
        "min": 8,
        "max": 16,
        "message": None
    },
    "password": {
        "min": 8,
        "max": 30,
        "message": None
    },
    "firstName": {
        "min": 1,
        "max": 30,
        "message": None
    },
    "lastName": {
        "min": 1,
        "max": 30,
        "message": None
    },
    "email": {
        "min": 5,
        "max": 254,
        "message": None
    },
}