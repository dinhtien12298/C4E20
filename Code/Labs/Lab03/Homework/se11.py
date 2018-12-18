def is_inside(point, rec):
    if rec[0] <= point[0] <= (rec[0] + rec[2]) and rec[1] <= point[1] <= (rec[1] + rec[3]):
        print('Be Inside')
        return True
    else:
        print('Not Be Inside')
        return False
        