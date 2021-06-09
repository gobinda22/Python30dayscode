n = int(input("enter number of key value pair: "))
name_numbers = [input("enter key and value : ").split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input("enter the key:")
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
