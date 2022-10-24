# Clear all the __pycache__ folders in the project

import os
import shutil


def clean():
    for root, dirs, files in os.walk("Backend"):
        for directory in dirs:
            if directory == "__pycache__":
                os.system(f'git rm -r {os.path.join(root, directory)} -f')
            # Delete migrations too
            if directory == "migrations":
                os.system(f'git rm -r {os.path.join(root, directory)} -f')


if __name__ == "__main__":
    clean()
