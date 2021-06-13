import re as regex

if __name__ == '__main__':
    url = "https://www.facebook.com/fahimfaisaal"

    print(regex.split("(https://www\\.\\w+\\.[a-z]{3}/)", url))
