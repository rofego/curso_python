# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (sem self, sem cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user
        # setter
    
    def set_password(self, password):
        self.password = password
        
    @classmethod
    def create_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
# c1 = Connection()
# print(c1.user)
# c1.set_user('Residencial')
# print(c1.user)

# c1.set_password(12345)
# print(c1.password)

c1 = Connection.create_auth('Resid', '12345')
print(vars(c1))

