@echo off
set /p RAM="할당할 메모리 크기(Mb단위)를 입력하세요.(예: 2048): "
start python communication.py
cd ..
java -Xms%RAM%M -jar spigot-1.20.2.jar nogui
cd craftcord
