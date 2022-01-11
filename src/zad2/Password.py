class Password:

    def isValid(self, password):
        special = ['$', '@', '#', '%', '!', "\"", "\'", "*", "+", "-", "\\", "/", ":", ";", "=", "<", ">", "?", "^",
                   "_", "`", "~", "[", "]", "{", "}", "(", ")"]
        if type(password) != str:
            raise ValueError("Password must be string!")
        if len(password) == 0:
            raise Exception("Password can't be empty!")
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char in special for char in password):
            return False
        else:
            return True
