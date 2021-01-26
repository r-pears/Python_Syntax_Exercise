def print_upper_words(words):
  """Print out each word in a list on separate lines, all in uppercase"""
    for word in words:
        print(word.upper())

def print_upper_words_with_e(words):
  """Print out every word that starts with an E or an e on separate lines, all in uppercase"""
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_words_with_e(words, must_start):
  """Print out each word in a list on separate lines, all in uppercase, if the word starts with the provided letter."""
    for word in words:
        for letter in must_start:
            if word.startswith(letter):
                print(word.upper())
                break