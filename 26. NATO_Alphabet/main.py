# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
df = pd.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(nato_dict)
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user = input('Enter a word: ')
    try:
        user_nato = [nato_dict[letter.upper()] for letter in user]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
        print(user_nato)

generate_phonetic()