class People:
    def __init__(self, fullname, birthday, weight):
        self.fullname = fullname
        self.birthday = birthday
        self.weight = weight

    def change_fullname(self, fullname):
        self.fullname = fullname

    def change_birthday(self, birthday):
        self.birthday = birthday

    def change_weight(self, new_weight):
        self.weight = new_weight
