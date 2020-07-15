import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.settimeout(0.1)
sock.listen(6)

para = {
        "status":True,
        "conn": None,
        "addr": None}
pars = []
while True:
    try:
        conn, addr = sock.accept()
        if para["status"] == True:
            print("para nacalo")
            para["status"] = False
            para["conn"] = conn
            para["addr"] = addr
        elif para["status"] == False:
            print("para create")
            para["status"] = True
            pars.append({"conn1":para["conn"],
                         "addr1":para["addr"],
                         "conn2":conn,
                         "addr2":addr})
    except Exception as e:
        pass
    for para_one in pars:
        try:
            response_conn1 = para_one["conn1"].recv(1024)
            response_conn2 = para_one["conn2"].recv(1024)
            para_one["conn1"].send(response_conn2)
            para_one["conn2"].send(response_conn1)
        except ConnectionAbortedError as e:
            pass




