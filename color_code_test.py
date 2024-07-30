#from color_coding_utility import get_color_from_pair_number, get_pair_number_from_color
import color_coding_utility

def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    major_color, minor_color = color_coding_utility.get_color_from_pair_number(pair_number)
    assert major_color == expected_major_color, f'Expected {expected_major_color}, got {major_color}'
    assert minor_color == expected_minor_color, f'Expected {expected_minor_color}, got {minor_color}'

def test_pair_to_number(major_color, minor_color, expected_pair_number):
    pair_number = color_coding_utility.get_pair_number_from_color(major_color, minor_color)
    assert pair_number == expected_pair_number, f'Expected {expected_pair_number}, got {pair_number}'
