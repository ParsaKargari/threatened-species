# Done by Parsa Kargari & Atonu Dey 12/9/2021
# Reads the data from csv files and manipulates data from them into useful, and presentable information
# Graphs are also plotted to present the data in the best possible way
#
#

# need to import numpy for using array calculations
# need to import matplotlib.pyplot for graphing and plotting
import numpy as np
import matplotlib.pyplot as plt


# CLASSES
#

class Country():
    '''
    Country class takes in information that was calculated by the functions and presents/prints them for the user on the terminal.
    Also is able to calculate the density based on the passed by population and area

    Arguments:
    country - country name of the user's choice
    population - the population of that country
    area - the area of that country
    rank - the rank of that country, when compared to other countries based on their population density worldwide
    poplower - the population of the country at the starting entered year
    pophigher - the population of the country at the ending/stop entered year
    yearlow - the year at which the poplower occured
    yearhigh - the year at which the pophigher occured
    top_list - all countries in a list from greatest to least based on their population density
    sorted_density1 - all population densities in a list from greatest to least
    year_chosen1 - the year that is chosen by the user

    Methods:
    get_country_density - doesnt return anything, prints the country, it's population density and the rank at the chosen year
    top_countries_density - doesnt return anything, prints the countries ranked top in population density. Country names and the density of them
    density_diff_info - doesnt return anything, prints the country population density at the first entered year and as well as the second. Also prints the change in population density

    '''
    def __init__(self, country, population, area, rank, poplower, pophigher, yearlow, yearhigh, top_list, sorted_density1, year_chosen1):
        self.country = country
        self.population = population
        self.area = area
        self.rank = rank
        self.poplower = poplower
        self.pophigher = pophigher
        self.yearlow = yearlow
        self.yearhigh = yearhigh
        self.top_list = top_list
        self.sorted_density1 = sorted_density1
        self.year_chosen1 = year_chosen1

    def get_country_density(self):
        self.density = float(self.population) / float(self.area)
        print('--------'*5)
        print('')
        print(f'{self.country}\'s population density is {self.density:.2f} and its rank in {self.year_chosen1}: #{self.rank} globally.')

    def top_countries_density(self):
        print(f'The top 5 countries with the highest population density globally:')
        print(f'{self.top_list[0]}: {self.sorted_density1[0]:.2f}, {self.top_list[1]}: {self.sorted_density1[1]:.2f}, {self.top_list[2]}: {self.sorted_density1[2]:.2f}, {self.top_list[3]}: {self.sorted_density1[3]:.2f}, {self.top_list[4]}: {self.sorted_density1[4]:.2f}\n\n')
        print('--------'*5)

    def density_diff_info(self):
        print('--------'*5)
        print('')
        print(f'{self.country}\'s population density was {float(self.poplower) / float(self.area):.2f} in {self.yearlow} and it changed to {float(self.pophigher) / float(self.area):.2f} in {self.yearhigh}.')
        print(f'That is a total change of {((float(self.pophigher) / float(self.area)) - (float(self.poplower) / float(self.area))):.2f} in population density.')
        

class Region():
    '''
    Region class which takes in the information regarding regions and sub-regions that was calculated by functions and main(), and presents them to the user in the terminal

    Arguments:
    region - the user selected region
    year - the user selected year
    density - the population density of the region during the selected year
    sorted_density2 - the population densities ranked from highest to least
    sorted_regions2 - the sorted region names ranked from highest to least based on population density / This can also be for subregions when we're calculating for subregion and not region
    year_2000_dens - the population density during the year 2000
    top_list - the countries with the highest population densities that are in the region or sub-region

    Methods:
    print_region_info - doesnt return anything, prints the information regarding the region. Prints the region name, the year, gets the change in population density when compared to the year 2000
                        displays the top and low ranked regions, and also prints the countries ranked the highest and lowest within the region

    print_subregion_info - doesnt return anything, prints the information regarding the subregion. Prints the subregion name, the year, gets the change in population density when compared to the year 2000
                            displays the top and low ranked subregions, and also prints the countries ranked the highest and lowest within the subregion
    '''
    def __init__(self, region, year, density, sorted_density2, sorted_regions2, year_2000_dens, top_list):
        self.region = region
        self.year = year
        self.density = density
        self.sorted_density2 = sorted_density2
        self.sorted_regions2 = sorted_regions2
        self.year_2000_dens = year_2000_dens
        self.top_list = top_list

    def print_region_info(self):
        print('--------'*5)
        print('')
        print(f'In {self.region} at {self.year} the population density was found to be {self.density:.2f}. This is a difference of {self.density - self.year_2000_dens:.2f} ({self.year_2000_dens:.2f} in 2000) when compared to population density in the year 2000.')
        print(f'The 2 regions with the highest population density in the year {self.year} are: \n{self.sorted_regions2[0]}: {self.sorted_density2[0]:.2f}, {self.sorted_regions2[1]}: {self.sorted_density2[1]:.2f}')
        print(f'The 2 regions with the lowest population density in the year {self.year} are: \n{self.sorted_regions2[-1]}: {self.sorted_density2[-1]:.2f}, and {self.sorted_regions2[-2]}: {self.sorted_density2[-2]:.2f}')
        print(f'\n{self.top_list[0]}, {self.top_list[1]}, {self.top_list[2]} are countries with the highest population density, where {self.top_list[-1]}, {self.top_list[-2]}, and {self.top_list[-3]} are countries with the lowest population density in {self.region}.')
        print('')
        print('--------'*5)

    def print_subregion_info(self):
        print('--------'*5)
        print('')
        print(f'In {self.region} at {self.year} the population density was found to be {self.density:.2f}. This is a difference of {self.density - self.year_2000_dens:.2f} ({self.year_2000_dens:.2f} in 2000) when compared to population density in the year 2000.')
        print(f'The 2 subregions with the highest population density in the year {self.year} are: \n{self.sorted_regions2[0]}: {self.sorted_density2[0]:.2f}, {self.sorted_regions2[1]}: {self.sorted_density2[1]:.2f}')
        print(f'The 2 subregions with the lowest population density in the year {self.year} are: \n{self.sorted_regions2[-1]}: {self.sorted_density2[-1]:.2f}, and {self.sorted_regions2[-2]}: {self.sorted_density2[-2]:.2f}')
        print(f'\n{self.top_list[0]}, {self.top_list[1]}, {self.top_list[2]} are countries with the highest population density, where {self.top_list[-1]}, and {self.top_list[-2]}, are countries with the lowest population density in {self.region}.')
        print('')
        print('--------'*5)

# FUNCTIONS
#

def country_list(data_set):
    """A function that makes a list of countries from provided data set.

    Arguments:
    data_set -- Provided input set of data

    Returns:
    Returns the list of countries

    """
    country_list =[]
    for x in data_set:
        country_list.append(x[0])
    return country_list

def print_menu():
    print('-------------------------------------------------')
    print('(1) Population Density by Country')
    print('(2) Population Density by Region / Sub-Region')
    print('(3) Species Threatened by Country')
    print('(4) Species Threatened by Region / Sub-Region')
    print('(5) Thank You')
    print('(6) Exit')
    print('-------------------------------------------------')
    print('')

def dict_maker(list_1, list_2):
    """A function that makes a dictionary from two lists.

    Arguments:
    list_1 -- Represents first input list
    list_2 -- Represents seceond input list

    Returns:
    Returns a dictionary made of two lists

    """
    new_dict = dict(zip(list_1, list_2))

    return new_dict

def rank_counter(user_country, sort_list):
    """A function that calculates the rank of a country from a list.

    Arguments:
    user_country -- Represents the input country
    sort_list -- Represents the input list where rank is to be selected from

    Returns:
    Returns the rank of the country

    """
    country_rank = 0
    for rank, country in enumerate(sort_list):
            if country == user_country:
                country_rank = rank + 1

    return country_rank

def overall_rank_calc(country, data_set):
    """A function that calculates rank of input country from provided data set and prints it out.

    Arguments:
    country -- Represents the input country
    data_set -- Represents the provided data set

    Returns:
    None

    """

    sum_list = []                                                                                                           # Empty list for loop

    for x in data_set:                                                                                                      # Condition for initiating loop
        sum_species = x[1] + x[2] + x[3] + x[4]

        sum_list.append(sum_species)                                                                                        # Appends the total of each species of countries to the list

    dict_country_overall = dict_maker(country_list(data_set), sum_list)                                                     # Making the country list and total species list into dictionary

    sort_overall = sorted(dict_country_overall, key = dict_country_overall.get, reverse = True)                             # Sorting dictionary through values and getting keys in descending order
        
    total_rank = rank_counter(country, sort_overall)                                                                        # Calling rank_counter function

    print(f'{country:} ranks #{total_rank:} in the number of threatened species of all types.')



def threaten_by_country(country_input,species_check,data_set):
    """
    A function that inputs a country and an option for species and prints the rank, 
    percentage threatened compared to other species, top 3 countries with the highest threatened species,
    overall ranking and plots the bar graph comparing the output to the top countries.

    Arguments:
    country_input -- Represents the country input
    species_check -- Represents the selection of species
    data_set -- Represents the provided data set

    Returns:
    None

    """
        
    if species_check == '1':                                                                                                # Condition when species is Plants 
        threat_list = []
        
        sum_threat_list = []

        for x in data_set[1:]:                                                                                                  # Condition for appending threat list and sum threat list
            threat_list.append(int(x[1]))
            
            sum_of_threat = int(x[1]) + int(x[2]) + int(x[3]) + int(x[4])

            sum_threat_list.append(sum_of_threat)


        dict_country = dict_maker(country_list(data_set[1:]), threat_list)                                                      # Calling dict_maker function with country list and threat list

        sort_dict = sorted(dict_country, key= dict_country.get, reverse= True)                                              # Sorting the new dictionary according to value and getting list of keys in descending order

        dict_sum_threat = dict_maker(country_list(data_set[1:]), sum_threat_list)                                               # Calling dict_maker function with country list and sum list 

        sort_sum_threat = sorted(dict_sum_threat, key= dict_sum_threat.get, reverse= True)                                  # Sorting the sum of threat lists according to values and getting keys in descending order

        sum_threat_list.sort(reverse = True)
        threat_list.sort(reverse = True)
        
        rank_country = rank_counter(country_input, sort_dict) 
        rank_country_total = rank_counter(country_input, sort_sum_threat)

        percentage_of_total = ((threat_list[rank_country-1])*100/(sum_threat_list[rank_country_total-1]))                   # Percentage of threatened plant species out of total threatened species
        
        print(f'{data_set[0][1]}:\n{country_input:} ranks #{rank_country:} in number of threatened species of {data_set[0][1]}')
        print(f'Number of threatened {data_set[0][1]} species: {threat_list[rank_country-1]:}')
        print(f'{data_set[0][1]} are {percentage_of_total:.3f}% of the total threatened species of {country_input:}.')
        print(f'Top 3 countries with the highest threatened species of {data_set[0][1]}:\n')
        print(f'{sort_dict[0]:}:{threat_list[0]:}\n{sort_dict[1]:}:{threat_list[1]:}\n{sort_dict[2]:}:{threat_list[2]:}')
        overall_rank_calc(country_input, data_set[1:])                                                                          # Calling overall_rank_calc function

        country_comparison = [sort_dict[0], sort_dict[1], sort_dict[2], country_input]                                      # List for x-axis

        num_comparison = [threat_list[0], threat_list[1], threat_list[2], threat_list[rank_country-1]]                      # List for y-axis

        good_colors = ['#2193b0', '#33b7d9', '#54c3df', '#75cee5' ]                                                         # List for color of graph

        
        
        plt.bar(country_comparison, num_comparison, color = good_colors)
        plt.title('Comparison of Input Country with Others', fontsize= 14)                                                  # Title of plot
        plt.xlabel('Country', fontsize= 14)                                                                                 # Label of x-axis
        plt.ylabel(f'Threatened species of {data_set[0][1]}', fontsize= 14)                                                            # Label of y-axis
        plt.show()

    elif species_check == '2':                                                                                              # Condition when species is Fish
        threat_list = []
        
        sum_threat_list = []
        for x in data_set[1:]:                                                                                                  # Condition for appending threat list and sum threat list
            threat_list.append(int(x[2]))

            sum_of_threat = int(x[1]) + int(x[2]) + int(x[3]) + int(x[4])

            sum_threat_list.append(sum_of_threat)
        
        dict_country = dict_maker(country_list(data_set[1:]), threat_list)                                                      # Calling dict_maker function with country list and threat list

        sort_dict = sorted(dict_country, key= dict_country.get, reverse= True)                                              # Sorting the new dictionary according to value and getting list of keys in descending order

        dict_sum_threat = dict_maker(country_list(data_set[1:]), sum_threat_list)                                               # Calling dict_maker function with country list and sum list

        sort_sum_threat = sorted(dict_sum_threat, key= dict_sum_threat.get, reverse= True)                                  # Sorting the sum of threat lists according to values and getting keys in descending order

        sum_threat_list.sort(reverse = True)
        
        rank_country = rank_counter(country_input, sort_dict)
        rank_country_total = rank_counter(country_input, sort_sum_threat)
        threat_list.sort(reverse = True)

        percentage_of_total = ((threat_list[rank_country-1])*100/(sum_threat_list[rank_country_total-1]))                   # Percentage of threatened plant species out of total threatened species

        print(f'{data_set[0][2]}:\n{country_input:} ranks #{rank_country:} in number of threatened species of {data_set[0][2]}')
        print(f'Number of threatened {data_set[0][2]} species: {threat_list[rank_country-1]:}')
        print(f'{data_set[0][2]} are {percentage_of_total:.3f}% of the total threatened species of {country_input:}.')
        print(f'Top 3 countries with the highest threatened species of {data_set[0][2]}:\n')
        print(f'{sort_dict[0]:}:{threat_list[0]:}\n{sort_dict[1]:}:{threat_list[1]:}\n{sort_dict[2]:}:{threat_list[2]:}')
        overall_rank_calc(country_input, data_set[1:])                                                                          # Calling overall_rank_calc function

        country_comparison = [sort_dict[0], sort_dict[1], sort_dict[2], country_input]                                      # List for x-axis

        num_comparison = [threat_list[0], threat_list[1], threat_list[2], threat_list[rank_country-1]]                      # List for y-axis

        good_colors = ['#2193b0', '#33b7d9', '#54c3df', '#75cee5' ]                                                         # List for color of graph

        

        plt.bar(country_comparison, num_comparison, color = good_colors)
        plt.title('Comparison of Input Country with Others', fontsize= 14)                                                  # Title of plot
        plt.xlabel('Country', fontsize= 14)                                                                                 # Label of x-axis
        plt.ylabel(f'Threatened species of {data_set[0][2]}', fontsize= 14)                                                              # Label of y-axis
        plt.show()

        

    elif species_check == '3':                                                                                              # Condition when species is Birds
        threat_list = []
        
        sum_threat_list = []
        for x in data_set[1:]:                                                                                                  # Condition for appending threat list and sum threat list
            threat_list.append(int(x[3]))

            sum_of_threat = int(x[1]) + int(x[2]) + int(x[3]) + int(x[4])

            sum_threat_list.append(sum_of_threat)
        
        dict_country = dict_maker(country_list(data_set[1:]), threat_list)                                                      # Calling dict_maker function with country list and threat list

        sort_dict = sorted(dict_country, key= dict_country.get, reverse= True)                                              # Sorting the new dictionary according to value and getting list of keys in descending order

        dict_sum_threat = dict_maker(country_list(data_set[1:]), sum_threat_list)                                               # Calling dict_maker function with country list and sum list

        sort_sum_threat = sorted(dict_sum_threat, key= dict_sum_threat.get, reverse= True)                                  # Sorting the sum of threat lists according to values and getting keys in descending order

        sum_threat_list.sort(reverse = True)

        rank_country = rank_counter(country_input, sort_dict)
        rank_country_total = rank_counter(country_input, sort_sum_threat)
        threat_list.sort(reverse = True)

        percentage_of_total = ((threat_list[rank_country-1])*100/(sum_threat_list[rank_country_total-1]))                   # Percentage of threatened plant species out of total threatened species
        
        print(f'{data_set[0][3]}:\n{country_input:} ranks #{rank_country:} in number of threatened species of {data_set[0][3]}')
        print(f'Number of threatened Bird species: {threat_list[rank_country-1]:}')
        print(f'{data_set[0][3]} are {percentage_of_total:.3f}% of the total threatened species of {country_input:}.')
        print(f'Top 3 countries with the highest threatened species of {data_set[0][3]}:\n')
        print(f'{sort_dict[0]:}:{threat_list[0]:}\n{sort_dict[1]:}:{threat_list[1]:}\n{sort_dict[2]:}:{threat_list[2]:}')
        overall_rank_calc(country_input, data_set[1:])                                                                          # Calling overall_rank_calc function

        country_comparison = [sort_dict[0], sort_dict[1], sort_dict[2], country_input]                                      # List for x-axis

        num_comparison = [threat_list[0], threat_list[1], threat_list[2], threat_list[rank_country-1]]                      # List for y-axis

        good_colors = ['#2193b0', '#33b7d9', '#54c3df', '#75cee5' ]                                                         # List for color of graph

        
        plt.bar(country_comparison, num_comparison, color = good_colors)
        plt.title('Comparison of Input Country with Others', fontsize= 14)                                                  # Title of plot
        plt.xlabel('Country', fontsize= 14)                                                                                 # Label of x-axis
        plt.ylabel(f'Threatened species of {data_set[0][3]}', fontsize= 14)                                                             # Label of y-axis
        plt.show()


    elif species_check == '4':                                                                                              # Condition when species is Mammals
        threat_list = []
        
        sum_threat_list = []
        for x in data_set[1:]:                                                                                                  # Condition for appending threat list and sum threat list
            threat_list.append(int(x[4]))

            sum_of_threat = int(x[1]) + int(x[2]) + int(x[3]) + int(x[4])

            sum_threat_list.append(sum_of_threat)
        
        dict_country = dict_maker(country_list(data_set[1:]), threat_list)                                                      # Calling dict_maker function with country list and threat list

        sort_dict = sorted(dict_country, key= dict_country.get, reverse= True)                                              # Sorting the new dictionary according to value and getting list of keys in descending order
        
        dict_sum_threat = dict_maker(country_list(data_set[1:]), sum_threat_list)                                               # Calling dict_maker function with country list and sum list

        sort_sum_threat = sorted(dict_sum_threat, key= dict_sum_threat.get, reverse= True)                                  # Sorting the sum of threat lists according to values and getting keys in descending order

        sum_threat_list.sort(reverse = True)
        threat_list.sort(reverse = True)
        rank_country = rank_counter(country_input, sort_dict)
        rank_country_total = rank_counter(country_input, sort_sum_threat)

        percentage_of_total = ((threat_list[rank_country-1])*100/(sum_threat_list[rank_country_total-1]))                   # Percentage of threatened plant species out of total threatened species

        print(f'{data_set[0][4]}:\n{country_input:} ranks #{rank_country:} in number of threatened species of {data_set[0][4]}')
        print(f'Number of threatened {data_set[0][4]} species: {threat_list[rank_country-1]:}')
        print(f'{data_set[0][4]} are {percentage_of_total:.3f}% of the total threatened species of {country_input:}.')
        print(f'Top 3 countries with the highest threatened species of {data_set[0][4]}:\n')
        print(f'{sort_dict[0]:}:{threat_list[0]:}\n{sort_dict[1]:}:{threat_list[1]:}\n{sort_dict[2]:}:{threat_list[2]:}')
        overall_rank_calc(country_input, data_set[1:])                                                                          # Calling overall_rank_calc function

        country_comparison = [sort_dict[0], sort_dict[1], sort_dict[2], country_input]                                      # List for x-axis

        num_comparison = [threat_list[0], threat_list[1], threat_list[2], threat_list[rank_country-1]]                      # List for y-axis

        good_colors = ['#2193b0', '#33b7d9', '#54c3df', '#75cee5' ]                                                         # List for color of graph

        
        plt.bar(country_comparison, num_comparison, color = good_colors)
        plt.title('Comparison of Input Country with Others', fontsize= 14)                                                  # Title of plot
        plt.xlabel('Country',fontsize= 14)                                                                                  # Label of x-axis
        plt.ylabel(f'Threatened species of {data_set[0][4]}', fontsize= 14)                                                           # Label of y-axis
        plt.show()

        
    else:
        print('Enter a valid option')

def threaten_by_region(region, species_check, data_set_species, data_set_region):
    """
    A function that inputs the region and an option for species and prints the 
    number of countries in that region, the top 3 countries with the highest number 
    threatened species, the top 3 countries with the lowest number of threatened species and 
    a pie chart comparing the high ranked countries to the total threatened species in that
    region in percentage.

    Arguments:
    region -- Represents the input region
    species_check -- Represents the selection of species
    data_set_species -- Represents the provided data set for species
    data_set_region -- Represents the provided data set for country and region

    Returns:
    None

    """

    threat_list = []                                                                                                                                                    # Initial empty list

    country_in_region = country_list_region(data_set_region[1:], region)                                                                                                    # Making a list of countries in the input region

    if species_check == '1':                                                                                                                                            # Condition when species is Plant
        for i in country_in_region:                                                                                                                                     # Condition for appending threat list 
            for x in data_set_species[1:]:
                if i == x[0]:
                    threat_list.append(int(x[1]))
            
        sum_whole_region = np.sum(threat_list)                                                                                                                          # Summing over all the elements of threat_list
        
        region_threat_dict = dict_maker(country_in_region, threat_list)                                                                                                 # Calling dict_maker function with countries of region list and threat list

        sort_dict = sorted(region_threat_dict, key= region_threat_dict.get, reverse= True)                                                                              # Sorting the new dictionary according to value and getting list of keys in descending order

        threat_list.sort(reverse = True)                                                                                                                                # Sorting threat_list in descending order
        
        print(f'{region:} has {len(country_in_region):} countries, of which the countries with the highest threatened species of {data_set_species[0][1]} are as follows:\n')
        print(f'{sort_dict[0]:}: {threat_list[0]:}\n{sort_dict[1]:}: {threat_list[1]:}\n{sort_dict[2]:}: {threat_list[2]:}')
        print(f'\nThe countries with the lowest threatened species of {data_set_species[0][1]} are:\n')
        print(f'{sort_dict[-1]:}: {threat_list[-1]:}\n{sort_dict[-2]:}: {threat_list[-2]:}\n{sort_dict[-3]:}: {threat_list[-3]:}')

        percent_1_country = float((threat_list[0]*100)/(sum_whole_region))                                                                                              # Percentage of rank 1 country's threatened species 
        percent_2_country = float((threat_list[1]*100)/(sum_whole_region))                                                                                              # Percentage of rank 2 country's threatened species
        percent_3_country = float((threat_list[2]*100)/(sum_whole_region))                                                                                              # Percentage of rank 3 country's threatened species
        other_percent = 100 - (percent_1_country + percent_2_country + percent_3_country)                                                                               # Percentage of the rest of the countries' threatened species
        
        my_explode = [0.2, 0.2, 0.2, 0]                                                                                                                                 # Explode list

        plt.pie([percent_1_country, percent_2_country, percent_3_country, other_percent], 
        labels= [sort_dict[0], sort_dict[1], sort_dict[2], 'Others'], 
        explode= my_explode ,shadow= True)                                                                                                                              # Pie chart plot
        plt.title(f'Percentage of Threatened {data_set_species[0][1]} in {region:}', pad= 20, fontsize= 14)                                                                               # Title of pie chart
        plt.show()

    elif species_check == '2':                                                                                                                                          # Condition when species is Fish
        for i in country_in_region:                                                                                                                                     # Condition for appending threat list
            for x in data_set_species[1:]:
                if i == x[0]:
                    threat_list.append(int(x[2]))
            
        sum_whole_region = np.sum(threat_list)                                                                                                                          # Summing over all the elements of threat_list
        
        region_threat_dict = dict_maker(country_in_region, threat_list)                                                                                                 # Calling dict_maker function with countries of region list and threat list

        sort_dict = sorted(region_threat_dict, key= region_threat_dict.get, reverse= True)                                                                              # Sorting the new dictionary according to value and getting list of keys in descending order

        threat_list.sort(reverse = True)                                                                                                                                # Sorting threat_list in descending order
        
        print(f'{region:} has {len(country_in_region):} countries, of which the countries with the highest threatened species of {data_set_species[0][2]} are as follows:\n')
        print(f'{sort_dict[0]:}: {threat_list[0]:}\n{sort_dict[1]:}: {threat_list[1]:}\n{sort_dict[2]:}: {threat_list[2]:}')
        print(f'\nThe countries with the lowest threatened species of {data_set_species[0][2]} are:\n')
        print(f'{sort_dict[-1]:}: {threat_list[-1]:}\n{sort_dict[-2]:}: {threat_list[-2]:}\n{sort_dict[-3]:}: {threat_list[-3]:}')

        percent_1_country = float((threat_list[0]*100)/(sum_whole_region))                                                                                              # Percentage of rank 1 country's threatened species 
        percent_2_country = float((threat_list[1]*100)/(sum_whole_region))                                                                                              # Percentage of rank 2 country's threatened species 
        percent_3_country = float((threat_list[2]*100)/(sum_whole_region))                                                                                              # Percentage of rank 3 country's threatened species 
        other_percent = 100 - (percent_1_country + percent_2_country + percent_3_country)                                                                               # Percentage of the rest of the countries' threatened species
        
        my_explode = [0.2, 0.2, 0.2, 0]                                                                                                                                 # Explode list

        plt.pie([percent_1_country, percent_2_country, percent_3_country, other_percent], 
        labels= [sort_dict[0], sort_dict[1], sort_dict[2], 'Others'], 
        explode= my_explode ,shadow= True)                                                                                                                              # Pie chart plot
        plt.title(f'Percentage of Threatened {data_set_species[0][2]} in {region:}', pad= 20, fontsize= 14)                                                                                 # Title of pie chart
        plt.show()


    elif species_check == '3':                                                                                                                                          # Condition when species is Bird
        for i in country_in_region:                                                                                                                                     # Condition for appending threat list
            for x in data_set_species[1:]:
                if i == x[0]:
                    threat_list.append(int(x[3]))
            
        sum_whole_region = np.sum(threat_list)                                                                                                                          # Summing over all the elements of threat_list
        
        region_threat_dict = dict_maker(country_in_region, threat_list)                                                                                                 # Calling dict_maker function with countries of region list and threat list

        sort_dict = sorted(region_threat_dict, key= region_threat_dict.get, reverse= True)                                                                              # Sorting the new dictionary according to value and getting list of keys in descending order

        threat_list.sort(reverse = True)                                                                                                                                # Sorting threat_list in descending order
        
        print(f'{region:} has {len(country_in_region):} countries, of which the countries with the highest threatened species of {data_set_species[0][3]} are as follows:\n')
        print(f'{sort_dict[0]:}: {threat_list[0]:}\n{sort_dict[1]:}: {threat_list[1]:}\n{sort_dict[2]:}: {threat_list[2]:}')
        print(f'\nThe countries with the lowest threatened species of {data_set_species[0][3]} are:\n')
        print(f'{sort_dict[-1]:}: {threat_list[-1]:}\n{sort_dict[-2]:}: {threat_list[-2]:}\n{sort_dict[-3]:}: {threat_list[-3]:}')

        percent_1_country = float((threat_list[0]*100)/(sum_whole_region))                                                                                              # Percentage of rank 1 country's threatened species 
        percent_2_country = float((threat_list[1]*100)/(sum_whole_region))                                                                                              # Percentage of rank 2 country's threatened species 
        percent_3_country = float((threat_list[2]*100)/(sum_whole_region))                                                                                              # Percentage of rank 3 country's threatened species 
        other_percent = 100 - (percent_1_country + percent_2_country + percent_3_country)                                                                               # Percentage of the rest of the countries' threatened species
        
        my_explode = [0.2, 0.2, 0.2, 0]                                                                                                                                 # Explode list

        plt.pie([percent_1_country, percent_2_country, percent_3_country, other_percent], 
        labels= [sort_dict[0], sort_dict[1], sort_dict[2], 'Others'], 
        explode= my_explode ,shadow= True)                                                                                                                              # Pie chart plot
        plt.title(f'Percentage of Threatened {data_set_species[0][3]} in {region:}', pad= 20, fontsize= 14)                                                                                # Title of pie chart
        plt.show()


    elif species_check == '4':                                                                                                                                          # Condition when species is Mammal
        for i in country_in_region:                                                                                                                                     # Condition for appending threat list
            for x in data_set_species[1:]:
                if i == x[0]:
                    threat_list.append(int(x[4]))
            
        sum_whole_region = np.sum(threat_list)                                                                                                                          # Summing over all the elements of threat_list
        
        region_threat_dict = dict_maker(country_in_region, threat_list)                                                                                                 # Calling dict_maker function with countries of region list and threat list

        sort_dict = sorted(region_threat_dict, key= region_threat_dict.get, reverse= True)                                                                              # Sorting the new dictionary according to value and getting list of keys in descending order

        threat_list.sort(reverse = True)                                                                                                                                # Sorting threat_list in descending order
        
        print(f'{region:} has {len(country_in_region):} countries, of which the countries with the highest threatened species of {data_set_species[0][4]} are as follows:\n')
        print(f'{sort_dict[0]:}: {threat_list[0]:}\n{sort_dict[1]:}: {threat_list[1]:}\n{sort_dict[2]:}: {threat_list[2]:}')
        print(f'The countries with the lowest threatened species of {data_set_species[0][4]} are:\n')
        print(f'{sort_dict[-1]:}: {threat_list[-1]:}\n{sort_dict[-2]:}: {threat_list[-2]:}\n{sort_dict[-3]:}: {threat_list[-3]:}')

        percent_1_country = float((threat_list[0]*100)/(sum_whole_region))                                                                                              # Percentage of rank 1 country's threatened species 
        percent_2_country = float((threat_list[1]*100)/(sum_whole_region))                                                                                              # Percentage of rank 2 country's threatened species 
        percent_3_country = float((threat_list[2]*100)/(sum_whole_region))                                                                                              # Percentage of rank 3 country's threatened species 
        other_percent = 100 - (percent_1_country + percent_2_country + percent_3_country)                                                                               # Percentage of the rest of the countries' threatened species
        
        my_explode = [0.2, 0.2, 0.2, 0]                                                                                                                                 # Explode list

        plt.pie([percent_1_country, percent_2_country, percent_3_country, other_percent], 
        labels= [sort_dict[0], sort_dict[1], sort_dict[2], 'Others'], 
        explode= my_explode ,shadow= True)                                                                                                                              # Pie chart plot
        plt.title(f'Percentage of Threatened {data_set_species[0][4]} in {region:}', pad= 20, fontsize= 14)                                                                              # Title of pie chart
        plt.show()

    else:
        print('Enter a valid option.')

def threaten_by_subregion(subregion, species_check, data_set_species, data_set_subregion):
    """
    A function that inputs the subregion and an option for species and prints the 
    number of countries in that subregion, the top 3 countries with the highest number 
    threatened species, the top 3 countries with the lowest number of threatened species and 
    a pie chart comparing the high ranked countries to the total threatened species in that
    subregion in percentage.

    Arguments:
    subregion -- Represents the input subregion
    species_check -- Represents the selection of species
    data_set_species -- Represents the provided data set for species
    data_set_subregion -- Represents the provided data set for country and subregion

    Returns:
    None

    """

    threat_list = []                                                                                                                                                    # Initial empty list

    country_in_subregion = country_list_subregion(data_set_subregion[1:], subregion)                                                                                        # Making a list of countries in the input region

    if species_check == '1':                                                                                                                                            # Condition when species is Plant
        for i in country_in_subregion:                                                                                                                                  # Condition for appending threat list 
            for x in data_set_species[1:]:
                if i == x[0]:
                    threat_list.append(int(x[1]))
            
        sum_whole_subregion = np.sum(threat_list)                                                                                                                       # Summing over all the elements of threat_list
        
        subregion_threat_dict = dict_maker(country_in_subregion, threat_list)                                                                                           # Calling dict_maker function with countries of subregion list and threat list

        sort_dict = sorted(subregion_threat_dict, key= subregion_threat_dict.get, reverse= True)                                                                        # Sorting the new dictionary according to value and getting list of keys in descending order

        threat_list.sort(reverse = True)                                                                                                                                # Sorting threat_list in descending order
        
        print(f'{subregion:} has {len(country_in_subregion):} countries, of which the countries with the highest threatened species of {data_set_species[0][1]} are as follows:\n')
        print(f'{sort_dict[0]:}: {threat_list[0]:}\n{sort_dict[1]:}: {threat_list[1]:}\n{sort_dict[2]:}: {threat_list[2]:}')
        print(f'\nThe countries with the lowest threatened species of {data_set_species[0][1]} are:\n')
        print(f'{sort_dict[-1]:}: {threat_list[-1]:}\n{sort_dict[-2]:}: {threat_list[-2]:}\n{sort_dict[-3]:}: {threat_list[-3]:}')
        
        percent_1_country = float((threat_list[0]*100)/(sum_whole_subregion))                                                                                           # Percentage of rank 1 country's threatened species 
        percent_2_country = float((threat_list[1]*100)/(sum_whole_subregion))                                                                                           # Percentage of rank 2 country's threatened species 
        percent_3_country = float((threat_list[2]*100)/(sum_whole_subregion))                                                                                           # Percentage of rank 3 country's threatened species 
        other_percent = 100 - (percent_1_country + percent_2_country + percent_3_country)                                                                               # Percentage of the rest of the countries' threatened species
        
        my_explode = [0.2, 0.2, 0.2, 0]                                                                                                                                 # Explode list

        plt.pie([percent_1_country, percent_2_country, percent_3_country, other_percent], 
        labels= [sort_dict[0], sort_dict[1], sort_dict[2], 'Others'], 
        explode= my_explode ,shadow= True)                                                                                                                              # Pie chart plot
        plt.title(f'Percentage of Threatened {data_set_species[0][1]} in {subregion:}', pad= 20, fontsize= 14)                                                                            # Title of pie chart
        plt.show()

    elif species_check == '2':                                                                                                                                          # Condition when species is Fish
        for i in country_in_subregion:                                                                                                                                  # Condition for appending threat list 
            for x in data_set_species[1:]:
                if i == x[0]:
                    threat_list.append(int(x[2]))
            
        sum_whole_subregion = np.sum(threat_list)                                                                                                                       # Summing over all the elements of threat_list
        
        subregion_threat_dict = dict_maker(country_in_subregion, threat_list)                                                                                           # Calling dict_maker function with countries of subregion list and threat list

        sort_dict = sorted(subregion_threat_dict, key= subregion_threat_dict.get, reverse= True)                                                                        # Sorting the new dictionary according to value and getting list of keys in descending order

        threat_list.sort(reverse = True)                                                                                                                                # Sorting threat_list in descending order
        
        print(f'{subregion:} has {len(country_in_subregion):} countries, of which the countries with the highest threatened species of {data_set_species[0][2]} are as follows:\n')
        print(f'{sort_dict[0]:}: {threat_list[0]:}\n{sort_dict[1]:}: {threat_list[1]:}\n{sort_dict[2]:}: {threat_list[2]:}')
        print(f'\nThe countries with the lowest threatened species of {data_set_species[0][2]} are:\n')
        print(f'{sort_dict[-1]:}: {threat_list[-1]:}\n{sort_dict[-2]:}: {threat_list[-2]:}\n{sort_dict[-3]:}: {threat_list[-3]:}')

        percent_1_country = float((threat_list[0]*100)/(sum_whole_subregion))                                                                                           # Percentage of rank 1 country's threatened species 
        percent_2_country = float((threat_list[1]*100)/(sum_whole_subregion))                                                                                           # Percentage of rank 2 country's threatened species 
        percent_3_country = float((threat_list[2]*100)/(sum_whole_subregion))                                                                                           # Percentage of rank 3 country's threatened species 
        other_percent = 100 - (percent_1_country + percent_2_country + percent_3_country)                                                                               # Percentage of the rest of the countries' threatened species
        
        my_explode = [0.2, 0.2, 0.2, 0]                                                                                                                                 # Explode list

        plt.pie([percent_1_country, percent_2_country, percent_3_country, other_percent], 
        labels= [sort_dict[0], sort_dict[1], sort_dict[2], 'Others'], 
        explode= my_explode ,shadow= True)                                                                                                                              # Pie chart plot
        plt.title(f'Percentage of Threatened {data_set_species[0][2]} in {subregion:}', pad= 20, fontsize= 14)                                                                              # Title of pie chart
        plt.show()


    elif species_check == '3':                                                                                                                                          # Condition when species is Bird
        for i in country_in_subregion:                                                                                                                                  # Condition for appending threat list 
            for x in data_set_species[1:]:
                if i == x[0]:
                    threat_list.append(int(x[3]))
            
        sum_whole_subregion = np.sum(threat_list)                                                                                                                       # Summing over all the elements of threat_list
        
        subregion_threat_dict = dict_maker(country_in_subregion, threat_list)                                                                                           # Calling dict_maker function with countries of subregion list and threat list

        sort_dict = sorted(subregion_threat_dict, key= subregion_threat_dict.get, reverse= True)                                                                        # Sorting the new dictionary according to value and getting list of keys in descending order

        threat_list.sort(reverse = True)                                                                                                                                # Sorting threat_list in descending order
        
        print(f'{subregion:} has {len(country_in_subregion):} countries, of which the countries with the highest threatened species of {data_set_species[0][3]} are as follows:\n')
        print(f'{sort_dict[0]:}: {threat_list[0]:}\n{sort_dict[1]:}: {threat_list[1]:}\n{sort_dict[2]:}: {threat_list[2]:}')
        print(f'\nThe countries with the lowest threatened species of {data_set_species[0][3]} are:\n')
        print(f'{sort_dict[-1]:}: {threat_list[-1]:}\n{sort_dict[-2]:}: {threat_list[-2]:}\n{sort_dict[-3]:}: {threat_list[-3]:}')

        percent_1_country = float((threat_list[0]*100)/(sum_whole_subregion))                                                                                           # Percentage of rank 1 country's threatened species 
        percent_2_country = float((threat_list[1]*100)/(sum_whole_subregion))                                                                                           # Percentage of rank 2 country's threatened species 
        percent_3_country = float((threat_list[2]*100)/(sum_whole_subregion))                                                                                           # Percentage of rank 3 country's threatened species 
        other_percent = 100 - (percent_1_country + percent_2_country + percent_3_country)                                                                               # Percentage of the rest of the countries' threatened species
        
        my_explode = [0.2, 0.2, 0.2, 0]                                                                                                                                 # Explode list

        plt.pie([percent_1_country, percent_2_country, percent_3_country, other_percent], 
        labels= [sort_dict[0], sort_dict[1], sort_dict[2], 'Others'], 
        explode= my_explode ,shadow= True)                                                                                                                              # Pie chart plot
        plt.title(f'Percentage of Threatened {data_set_species[0][3]} in {subregion:}', pad= 20, fontsize= 14)                                                                             # Title of pie chart
        plt.show()


    elif species_check == '4':                                                                                                                                          # Condition when species is Mammal
        for i in country_in_subregion:                                                                                                                                  # Condition for appending threat list 
            for x in data_set_species[1:]:
                if i == x[0]:
                    threat_list.append(int(x[4]))
            
        sum_whole_subregion = np.sum(threat_list)                                                                                                                       # Summing over all the elements of threat_list
        
        subregion_threat_dict = dict_maker(country_in_subregion, threat_list)                                                                                           # Calling dict_maker function with countries of subregion list and threat list

        sort_dict = sorted(subregion_threat_dict, key= subregion_threat_dict.get, reverse= True)                                                                        # Sorting the new dictionary according to value and getting list of keys in descending order

        threat_list.sort(reverse = True)                                                                                                                                # Sorting threat_list in descending order
        
        print(f'{subregion:} has {len(country_in_subregion):} countries, of which the countries with the highest threatened species of {data_set_species[0][4]} are as follows:\n')
        print(f'{sort_dict[0]:}: {threat_list[0]:}\n{sort_dict[1]:}: {threat_list[1]:}\n{sort_dict[2]:}: {threat_list[2]:}')
        print(f'The countries with the lowest threatened species of {data_set_species[0][4]} are:\n')
        print(f'{sort_dict[-1]:}: {threat_list[-1]:}\n{sort_dict[-2]:}: {threat_list[-2]:}\n{sort_dict[-3]:}: {threat_list[-3]:}')

        percent_1_country = float((threat_list[0]*100)/(sum_whole_subregion))                                                                                           # Percentage of rank 1 country's threatened species 
        percent_2_country = float((threat_list[1]*100)/(sum_whole_subregion))                                                                                           # Percentage of rank 2 country's threatened species 
        percent_3_country = float((threat_list[2]*100)/(sum_whole_subregion))                                                                                           # Percentage of rank 3 country's threatened species 
        other_percent = 100 - (percent_1_country + percent_2_country + percent_3_country)                                                                               # Percentage of the rest of the countries' threatened species
        
        my_explode = [0.2, 0.2, 0.2, 0]                                                                                                                                 # Explode list

        plt.pie([percent_1_country, percent_2_country, percent_3_country, other_percent], 
        labels= [sort_dict[0], sort_dict[1], sort_dict[2], 'Others'], 
        explode= my_explode ,shadow= True)                                                                                                                              # Pie chart plot
        plt.title(f'Percentage of Threatened {data_set_species[0][4]} in {subregion:}', pad= 20, fontsize= 14)                                                                           # Title of pie chart
        plt.show()

    else:
        print('Enter a valid option.')

def country_validator(countries):
    '''
    A function that validates the user inputted country. It makes sure the the country that is inputted exists within the database no matter if it's inputted uppercase or lower or mixed.
    It turns it into a standard case with the first letter of the country capitalized.

    Arguments:
    countries - array of country data

    Returns:
    countryuser_caps - The chosen country with first letter capitalized
    '''
    countryuser = input('Please enter a country: ')
    countryuser_caps = countryuser.title()
    country_list = []
    arb_num2 = 0

    for x in countries:
        country_list.append(x[0])

    while arb_num2 == 0:
        if countryuser_caps in country_list:
            print(f'Your country of select is {countryuser_caps}')
            break
        else:
            print('Your country of select was not found, please try again.')
            countryuser = input('Please enter a country: ')
            countryuser_caps = countryuser.title()

    return countryuser_caps
        

def pop_country(pop_dat, country, year):
    '''
    Takes in a user chosen year with their selected country. It gets the total number of population of a country at a specific year

    Arguments:
    pop_dat - population data array
    country - user chosen country
    year - specific user chosen year

    Returns:
    country_population_chosen_year - the population of the country at the chosen year
    '''
    column_chosen_year = int(year) - 1999
    for row, country_pop in enumerate(pop_dat):
        if country_pop[0] == country:
            row_chosen_year = row
    country_population_chosen_year = pop_dat[row_chosen_year][column_chosen_year]
    return country_population_chosen_year


def country_area(countries, user_choice):
    '''
    A function that takes in a specific user chosen country and gets the area of that country.

    Arguments:
    countries - array of country data
    user_choice - chosen country

    Returns:
    country_area - the area of the country at the chosen specific year
    '''
    for x in countries:
        if x[0] == user_choice:
            country_area = x[3]
    return country_area
    

def population_density_ranking_global(user_year, countries, population, country_user, sortdens, toplist):
    '''
    Calculates the rank of the country based on population density. Ranks the country compared to other countries in population density from highest to least.

    Arguments:
    user_year - chosen specific year
    countries - countries data array
    population - population data array
    country_user - the chosen country of the user
    sortdens - a blank list that will be appended the sorted density numbers
    toplist - a blank list that will be apended like the sortdens but instead of the numbers, it's the country names sorted from highest density to lowest

    Return:
    The rank number of the user chosen country when compared to the population density of the other countries
    '''
    column_chosen_year = int(user_year) - 1999
    density_list = []
    country_list2 = []
    for x in countries[1:]:
        country_list2.append(x[0])
    for x in countries[1:]:
        for num, y in enumerate(population[1:]):
            if x[0] == y[0]:
                
                density_list.append(float(population[num+1][column_chosen_year]) / float(x[3]))
                
                break
    
    density_list_sorted = sorted(density_list, reverse=True)
    
    for s in density_list_sorted:
        sortdens.append(s)

    dictionary_countries = dict(zip(country_list2, density_list))

    for z in sortdens:
        for a in dictionary_countries:
            if z == dictionary_countries[a]:
                if a not in toplist:
                    toplist.append(a)
                    break
    for rank, country in enumerate(toplist):
        if country == country_user:
            country_rank = rank + 1
    
    return country_rank

def population_finder_list(lowyear, highyear, popdata, country):
    '''
    Gets a list of the population of a user inputted country over a specific time which is also an interval inputted by the user. Looks for the country in the arrays, then makes a list of the population based on interval of 2 years.

    Arguments:
    lowyear - Starting year, which is the starting year of the interval (inputted by user)
    highyear - Ending year, which is the ending year of the interval (inputted by user)
    popdata - population data array
    country - user's choice of country

    Returns:
    population_list - the list of population in an interval of years
    '''
    population_list =[]
    start_index = int(lowyear) - 1999
    stop_index = int(highyear) - 1999
    for row, country_pop in enumerate(popdata):
        if country_pop[0] == country:
            row_chosen_year = row
    country_all_density = (popdata[row_chosen_year])
    population_list1 = (list(country_all_density)[start_index:stop_index+1])
    for i in population_list1:
        population_list.append(int(i))

    return population_list

def density_finder_list(lowyear, highyear, popdata, country, area_country):
    '''
    Gets a list of the population of a user inputted country over a specific time which is also an interval inputted by the user. Looks for the country in the arrays, then makes a list of the population based on interval of 2 years.

    Arguments:
    lowyear - Starting year, which is the starting year of the interval (inputted by user)
    highyear - Ending year, which is the ending year of the interval (inputted by user)
    popdata - population data array
    country - user's choice of country
    area_country - the area of the country

    Returns:
    population_list - the list of population in an interval of years
    '''
    converted_array_float =[]
    start_index = int(lowyear) - 1999
    stop_index = int(highyear) - 1999
    for row, country_pop in enumerate(popdata[1:]):
        if country_pop[0] == country:
            row_chosen_year = row

    country_all_density = (popdata[row_chosen_year+1])
    array_1 = np.array(list(country_all_density)[start_index:stop_index+1])

    for num in array_1:
        converted_array_float.append(int(num))
    
    density_list = np.array(converted_array_float) / int(area_country)
    
    return density_list

def max_density_range(lowyear, highyear, popdata, country, area_country):
    '''
    Uses the list of density from the density_finder_list function to get the maximum density in that list.

    Arguments:
    lowyear - Starting year, which is the starting year of the interval (inputted by user)
    highyear - Ending year, which is the ending year of the interval (inputted by user)
    popdata - population data array
    country - user's choice of country
    area_country - the area of the country

    Returns:
    The maximum value of density in the list
    '''
    density_list = density_finder_list(lowyear, highyear, popdata, country, area_country)
    max_dens = density_list.max()
    return max_dens

def min_density_range(lowyear, highyear, popdata, country, area_country):
    '''
    Uses the list of density from the density_finder_list function to get the minimum density in that list.

    Arguments:
    lowyear - Starting year, which is the starting year of the interval (inputted by user)
    highyear - Ending year, which is the ending year of the interval (inputted by user)
    popdata - population data array
    country - user's choice of country
    area_country - the area of the country

    Returns:
    The minumum value of density in the list
    '''
    density_list = density_finder_list(lowyear, highyear, popdata, country, area_country)
    min_dens = density_list.min()
    return min_dens

def mean_density_range(lowyear, highyear, popdata, country, area_country):
    '''
    Uses the list of density from the density_finder_list function to get the mean density in that list.

    Arguments:
    lowyear - Starting year, which is the starting year of the interval (inputted by user)
    highyear - Ending year, which is the ending year of the interval (inputted by user)
    popdata - population data array
    country - user's choice of country
    area_country - the area of the country

    Returns:
    Calculates and returns the mean value from the given density list
    '''
    density_list = density_finder_list(lowyear, highyear, popdata, country, area_country)
    mean_dens = density_list.mean()
    return mean_dens

def year_locator_max(lowyear, highyear, popdata, country, area_country):
    '''
    Uses the list of density from the density_finder_list, finds the maximum value then counts which year this maximum value occured in.

    Arguments:
    lowyear - Starting year, which is the starting year of the interval (inputted by user)
    highyear - Ending year, which is the ending year of the interval (inputted by user)
    popdata - population data array
    country - user's choice of country
    area_country - the area of the country

    Returns:
    the year in which the maximum density occured during
    '''
    density_list = density_finder_list(lowyear, highyear, popdata, country, area_country)
    max_dens = density_list.max()
    for x, densities in enumerate(density_list):
        if densities == max_dens:
            max_year = x + int(lowyear)
    return max_year

def year_locator_min(lowyear, highyear, popdata, country, area_country):
    '''
    Uses the list of density from the density_finder_list, finds the minimum value then counts which year this minimum value occured in.

    Arguments:
    lowyear - Starting year, which is the starting year of the interval (inputted by user)
    highyear - Ending year, which is the ending year of the interval (inputted by user)
    popdata - population data array
    country - user's choice of country
    area_country - the area of the country

    Returns:
    the year in which the minimum density occured during
    '''
    density_list = density_finder_list(lowyear, highyear, popdata, country, area_country)
    max_dens = density_list.min()
    for x, densities in enumerate(density_list):
        if densities == max_dens:
            min_year = x + int(lowyear)
    return min_year

def print_menu_species():
    '''
    Prints the menu options for option 3 (species menu)

    Arguments:
    None

    Returns:
    None
    '''
    print('-------------------------------------------------')
    print('(1) Plants')
    print('(2) Fishes')
    print('(3) Birds')
    print('(4) Mammals')
    print('-------------------------------------------------')

def menu_density_region():
    '''
    Prints the menu options for option 2 (Subregion/Region population density)

    Arguments:
    None

    Returns:
    None
    '''
    print('-------------------------------------------------')
    print('(1) Search by Region')
    print('(2) Search by Sub-Region')
    print('-------------------------------------------------')

def user_region_select(countrydata):
    '''
    User inputs a region, and this function makes sure that the region entered is correctly located in the database. If not, the user is prompted to enter it again.

    Arguments:
    countrydata - country data array

    Returns:
    The region of the selected user with first letter capitalized
    '''
    region_list = []
    user_region = input('Please enter a region: ')
    user_region_caps = user_region.title()
    for regions in countrydata:
        if regions[1] not in region_list:
            region_list.append(regions[1])
    region_list_string = ', '.join(region_list[1:])
    while True:
        if user_region_caps in region_list:
            break
        else:
            print('The region that you\'ve entered was not recognized please try again.')
            print(f'Tip consider choosing from: {region_list_string}')
            user_region_caps = (input('Please enter a region: ')).title()
    print(f'Your selected region is {user_region_caps}')
    return user_region_caps

def country_list_region(data_country, user_select_region):
    '''
    Makes a list of country given the region. Looks at the arrat of countries and compares if the country has the region name of what the user wants, if it does, it adds the country to the list.

    Arguments:
    data_country - country data array
    user_select_region - the choice of region from the user

    Return:
    returns the list of countries in the specific selected region
    '''
    country_list_regionvar = [] 
    for countries in data_country:
        if countries[1] == user_select_region:
            country_list_regionvar.append(countries[0])
    
    return country_list_regionvar

def region_year_select():
    '''
    Makes sure that the year entered is within the appropiate range, if not, it prompts the user to enter again.

    Arguments:
    None

    Returns:
    The selected year of the user
    '''
    region_year = input('Please enter a year from 2000 and 2020: ')
    while True:
        if region_year.isnumeric() == True:
            if int(region_year) in range(2000, 2021):
                break
            else:
                print('Please enter a valid integer between 2000 and 2020.')
                region_year = input('Please enter a year from 2000 and 2020: ')
        else:
            print('Please enter a valid integer between 2000 and 2020.')
            region_year = input('Please enter a year from 2000 and 2020: ')
    return region_year

def density_region_func(year, data_country, country_list, data_pop):
    '''
    Program gets the population of the countries in that region and divides each one of them by the region area to calculate the overall population density of the region.

    Arguments:
    year - the selected year by the user
    data_country - country data array
    country_list - the list of countries in that particular region
    data_pop - population data array

    Returns:
    The population density value of the region
    '''
    area_total = 0
    density_region = 0
    columns_index = int(year) - 1999
    for area in data_country[1:]:    
        if area[0] in country_list:
            area_total += float(area[3])
    for population in data_pop[1:]:
        if population[0] in country_list:
            density_region += float(population[columns_index]) / area_to1tal
    
    return density_region

def region_density_sort(list_regions, year, contdat, popdat, sortdensreg):
    '''
    Checks for the unique regions in the database. Calculates the region population density of each one of them and ranks them based on the highest population density to the lowest.
    Also appends a list of the region names from highest density to lowest

    Arguments:
    list_regions - the list of different unique regions in the database
    year - the chosen specific year of the user
    contdat - country data array
    popdat - population data array
    sortdensreg - a blank list which is later appended the regions (names) based on population density from highest to lowest

    Returns:
    density_list_sorted - densities sorted from highest to least of the regions worldwide
    '''
    denity_list = []
    for reg in list_regions:
        density_region2 = density_region_func(year, contdat, country_list_region(contdat, reg), popdat)
        
        if density_region2 not in denity_list:
            denity_list.append(density_region2)
    
    dictionary_region_density = dict(zip(list_regions, denity_list))
    
    density_list_sorted = sorted(denity_list, reverse=True)
    
    for x in density_list_sorted:
        for y in dictionary_region_density:
            if x == dictionary_region_density[y]:
                sortdensreg.append(y)
    
    return density_list_sorted


def subregion_density_sort(list_regions, year, contdat, popdat, sortdensreg):
    '''
    Like the region_density_sort but it works for subregions instead.
    Calculates the population density of each subregion and sorts then from highest to least.

    Arguments:
    list_regions - the list of different unique sub-regions in the database
    year - the chosen specific year of the user
    contdat - country data array
    popdat - population data array
    sortdensreg - a blank list which is later appended the regions (names) based on population density from highest to lowest

    Returns:
    density_list_sorted - densities sorted from highest to least of the sub-regions worldwide
    '''
    denity_list = []
    for reg in list_regions:
        density_region2 = density_region_func(year, contdat, country_list_subregion(contdat, reg), popdat)
        
        if density_region2 not in denity_list:
            denity_list.append(density_region2)
    
    dictionary_region_density = dict(zip(list_regions, denity_list))
    
    density_list_sorted = sorted(denity_list, reverse=True)
    
    for x in density_list_sorted:
        for y in dictionary_region_density:
            if x == dictionary_region_density[y]:
                sortdensreg.append(y)
    return density_list_sorted

def countryrank_on_region(user_year, countries, population, chosen_countries, sorteddens, toplist):
    '''
    Ranks the countries within a region based on the order of their population density from highest to least.
    Appends two lists one which is the density numbers from highest to least and another which is the names of the countries from highest to least.

    Arguments:
    user_year - the chosen specific year of the user
    countries - country data array
    population - population data array
    chosen_countries - the list of countries within that region
    sortdens - blank list which gets appended of the population densities ranked from highest to lowest
    toplist - list countries ranked from highest to least based on their population density

    Returns:
    None
    '''
    column_chosen_year = int(user_year) - 1999
    density_list = []
    country_list2 = []
    for x in chosen_countries:
        country_list2.append(x)
    for x in countries:
        
        if x[0] in chosen_countries:
            for num, y in enumerate(population[1:]):
                if x[0] == y[0]:
                    density_list.append(float(population[num+1][column_chosen_year]) / float(x[3]))
                    break
    density_list_sorted = sorted(density_list, reverse=True)
    for s in density_list_sorted:
        sorteddens.append(s)

    dictionary_countries = dict(zip(country_list2, density_list))

    for z in sorteddens:
        for a in dictionary_countries:
            if z == dictionary_countries[a]:
                if a not in toplist:
                    toplist.append(a)
                    break

def countryrank_on_subregion(user_year, countries, population, chosen_countries, sorteddens, toplist):
    '''
    Like countryrank_on_region except this function ranks the population density based on sub-region
    Ranks the countries within a subregion based on the order of their population density from highest to least.
    Appends two lists one which is the density numbers from highest to least and another which is the names of the countries from highest to least.

    Arguments:
    user_year - the chosen specific year of the user
    countries - country data array
    population - population data array
    chosen_countries - the list of countries within that subregion
    sortdens - blank list which gets appended of the population densities ranked from highest to lowest within the subregion
    toplist - list countries ranked from highest to least based on their population density within the subregion

    Returns:
    None
    '''
    column_chosen_year = int(user_year) - 1999
    density_list1 = []
    country_list3 = []
    for x in chosen_countries:
        country_list3.append(x)
    for x in countries:
        if x[0] in chosen_countries:
            for num, y in enumerate(population[1:]):
                if x[0] == y[0]:
                    density_list1.append(float(population[num+1][column_chosen_year]) / float(x[3]))
                    break
    density1_list_sorted = sorted(density_list1, reverse=True)

    for s in density1_list_sorted:
        sorteddens.append(s)
    dictionary_countries1 = dict(zip(country_list3, density_list1))
    

    for z in sorteddens:
        for a in dictionary_countries1:
            if z == dictionary_countries1[a]:
                if a not in toplist:
                    toplist.append(a)
                    break
    
   
def user_subregion_select(countrydata):
    '''
    Function asks the user to enter a subregion. Checks if the subregion is in the database, if not, it asks the user to enter again.

    Arguments:
    countrydata - country data array

    Returns:
    user_subregion_caps - returns the subregion with the first letter capitalized
    '''
    subregion_list = []
    user_subregion = input('Please enter a subregion: ')
    user_subregion_caps = user_subregion.title()
    print(user_subregion_caps)
    for subregions in countrydata[1:]:
        if subregions[2].title() not in subregion_list:
            subregion_list.append(subregions[2].title())
    
    string_subregion = ', '.join(subregion_list[0:4])
    while True:
        if user_subregion_caps in subregion_list:
            break
        else:
            print('The region that you\'ve entered was not recognized please try again.')
            print(f'Few examples of subregions: {string_subregion}...')
            user_subregion_caps = (input('Please enter a subregion: ')).title()
    return user_subregion_caps

def country_list_subregion(data_country, user_select_subregion):
    '''
    Finds the list of countries in a user specified subregion.

    Arguments:
    data_country - country data array
    user_select_subregion - the selected subregion by the user

    Returns:
    country_list_regionvar - list of countries in the subregions
    '''
    country_list_regionvar = [] 
    for countries in data_country:
        if countries[2] == user_select_subregion:
            country_list_regionvar.append(countries[0])
    
    return country_list_regionvar

def plt_yaxis_bar(user_year, countries, population, chosen_countries):
    '''
    Used to make the y axis of the graph in option 2 2nd part.
    Calculates and constructs a list of densities in a particular subregion. As stated, this can be helpful in graphing as the y axis.

    Arguments:
    user_year - The chosen specific year of the user
    countries - country data array
    population - population data array
    chosen_countries - the list of countries in that particular sub region

    Returns:
    density_list1 - the population density of each country in the subregion as a list

    '''
    column_chosen_year = int(user_year) - 1999
    density_list1 = []
    country_list3 = []
    for x in chosen_countries:
        country_list3.append(x)
    for x in countries:
        if x[0] in chosen_countries:
            for num, y in enumerate(population[1:]):
                if x[0] == y[0]:
                    density_list1.append(float(population[num+1][column_chosen_year]) / float(x[3]))
                    break
    return density_list1


def density_axis(contdat, userreg, popdat, startyer, endyer):
    '''
    Given a particular region, it constructs a list of population densities of the countries in that particular region. 
    Useful for graphing. List of population densities of the countries located in that region.
    Also given/inputted is an interval of year. This function takes into consideration on when to start and when to stop (starting to ending year)

    Arguments:
    contdat - country data array
    userreg - chosen region by the user or any particular region
    popdat - population data array
    startyer - starting year in the interval
    endyer - stoping year in the interval

    Returns:
    The list of population density in each country in a particular region
    '''
    region_list = []
    for year in range(int(startyer), int(endyer)+1):
        region = density_region_func(year, contdat, country_list_region(contdat, userreg), popdat)
        region_list.append(region)
    
    return region_list



def graph_option1a(x_axis, y_axis, country, population, area, rank, currentyear):
    '''
    Function that graphs for the first menu option into 1st sub-option
    If the country is among the top countries, it only graphs the country compared with the top country's population denisity
    If the country isn't among the top countries, it graphs two subplots. One is the country compared to the countrys surrounding it, the second is the country compared to the top countrys

    Arguments:
    x_axis - the x axis for the plot
    y_axis - the y axis for the plot
    country - the selected user country
    population - the population of the country
    area - the area of the country
    rank - the rank of the country in popultion density worldwide
    currentyear - the selected user year

    Returns:
    None
    '''
    
    FIGURE1 = 1
    plt.figure(FIGURE1)
       
    if rank > 7:
        x_axis_sub1 = [x_axis[rank-4], x_axis[rank-3], x_axis[rank-2], x_axis[rank-1], x_axis[rank], x_axis[rank+1], x_axis[rank+2]]
        y_axis_sub1 = [y_axis[rank-4], y_axis[rank-3], y_axis[rank-2], y_axis[rank-1], y_axis[rank], y_axis[rank+1], y_axis[rank+2]]

        plt.subplot(2,1,1)
        plt.title(f'{country} amongst countries ranking from #{rank-3} to #{rank+1} in {currentyear}')
        plt.barh(x_axis_sub1, y_axis_sub1, color='#7884a5')
        plt.barh(country, float(population) / float(area), color='#444454')

        plt.subplot(2,1,2)
        plt.title(f'{country} compared to countries ranking the highest in Population Density in {currentyear}')
        plt.xlabel('Population Density Per Square Kilometers')  
        plt.barh(x_axis[0:7], y_axis[0:7], color='#9eb6d0')
        plt.barh(country, float(population) / float(area), color='#444454')
        
        plt.show()

    else:
        plt.title(f'{country} amongst the top countries ranking #{rank} in {currentyear}')
        plt.barh(x_axis[0:7], y_axis[0:7], color='#9eb6d0')
        plt.barh(country, float(population) / float(area), color='#444454')
        plt.xlabel('Population Density Per Square Kilometers') 
            
        plt.show()

def graph_option1b(x_axis, y_axis, country, population_list):
    '''
    Plotting function for the first option, sub-option 2.
    Creates two subplots both of which are both line graphs.
    First is the change in population from the start year to the stop year of the user inputted years. Followed by the total change (line from start to end)
    Second subplot is the change in population density from the start year to the stop year of the user inputted years. Followed by the total change (line from start to end)

    Arguments:
    x_axis - the plot x axis
    y_axis - the plot y axis
    country - the country of select from the user
    population_list - the list of population accross the interval of year

    Returns:
    None
    '''
    FIGURE2 = 2
    startend_point_x = [x_axis[0], x_axis[-1]]
    startend_point_y = [y_axis[0], y_axis[-1]]
    startend_point_ypop = [population_list[0], population_list[-1]]
    
    plt.figure(FIGURE2)
    plt.subplot(2, 1, 1)
    plt.title(f'The change in Popluation in {country} from {x_axis[0]} to {x_axis[-1]}')
    plt.plot(x_axis, population_list, marker='.', color='#664E88', label='Population')
    plt.plot(startend_point_x, startend_point_ypop, '--', color='#63B4B8', label='Total Change in Population')

    plt.xticks(x_axis)
    plt.ylabel('Population')
    

    plt.legend(shadow='True')
    plt.grid(True)
    plt.tight_layout()


    plt.subplot(2, 1, 2)
    plt.title(f'The change in Popluation Density in {country} from {x_axis[0]} to {x_axis[-1]}')
    plt.plot(x_axis, y_axis, marker='.', color='#456268', label='Population Density')
    plt.plot(startend_point_x, startend_point_y, '--', color='#79A3B1', label='Total Change in Population Density')

    plt.xticks(x_axis)
    plt.ylabel('Population Density Per Square Kilometers')
    plt.xlabel('Years')

    plt.legend(shadow='True')
    plt.grid(True)
    plt.tight_layout()

    plt.show()

def graph_option2a(y_axis, x_axis, userreg, userdens, year, country_data, population_data, startyear, region_list):
    '''
    Plotting function for second option sub option 1.
    graphs 2 seperate figures.
    One of which is a line graph of all the regions from 2000 up to the selected year. This occurs on 1 graph and is done by using a for loop. The for loop finds the region and changes the y axis values and plots the region. 
    It does this for all available regions so that it is possible to graph all regions in 1 plot.
    Second figure is a horizontal bar-graph that compares the population density of all regions in the specified year

    Arguments:
    y_axis - the y axis of the blot
    x_axis - the x axis of the plot
    userreg - the region of select by the user
    userdens - the population density of the region that is selected by the user
    year - the year of select of the user
    country_data - the country data imported array
    population_data - the population data imported array
    startyear - the year 2000, the year where the graph starts at
    region_list - the list of all available regions

    Returns:
    None
    '''
    FIGURE3 = 3
    FIGURE4 = 4
    x_axis2 = []
    color_list = ['#2D4059', '#EA5455', '#F07B3F', '#FFD460', '#9A0680', '#BBBBBB', '#726A95']
    for x in range(2000, int(year)+1):
        x_axis2.append(str(x))


    plt.figure(FIGURE3)
    plt.title(f'Population Density of Regions in {year}')
    plt.xlabel('Population Density per Square Kilometers')
    plt.ylabel('Regions')
    plt.barh(x_axis, y_axis, color='#9eb6d0')
    plt.barh(userreg, userdens, color='#444454')
    

    plt.figure(FIGURE4)

    arbnum = 0
    for r in region_list:
        y_axis2 = density_axis(country_data, r, population_data, startyear, year)
        plt.plot(x_axis2, y_axis2, label=f'{r}', marker='.', color=f'{color_list[arbnum]}')
        arbnum += 1

    plt.title(f'Region Population Density from 2000 to {year}')
    plt.xlabel('Years')
    plt.ylabel('Population Density per Square Kilometers')
    plt.grid(True)
    plt.legend(shadow='True')
    plt.show()

def graph_option2b(y_axis, x_axis, userreg, userdens, year, contdata, popdata):
    '''
    Plotting function that graphs for the second option, sub-option 2.
    Creates two subplots both of which are horizontal bar graphs.
    First subplot are all subregions compared with each other in population density
    Second subplot are the countries which are in the subregion and their population densities compared with each other

    Arguments:
    y_axis - the plot's y axis
    x_axis - the plot's x axis
    userreg - the selected subregion of the user
    userdens - the density of the subregion that is selected by user
    year - the inputted year
    contdata - country data array
    popdata - population data array

    '''
    FIGURE5 = 5
    plt.figure(FIGURE5)

    plt.subplot(2,1,1)
    plt.title(f'Population Density of Sub-Regions in {year}')
    plt.barh(x_axis, y_axis, color='#9eb6d0')
    plt.barh(userreg, userdens, color='#444454')

    plt.subplot(2,1,2)
    plt.title(f'Population Density of countries in {userreg} in {year}')
    x_values_bar = country_list_subregion(contdata, userreg)
    y_values_bar = plt_yaxis_bar(year, contdata, popdata, country_list_subregion(contdata, userreg))
    
    plt.barh(x_values_bar, y_values_bar, color='#678983')
    plt.xlabel('Population Density per Square Kilometers')

    
    plt.show()
#
#
#

def main():
    
    # generates arrays for the 3 given CSV files
    country_data = np.genfromtxt('Country_Data.csv', delimiter=',', skip_header=False, encoding=None, dtype=None)           # generates an array based on the given country_data dataset
    population_data = np.genfromtxt('Population_Data.csv', delimiter=',', skip_header=False, encoding=None, dtype=None)     # generates an array based on the given population_data dataset
    species_data = np.genfromtxt('Threatened_Species.csv', delimiter=',', skip_header=False, encoding=None, dtype=None)     # generates an array based on the given species_data dataset
    main_choices = ['1','2','3','4', '5', '6']  # List of main choices available for the user
    
    
    # Blank lists that will be appended with objects
    top_list = []
    sorted_density = []
    sorted_density_regions = []
    top_list_region = []
    top_list_subregion = []
    

    
    while True: 
        print_menu()    # Calls and Prints the main menu options
        user_choice = input('Please choose an option from the menu options above: ')  # Prompts the user to choose an option from the main menu

        # Based on the entered main options, the program will perform different tasks
        if user_choice not in main_choices: # If the choice entered by the user is not recognized as the main options, user will be asked to enter the option again
            print('\nYou\'ve entered an invalid option that is not apart of the options above, please try again.')
            continue


        elif user_choice == '6': # Exits out of program
            break

        # Population density by Country option
        elif user_choice == '1':    
            user_country = country_validator(country_data)  # Verifies and stores the country of the user's choice

            print('-------------------------------------------------')
            print('(1) Population density by specific year')
            print('(2) Population density by a range of years')
            print('-------------------------------------------------\n')
            population_density_choice = input('Please choose an option from the menu options above: ')  # Prompts the user to make a choice based on the choices above
            while population_density_choice != '1' and population_density_choice != '2':    # Choice must be either 1 or 2, if not, user will be prompted to enter the options again
                print('The menu option that you\'ve entered does not exist, please try again.')
                population_density_choice = input('Please choose an option from the menu options above: ')

            # Population Density by a specific Year
            if population_density_choice == '1':
                year_chosen = input('Enter a year from the year 2000 to 2020: ')    # Prompts the user to enter a year

                # Makes sure that the entered year is within the interval 2000 - 2020 (including both) and that it's numeric
                while True:
                    if year_chosen.isnumeric() == True: # If entered input is numeric, it will be judged based on the range
                        if int(year_chosen) not in range(2000, 2021):
                            print('The year that you\'ve entered is not between 2000 and 2021, please try again.')
                            year_chosen = input('Enter a year from the year 2000 to 2020: ')
                        else:
                            break
                    else:             # If it isnt numberic, input is automatically wrong
                        print('The year that you\'ve entered is not between 2000 and 2021, please try again.')
                        year_chosen = input('Enter a year from the year 2000 to 2020: ')


                population_country = pop_country(population_data, user_country, year_chosen)    # Calls function and calculates the total number of population of the country at the given year
                country_area_choice = country_area(country_data, user_country)                  # Calls function and recieves the area of the country
                rank_country = population_density_ranking_global(year_chosen, country_data, population_data, user_country, sorted_density, top_list)    # Calls function and calculates the rank of the country based on it's population density worldwide
                country_data_density = Country(user_country, population_country, country_area_choice, rank_country, 'NA', 'NA', 'NA', 'NA', top_list, sorted_density, year_chosen) # Stores the country information at the class Country
                country_data_density.get_country_density()      # Prints information regarding the country
                country_data_density.top_countries_density()    # Prints information regarding the country, and other top ranked countries
                graph_option1a(top_list, sorted_density, user_country, population_country, country_area_choice, rank_country, year_chosen)  # Graph's information based on the calculated infromations. Displays the country's rank compared to the countries surrounding
                top_list = []        # Resets the lists                                                                                       it and graphs the country's population compared to other countries ranked the highest in another subplot.
                sorted_density = []
                input('Press ENTER to continue')  # User must enter something to continue, to avoid the cluster of messages
        
            # Population density by a range of year
            elif population_density_choice == '2':
                list_years = []
                year_lower = input('Please enter the lower year from 2000 to 2020: ')       # Starting year
                year_higher = input('Please enter the higher year from 2000 to 2020: ')     # Ending year

                # Makes sure that the entered years are both numeric and within the range of 2000 - 2020
                # Also checks for logic flaw, as the second number must be higher than the first number
                # The Two numbers also cannot be equal to each other
                # If any of those conditions aren't met, user has to enter the 2 years again
                while True:
                    if year_lower.isnumeric() == True and year_higher.isnumeric() == True:  # If both are numeric, then program tests for which number is bigger followed by the range check
                        if int(year_higher) > int(year_lower):
                            if int(year_higher) in range(2000,2021) and int(year_lower) in range(2000,2021):
                                break
                            else:
                                print('Your entered years must be within the range.')
                                year_lower = input('Please enter the lower year from 2000 to 2020: ')
                                year_higher = input('Please enter the higher year from 2000 to 2020: ')
                        else:
                            print('Your higher year must be higher than the lower year.')
                            year_lower = input('Please enter the lower year from 2000 to 2020: ')
                            year_higher = input('Please enter the higher year from 2000 to 2020: ')
                    else:
                        print('You need to enter 2 integer values')
                        year_lower = input('Please enter the lower year from 2000 to 2020: ')
                        year_higher = input('Please enter the higher year from 2000 to 2020: ')

                for years in range(int(year_lower), int(year_higher)+1):    # List of the years starting from the starting year and end at the enting year.
                    if years not in list_years:
                        list_years.append(years)    # Appends the years to list_years
                
                print('')
                lower_population = pop_country(population_data, user_country, year_lower)       # Population of the starting year
                higher_population = pop_country(population_data, user_country, year_higher)     # Population of the ending year
                country_area_choice = country_area(country_data, user_country)                  # Calculates the area of the country
                country_high_low_data = Country(user_country, 'NA', country_area_choice, 'NA', lower_population, higher_population, year_lower, year_higher, top_list, 'NA', 'NA')  # Stores the informations into class Country
                country_high_low_data.density_diff_info()   # Prints the information by accessing the class
                max_density = max_density_range(year_lower, year_higher, population_data, user_country, country_area_choice)    # Stores the highest population density that occured during the start year and end year
                max_year = year_locator_max(year_lower, year_higher, population_data, user_country, country_area_choice)        # Stores the year at which the highest population density occured during the start and end year
                min_density = min_density_range(year_lower, year_higher, population_data, user_country, country_area_choice)    # Stores the lowest population density that occured during the start year and end year
                min_year = year_locator_min(year_lower, year_higher, population_data, user_country, country_area_choice)        # Stores the year at which the lowest population density occured during the start and end year
                mean_density = mean_density_range(year_lower, year_higher, population_data, user_country, country_area_choice)  # Calculates the mean population density from the start year and end year

                # Prints the highest, lowest population densities along with their appropiate years. And prints the mean density
                print(f'The highest population density between {year_lower} and {year_higher} was {max_density:.2f} in {max_year}. And the lowest was {min_density:.2f} in {min_year}!')
                print(f'The average population density was found to be around {mean_density:.3f}.')
                print('')
                print('--------'*5)
                

                # Graphs the informations that were calculated into two seperared subplots, line graphs. First one is the change in population over the interval of entered year, and second subplot is the 
                # change in population density over the specifies interval year
                graph_option1b(list_years, density_finder_list(year_lower, year_higher, population_data, user_country, country_area_choice), user_country, population_finder_list(year_lower, year_higher, population_data, user_country))


                input('Press ENTER to continue')    # User must enter something to continue, to avoid the cluster of messages

                list_years = [] # Resets list


        # Population Density by Region/Subregion
        elif user_choice == '2':
            menu_density_region()   # Prints the menu
            user_choice2 = input('Please choose an option (1 or 2) from the option list above: ')
            # User choice must either be 1 or 2, if not, user must enter again
            while True:         
                if user_choice2 == '1':
                    break
                elif user_choice2 == '2':
                    break
                else:
                    print('The option that you\'ve is not recognized. Make sure to enter (1 or 2).')
                    user_choice2 = input('Please choose an option (1 or 2) from the option list above: ')

            # Search by Region
            if user_choice2 == '1':
                all_regions = []
                user_region = user_region_select(country_data)                              # Prompts the user to enter a region and then stores that region in a variable
                region_country_list = country_list_region(country_data, user_region)        # All the countries in that region are stored in a list
                region_year = region_year_select()                                          # The selected year of the user
                region_density = density_region_func(region_year, country_data, region_country_list, population_data)   # Calls and calculates the population density of the specific region at the entered year
                

                for region in country_data[1:]:         # List of the unique reions while skipping the header
                    if region[1] not in all_regions:
                        all_regions.append(region[1])



                sorted_density_numbers = region_density_sort(all_regions, region_year, country_data, population_data, sorted_density_regions)                       # The population densities of the countries in the region sorted from greatest to least
                dens_2000 = density_region_func(2000, country_data, country_list_region(country_data, user_region), population_data)                                # The population density during the year 2000 if the region
                countryrank_on_region(region_year, country_data, population_data, country_list_region(country_data, user_region), sorted_density, top_list_region)  # The countries ranked on their population density from highest to lowest, but all countries are within the region
                region_density_inf = Region(user_region, region_year, region_density, sorted_density_numbers, sorted_density_regions, dens_2000, top_list_region)   # Stores the information of the region in the class Region
                print('')
                region_density_inf.print_region_info()  # Prints the information regarding the region using the class

                # Graphs in two different figures.
                # One is the population density of the selected region compared with other regions in the entered year
                # The other is the change in population density of all regions starting from 2000 upto the year selected.
                graph_option2a(sorted_density_numbers, sorted_density_regions, user_region, region_density, region_year, country_data, population_data, 2000, all_regions)  
                print('')
                input('Press ENTER to continue')    # User must enter something to continue, to avoid the cluster of messages

                # Resets all of the lists
                top_list = []
                sorted_density = []
                sorted_density_regions = []
                top_list_region = []
                top_list_subregion = []

            # Search by Subregion
            elif user_choice2 == '2':
                all_regions = []
                all_subregions = []
                user_subregion = user_subregion_select(country_data)                            # The subregion inputted by the user is stored in the variable
                subregion_country_list = country_list_subregion(country_data, user_subregion)   # List of countries located and identified under the subregion
                subregion_year = region_year_select()                                           # The selected year by the user
                subregion_density = density_region_func(subregion_year, country_data, subregion_country_list, population_data)      # Calls function and calculates the population density of the subregion

                for subregion in country_data[1:]:              # Appends all the different unique sub regions into a list
                    if subregion[2] not in all_subregions:
                        all_subregions.append(subregion[2])

                sorted_density_subnumbers = subregion_density_sort(all_subregions, subregion_year, country_data, population_data, sorted_density_regions)                               # The population densities of the countries in the subregion sorted from greatest to least
                subdens_2000 = density_region_func(2000, country_data, country_list_subregion(country_data, user_subregion), population_data)                                           # The population density during the year 2000 of the subregion
                countryrank_on_subregion(subregion_year, country_data, population_data, country_list_subregion(country_data, user_subregion), sorted_density, top_list_subregion)       # The countries ranked on their population density from highest to lowest, but all countries are within the subregion
                subregion_density_inf = Region(user_subregion, subregion_year, subregion_density, sorted_density_subnumbers, sorted_density_regions, subdens_2000, top_list_subregion)  # Stores the information of the subregion in the class Region
                print('')
                subregion_density_inf.print_subregion_info()    # Prints the information regarding the subregion using the class

                # Graphs the calculated information
                # Shows the horizonatal bar graph of the subregion compared to other subregion's population density as the first subplot
                # Second subplot shows the horizontal bar graph of all the countries within the subregion and their population densities
                graph_option2b(sorted_density_subnumbers, sorted_density_regions, user_subregion, subregion_density, subregion_year, country_data, population_data)
                print('')
                
                input('Press ENTER to continue')    # User must enter something to continue, to avoid the cluster of messages

                # Resets all the lists
                top_list = []
                sorted_density = []
                sorted_density_regions = []
                top_list_region = []
                top_list_subregion = []
                

        # Species threatened by country
        elif user_choice == '3':
            specie_choices_list = ['1', '2', '3', '4']      # Available choices of specie types
            user_country = country_validator(country_data)  # Stores in the user's choice of country
            print_menu_species()                            
            species_choice_user = input('Please choose a specie type from the options above: ')    # Stores what specie the user requires information on

            # Makes sure that the choice entered by the user is valid and in the database (1 to 4), if not, prompts the user to enter it agiain
            while True:
                if species_choice_user in specie_choices_list:
                    break
                else:
                    print('Please enter a valid choice (from 1 to 4), as your choice was not recognized.')
                    species_choice_user = input('Please choose a specie type from the options above: ')

            # More information regarding this function can be found at the line of the function
            print('--------'*5)
            print('')
            threaten_by_country(user_country, species_choice_user, species_data)        
            print('')
            print('--------'*5)
            input('Press ENTER to continue')
            

        # Species threatened by Region / Sub-Region
        elif user_choice == '4':
            specie_choices_list = ['1', '2', '3', '4']  # Specie choices available to the user
            choices_list = ['1', '2']                   # Choices available to the user where 1 is search by region and 2 is search by sub region

            print('(1) Search by Region')
            print('(2) Search by Sub-Region')

            option4_choice = input('Please choose an option from above: ') # Stores the user's choice (whether region or subregion)

            # Makes sure that the entered choice is valid and exists within the data base (1 or 2)
            while True:
                if option4_choice in choices_list:
                    break
                else:
                    print('Please enter a valid choice 1 or 2)')
                    option4_choice = input('Please choose an option from above: ')

            # Search by Region
            if option4_choice == '1':
                user_region1 = user_region_select(country_data) # Stores the user's choice of region
                print_menu_species()
                species_choice_user1 = input('Please choose a specie type from the options above: ')    # Stores the user's choice of specie type

                # Makes sure that the entered specie type is existant within the data base (1 to 4), if not, user is prompted to enter again
                while True:
                    if species_choice_user1 in specie_choices_list:
                        break
                    else:
                        print('Please enter a valid choice (from 1 to 4), as your choice was not recognized.')
                        species_choice_user1 = input('Please choose a specie type from the options above: ')

                # More information regarding this function can be found at the line of the function
                print('--------'*5)
                print('')
                threaten_by_region(user_region1, species_choice_user1, species_data, country_data)
                print('')
                print('--------'*5)
                input('Press ENTER to continue')
            # Searches by Subegion
            elif option4_choice == '2':
                user_subregion1 = user_subregion_select(country_data) # Stores the user's choice of subregion
                print_menu_species()
                species_choice_user2 = input('Please choose a specie type from the options above: ')    # Stores the user's choice of specie type

                # Makes sure that the entered specie type is existant within the data base (1 to 4), if not, user is prompted to enter again
                while True:
                    if species_choice_user2 in specie_choices_list:
                        break
                    else:
                        print('Please enter a valid choice (from 1 to 4), as your choice was not recognized.')
                        species_choice_user2 = input('Please choose a specie type from the options above: ')
            
                # More information regarding this function can be found at the line of the function
                print('--------'*5)
                print('')
                threaten_by_subregion(user_subregion1, species_choice_user2, species_data, country_data)
                print('')
                print('--------'*5)
                input('Press ENTER to continue')


        elif user_choice == '5':
            
            print('')
            
if __name__ == '__main__':
    main()
