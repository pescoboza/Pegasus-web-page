
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
    "first_name": {
        "min": 1,
        "max": 30,
        "message": None
    },
    "last_name": {
        "min": 1,
        "max": 30,
        "message": None
    },
    "email": {
        "min": 5,
        "max": 254,
        "message": None
    },
    "location":{
        "min":0,
        "max":64
    },
    "about_me":{
        "min":0,
        "max":64
    }
    
}