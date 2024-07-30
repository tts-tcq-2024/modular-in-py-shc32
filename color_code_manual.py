import color_code_map

# new functionality added - coding to be printed as a reference manual. This manual is a mapping from the color-names to the corresponding numbers
def generate_color_manual():
    manual = []
    for major_color in color_code_map.MAJOR_COLORS:
        for minor_color in color_code_map.MINOR_COLORS:
            pair_number = color_code_map.get_pair_number_from_color(major_color, minor_color)
            manual.append(f'Pair Number {pair_number}: {color_code_map.color_pair_to_string(major_color, minor_color)}')
    return "\n".join(manual)

def print_color_manual():
    print(generate_color_manual())
