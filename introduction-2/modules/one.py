def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    print('ONE.PY running directily')
else:
    print('ONE.PY was imported')