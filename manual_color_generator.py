import color_code_mapping

def generate_color_manual():
    manual = []
    for major_color in color_code.MAJOR_COLORS:
        for minor_color in color_code.MINOR_COLORS:
            pair_number = color_code.get_pair_number_from_color(major_color, minor_color)
            manual.append(f'Pair Number {pair_number}: {color_code.color_pair_to_string(major_color, minor_color)}')
    return "\n".join(manual)

def print_color_manual():
    print(generate_color_manual())

if __name__ == '__main__':
    print_color_manual()
