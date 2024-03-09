class Usuario:
    def __init__(self, id_user, username, password):
        self._id_user = id_user
        self._username = username
        self._password = password

    def __str__(self):
        return f'Id: {self._id_user},\nUsername: {self._username},\npassword: {self._password}'

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self,id_user):
        self._id_user = id_user

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

if __name__ == '__main__':
    user1 = Usuario(1, 'teilorza17', '12345')
    print(user1)
