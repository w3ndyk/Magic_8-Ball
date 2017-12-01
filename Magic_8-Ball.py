import random
import time
import sys
from enchant.checker import SpellChecker


def delay(text):
    for c in text:
        if text == '...':
            sys.stdout.write(c)
            time.sleep(0.5)
        else:
            sys.stdout.write(c)
            time.sleep(0.1)


def check_repeat(repeat, index, num):
    if repeat[index] > 0:
        print_repeat(num)

    repeat[index] += 1


def print_repeat(num):
    if num == 1:
        print("\n\nHaven\'t you asked this question already? Anyways...\n")
        time.sleep(1)
    elif num == 2:
        print("\n\nYet again with the same question, eh? Well, it is you we\'re talking about. Anyhow...\n")
        time.sleep(1)
    else:
        print("\n\nDon\'t you wanna ask any OTHER question? I\'ve got loads of wisdom to tell you but fine...\n")
        time.sleep(1)


# Answers intelligently to following questions:
#   Will I fall in love?
#   Am I good/perfect for her/him/them?
#   Is anybody going to love me?
#   Do you like/love me?
def love_life(choice, num, repeat, index):
    check_repeat(repeat, index, num)

    if choice == 'fall':
        if num == 1:
            print('\nHmm... since it\'s you, I\'m gonna have to say...\n')
        elif num == 2:
            print('\nYou\'re asking THAT question? Well, I am a know-it-all, so Magic 8-Ball says...\n')
        else:
            print('\nOoh, very intriguing! Well, Magic 8-Ball is saying...\n')

    elif choice == 'good':
        if num == 1:
            print('\nInteresting question... Magic 8-Ball is saying...\n')
        elif num == 2:
            print('\nI think you should\'ve ask someone else this question, but Magic 8-Ball says...\n')
        else:
            print('\nHmm... This is difficult to answer, but Magic 8-Ball is gonna have to say...\n')

    elif choice == 'anybody':
        if num == 1:
            print('\nFirst of all, you should ask someone else about this. Second, Magic 8-Ball says...\n')
        elif num == 2:
            print('\nWell, knowing that we\'re talking about you, I\'m gonna have to say...\n')
        else:
            print('\n"WARNING: GET READY FOR SOME HARD TRUTH"')
            print('It\'s just a notice for my answer. Magic 8-Ball is saying...\n')

    elif choice == 'you':
        if num == 1:
            print('\nOh... I am flattered. I\'m gonna have to say...\n')
        elif num == 2:
            print('\nMy, oh my! Taking initiative are we? Well, Magic 8-Ball says...\n')
        else:
            print('\nOh, wow. Um... this is awkward... I don\'t know how this would work. I\'m saying...\n')


# Answers questions about love life
def love(x, num, repeat):
    if 'will' in x and 'i' in x and 'fall' in x and 'in' in x and 'love' in x:
        love_life('fall', num, repeat, 0)
    elif 'am' in x and 'i' in x and ('good' in x or 'perfect' in x) and ('her' in x or 'him' in x or 'them' in x):
        love_life('good', num, repeat, 0)
    elif 'anybody' in x and 'love' in x and 'me' in x:
        love_life('anybody', num, repeat, 0)
    elif 'do' in x and 'you' in x and ('love' in x or 'like' in x) and 'me' in x:
        love_life('you', num, repeat, 0)


# Answers intelligently to following questions:
#   Will I get an A in this class?
#   Is this class hard?
#   Will I get a good grade in this class?
#   Will I fail this class?
def rand_grade(choice, num, repeat, index):
    check_repeat(repeat, index, num)

    if choice == 'a':
        if num == 1:
            print('\nWell, based on what you\'ve done so far, Magic 8-Ball is saying...')
        elif num == 2:
            print('\nYou\'ve come this far, so Magic 8-Ball says...')
        else:
            print('\nYou\'re asking that question, huh? Well, I\'m gonna have to say...')

    elif choice == 'hard':
        if num == 1:
            print('\nWell since you\'re taking THAT class, Magic 8-Ball is gonna have to say...')
        elif num == 2:
            print('\nLooking at the previous students who took that class, I\'m saying...')
        else:
            print('\nWell, this is about you after all, so Magic 8-Ball says...')

    elif choice == 'good':
        if num == 1:
            print('\nIs this that important to you? Well, Magic 8-Ball says...')
        elif num == 2:
            print('\nSeeing your previous works, Magic 8-Ball is saying...')
        else:
            print('\nSince we\'re talking about you, I\'m gonna have to say...')

    elif choice == 'fail':
        if num == 1:
            print('\nHmm... you really wanna know huh? Magic 8-Ball says...')
        elif num == 2:
            print('\nFingers crossed that you don\'t, but Magic 8-Ball is gonna have to say...')
        else:
            print('\nChecking your average scores, Magic 8-Ball is saying...')


# Answers questions about grade
def get_a(x, num, repeat):
    if 'will' in x and 'i' in x and 'get' in x and ("an 'a'" in x or 'an a' in x):
        rand_grade('a', num, repeat, 0)
    elif 'this' in x and 'class' in x and 'hard' in x:
        rand_grade('hard', num, repeat, 0)
    elif 'will' in x and 'i' in x and 'get' in x and 'good' in x and 'grade' in x:
        rand_grade('good', num, repeat, 0)
    elif 'will' in x and 'i' in x and 'fail' in x and 'class' in x:
        rand_grade('fail', num, repeat, 0)

######################### ONE MORE CATEGORY???? ############ SHOULD I CONFESS TO HIM/HER?
def ai(n, repeat):
    num = int(random.random() * 3) + 1

    love(n, num, repeat)
    get_a(n, num, repeat)


def ask():
    roll = int(random.random() * 12) + 1
    if roll == 1:
        time.sleep(1)
        print("\nYes")
    elif roll == 2:
        time.sleep(1)
        print("\nNo")
    elif roll == 3:
        time.sleep(1)
        print("\nMaybe")
    elif roll == 4:
        time.sleep(1)
        print('\nConcentrate and ask again')
    elif roll == 5:
        time.sleep(1)
        print("\nSigns point to yes")
    elif roll == 6:
        time.sleep(1)
        print("\nOutlook not so good")
    elif roll == 7:
        time.sleep(1)
        print("\nI have no idea")
    elif roll == 8:
        time.sleep(1)
        print("\nAsk again later")
    elif roll == 9:
        time.sleep(1)
        print("\nIt is certain")
    elif roll == 10:
        time.sleep(1)
        print("\nMy sources say no")
    elif roll == 11:
        time.sleep(1)
        print("\nPerhaps")
    elif roll == 12:
        time.sleep(1)
        print("\nCannot tell now")


def spell_check(response):
    count = 0

    checker = SpellChecker("en_US")
    checker.set_text(response)
    for err in checker:
        if err:
            count += 1

    return count


def check_input(choice):
    num = int(random.random() * 3) + 1
    while True:
        response = raw_input().lower()
        delay('...')

        if spell_check(response) > 0:
            if num == 1:
                print("\n\nIt\'s not me. It\'s you. Use words found in the US English dictionary. Please try again:")
            elif num == 2:
                print("\n\nMagic 8-Ball only understands words from the US English dictionary. Please try again:")
            elif num == 3:
                print("\n\nBring out your dictionary since it looks like you don\'t know how to spell. "
                      "Please try again:")

        elif choice == 'again':
            if response == 'yes' or response == 'y':
                return True
            elif response == 'no' or response == 'n':
                delay("\nThanks for playing!")
                return False
            else:
                print("\n\nPlease answer correctly if you want to play again:\n")

        elif choice == 'question':
            if response == '':
                print("\n\nPlease try again because I literally can\'t answer you if there\'s no question.\n")
                time.sleep(0.75)
                print("Ask away. Come on, don\'t be shy:  ")
            elif '?' not in response:
                print("\n\nMerriam Webster says that a question mark is")
                print("\'a mark (?) used in writing and printing at the conclusion of a sentence to indicate a "
                      "direct question\' ")
                print("so use a question mark (this guy -> ?) next time.\n")
                time.sleep(0.75)
                print("Ask away but correctly this time: ")
            else:
                return response


def main():
    repeat = [0] * 7
    print("                                                              =-=-=  Welcome to the Magic 8-Ball!  =-=-=")
    time.sleep(0.75)

    answer = True
    while answer:
        print("\n\n\n\nAsk any yes or no question about how you\'re doing in class or about your love life: ")
        ai(check_input("question"), repeat)
        ask()

        print("\n\n\n\nWould you like to ask another question?")
        answer = check_input("again")


main()
