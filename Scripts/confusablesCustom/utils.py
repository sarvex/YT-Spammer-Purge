def is_ascii(string):
    return all(ord(char) < 128 for char in string)
