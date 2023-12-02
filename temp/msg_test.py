import msg_converter as mc

res = mc.convert_minecraft_msg("[02:01:12] [Async Chat Thread - #13/INFO]: <ksw20011> 집가는 길에 엔더맨있는데")
print(res)
res = mc.convert_minecraft_msg("[02:04:35] [Server thread/INFO]: ksw20011 lost connection: Disconnected")
print(res)