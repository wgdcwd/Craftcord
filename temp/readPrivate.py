with open('private.txt', 'r') as file:
    lines = file.readlines()

    # 변수에 값 저장
    server_address = lines[0].strip().split('=')[1]
    bot_token = lines[1].strip().split('=')[1]
    channel_id = int(lines[2].strip().split('=')[1])  # channel_id를 정수로 변환

    # 값 확인 (선택사항)
    print(f"Server Address: {server_address}")
    print(f"Bot Token: {bot_token}")
    print(f"Channel ID: {channel_id}")