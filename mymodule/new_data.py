def get_data():
    locations = open('files/locations.list', 'r', encoding='latin-1')
    counter = 0
    for line in locations.readlines():
        name, year = get_year_name(line)
        location = get_location(line)
        print(line.strip())
        print(name, year, location, '\t\tBB')
    # return name, year, location


def get_location(line):
    if '}' in line:
        line = line.split('}')
    else:
        line = line.split(')')
    location = line[1].strip().split('\t')[0]
    return location


def get_year_name(line):
    line.replace('\t', ' ')
    line = line.strip().split()
    name = line[0].replace('#', '').replace('"', '')
    year = line[1][1:5]
    return name, year


if __name__ == '__main__':
    # get_data()
    test = {1 : 'kek'}
    nother = {1: 'top'}
    print(test.update(nother))


