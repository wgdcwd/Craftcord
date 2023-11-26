from mctools import RCONClient  # Import the RCONClient

HOST = 'wgdcwd.k'  # Hostname of the Minecraft server
PORT = 25575    # Port number of the RCON server
PASSWORD = "1234"
# Create the RCONClient:

rcon = RCONClient(HOST, port=PORT)

# Login to RCON:

if rcon.login(PASSWORD):

    # Send command to RCON - broadcast message to all players:

    response = rcon.command("list")
    rcon.command("say hi")

    # 결과 출력
    print("서버 응답:", response)