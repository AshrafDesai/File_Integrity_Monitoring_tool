import hashlib

def calculate_md5(file_path):
    with open(file_path, "rb") as f:
        content = f.read()
        return hashlib.md5(content).hexdigest()
