# initialize response:
response = ''
counter = 0
while True:
    response = input('hi!')
    print(counter)
    counter += 1
    print(counter)
    if counter >= 5:
        print('i dont have all day')
        break
    else:
        print('let\'s try that again')
