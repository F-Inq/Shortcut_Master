from keyboard import add_abbreviation


def add_all_abbreviations():
    add_abbreviation('@m', 'user@mail.ru')  # @m followed by a space will turn into user@mail.ru
    add_abbreviation('"ь', 'user@mail.ru')  # same for russian layout
    add_abbreviation('@g', 'your@gmail.com')
    add_abbreviation('"п', 'your@gmail.com')
