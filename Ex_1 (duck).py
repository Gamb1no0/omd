def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар.'
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_no_umbrella():
    print(
        'На улице пошел ливень.'
        ' утка не захотела промокнуть, поэтому вернулась домой.\n'
        'Дома уточка сделала себе зеленый чай.'
        'села ответственно делать дз по питону.'
    )


def step2_umbrella():
    print(
        'На улице пошел ливень.'
        'но утке это не помешало добраться до бара и уйти в запой.'
        'Когда утка вышла из запоя оказалось, что горят все возможные сроки по дз.'
    )


if __name__ == '__main__':
    step1()