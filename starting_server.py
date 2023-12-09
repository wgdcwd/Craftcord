#서버실행시 실행되는 코드.
import os
import create_bat
from private import Private

def check_eula(): #eula.txt를 검사하는 함수. eula=true면 0 false나 txt가 존재하지않으면 1,2리턴.
    # eula.txt 파일 경로
    eula_path = "..\\eula.txt"
    
    # eula.txt 파일 확인
    if os.path.exists(eula_path):
        with open(eula_path, 'r') as file:
            lines = file.readlines()
            for line in lines :
                line = line.strip().split("=")
                if line[0] == "eula" :
                    if line[1] == "true" :
                        return 0
                    else :
                        return 1
                else :
                    continue
    else:
        return 2
    
def change_server_property(property_name, new_value): #server.properties의 원하는 값들을 수정하는 함수.
    if not os.path.exists("..\\server.properties"):
        exit(1)
    # 파일을 읽기 모드로 열기
    with open("..\\server.properties", 'r') as file:
        lines = file.readlines()

    # 속성 찾기 및 변경
    for i, line in enumerate(lines):
        if line.startswith(property_name + '='):
            lines[i] = f'{property_name}={new_value}\n'
            break

    # 파일을 쓰기 모드로 열어 변경된 내용 쓰기
    with open("..\\server.properties", 'w') as file:
        file.writelines(lines)

def set_properties() : # 프로그램이 정상작동되기 위해 server.properties에서 특정 값들을 수정하는 함수.
    private = Private()
    change_server_property("server-port",private.vars["server_port"])
    change_server_property("rcon.port",private.vars["rcon_port"])
    change_server_property("rcon.password",private.vars["rcon_password"])
    change_server_property("broadcast-rcon-to-ops","true")
    change_server_property("enable-rcon","true")

if __name__ == "__main__":
    i = check_eula()

    if i == 0 : # eula=true
        create_bat.create(True)
        set_properties()
        exit(0)
       
    else : # eula=false거나 eula.txt가 존재하지 않을경우
        create_bat.create(False)
        exit(1)