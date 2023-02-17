import os
import random
import time

import YahtzeeCheckDice

clear = lambda: os.system("cls")  # noqa

game_counter = 0

player_counter = 0
players = []


class Dices:
    def __init__(self, dice):
        self.dice = dice

    def __str__(self) -> str:
        dice_to_string = {
            0: [
                " ┌───────┐ ",
                " │       │ ",
                " │       │ ",
                " │       │ ",
                " └───────┘ ",
            ],
            1: [
                " ┌───────┐ ",
                " │       │ ",
                " │   •   │ ",
                " │       │ ",
                " └───────┘ ",
            ],
            2: [
                " ┌───────┐ ",
                " │ •     │ ",
                " │       │ ",
                " │     • │ ",
                " └───────┘ ",
            ],
            3: [
                " ┌───────┐ ",
                " │ •     │ ",
                " │   •   │ ",
                " │     • │ ",
                " └───────┘ ",
            ],
            4: [
                " ┌───────┐ ",
                " │ •   • │ ",
                " │       │ ",
                " │ •   • │ ",
                " └───────┘ ",
            ],
            5: [
                " ┌───────┐ ",
                " │ •   • │ ",
                " │   •   │ ",
                " │ •   • │ ",
                " └───────┘ ",
            ],
            6: [
                " ┌───────┐ ",
                " │ •   • │ ",
                " │ •   • │ ",
                " │ •   • │ ",
                " └───────┘ ",
            ],
        }
        return f"""
{''.join([dice_to_string[number][0] for number in self.dice])}
{''.join([dice_to_string[number][1] for number in self.dice])}
{''.join([dice_to_string[number][2] for number in self.dice])}
{''.join([dice_to_string[number][3] for number in self.dice])}
{''.join([dice_to_string[number][4] for number in self.dice])}
"""


class YahtzeeCard:
    def __init__(self, owner_name, is_player):
        self.owner_name = owner_name if is_player else "Computer"
        self.is_player = is_player
        self.ones = ""
        self.twos = ""
        self.threes = ""
        self.fours = ""
        self.fives = ""
        self.sixes = ""
        self.top_sum = 0
        self.bonus = 0

        self.triplet = ""
        self.quadruplet = ""
        self.full_house = ""
        self.small_street = ""
        self.big_street = ""
        self.yahtzee = ""
        self.chance = ""
        self.summary = 0

    def get_summary(self):
        return self.summary

    def __str__(self) -> str:
        return f"Der Spieler {self.owner_name} hat {self.summary} Punkte."

    def calculate_summaries(self):
        self.top_sum = sum(
            value
            for value in [
                self.ones,
                self.twos,
                self.threes,
                self.fours,
                self.fives,
                self.sixes,
            ]
            if value != ""
        )
        self.bonus = 35 if self.top_sum >= 63 else 0
        self.summary = sum(
            value
            for value in [
                self.top_sum,
                self.triplet,
                self.quadruplet,
                self.full_house,
                self.small_street,
                self.big_street,
                self.yahtzee,
                self.chance,
                self.bonus,
            ]
            if value != ""
        )

    def print_yahtzee_card(self):
        print(
            f"""
    Name: {self.owner_name}
[1] Nur einser: {self.ones}
[2] Nur zweier: {self.twos}
[3] Nur dreier: {self.threes}
[4] Nur vierer: {self.fours}
[5] Nur fünfer: {self.fives}
[6] Nur Sechser: {self.sixes}
[~] Summe oben: {self.top_sum}
[~] Bonus: {self.bonus}
────────────────────────
[7] Dreierpasch: {self.triplet}
[8] Viererpasch: {self.quadruplet}
[9] Full House: {self.full_house}
[10] kleine Straße: {self.small_street}
[11] große Straße: {self.big_street}
[12] yahtzee: {self.yahtzee}
[13] Chance: {self.chance}
[~] Summe: {self.summary}
"""
        )


def yahtzee_card_update(all_dice: list, self: YahtzeeCard):
    while True:
        user_input = -1
        while user_input < 1 or user_input > 13:
            try:
                user_input = int(input("Wo möchtest du deinen Wurf eintragen? (1-13)"))
            except ValueError:
                print("Bitte gebe eine Zahl zwischen 1 und 13 ein.")
                user_input = -1

        match user_input:
            case 1:
                if self.ones == "":
                    self.ones = all_dice.count(1) * 1
                    break

            case 2:
                if self.twos == "":
                    self.twos = all_dice.count(2) * 2
                    break

            case 3:
                if self.threes == "":
                    self.threes = all_dice.count(3) * 3
                    break

            case 4:
                if self.fours == "":
                    self.fours = all_dice.count(4) * 4
                    break

            case 5:
                if self.fives == "":
                    self.fives = all_dice.count(5) * 5
                    break

            case 6:
                if self.sixes == "":
                    self.sixes = all_dice.count(6) * 6
                    break

            case 7:
                if self.triplet == "":
                    if YahtzeeCheckDice.count_dice_with_occurrence(all_dice, 3):
                        self.triplet = sum(all_dice)
                    else:
                        self.triplet = 0
                    break

            case 8:
                if self.quadruplet == "":
                    if YahtzeeCheckDice.count_dice_with_occurrence(all_dice, 4):
                        self.quadruplet = sum(all_dice)
                    else:
                        self.quadruplet = 0
                    break

            case 9:
                if self.full_house == "":
                    self.full_house = YahtzeeCheckDice.calculate_full_house_score(
                        all_dice
                    )
                    break

            case 10:
                if self.small_street == "":
                    if YahtzeeCheckDice.has_consecutive_dice(all_dice, 4):
                        self.small_street = 30
                    else:
                        self.small_street = 0
                    break

            case 11:
                if self.big_street == "":
                    if YahtzeeCheckDice.has_consecutive_dice(all_dice, 5):
                        self.big_street = 40
                    else:
                        self.big_street = 0
                    break

            case 12:
                if self.yahtzee == "":
                    if (
                        YahtzeeCheckDice.count_dice_with_occurrence(all_dice, 5) / 5
                        == all_dice[0]
                    ):
                        self.yahtzee = 50
                    else:
                        self.yahtzee = 0
                    break

            case 13:
                if self.chance == "":
                    self.chance = sum(all_dice)
                    break

    YahtzeeCard.calculate_summaries(self)
    YahtzeeCard.print_yahtzee_card(self)
    time.sleep(5)


def roll_dice():
    global players
    global player_counter
    end_early = False
    all_dice = Dices(
        [
            random.randint(1, 6),
            random.randint(1, 6),
            random.randint(1, 6),
            random.randint(1, 6),
            random.randint(1, 6),
        ]
    )
    for reroll_counter in range(2):
        if end_early:
            end_early = False
            break
        all_dice.dice.sort()
        counter = 0
        while counter < len(all_dice.dice):
            user_input = ""
            while (
                user_input.lower() != "y"
                and user_input.lower() != "n"
                and user_input.lower() != "0"
                and user_input.lower() != "1"
            ):
                clear()
                print(f"Spieler {players[player_counter].owner_name} ist dran")
                print(f"Neu Würfeln Nr. {reroll_counter + 2}/3")
                print(str(all_dice))
                user_input = input(
                    f"""Möchtest du Würfel nr. {counter + 1} behalten?(y/n)
Mit 0 beendest du deinen Zug komplett.
Mit 1 kannst du dir nochmal dein yahtzee Bord angucken."""
                )
            if user_input == "n":
                all_dice.dice[counter] = 0
            if user_input == "0":
                end_early = True
                break
            if user_input == "1":
                YahtzeeCard.print_yahtzee_card(players[player_counter])
                time.sleep(5)
                continue
            counter += 1
        all_dice.dice = [
            item if item != 0 else random.randint(1, 6) for item in all_dice.dice
        ]
        all_dice.dice.sort()
    return all_dice.dice


def main():
    # import ComputerDoingStuff
    # ComputerDoingStuff.bot_move()
    global player_counter
    global players
    global game_counter

    while True:
        try:
            clear()
            amount_of_player = int(
                input(
                    """───╣yahtzee╠───
Wie viele wollen mitspielen
>"""
                )
            )
            break
        except ValueError:
            clear()

    for player_to_add in range(amount_of_player):
        clear()
        players.append(
            YahtzeeCard(
                input(
                    f"""Bitte trage einen Namen für Spieler {player_to_add + 1} ein.
"""
                ),
                True,
            )
        )
    if players[player_counter].is_player:
        while game_counter < 13:
            clear()
            print(players[player_counter].owner_name, " ist dran")
            all_dice = Dices(roll_dice())
            YahtzeeCard.calculate_summaries(players[player_counter])
            YahtzeeCard.print_yahtzee_card(players[player_counter])

            print(str(all_dice))
            yahtzee_card_update(all_dice.dice, players[player_counter])

            if player_counter == len(players) - 1:
                player_counter = 0
                game_counter += 1

            else:
                player_counter += 1

        scoreboard = sorted(players, key=lambda x: x.get_summary())
        scoreboard.reverse()
        for player in scoreboard:
            print(str(player))


main()
