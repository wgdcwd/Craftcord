from mctools import RCONClient
from private import Private

private = Private()

while True :
    try :
        rcon_client = RCONClient(private.vars["server_address"], private.vars["rcon_port"])
        rcon_client.login(private.vars["rcon_password"])
        print(True)
    except :
        print(False)