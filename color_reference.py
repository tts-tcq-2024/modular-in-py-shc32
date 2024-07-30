from color_coding_utility import MAJOR_COLORS, MINOR_COLORS, color_pair_to_string, get_pair_number_from_color

# new functionality added - coding to be printed as a reference manual. This manual is a mapping from the color-names to the corresponding numbers
def generate_color_manual():
    manual = []
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            pair_number = get_pair_number_from_color(major_color, minor_color)
            manual.append(f'Pair Number {pair_number}: {color_pair_to_string(major_color, minor_color)}')
    return "\n".join(manual)

def print_color_manual():
    print(generate_color_manual())
