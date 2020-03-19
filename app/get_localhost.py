def get_localhost():
    uri = str()
    with open("../db-uri.txt", 'r') as f:
        uri = f.read()
    return uri


print(get_localhost())
