class Person():
    def __init__(self, id, name, family, national_id, username, password):
        self.id = id
        self.name = name
        self.family = family
        self.national_id = national_id
        self.username = username
        self.password = password

    def __str__(self):
        return f'{self.id} {self.name} {self.family} {self.national_id} {self.username} {self.password}'

    def to_tuple(self):
        return (self.id, self.name, self.family, self.national_id, self.username, self.password)
