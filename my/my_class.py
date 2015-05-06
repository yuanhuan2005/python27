#!/usr/bin/env python


class MyUser:
    def __init__(self, user_id=None, username=None, age=0):
        self.user_id = user_id
        self.username = username
        self.age = age

    user_id = None
    username = None
    age = 0

    def get_username(self, user_id):
        if user_id == self.user_id:
            return self.username
        else:
            return None

    def to_json_string(self):
        return "{\"user_id\":\"" + self.user_id + "\",\"username\":\"" + self.username + "\",\"age\":" + str(
            self.age) + "}"


user = MyUser()
user.user_id = "102343"
user.username = "Jason"
user.age = 25
print user.get_username("10002341")
print user.to_json_string()

user = MyUser("102343", "Jason", 25)
print user.get_username("10002341")
print user.to_json_string()


