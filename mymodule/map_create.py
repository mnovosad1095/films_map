from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
import pandas
import random

locations = open('files/locations.csv', 'r', )
file_data = pandas.read_csv(locations, error_bad_lines=False)
names_data = file_data['movie']
years = file_data['year']
locations_data = file_data['location']

geolocator = Nominatim(user_agent='not_my_app', timeout=5)
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2)

print(file_data)
# for i in range(1241206):
#     location = geocoder.yandex(locations_data[i])
#     print(location.latlng)


def update_dict(dictionary, k, v):
    '''
    Updates dictionary:
    If key is not in dictionary, it adds it
    If it is already there, just ads value to it
    '''
    if k not in dictionary.keys():
        location = geolocator.geocode(k)
        print(location)
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

    loc_dict = dict()
    for i in range(1241206):
        try:
            if years_data[i] == year:
                loc_dict = update_dict(loc_dict, locs[i], names[i])
        except:
            return loc_dict
    return loc_dict


map = folium.Map()


def create_popup(dictionary_i):
    name = ''
    name += random.choice(dictionary_i[1:])
    if len(dictionary_i)-2 > 0:
        name += ' and other ' + str(len(dictionary_i)-2)
    return name


def pick_color(quantity):
    if quantity >= 100:
        return 'red'
    elif quantity >= 10:
        return 'yellow'
    else:
        return 'green'

#test_dict = create_dict(years, locations_data, names_data, '1978')


#test_dict = {'Ventura County California USA': [[34.4458248, -119.0779359], 'The Nuisance ', 'Blah', 'Blah, blah', 'KEk'], }
locations.close()
test_dict = {'USA': [[39.7837304, -100.4458825], '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 ', '20/20 '], 'San Diego California USA': [[32.7174209, -117.1627714], '20/20 '], 'Miami Beach Florida USA': [[25.7929198, -80.1353006], '20/20 '], 'Venice Italy': [[45.4371908, 12.3345898], '20/20 '], 'Philippines': [[12.7503486, 122.7312101], '20/20 '], 'Paris France': [[48.8566101, 2.3514992], '20/20 '], 'Chicago Illinois USA': [[41.8755616, -87.6244212], '20/20 '], 'Spain': [[39.3262345, -4.8380649], '20/20 '], 'Minneapolis Minnesota USA': [[44.9772995, -93.2654692], '20/20 '], 'Philadelphia Pennsylvania USA': [[39.9524152, -75.1635755], '20/20 '], 'New Orleans Louisiana USA': [[29.9499323, -90.0701156], '20/20 '], 'Bangkok Thailand': [[13.7538929, 100.8160803], '20/20 '], 'Sioux Falls South Dakota USA': [[43.5499749, -96.700327], '20/20 '], 'Phoenix Arizona USA': [[33.4485866, -112.0773456], '20/20 '], 'New York City New York USA': [[40.7308619, -73.9871558], '30 Minutes '], 'Mexico': [[19.4326009, -99.1333416], '60 Minutos '], 'Faraday Melbourne Victoria Australia': [[-37.8879823, 145.1836284], 'A Life at Stake '], 'California USA': [[36.7014631, -118.7559974], 'A Woman Called Moses ', 'Amerikanske bruddstykker '], 'Luanda Angola': [[-8.8272699, 13.2439512], 'Africa nera Africa rossa '], 'New South Wales Australia': [[-31.8759835, 147.2869493], 'Against the Wind '], 'Coverdale North Yorkshire England UK': [[54.2590471, -1.879848], 'All Creatures Great and Small '], 'Ellerton Abbey North Yorkshire England UK': [[54.371143, -1.8807686], 'All Creatures Great and Small '], 'Hawes North Yorkshire England UK': [[54.3039411, -2.1965194], 'All Creatures Great and Small '], 'Holy Trinity Church Wensley North Yorkshire England UK': [[54.3027872, -1.86199295443596], 'All Creatures Great and Small '], 'Langthwaite North Yorkshire England UK': [[54.4178141, -1.9937274], 'All Creatures Great and Small '], 'Swaledale North Yorkshire England UK': [[54.3853314, -1.9579669], 'All Creatures Great and Small '], 'Wensleydale North Yorkshire England UK': [[54.2945308, -2.0000084], 'All Creatures Great and Small '], 'Goathland Station Goathland North Yorkshire England UK': [[54.4004864, -0.7120022], 'All Creatures Great and Small '], 'Austin Texas USA': [[30.2711286, -97.7436995], 'Alternative Views '], 'UCLA Westwood Los Angeles California USA': [[34.05996195, -118.447770092291], 'America Alive! '], 'Los Angeles California USA': [[34.0536834, -118.2427669], 'Amerikanske bruddstykker '], 'Lisbon Portugal': [[38.7077507, -9.1365919], 'Amor de Perdio: Memrias de uma Famlia '], 'Viseu Portugal': [[40.6574713, -7.9138664], 'Amor de Perdio: Memrias de uma Famlia '], 'Coimbra Portugal': [[40.2109801, -8.4292057], 'Amor de Perdio: Memrias de uma Famlia '], 'Porto Portugal': [[37.239243, -121.8767664], 'Amor de Perdio: Memrias de uma Famlia ']}

print(test_dict)
locs = folium.FeatureGroup(name='Locations')
rich_locs = folium.FeatureGroup(name="Richest locations")

for i in test_dict.keys():
    locs.add_child(folium.Marker(location=test_dict[i][0],
                                 popup=create_popup(test_dict[i]),
                                 icon=folium.Icon()
                                 ))
    rich_locs.add_child(folium.CircleMarker(radius=5,
                                            location=test_dict[i][0],
                                            color=pick_color(len(test_dict[i]) - 1),
                                            fill_color=pick_color(len(test_dict[i]) - 1)
                                            ))
map.add_child(locs)
map.add_child(rich_locs)
map.add_child(folium.LayerControl())
map.save('map.html')

