from INTERNET.client import client
from keyboard import is_pressed as key
cli = None
x = 0
y = 0
while True:
    if key("p"):
        x += 5
        print("X")
    if key("l"):
        y += 5
        print("Y")
    if cli == None:
        cli = client(host="localhost", port=9090)
        cli.connect_server()
    else:
        pass
    Y_and_X = cli.send("{0}:{1}".format(x, y))
    Y_and_X = str(Y_and_X)
    Y_and_X = Y_and_X.split(":")
    print(Y_and_X)
