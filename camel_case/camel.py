import re


def capitalize(word):
    # Converting word to have uppercase first letter, rest in lowercase
    return word[0:1].upper() + word[1:].lower()


def filter(s):
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    res = ""
    for x in s:
        if not(x in punctuations):
            res += x
    return res

def lowercase(word):
    # converting a word to lowercase
    return word.lower()


def camel_case(sentence):
    remove_multiple_spaces = re.sub(r'\s+', ' ', sentence)  # Replaces any groups of whitespace with a single space
    remove_surrounding_space = remove_multiple_spaces.strip()  # removes any remaining whitespace

    words = remove_surrounding_space.split(' ')  # Breaks by spaces
    first_word = lowercase(words[0])  # Lowercase the first word

    # Capitalizes the second and subsequent words, put in a new list.
    capitalized_words = [capitalize(word) for word in words[1:]]

    # Collecting all of the words into one list
    camel_cased_words = [first_word] + capitalized_words

    # Putting words back together
    camel_cased_sentance = ''.join(camel_cased_words)

    return camel_cased_sentance



def main():
    sentence = input('Enter your sentence: ')
    camelcased = camel_case(sentence)
    print(camelcased)


if __name__ == '__main__':
    main()