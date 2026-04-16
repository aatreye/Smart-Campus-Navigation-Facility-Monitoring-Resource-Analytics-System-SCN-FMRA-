def validate_location(loc, campus_map):
    if loc in campus_map:
        return True
    else:
        print('Invalid location!')
        return False
