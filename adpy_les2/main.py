from countrylinks_class import CountryLinks
from making_hashstr import making_hashstrings

url = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'

with open('country_links.txt', 'w', encoding='utf-8') as write_file:
    for line in CountryLinks(url):
        write_file.write(line + '\n')

for hash_string in making_hashstrings():
    print(hash_string)
