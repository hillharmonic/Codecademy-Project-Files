"""
This code uses list data provided in the script to run multiple functions assessing hurrican data from 1924-2018. 

Results, mainly summary statistics, will from this code will print in the terminal. 
"""

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
print('\n')
print('This is the updated damages list. Values with markers for millions or billions have been converted to floats.')
def update_damages(damages):
    conversion = {'M': 1000000, 'B': 1000000000}
    updated_damages = []

    for i in damages:
        if i == 'Damages not recorded':
            updated_damages.append(i)
        if i[-1] == 'M':
            updated_damages.append(float(i.strip('M'))*conversion['M'])
        if i[-1] == 'B':
            updated_damages.append(float(i.strip('B'))*conversion['B'])
    return updated_damages

updated_damages = update_damages(damages)
print(updated_damages)
print('\n')

# write your construct hurricane dictionary function here:
print('This is the dictionary of hurricanes by name. Given value is "Cuba I"')
def construct_hurricane_dictionary():
    hurricane_dictionary = {}
    num_hurricanes = len(names)
    for i in range(num_hurricanes):
        hurricane_dictionary[names[i]] = {'Name': names[i],
                                        'Month': months[i],
                                        'Year': years[i],
                                        'Max Sustained Wind': max_sustained_winds[i],
                                        'Areas Affected': areas_affected[i],
                                        'Damage': updated_damages[i],
                                        'Deaths': deaths[i]}
    return hurricane_dictionary

hurricane_dictionary = construct_hurricane_dictionary()
print(hurricane_dictionary['Cuba I']) 
print('\n')

# write your construct hurricane by year dictionary function here:

print('This is the dictionary of hurricanes by Year. Given value is "1924"')
def year_dict():
    year_dict = {}
    for n,m,y,m,a,da,de in zip(names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths):
        year_dict[y] = {'Name': n, 'Month': m, 'Year': y, 'Max Sustained Wind': m, 'Areas Affected':a, 'Damage': da, 'Deaths': de}
    return year_dict

year_dict = year_dict()
print(year_dict[1924])
print('\n')

# write your count affected areas function here:
print('This is the count of each area affected.')

list_of_areas = []
for x in areas_affected:
    for area in x:
        if area not in list_of_areas:
            list_of_areas.append(area)
list_of_areas.sort()


def count_areas_affected():
    areas_damage_count = {}
    
    for z in list_of_areas:
        areas_damage_count[z] = 0

    for n in names:
        for a in hurricane_dictionary[n]['Areas Affected']:
            areas_damage_count[a] += 1
    return areas_damage_count

areas_damage_count = count_areas_affected()
print(areas_damage_count)
print('\n')

# write your find most affected area function here:

def most_hit_area():
    max_hit_area = 'Default'
    max_hit_num = 0

    for area in list_of_areas:
        if areas_damage_count[area] > max_hit_num:
            max_hit_area = area
            max_hit_num = areas_damage_count[area]
    return('The most hit area is ' + max_hit_area + ' with a hit count of ' + str(max_hit_num) + '.')
print(most_hit_area())
print('\n')

# write your greatest number of deaths function here:

def most_deaths():
    max_deaths_hurricane = 'Default'
    max_deaths = 0

    for n in names:
        if hurricane_dictionary[n]['Deaths'] > max_deaths:
            max_deaths_hurricane = n
            max_deaths = hurricane_dictionary[n]['Deaths']
    return('The most deadly hurricane is ' + max_deaths_hurricane + ' with ' + str(max_deaths) + ' deaths.')

most_deaths = most_deaths()
print(most_deaths)
print('\n')

# write your catgeorize by mortality function here:

print('This is the categorization of hurricanes by mortality rate.')
def mortality_function():
    mortality_rates = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

    for h in hurricane_dictionary:
        deaths = hurricane_dictionary[h]['Deaths']
        if deaths == 0:
            rating = 0
        elif deaths > 0 and deaths <= 100: 
            rating = 1
        elif deaths > 100 and deaths <= 500:
            rating = 2
        elif deaths > 500 and deaths <= 1000:
            rating = 3
        elif deaths > 1000 and deaths <= 10000:
            rating = 4
        else:
            rating = 5

        mortality_rates[rating].append(h)
    return mortality_rates

mortality_rates = mortality_function()
print(mortality_rates)
print('\n')
        
# write your greatest damage function here:

def max_damage():
    max_damage_hurricane = 'Default'
    max_damage = 0

    for h in hurricane_dictionary:
        if hurricane_dictionary[h]['Damage'] == 'Damages not recorded':
            continue
        if hurricane_dictionary[h]['Damage'] > max_damage:
            max_damage = hurricane_dictionary[h]['Damage']
            max_damage_hurricane = h
    return('Hurricane ' + max_damage_hurricane + ' dealt the most damage with $' + str(max_damage) + ' worth of Damages.')

max_damage = max_damage()
print(max_damage)
print('\n')

# write your catgeorize by damage function here:
print('This is the categorization of hurricanes by damages.')
def damage_function():
    damage_ratings = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 'Not Recorded': []}

    for h in hurricane_dictionary:
        damage = hurricane_dictionary[h]['Damage']
        if damage == 'Damages not recorded':
            rating = 'Not Recorded'
        elif damage == 0:
            rating = 0
        elif damage > 0 and damage <= 100000000: 
            rating = 1
        elif damage > 100000000 and damage <= 1000000000:
            rating = 2
        elif damage > 1000000000 and damage <= 10000000000:
            rating = 3
        elif damage > 10000000000 and damage <= 50000000000:
            rating = 4
        else:
            rating = 5
        
        damage_ratings[rating].append(h)
    return(damage_ratings)

damage_ratings = damage_function()
print(damage_ratings)        