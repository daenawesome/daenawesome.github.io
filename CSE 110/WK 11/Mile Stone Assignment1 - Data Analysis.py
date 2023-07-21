import csv

# Initialize variables to store the overall max and min life expectancy
overall_max_life_expectancy = 0
overall_min_life_expectancy = float('inf')
overall_max_life_expectancy_year = 0
overall_min_life_expectancy_year = 0
overall_max_life_expectancy_country = ''
overall_min_life_expectancy_country = ''

# Open the CSV file and read the data
with open("life-expectancy.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Check if the current row's life expectancy is greater than the overall max
        if float(row['Life expectancy (years)']) > overall_max_life_expectancy:
            overall_max_life_expectancy = float(row['Life expectancy (years)'])
            overall_max_life_expectancy_year = row['Year']
            overall_max_life_expectancy_country = row['Entity']
        # Check if the current row's life expectancy is less than the overall min
        if float(row['Life expectancy (years)']) < overall_min_life_expectancy:
            overall_min_life_expectancy = float(row['Life expectancy (years)'])
            overall_min_life_expectancy_year = row['Year']
            overall_min_life_expectancy_country = row['Entity']

# Print the overall max and min life expectancy
print(f"The overall max life expectancy is: {overall_max_life_expectancy} from {overall_max_life_expectancy_country} in {overall_max_life_expectancy_year}")
print(f"The overall min life expectancy is: {overall_min_life_expectancy} from {overall_min_life_expectancy_country} in {overall_min_life_expectancy_year}")

# Get the year of interest from the user
year_of_interest = input("\nEnter the year of interest: ")
# Get the country of interest from the user
country_of_interest = input("Enter the country of interest (eg. 'Africa'): ")

# Initialize variables to store the average life expectancy, max and min life expectancy for the year of interest
average_life_expectancy_across = 0
average_life_expectancy = 0
life_expectancy_count = 0
max_life_expectancy = 0
min_life_expectancy = float('inf')
max_life_expectancy_country = ''
min_life_expectancy_country = ''

# Initialize variables to store the life expectancy data for the country of interest
life_expectancy_list = []
min_life_expectancy = float('inf')
max_life_expectancy = 0

# Open the CSV file and read the data again
with open("life-expectancy.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Check if the current row's year matches the year of interest
        if row['Year'] == year_of_interest:
            # Check if the current row's country matches the country of interest
            if row['Entity'] == country_of_interest:
                # Add the life expectancy to the list
                life_expectancy_list.append(float(row['Life expectancy (years)']))
                # Check if the current row's life expectancy is greater than the max for the country of interest
                if float(row['Life expectancy (years)']) > max_life_expectancy:
                    max_life_expectancy = float(row['Life expectancy (years)'])
                # Check if the current row's life expectancy is less than the min for the country of interest
                if float(row['Life expectancy (years)']) < min_life_expectancy:
                    min_life_expectancy = float(row['Life expectancy (years)'])
            # Add the life expectancy to the average life expectancy
            average_life_expectancy_across += float(row['Life expectancy (years)'])
            average_life_expectancy += float(row['Life expectancy (years)'])
            life_expectancy_count += 1
            # Check if the current row's life expectancy is greater than the max for the year of interest
            if float(row['Life expectancy (years)']) > max_life_expectancy:
                max_life_expectancy = float(row['Life expectancy (years)'])
                max_life_expectancy_country = row['Entity']
            # Check if the current row's life expectancy is less than the min for the year of interest
            if float(row['Life expectancy (years)']) < min_life_expectancy:
                min_life_expectancy = float(row['Life expectancy (years)'])
                min_life_expectancy_country = row['Entity']

# Calculate the average life expectancy for the year of interest
average_life_expectancy_across /= life_expectancy_count

# Calculate the average life expectancy for the country of interest
average_life_expectancy = sum(life_expectancy_list) / len(life_expectancy_list)

# Print the results
print(f"\nFor the year {year_of_interest}:")
print(f"The average life expectancy across all countries was {round(average_life_expectancy_across,2)}")
print(f"The max life expectancy was in {max_life_expectancy_country} with {max_life_expectancy}")
print(f"The min life expectancy was in {min_life_expectancy_country} with {min_life_expectancy}")

print(f"\nFor the country {country_of_interest}:")
print(f"The average life expectancy is {round(average_life_expectancy,2)}")
print(f"The max life expectancy is {max_life_expectancy}")
print(f"The min life expectancy is {min_life_expectancy}")


"""
Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.
"""