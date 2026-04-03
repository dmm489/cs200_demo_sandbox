def func1():
    lst = []
    print('Enter numbers one at a time. Enter 0 to stop.')
    inpNum = int(input('num:'))
    while inpNum != 0:
        lst.append(inpNum)
        inpNum = int(input('num:'))
    print('You added: ', len(lst), ' numbers.')
    return lst


def func2(data):
    print('Here is the data:')
    print(data)

    selection = ''
    while True:
        selection = input('Select an option. 1-sum  2-min  3-max  4-quit')
        return menu(data, selection)


def menu(data, selection):
    if selection == '1':
        print('The sum is', sum(data))
    elif selection == '2':
        print('Not supported yet')
    elif selection == '3':
        print('Not supported yet')
    elif selection == '4':
        print('Goodbye')
        exit(0)


def main():
    print("Hello, World!")
    data = func1()
    func2(data)


if __name__ == "__main__":
    main()
