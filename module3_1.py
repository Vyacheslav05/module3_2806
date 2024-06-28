calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(str_):
    count_calls()
    str_ = (len(str_), str_.upper(), str_.lower())
    return str_
    count_calls()

def is_contains(string, list_to_search):
    count_calls()
    if string.lower() in list( map( lambda a : a.lower(), list_to_search )):
        return True
    else:
        return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)



