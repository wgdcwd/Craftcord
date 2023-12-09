#서버설정시 실행되는 코드.
import os
from private import Private


def auto_setting() :
    private = Private()
    
    private.vars["bot_token"] = input("디스코드 봇 토큰을 입력하세요 : ")

    private.vars["channel_id"] = input("사용할 디스코드 채널 아이디를 입력하세요 : ")

    i = input("서버주소를 기본값(localhost)으로 하시겠습니까?(Y/N)")
    if i == "N" or i == "n" :
        private.vars["server_address"] = input("사용자의 서버주소를 입력해주세요 : ")
    else :
        private.vars["server_address"] = "localhost"

    i = input("서버포트를 기본값(25565)으로 하시겠습니까?(Y/N)")
    if i == "N" or i == "n" :
        private.vars["server_port"] = input("사용할 서버포트를 입력해주세요 : ")
    else :
        private.vars["server_port"] = "25565"
    
    i = input("rcon포트를 기본값(25575)으로 하시겠습니까?(Y/N)")
    if i == "N" or i == "n" :
        private.vars["rcon_port"] = input("사용할 rcon포트를 입력해주세요 : ")
    else :
        private.vars["rcon_port"] = "25575"
    
    i = input("rcon암호를 기본값(1234)으로 하시겠습니까?(Y/N)")
    if i == "N" or i == "n" :
        private.vars["rcon_password"] = input("사용할 rcon암호를 입력해주세요 : ")
    else :
        private.vars["rcon_password"] = "1234"

    private.change_settings()
    print("성공적으로 설정되었습니다.")
    os.system("pause")
    

def individual_setting() :
    private = Private()
    while True :
        private.change_settings()
        os.system("cls")
        print("1.디스코드 봇 토큰")
        print("2.디스코드 채널 아이디")
        print("3.서버주소")
        print("4.서버포트")
        print("5.rcon포트")
        print("6.rcon암호")
        print("7.뒤로가기")
        n = input("원하는 번호를 입력하시오 : ")
        os.system("cls")
    
        if n == "1" :
            private.vars["bot_token"] = input("디스코드 봇 토큰을 입력하세요 : ")
        elif n == "2" :
            private.vars["channel_id"] = input("사용할 디스코드 채널 아이디를 입력하세요 : ")
        elif n == "3" :
            private.vars["server_address"] = input("사용자의 서버주소를 입력하세요 : ")
        elif n == "4" :
            private.vars["server_port"] = input("사용할 서버포트를 입력하세요 : ")
        elif n == "5" :
            private.vars["rcon_port"] = input("사용할 rcon포트를 입력하세요 : ")
        elif n == "6" :
            private.vars["rcon_password"] = input("사용할 rcon암호를 입력하세요 : ")
        elif n == "7" :
            break
        else :
            print("잘못된 번호입니다.")
            os.system("pause")


while True :
    os.system("cls")
    print("1.서버자동설정")
    print("2.서버수동설정")
    print("3.서버설정확인")
    print("4.서버설정초기화")
    print("5.뒤로가기")
    n = input("원하는 번호를 입력하시오 : ")
    os.system("cls")

    if n == "1" :
        auto_setting()
    elif n == "2" :
        individual_setting()
    elif n == "3" :
        p = Private()
        p.print_settings()
        os.system("pause")
    elif n == "4" :
        private = Private()
        private.set_private_default()
        print("설정을 기본값으로 초기화했습니다. 기본값 : ")
        private.print_settings()
        os.system("pause")
    elif n == "5" :
        break
    else :
        print("잘못된 번호입니다.")
        os.system("pause")