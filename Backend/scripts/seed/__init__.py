from . import user


def run():
    user.create_superuser()
    user.create_default_user()
