
def clear_line(line):
    cleared_line = list()
    #cleared_line.append(line[0].split()[1])
    # for i in line:
    #     if len(i) != 0:
    #         cleared_line.append(i)
    print(line)
    year = find_year(cleared_line)
    name = find_name(cleared_line)
    location = find_location(cleared_line)
    print(year, name, location, '\t\tAAAAAA')
    return year, location, name


def clear_failed_line(line):
    line = line.split('\\t')
    name = find_name(line).strip()
    year = find_year(line)
    location = find_location(line)
    print(year, name, location, '\t\tBBBBB')

    return year, location, name


def find_location(line):
    cleared_line = list()
    for i in line:
        if i != '':
            cleared_line.append(i)
    location = cleared_line[1]
    if '\\n' in location:
        location = location.replace('\\n', '')
    if "'" in location:
        location = location.replace("'", '')
    return location


def find_year(line):
    year = None
    line1 = line.copy()
    try:
        line = line[0].split()
        for i in line:
            if i[0] == '(':
                year = int(i[1:5])
        if year == None:
            print(line1)
        return year
    except:
        pass


def find_name(line):
    line = line[0].split('"')
    name = line[1]
    return name


def transform_location(location):
    if '\\' in location:
        location = location.split()[1]
    return location


def get_data(needed_year):
    locations = open('files/locations.list', 'rb')
    another_locations = open('files/new_locations', 'w')
    locations_list = list()
    for i in range(1241773):
        try:
            try:
                line = locations.readline().decode('utf-8')
                line = line.split('\t')
                year, location, name = clear_line(line)
            except:
                year, location, name = clear_failed_line(str(locations.readline()))
            #print(year, location, name)
            if year == needed_year:
                locations_list.append((transform_location(location), name))
        except:
            continue
    another_locations.close()
    locations.close()
    return locations_list


if __name__ == '__main__':
    print(get_data(2014))
