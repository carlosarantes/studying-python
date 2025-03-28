try:
    result = 10 + 10
except:
    ##
    print("Something happened.... ERROR")
else:
    print("Add went well....")
finally:
    print("this will always run....")

## -------------
    
try:
    f = open('testfile', 'w')
    f.write('WRITE A SAMPLE TEST')
except TypeError:
    print("Oh.... there is an error....")
except OSError:
    print('OS error :)')
finally:
    print('Always run ...')


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whooops!")
        else:
            print("GOOD")
            break
        finally:
            print("It will run always...")

ask_for_int()