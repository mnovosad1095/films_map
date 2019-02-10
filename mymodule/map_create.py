from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
import pandas
import random


geolocator = Nominatim(user_agent='not_my_app', timeout=5)
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2)


def take_input():
    while True:
        year = input('Please enter your year: ')
        try:
            year = int(year)
            if year > 0:
                break
            else:
                print('You entered a wrong year')
        except ValueError:
            print('You entered a wrong year')

    return str(year)


def update_dict(dictionary, k, v):
    """
    Updates dictionary:
    If key is not in dictionary, it adds it
    If it is already there, just ads value to it

    """

    if k not in dictionary.keys():
        location = geolocator.geocode(k)
        try:
            latlng = [location.latitude, location.longitude]
            dictionary[k] = [latlng]
            dictionary[k].append(v)
        except AttributeError:
            return dictionary

    else:
        dictionary[k].append(v)
    return dictionary


def create_dict(years_data, locs, names, year):
    """
    Takes given data and creates dictionary of type:
    {Location name:[[coordinates], names of films, filmed in this location]}

    """
    loc_dict = dict()
    for i in range(1241206):
        try:
            if years_data[i] == year:
                loc_dict = update_dict(loc_dict, locs[i], names[i])
        except:
            return loc_dict
    return loc_dict


def create_popup(dictionary_i):
    name = ''
    name += random.choice(dictionary_i[1:])
    if len(dictionary_i)-2 > 0:
        name += ' and other ' + str(len(dictionary_i)-2)
    return name


def pick_color(quantity):
    if quantity >= 20:
        return 'red'
    elif quantity >= 5:
        return 'yellow'
    else:
        return 'green'


locations = open('files/locations.csv', 'r', )
file_data = pandas.read_csv(locations, error_bad_lines=False)
names_data = file_data['movie']
years = file_data['year']
locations_data = file_data['location']
locations.close()


map = folium.Map()
locs = folium.FeatureGroup(name='Locations')
rich_locs = folium.FeatureGroup(name="Richest locations")

year = take_input()
locs_dict = create_dict(years, locations_data, names_data, year)

for i in locs_dict.keys():
    locs.add_child(folium.Marker(location=locs_dict[i][0],
                                 popup=create_popup(locs_dict[i]),
                                 icon=folium.Icon()
                                 ))
    rich_locs.add_child(folium.CircleMarker(radius=5,
                                            location=locs_dict[i][0],
                                            color=pick_color(len(locs_dict[i]) - 1),
                                            fill_color=pick_color(len(locs_dict[i]) - 1)
                                            ))

map.add_child(locs)
map.add_child(rich_locs)
map.add_child(folium.LayerControl())
map.save('map.html')
print('Done!')
