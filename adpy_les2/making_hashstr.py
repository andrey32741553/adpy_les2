import hashlib


def making_hashstrings():
    with open('country_links.txt', encoding='utf-8') as file:
        while True:
            string = file.readline().rstrip()
            hash_object = hashlib.md5(string.encode())
            yield hash_object.hexdigest()
            if not string:
                break


if __name__ == '__main__':
    for hash_string in making_hashstrings():
        print(hash_string)
