"""
1) реализовать дескрипторы для любых двух классов
"""

import datetime


class CheckIsInt:
    def __set_name__(self, owner, attr_name):
        self.attr_name = attr_name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('Type error')
        instance.__dict__[self.attr_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.attr_name]

    def __delete__(self, instance):
        del instance.__dict__[self.attr_name]


class CheckIsDate:
    def __set_name__(self, owner, attr_name):
        self.attr_name = attr_name

    def __set__(self, instance, value):
        if not isinstance(value, datetime.datetime):
            raise ValueError('Type error')
        instance.__dict__[self.attr_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.attr_name]

    def __delete__(self, instance):
        del instance.__dict__[self.attr_name]


class CheckLen:
    def __set_name__(self, owner, attr_name):
        self.attr_name = attr_name

    def __set__(self, instance, value):
        if len(value) > 128:
            raise ValueError('Length exceeded')
        instance.__dict__[self.attr_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.attr_name]

    def __delete__(self, instance):
        del instance.__dict__[self.attr_name]


class User:
    user_id = CheckIsInt()
    auth_date_time = CheckIsDate()

    def __init__(self, user_id, name, auth_date_time):
        self.user_id = user_id
        self.name = name
        self.auth_date_time = auth_date_time

    def __str__(self):
        return f'Пользователь: {self.name}, id: {self.user_id}, зарегистрирован: {self.auth_date_time}'


class Message:
    message_id = CheckIsInt()
    sender_id = CheckIsInt()
    receiver_id = CheckIsInt()
    message_text = CheckLen()
    send_date_time = CheckIsDate()

    def __init__(self, message_id, message_text, sender_id, receiver_id, send_date_time):
        self.message_id = message_id
        self.message_text = message_text
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.send_date_time = send_date_time

    def __str__(self):
        return f'Идентификатор сообщения: {self.message_id}, текст сообщения: {self.message_text}, ' \
               f'id отправителя: {self.sender_id}, получателя: {self.receiver_id}'


new_user = User(5, 'Петров Иван', datetime.datetime.now())
print(new_user)
new_message = Message(1, 'Иван, привет!', 3, 5, datetime.datetime.now())
print(new_message)
