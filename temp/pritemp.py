class Private:
    def __init__(self):
        with open('private.txt', 'r') as file:
            lines = file.readlines()

            # 변수에 값 저장
            self.server_address = lines[0].strip().split('=')[1]
            self.bot_token = lines[1].strip().split('=')[1]
            self.channel_id = int(lines[2].strip().split('=')[1])  # channel_id를 정수로 변환

    

