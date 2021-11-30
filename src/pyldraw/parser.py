from pyldraw.brick import BrickFactory


def parser(data):
    result = {}

    for line in data:
        parts = line.split(' ')
        if parts[0] == '0':
            if parts[1].upper() == 'FILE':
                result['name'] = parts[-1].split('.')[0]
        elif parts[0] == '1':
            brick = BrickFactory.gen(" ".join(parts[1:]))
            result['bricks'] = [brick]
    return result
