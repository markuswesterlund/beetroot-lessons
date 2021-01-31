def make_country(country, capital):
    a_dict = {}
    a_dict['Name'] = country
    a_dict['Capital'] = capital
    for key, value in a_dict.items():
        a_dict[key] = value
    return a_dict


tot_val = make_country('Stockholm', 'Sweden')

print(tot_val)
