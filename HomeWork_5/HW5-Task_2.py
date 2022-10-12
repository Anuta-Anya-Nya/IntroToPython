# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

def code_file(text, file_record):
    with open(text, 'r', encoding="utf-8") as my_text:
        list_strings = my_text.readlines()
        with open(file_record, 'a', encoding="utf-8") as my_f:
            for s in range(0, len(list_strings)):
                string_code = list_strings[s].strip()
                new_text = ''
                count = 1
                letter = string_code[0]

                for i in range(1, len(string_code)):

                    if string_code[i] == string_code[i-1]:
                        count += 1
                    else:
                        new_text += str(count)
                        new_text += letter
                        count = 1
                        letter = string_code[i]
                new_text += str(count)
                new_text += letter
                my_f.write(new_text + "\n")


def decode_file(decode_file, text):
    with open(decode_file, 'r', encoding="utf-8") as my_text:
        list_strings = my_text.readlines()
        with open(text, 'a', encoding="utf-8") as my_f:
            for s in range(0, len(list_strings)):
                string_decode = list_strings[s].strip()
                new_text = ''
                number = string_decode[0]
                for i in range(1, len(string_decode)):
                    if string_decode[i].isdigit():
                        number += string_decode[i]
                    else:
                        for c in range(0, int(number)):
                            new_text += string_decode[i]
                            number = ''
                my_f.write(new_text + "\n")


code_file(input('Enter the name of the file with the text:'),
          input('Enter the file name to record: '))
decode_file(input('Enter the name of the file to decode: '),
            input('Enter the name of the file with the text: '))
