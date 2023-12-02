import os
class Private:
    def __init__(self):
        self.vars =  {}
        
        with open('private.txt', 'r') as file:
            lines = file.readlines()
            for line in lines :
                key, value = map(str.strip, line.split('='))
                self.vars[key] = value
            
    
    def print_settings(self) :
        for key, value in self.vars.items() :
            print(f"{key}={value}")

    def change_settings(self) :
        with open("private.txt", "w") as file:
            for key, value in self.vars.items() :
                file.write(f"{key}={value}\n")

    def set_private_default(self) :
        self.vars["bot_token"] = "None"
        self.vars["channel_id"] = "None"
        self.vars["server_address"] = "localhost"
        self.vars["server_port"] = "25565"
        self.vars["rcon_port"] = "25575"
        self.vars["rcon_password"] = "1234"

        self.change_settings()
        