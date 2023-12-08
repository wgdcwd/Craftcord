@echo off
set /p RAM="Enter the amount of RAM to allocate (e.g., 2048): "
start python a_to_a.py
cd ..
java -Xms%RAM%M -jar spigot-1.20.2.jar nogui
cd craftcord
