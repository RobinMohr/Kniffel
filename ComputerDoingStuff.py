import random
import YahtzeeCheckDice
from MainKniffel import YahtzeeCard
from MainKniffel import dices


def bot_move(com_card: YahtzeeCard):
    # throw dice
    all_dice = dices(
        [
            random.randint(0, 6),
            random.randint(0, 6),
            random.randint(0, 6),
            random.randint(0, 6),
            random.randint(0, 6),
        ]
    )

    is_full_house = yahtzeeCheckStuff.calculate_full_house_score(all_dice.dice)
    if is_full_house == 25 and com_card.full_house == "":
        if sum(all_dice.dice) > is_full_house and com_card.triplet == "":
            com_card.triplet = sum(all_dice.dice)
        else:
            com_card.full_house = is_full_house
            return com_card

    if (
        yahtzeeCheckStuff.has_consecutive_dice(all_dice.dice, 5)
        and com_card.big_street == ""
    ):
        com_card.big_street = 40
        return com_card

    elif (
        yahtzeeCheckStuff.has_consecutive_dice(all_dice.dice, 4)
        and com_card.small_street == ""
    ):
        if com_card.big_street == "":
            return 1
        else:
            com_card.small_street
            return com_card

    is_yahtzee = yahtzeeCheckStuff.count_dice_with_occurrence(all_dice.dice, 5)
    if is_yahtzee != 0 and com_card.yahtzee == "":
        com_card.yahtzee = 50
        return com_card

    is_quadruplet = yahtzeeCheckStuff.count_dice_with_occurrence(all_dice.dice, 4)
    if is_quadruplet != 0 and com_card.quadruplet == "":
        com_card.quadruplet = sum(all_dice.dice)
        return com_card

    is_triplet = yahtzeeCheckStuff.count_dice_with_occurrence(all_dice.dice, 3)
    if is_triplet != 0 and com_card.triplet == "":
        com_card.triplet = sum(all_dice.dice)
        return com_card

    else:
        return "go_for_yahtzee"
