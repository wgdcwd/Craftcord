class Private:
    def __init__(self):
        with open('private.txt', 'r') as file:
            lines = file.readlines()

            # 변수에 값 저장
            self.server_address = lines[0].strip().split('=')[1]
            self.server_port = lines[1].strip().split('=')[1]
            self.rcon_port = lines[2].strip().split('=')[1]
            self.rcon_password = lines[3].strip().split('=')[1]
            self.bot_token = lines[4].strip().split('=')[1]
            self.channel_id = lines[5].strip().split('=')[1]

if __name__=="__main__":
    print("im main")