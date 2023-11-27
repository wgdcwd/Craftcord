#디스코드와 마인크래프트의 채팅들을 실시간으로 python 터미널에 출력

import discord
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user}로 로그인했습니다!')

    async def on_message(self, message):
        print(f'{message.author}로부터 메시지: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

# 루프 함수 정의
async def follow_minecraft_chat():
    try:
        with open("logs/latest.log", "r", encoding="utf-8") as file:
            # 파일의 끝으로 이동
            file.seek(0, 2)

            while True:
                line = file.readline()
                if not line:
                    # 파일이 갱신되지 않았으면 잠시 대기
                    await asyncio.sleep(1)
                    continue

                # 채팅 메시지인지 확인
                print(line, end='')  # print()에서 추가 개행 방지
    except Exception as e:
        print(f"에러 발생: {e}")

# Discord 봇 실행과 루프 함수를 병렬로 실행
async def main():
    await asyncio.gather(
        client.start('MTE3NDc4MjUzODU3Nzg3NDk0NA.GZKcnw.CwZp8VLTnd0rlRP1WaX2K0Ut6c_0OjQQYm93YU'),
        follow_minecraft_chat()
    )

# 이벤트 루프 시작
asyncio.run(main())