import random

import YahtzeeCheckDice
from MainKniffel import Dices
from MainKniffel import YahtzeeCard


def bot_move(com_card: YahtzeeCard):
    # throw dice
    all_dice = Dices(
        [
            random.randint(0, 6),
            random.randint(0, 6),
            random.randint(0, 6),
            random.randint(0, 6),
            random.randint(0, 6),
        ]
    )

    is_full_house = YahtzeeCheckDice.calculate_full_house_score(all_dice.dice)
    if is_full_house == 25 and com_card.full_house == "":
        if sum(all_dice.dice) > is_full_house and com_card.triplet == "":
            com_card.triplet = sum(all_dice.dice)
        else:
            com_card.full_house = is_full_house
            return com_card

    if YahtzeeCheckDice.has_consecutive_dice(all_dice.dice, 5) and com_card.big_street == "":
        com_card.big_street = 40
        return com_card

    elif YahtzeeCheckDice.has_consecutive_dice(all_dice.dice, 4) and com_card.small_street == "":
        if com_card.big_street == "":
            return 1
        else:
            com_card.small_street
            return com_card

    is_yahtzee = YahtzeeCheckDice.count_dice_with_occurrence(all_dice.dice, 5)
    if is_yahtzee != 0 and com_card.yahtzee == "":
        com_card.yahtzee = 50
        return com_card

    is_quadruplet = YahtzeeCheckDice.count_dice_with_occurrence(all_dice.dice, 4)
    if is_quadruplet != 0 and com_card.quadruplet == "":
        com_card.quadruplet = sum(all_dice.dice)
        return com_card

    is_triplet = YahtzeeCheckDice.count_dice_with_occurrence(all_dice.dice, 3)
    if is_triplet != 0 and com_card.triplet == "":
        com_card.triplet = sum(all_dice.dice)
        return com_card

    else:
        return "go_for_yahtzee"
