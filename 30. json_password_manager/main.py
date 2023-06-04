## FileNotFound
#with open('a_file.txt') as file:
#    file.read()
#
## KeyError
#a_dictionary = {'key': 'value'}
#value = a_dictionary['non_existent_key']
#
## IndexError
#fruit_list = ['apple', 'orange', 'banana']
#fruit = fruit_list[3]

# Type Error
#text = 'abc'
#print(text + 5)

# FileNotFound
try:
    file = open('a_file.txt')
    a_dictionary = {'key': 'value'}
    print(a_dictionary['key'])
except FileNotFoundError:
    # print('There was an error')
    file = open('a_file.txt', 'w')
    file.write('something')
except KeyError as error_message:
    print(f'That key {error_message} does not exist.')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('File was closed.')