def calculate_full_house_score(dice_list):
    triplet_value = count_dice_with_occurrence(dice_list, 3) // 3
    if triplet_value == 0:
        return 0
    remaining_dice = [item for item in dice_list if item != triplet_value]
    if remaining_dice[0] == remaining_dice[1]:
        return 25
    return 0


def count_dice_with_occurrence(throw, occurrence_threshold):
    return (
        sum(throw)
        if any(throw.count(dice) >= occurrence_threshold for dice in set(throw))
        else 0
    )


def has_consecutive_dice(all_dice, desired_length):
    unique_dice = list(set(all_dice))
    current_length = 1
    max_length = 1
    for dice_pos in range(1, len(unique_dice)):
        if unique_dice[dice_pos] == unique_dice[dice_pos - 1] + 1:
            current_length += 1
        else:
            current_length = 1
        max_length = max(max_length, current_length)
    return max_length >= desired_length
