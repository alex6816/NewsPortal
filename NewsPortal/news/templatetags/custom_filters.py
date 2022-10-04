from django import template

register = template.Library()
black_list_word = ['fuck']


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Нельзя цензурировать НЕ строку!')
    new_black_list_word = [x.lower() for x in black_list_word]
    value_list = value.strip(' .,!?-#" ').split()
    for word in value_list:
        if word.lower() in new_black_list_word:
            subs = word[0] + ('*' * (len(word) - 1))
            value = value.replace(word, subs)
    return (value)
