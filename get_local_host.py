def get_local_host():
    uri = str()
    try:
        with open("db-uri.txt", 'r') as f:
            uri = f.read()
    except:
        uri = "bogus//bogus@bogus:1234"
    return uri
