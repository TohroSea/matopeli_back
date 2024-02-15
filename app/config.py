from os import urandom


DEBUG=False
SQLALCHEMY_DATABASE_URI="sqlite:///database.db"
SECRET_KEY = urandom(24)
