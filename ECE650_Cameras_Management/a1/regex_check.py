import re


def regexFlag(line):
    # street_pattern = r"\"[a-zA-Z\s]+\"\s*"    # Accept white spaces
    street_pattern = r"\"([a-zA-Z]+(\s?[a-zA-Z]+)*)\""
    # coordinate_pattern = r"(\s+\(\s*[\+|\-]?\s*\d+\s*\,\s*[\+|\-]?\s*\d+\s*\)\s*)+"  #Accept + and - with white space
    number_pattern = r"(\-?[1-9]\d*|0)"
    # coordinate_pattern = r"(\s+\(\-?\d+\,\-?\d+\)){2,}"
    coordinate_pattern = r"(\s+\(" + number_pattern + r"\," + number_pattern + r"\)){2,}"
    pattern_add = r'^add\s+' + street_pattern + coordinate_pattern + r'\s*'
    pattern_mod = r'^mod\s+' + street_pattern + coordinate_pattern + r'\s*'
    pattern_rm = r'^rm\s+' + street_pattern + r'\s*'
    pattern_gg = r'^gg\s*'

    # print(coordinate_pattern)
    if re.fullmatch(pattern_add, line) is not None:
        isFind = True
    elif re.fullmatch(pattern_mod, line) is not None:
        isFind = True
    elif re.fullmatch(pattern_rm, line) is not None:
        isFind = True
    elif re.fullmatch(pattern_gg, line) is not None:
        isFind = True
    else:
        isFind = False
    return isFind


if __name__ == '__main__':
    add_lines = ['add "weber" 1,2,3,4,5,6',
                 'add "weber" (1,2 (3,4) (5,6)',
                 'add "weber" (1,2)(3,4) (5,6)',
                 'add"weber" (1,2) (3,4) (5,6)',
                 'add "weber"(1,2) (3,4) (5,6)',
                 'add "" (1,2) (3,4) (5,6)',
                 'ADD "weber" (1,2) (3,4) (5,6)',
                 'add "weber" (-1,+2) (3,4) (5,6)',
                 'add "weber" ( -    1,2) (3,4) (5,6)',
                 'add "weber" (1,2)',
                 'add "weber*" (-1,2) (3,4) (5,6)',
                 'add "St. Weber" (-1,2) (3,4) (5,6)',
                 'add "2nd weber" (-1,2) (3,4) (5,6)',
                 'add "weber" (-1,2) (3,4) (5,6)',
                 'add "weber" ( -1 , 2 ) ( 3, 4) ( 5 , 6 )',
                 'add "weber" (-1,2) (3,4) (5,6)',
                 'add " weber" (-1,2) (3,4) (5,6)',
                 'add "Weber" (-1,2) (3,4) (5,6) ',
                 'add "King Street S" (4,2) (4,8)',
                 'add "King Street S" (-0,0) (4,8)',
                 'add "King Street S" (0,-2) (4,8)'
                 ]

    mod_lines = [
        'MOD "weber" (-1,2) (3,4) (5,6)',
        'mod "weber" (1,2) (3,4) (5,6)',
        'mod "Weber" (-1,2) (3,4) (5,6)',
        'mod "unit avenue" (-1,2) (3,4) (5,6)'
    ]

    rm_lines = [
        'rm "weber" (-1,2) (3,4) (5,6)',
        'rm "weber"',
        'rm "test weber"'
    ]

    gg_lines = [
        'gg',
        'gg "weber"'
    ]

    for l in add_lines:
        print(regexFlag(l))
