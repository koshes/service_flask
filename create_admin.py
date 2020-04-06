from getpass import getpass
import sys

from webapp import create_app
from webapp.db import db
from webapp.user.models import User
app = create_app()

with app.app_context():
    username = input('Enter the name:')

    if User.query.filter(User.username == username).count():
        print('User with the same name already exists')
        sys.exit(0)

    password1 = getpass('Enter the password:')
    password2 = getpass('Repeat the password:')

    if not password1 == password2:
        print('Password mismatch')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('User with id {} added'.format(new_user.id))
