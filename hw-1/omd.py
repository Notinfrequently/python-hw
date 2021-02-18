def step2_no_umbrella():
    print('''
              ,    ,   ,
            ,   ,    ,   ,
               __
             _/__\_
             <(o )___
              ( ._> /
               `---'
    ''')


def step2_umbrella():
    print('''
              ,    ,   ,
            ,   ,    ,   ,
               _.-^-.
             _/'"'|`"`
             <(o )|__
              ( ._j /
               `---'
    ''')


def step1():
    print(
        '''
        Утка-маляр
               __
             _/__\_
             <(o )___
              ( ._> /
               `---'     .-^-.
        решила погулять.'"'|`"`
        Взять ей зонтик?   j
        '''
    )

    option = ''
    options = {'да': step2_umbrella, 'нет': step2_no_umbrella}
    while option not in options:
        option = input('Выберите: ({}/{}): '.format(*options))
    return options[option]()


if __name__ == '__main__':
    step1()
