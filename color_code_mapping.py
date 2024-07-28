MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'

def get_color_from_pair_number(pair_number):
    if pair_number < 1 or pair_number > len(MAJOR_COLORS) * len(MINOR_COLORS):
        raise ValueError('Pair number out of range')
    
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    
    if major_index >= len(MAJOR_COLORS):
        raise ValueError('Major index out of range')
    if minor_index >= len(MINOR_COLORS):
        raise ValueError('Minor index out of range')
    
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
    if major_color not in MAJOR_COLORS:
        raise ValueError(f'Invalid major color: {major_color}')
    if minor_color not in MINOR_COLORS:
        raise ValueError(f'Invalid minor color: {minor_color}')
    
    major_index = MAJOR_COLORS.index(major_color)
    minor_index = MINOR_COLORS.index(minor_color)
    return major_index * len(MINOR_COLORS) + minor_index + 1

def generate_color_manual():
    manual = []
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            pair_number = get_pair_number_from_color(major_color, minor_color)
            manual.append(f'Pair Number {pair_number}: {color_pair_to_string(major_color, minor_color)}')
    return "\n".join(manual)
