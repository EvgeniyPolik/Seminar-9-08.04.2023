"""
2) реализовать метакласс. позволяющий создавать всегда один и тот же объект класса (см. урок)
"""

class SingleServer(type):
    Server = None

    def __call__(cls):
        if cls.Server is None:
            cls.Server = super().__call__()
            return cls.Server
        return cls.Server


class MainServer(metaclass=SingleServer):
    server_name = 'uni-server'
    port = 3535

    def __str__(self):
        return f'Server is running'


Server_mess = MainServer()
Server_app = MainServer()
Server_web = MainServer()

print(Server_app is Server_mess)
print(Server_mess is Server_app)
