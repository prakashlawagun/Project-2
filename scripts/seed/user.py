from django.contrib.auth import get_user_model
from yaspin import yaspin

User = get_user_model()

ADDRESS = 'Kathmandu'
TERMS_AND_CONDITIONS = True


def create_superuser():
    with yaspin(text='Create superuser', color='cyan') as spinner:
        username = '98123456789'
        if not User.objects.filter(username=username).exists():
            email = 'admin@example.com'
            password = 'pass'
            first_name = 'Super'
            last_name = 'User'

            user = User.objects.create_superuser(username=username,
                                                 phone=username,
                                                 address=ADDRESS,
                                                 tc=TERMS_AND_CONDITIONS,
                                                 first_name=first_name,
                                                 email=email,
                                                 last_name=last_name, )
            user.set_password(password)
            user.save()
            spinner.ok()
        else:
            spinner.fail()


def create_default_user():
    with yaspin(text="Create default user", color="cyan") as spinner:
        username = '9800000000'
        if not User.objects.filter(username=username).exists():
            email = 'default_user@example.com'
            password = 'pass'
            first_name = 'Default'
            last_name = 'User'
            user = User.objects.create_superuser(username=username,
                                                 email=email,
                                                 phone=username,
                                                 address=ADDRESS,
                                                 tc=TERMS_AND_CONDITIONS,
                                                 first_name=first_name,
                                                 last_name=last_name, )
            user.set_password(password)
            user.save()
            spinner.ok()
        else:
            spinner.fail()


__all__ = [
    'create_superuser',
    'create_default_user',
]
