def is_leap(leap):
    if leap % 4 != 0:
        return False
    else:
        if leap % 100 != 0:
            return True
        elif leap % 400 != 0:
            return False
        elif leap % 3200 != 0:
            return True

leap = input('請輸入年份: ')
leap = int(leap)
print(is_leap(leap))
