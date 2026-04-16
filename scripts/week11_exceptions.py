def safe_input():
    try:
        val = int(input('Enter number: '))
        return val
    except ValueError:
        print('Invalid input!')
        return 0
