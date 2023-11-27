import time

# Minecraft 서버의 logs/latest.log 파일 경로
log_file_path = "logs/latest.log"

def follow_minecraft_chat(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            # 파일의 끝으로 이동
            file.seek(0, 2)

            while True:
                line = file.readline()
                if not line:
                    # 파일이 갱신되지 않았으면 잠시 대기
                    time.sleep(1)
                    continue

                # 채팅 메시지인지 확인
                print(line)
    except Exception as e:
        print(f"Error: {e}")

# Minecraft 채팅을 실시간으로 받아오기
follow_minecraft_chat(log_file_path)