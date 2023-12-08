#마인크래프트, 디스코드에서 입력된 메세지들을 알맞게 가공하는 코드
import re
def convert_minecraft_msg(msg) :
    # 로그 형식에 맞게 정규표현식을 사용하여 각 부분을 추출
    match = re.match(r'\[(.*?)\] \[(.*?)\]: (.*)', msg)
    
    if match:
        time, thread_type, content = match.groups()
        
        # 쓰레드의 종류에 따라 처리
        if thread_type.startswith('Server'): #서버 쓰레드
            if "Stopping the server" in content : #서버가 종료됐을시
                exit(0)
            return None
            #return content
        elif thread_type.startswith('Async Chat'): #채팅 쓰레드
            return(content)
        else:
            # 다른 쓰레드에 대한 처리를 추가할 수 있음
            return None
    else:
        # 매치되지 않는 경우에 대한 처리
        return None

def convert_discord_msg(msg) :
    #디스코드 메세지는 처리과정이 쉽기때문에 쓰이지않음.
    pass