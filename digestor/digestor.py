import hashlib


def digest(value):
    hasher = hashlib.sha256()
    hasher.update(value.encode())
    return hasher.hexdigest()
