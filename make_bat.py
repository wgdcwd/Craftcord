#start.bat(jar 파일 실행시키는 bat)을 생성. bat파일의 내용이 jar파일의 이름에 맞춰서 작성됌.

import os

def find_jar_file(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jar"):
            return filename
    return None

def create_bat_file(script_directory, jar_name):
    bat_content = f'''@echo off
set /p RAM="Enter the amount of RAM to allocate (e.g., 2048): "
start python a_to_a.py
cd ..
java -Xms%RAM%M -jar {jar_name} nogui
cd craftcord
'''

    bat_file_path = os.path.join(script_directory, 'start.bat')

    with open(bat_file_path, 'w') as bat_file:
        bat_file.write(bat_content)

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.realpath(__file__))
    parent_directory = os.path.dirname(script_directory)
    
    jar_name = find_jar_file(parent_directory)

    if jar_name:
        create_bat_file(script_directory, jar_name)
        print(f'Successfully created start.bat with jar_name: {jar_name}')
    else:
        print('No jar file found in the parent directory.')
