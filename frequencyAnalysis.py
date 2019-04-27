# gives count of how many times a letter shows up in a string in percentage

import string
#import codecs


def frequency_analysis(inputted_string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_count = dict.fromkeys(string.ascii_lowercase, 0)

    #inputted_string = (input('initiate Frequency Analysis on: '))

    print(inputted_string)

    #Use codecs if you wont to output changes into a file
    # with codecs.open("filename", 'r', encoding='utf8') as f:
    #     text = f.read()

    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890.,/[]()- $;'
    letter_count = dict.fromkeys(alphabet, 0)

    count = 0
    for letter in inputted_string:
        if letter in alphabet:
            count += 1
            letter_count[letter] += 1

    for i in letter_count:
        letter_count[i] = letter_count[i] / count

    for k in sorted(letter_count, key=letter_count.get, reverse=True):
        print(k, '=', letter_count[k])

    print('The amount of characters in the inputted string is {0}'.format(count))

    # uncomment to use a file
    # with codecs.open("filename", 'w', encoding='utf8') as f:
    #     f.write(text)


def main():
    frequency_analysis("hello")


if __name__ == '__main__':
    main()
