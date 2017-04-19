import random, itertools


def play_game():
    rules()
    first_step()


def rules():
    print("Let's play a drinking game called ride the bus. This is a guessing game where you drink if your wrong, and the only way to get off is to guess them all right.")
    print("\n On the first guess, you are attempting to guess the color of the first card.")
    print("\n On the second guess, you are trying to guess whether the second card value is higher or lower than the first, Ace is high.")
    print("\n On the third guess, you are going to guess if the third card is in-between or outside the values of the first two cards.")
    print("\n On the fourth guess, you are going to guess the suit of the fourth card.")
    print("\n Guess them all correctly and you win, get one wrong and you restart and take a drink.")
    print("\n On the second and third guess, if the following card matches the one before it in value, you have bad luck and must take 2 drinks and restart.")
    print("\n Press 'q' to quit.")


def first_step():

    first_card = draw_card()

    valid_colors = ['red', 'black']

    guess_color = input('Please choose a color, red or black:')
    guess_color = guess_color.lower()

    if quit_game(guess_color):
        print("you have quit the game.")

    if guess_color == first_card['suit']['color']:
        print("Congrats, that is correct.")
        second_step(first_card)
    elif guess_color not in valid_colors:
        print("that is not an option.")
        first_step()
    else:
        print("that is incorrect, drink and we will restart.")
        first_step()


def second_step(first_card):

    print_card('first', first_card)

    print("Now you must guess whether the next card value is higher or lower than the first.")
    second_card = draw_card()

    guess_high_low = input('Please indicate whether you believe the second card is higher or lower than the first:')
    guess_high_low = guess_high_low.lower()

    if quit_game(guess_high_low):
        print("you have quit the game.")

    if guess_high_low not in ['high', 'low']:
        print('That is not an option, please retry.')
        second_step(first_card)

    if guess_high_low == 'high':
        if second_card['face']['rank'] > first_card['face']['rank']:
            print("You betcha, now you're halfway there!")
            third_step(first_card, second_card)
        elif second_card['face']['rank'] == first_card['face']['rank']:
            print("Rotten luck, drink twice and we will restart.")
            print_card('second', second_card)
            first_step()
        else:
            print_card('second', second_card)
            print("Whoops, Drink and we will restart.")
            first_step()

    elif guess_high_low == 'low':
        if second_card['face']['rank'] < first_card['face']['rank']:
            print("You betcha, now you're halfway there!")
            third_step(first_card, second_card)
        elif second_card['face']['rank'] == first_card['face']['rank']:
            print_card('second', second_card)
            print("Rotten luck, drink twice and we will restart.")
            first_step()
        else:
            print_card('second', second_card)
            print("Whoops, Drink and we will restart.")
            first_step()
    else:
        print("Im sorry, something went wrong.")
        second_step(first_card)


def third_step(first_card, second_card):
    top = max(first_card['face']['rank'], second_card['face']['rank'])
    bottom = min(first_card['face']['rank'], second_card['face']['rank'])

    print_card('first', first_card)
    print_card('second', second_card)

    print("Now you must guess whether the third card is in-between or outside the values of the first two.")
    third_card = draw_card()

    guess_location = input("Please indication 'in' or 'out':")
    guess_location = guess_location.lower()

    if quit_game(guess_location):
        print("you have quit the game.")

    if guess_location not in ['in', 'out']:
        print("That is not an option, please try again using 'in' or 'out'.")
        third_step(first_card, second_card)

    if top == third_card['face']['rank'] or third_card['face']['rank'] == bottom:
            print_card('third', third_card)
            print("WOW, you really suck at this, drink twice and startover.")
            first_step()

    if guess_location == 'in':
        if top > third_card['face']['rank'] > bottom:
            print("Bingo, just ONE more!!!")
            final_step(first_card, second_card, third_card)
        else:
            print_card('third', third_card)
            print("awww schucks, wrong again. Start over.")
            first_step()

    if guess_location == 'out':
        if top < third_card['face']['rank'] or third_card['face']['rank'] < bottom:
            print("Winner, Winner, Chicken Dinner!")
            final_step(first_card, second_card, third_card)
        else:
            print("HAHAHA, your card was a {} of {}. Sucks to suck now drink".format(
                third_card['face']['name'],
                third_card['suit']['name'].title()
            ))
            first_step()


def final_step(first_card, second_card, third_card):

    print_card('first', first_card)
    print_card('second', second_card)
    print_card('third', third_card)

    print("Now comes the worst part, guess the suit of the last card.")
    fourth_card = draw_card()

    guess_suit = input("Please guess which suit: diamonds, hearts, spades, or clubs:")
    guess_suit = guess_suit.lower()

    if quit_game(guess_suit):
        print("you have quit the game.")

    if guess_suit not in ['diamonds', 'hearts', 'spades', 'clubs']:
        print("Cmon man, that isnt and option, please try again.")
        final_step(first_card, second_card, third_card)

    if guess_suit == fourth_card['suit']['name']:
        print("Well Son of a Gun, you actually got it. Congrats, you are now off the bus.")
    else:
        print("Wow, thats rough! Gotta restart.")
        print_card('fourth', fourth_card)
        first_step()


def draw_card():
    suits = _get_suits()
    faces = _get_faces()

    face = random.choice(faces)
    suit = random.choice(suits)

    card = {
        'face': face,
        'suit': suit,
    }

    return card


def print_card(position, card):
    print("Your {} card was a {} of {}.".format(
            position,
            card['face']['name'],
            card['suit']['name'].title()
            ))


def quit_game(input):
    if input == 'q':
        exit()


def _get_suits():
    suits = [
        {
            'name': 'clubs',
            'color': 'black'
        },
        {
            'name': 'spades',
            'color': 'black'
        },
        {
            'name': 'diamonds',
            'color': 'red'
        },
        {
            'name': 'hearts',
            'color': 'red'
        },
    ]

    return suits


def _get_faces():
    faces = [
        {
            'name': 'Two',
            'rank': 2,
            'weight': 2
        },
        {
            'name': 'Three',
            'rank': 3,
            'weight': 3
        },
        {
            'name': 'Four',
            'rank': 4,
            'weight': 4
        },
        {
            'name': 'Five',
            'rank': 5,
            'weight': 5
        },
        {
            'name': 'Six',
            'rank': 6,
            'weight': 6
        },
        {
            'name': 'Seven',
            'rank': 7,
            'weight': 7
        },
        {
            'name': 'Eight',
            'rank': 8,
            'weight': 8
        },
        {
            'name': 'Nine',
            'rank': 9,
            'weight': 9
        },
        {
            'name': 'Ten',
            'rank': 10,
            'weight': 10
        },
        {
            'name': 'Jack',
            'rank': 11,
            'weight': 10
        },
        {
            'name': 'Queen',
            'rank': 12,
            'weight': 10
        },
        {
            'name': 'King',
            'rank': 13,
            'weight': 10
        },
        {
            'name': 'Ace',
            'rank': 14,
            'weight': 11
        },
    ]

    return faces

"""
print('{} {} {}'.format(1, 2, 3) # 1 2 3
"""
"""
example test

def test_draw_card():
    card = draw_card()

    assert card['face']['rank'] > 0
    assert card['suit']['color'] in ['red', 'black']
2) a card builder function, that accepts suit & face as args, returns you a specific card
(which you will need for)
3) a test function that will let you call third_step directly so you can easily test all of the different cases
eventually put this in place of just play_game() below

if __name__ == '__main__':
"""
play_game()

