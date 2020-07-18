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
        if para["status"] == False:
            try:
                para["conn"].send(b"finds")
            except BaseException as e:
                pass



    for para_num in range(len(pars)):
        try:
            response_conn1 = pars[para_num]["conn1"].recv(1024)
            response_conn2 = pars[para_num]["conn2"].recv(1024)
        except ConnectionAbortedError as e:
            try:
                pars[para_num]["conn1"].send(b"disconnect")
            except ConnectionAbortedError as e:
                if para["status"] == True:
                    print("para nacalo")
                    para["status"] = False
                    para["conn"] = pars[para_num]["conn2"]
                    para["addr"] = pars[para_num]["addr2"]

            try:
                pars[para_num]["conn2"].send(b"disconnect")
            except ConnectionAbortedError as e:
                if para["status"] == True:
                    print("para nacalo")
                    para["status"] = False
                    para["conn"] = pars[para_num]["conn1"]
                    para["addr"] = pars[para_num]["addr1"]

        else:
            try:
                pars[para_num]["conn1"].send(response_conn2)
                pars[para_num]["conn2"].send(response_conn1)
            except BaseException as e:
                pass





