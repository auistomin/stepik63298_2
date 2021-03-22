from django.template import Library

register = Library()


@register.filter
def stars_str(stars_count):
    return '★' * int(stars_count)


@register.filter
def tours_count_str(tours_count):
    if 2 <= tours_count % 10 <= 4 and tours_count % 100 // 10 != 1:
        suffix = 'a'
    elif tours_count % 10 == 1 and tours_count % 100 // 10 != 1:
        suffix = ''
    else:
        suffix = 'ов'
    return 'тур' + suffix


@register.filter
def nights_count_str(tours_count):
    if 2 <= tours_count % 10 <= 4 and tours_count % 100 // 10 != 1:
        suffix = 'и'
    elif tours_count % 10 == 1 and tours_count % 100 // 10 != 1:
        suffix = 'ь'
    else:
        suffix = 'ей'
    return 'ноч' + suffix
