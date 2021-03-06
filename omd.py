# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
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


def step2_umbrella():
    print(
        'В баре утка спросила: «А если я хочу уйти с зонтиком, мне его оставить или забрать?»',
        'Бармен ответил: «Вы можете забрать свой зонтик».',
        '«Но, как же его забрать, он ведь застрял у меня в горле!».',
        'Бармен сказал: «Не волнуйтесь, мы просто опустим его вниз.» ',
        'Утке понравилось, и она ушла.',
        sep='\n'
    )


def step2_no_umbrella():
    print(
        'лучше водочки!',
        'Заходит в бар, а там бармен ей:',
        '- водочка?',
        '- нет, лучше пивасика',
        'Она: - Да я водочку не пью, я ж на работу пришла!',
        'А он: - ну да, только надо добавить в нее моющего средства.',
        sep = '\n'
    )

if __name__ == '__main__':
    step1()