#start.bat(jar 파일 실행시키는 bat)을 생성. bat파일의 내용이 jar파일의 이름과 eula 값에 따라서 작성됌.

import os

def find_jar_file(directory): # jar파일 찾기. jar파일이 여러개있으면 오류가 날 수 있음.
    for filename in os.listdir(directory):
        if filename.endswith(".jar"):
            return filename
    return None

def write_bat_file(script_directory, jar_name, eula): # eula값에 따라 craftcord의 실행여부를 판별하여 jar파일 이름에 알맞게 bat파일 작성.
    bat_content = f'''@echo off
set /p RAM="할당할 메모리 크기(Mb단위)를 입력하세요.(예: 2048): "
{"start python communication.py" if eula else ""}
cd ..
java -Xms%RAM%M -jar {jar_name} nogui
cd craftcord
'''

    bat_file_path = os.path.join(script_directory, 'start.bat')

    with open(bat_file_path, 'w') as bat_file:
        bat_file.write(bat_content)



def create(eula) : # setting_server에서 bat파일을 만들기 위해 호출되는 함수.
    script_directory = os.path.dirname(os.path.realpath(__file__))
    parent_directory = os.path.dirname(script_directory)
    
    jar_name = find_jar_file(parent_directory)

    if jar_name:
        write_bat_file(script_directory, jar_name, eula)
        print(f'Successfully created start.bat with jar_name: {jar_name}')
    else:
        print('No jar file found in the parent directory.')
