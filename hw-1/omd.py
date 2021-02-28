def show_them_(it): print(it)

duck =  '''
               __
             <(o )___
              ( ._> /
               `---' 
'''
options = {'да': True, 'нет': False}

questions = {
    "puddles" : "Is there puddles?",
    "cold" : "Is it cold outside?",
    "shining_sun" : "Is it sunny outside? ",
    "wind" : "Is it windy outside?",
    "rain" : "Is it raining outside?"
}

def question_of_(function):
    return questions[function.__name__]

def puddles(yes):
    '''Is there puddles?
    '''
    if yes:
        print("Some waterproof boots?\n")
    else:
        print("It hasn't been raining for a long time.\n")

def cold(yes):
    '''Is it cold outside?
    '''
    if yes:
        print("Warm jacket it is!\n")
    else:
        print("Duck do not fear cold!.\n")

def shining_sun(yes):
    '''Is it sunny outside? 
    '''
    if yes:
        print("Do ducks need a sunglases?\n")
    else:
        print("Grumpy weather, ay?\n")

def wind(yes):
    '''Is it windy outside?
    '''
    if yes:
        print("Maybe duck do need a jacket.\n")
    else:
        print("That's nice!\n")


def rain(yes):
    '''Is it raining outside?
    '''
    if yes:
        print("Better take an umbrella!\n")
    else:
        print("No need in umbrella.\n")


def ask_duck_about_(function):
    show_them_(question_of_(function))
    option = ''
    options = {'yes' : True, 'no' : False}
    while option not in options:
        option = input('Выберите: ({}/{}): '.format(*options))
    return function(options[option])

if __name__ == "__main__":
    show_them_(duck)
    ask_duck_about_(rain)
    ask_duck_about_(puddles)
    ask_duck_about_(wind)
    ask_duck_about_(shining_sun)
    ask_duck_about_(cold)
