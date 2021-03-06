from characters import characters
import requests # makes API requests (this is a third-party module)
# import json # convert the API data into python dictionaries and arrays
import time # module for working with timestamps

A_count = 0
# find characers beggining with A, then print them
for character in characters:
    if character['name'][0]  == 'A':
        A_count = A_count + 1

print(A_count)

zed_count = 0
# find characers beggining with A, then print them
for character in characters:
    if character['name'][0]  == 'Z':
        zed_count = zed_count + 1

print(zed_count)

dead_men = 0
for character in characters:
    if character['died'] != '':
        dead_men = dead_men + 1

print(dead_men)

lodsa_titles = 0
for character in characters:
    if lodsa_titles < len(character['titles']) :
        lodsa_titles = len(character['titles'])
        biggest = character['name']

print(biggest)

# # count the number of people who are part of a house
# def make_house_histogram(character_list):
#     histogram = {}

#     # do the thing!
#     # loop through all the characters
#     for person in character_list:

#         # what do I check for each person?
#         allegiances = person['allegiances']
#         # allegiances is a list of URLs!
#         # they look like this:
#         # ["https://www.anapioficeandfire.com/api/houses/77"]
#         for house in allegiances:
#             # do something with that house
#             if house in histogram:
#                 histogram[house] = histogram[house] + 1
#             else:
#                 histogram[house] = 1

#     return histogram

# def pretty_print_histogram(histogram):
#     for house in histogram:
#         print("%s has %d members" % (house, histogram[house]))

# def translate_address_to_house_name(URL):
#     house_name = ''
#     r = requests.get(URL)
#     house_info = r.json()
#     house_name = house_info['name']
#     return house_name

# def convert_to_nice_names(histogram):
#     nice_histogram = {} 

#     for url in histogram:
#         house_name = translate_address_to_house_name(url)
#         nice_histogram[house_name] = histogram[url]
#         time.sleep(0.1)

#     return nice_histogram

# # print(translate_address_to_house_name("https://www.anapioficeandfire.com/api/houses/122"))

# ugly_histogram = make_house_histogram(characters)
# pretty_histogram = convert_to_nice_names(ugly_histogram)
# pretty_print_histogram(pretty_histogram)

# pretty_print_histogram(make_house_histogram(characters))
# {
#  "https://www.anapioficeandfire.com/api/houses/77": 459,   
#  "https://www.anapioficeandfire.com/api/houses/78": 32,   
#  "https://www.anapioficeandfire.com/api/houses/79": 89,   
# }