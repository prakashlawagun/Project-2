import contextlib
import os
from pathlib import Path

from Backend.settings import LOCAL_APPS

APPS_MIGRATIONS_PATH = [f'{app}/migrations' for app in LOCAL_APPS]


def restart():
    sqlite_path = Path(__file__).resolve().parent / 'db.sqlite3'
    # Delete file
    if sqlite_path.exists():
        print('Deleting db.sqlite3')
        sqlite_path.unlink()

    for path in APPS_MIGRATIONS_PATH:
        directory = Path(path)
        with contextlib.suppress(FileNotFoundError):
            for file in directory.iterdir():
                if file.is_file():
                    file.unlink()
                    print(f'Deleted {file}')

    APPS_LIST_STR = ' '.join(LOCAL_APPS)

    os.system(f'python3 manage.py makemigrations {APPS_LIST_STR}')
    os.system('python3 manage.py migrate')
    os.system('python3 manage.py runscript seed')
    print('Restarted successfully!')
    os.system('python3 manage.py runserver 127.0.0.1:8000 ')


if __name__ == '__main__':
    restart()
