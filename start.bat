@echo off
set /p RAM="�Ҵ��� �޸� ũ��(Mb����)�� �Է��ϼ���.(��: 2048): "
start python communication.py
cd ..
java -Xms%RAM%M -jar spigot-1.20.2.jar nogui
cd craftcord
