import hashlib
import os


def create_directory(directory_name: str) -> None:
    try:
        if not os.path.isdir(directory_name):
            os.makedirs(directory_name)
        else:
            print('Directory already exists.')
    except PermissionError:
        print('No permission to create directory')


def generate_md5_hash(binary: bytes) -> str:
    md5_hash = hashlib.md5()
    md5_hash.update(binary)
    md5_hash = str(md5_hash.hexdigest())
    return md5_hash


def save_file(binary: bytes, name: str, path: str) -> None:
    try:
        with open(f'{path}{name}', 'wb') as file:
            file.write(binary)
            file.close()
    except PermissionError:
        print('No permission to create file.')

