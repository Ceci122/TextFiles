input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        # code_lookup[code.casefold()] = country
        countries[code.casefold()] = country_dict

# print(countries)
while True:
    chosen_country = input('Please enter the name of the country: ')#.casefold() # input can be uppercase or lowercase
    country_key = chosen_country.casefold() # keeps case fold
    if country_key in countries:
        country_data = countries[country_key]  # retrieves values for chosen country
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == 'quit':
        break
