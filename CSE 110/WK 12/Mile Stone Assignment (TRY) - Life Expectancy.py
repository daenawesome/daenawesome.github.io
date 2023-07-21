from tabulate import tabulate
import csv
import time



# Display a loading message
print("\nLoading DataSet = 'Life-Expectancy'\n", end="")

# Create a loading animation
for i in range(11):
    print(" . ", end="", flush=True)
    time.sleep(.5)


def main():
            try:
                with open("life-expectancy.csv", "r") as f:
                
                    # Display a load success message
                    print("\n-- DataSet Successfully Loaded --\n", end="")

                    # Create a loading delay
                    for i in range(5):
                        print(" ", end="", flush=True)
                        time.sleep(1)

                    # Define the list of available features
                    features = [
                        "Find the year and country that has the lowest life expectancy in the dataset",
                        "Find the year and country that has the highest life expectancy in the dataset",
                        "Find the average life expectancy for a specific year and the country with the minimum and maximum life expectancies for that year",
                        "Find the minimum, maximum and average life expectancy for a specific country",
                        "Find the largest drop from one year to the next and the corresponding year and country",
                        "Find the average, minimum and maximum life expectancy for a range of years",
                        "Compare the life expectancy of two or more countries over time"
                    ]

                    while True:
                        # Print the list of available features
                        print("\n\nSelect the feature you would like to use: (1-7)")
                        for i, feature in enumerate(features):
                            print(f"{i + 1}. {feature}")

                        # Get the user's selection
                        selection = int(input("\nWhat would you like to do?: "))

                        # Execute the selected feature
                        if selection == 1:
                            # Find the year and country that has the lowest life expectancy in the dataset
                            min_life_expectancy = float('inf')
                            min_life_expectancy_year = 0
                            min_life_expectancy_country = ''
                            with open("life-expectancy.csv", "r") as f:
                                reader = csv.DictReader(f)
                                for row in reader:
                                    if float(row['Life expectancy (years)']) < min_life_expectancy:
                                        min_life_expectancy = float(row['Life expectancy (years)'])
                                        min_life_expectancy_year = row['Year']
                                        min_life_expectancy_country = row['Entity']
                            print(f"The overall min life expectancy is: {min_life_expectancy} from {min_life_expectancy_country} in {min_life_expectancy_year}")
                        elif selection == 2:
                            # Find the year and country that has the highest life expectancy in the dataset
                            max_life_expectancy = 0
                            max_life_expectancy_year = 0
                            max_life_expectancy_country = ''
                            with open("life-expectancy.csv", "r") as f:
                                reader = csv.DictReader(f)
                                for row in reader:
                                    if float(row['Life expectancy (years)']) > max_life_expectancy:
                                        max_life_expectancy = float(row['Life expectancy (years)'])
                                        max_life_expectancy_year = row['Year']
                                        max_life_expectancy_country = row['Entity']
                            print(f"The overall max life expectancy is: {max_life_expectancy} from {max_life_expectancy_country} in {max_life_expectancy_year}")
                        elif selection == 3:
                            # Find the average life expectancy for a specific year and the country with the minimum and maximum life expectancies for that year
                            year = input("Enter the year of interest: ")
                            life_expectancy_list = []
                            with open("life-expectancy.csv", "r") as f:
                                reader = csv.DictReader(f)
                                for row in reader:
                                    if row['Year'] == year:
                                        life_expectancy_list.append(float(row['Life expectancy (years)']))
                                if not life_expectancy_list:
                                    print(f"No data found for the year {year}")
                                else:
                                    average_life_expectancy = sum(life_expectancy_list) / len(life_expectancy_list)
                                    print(f"The average life expectancy for {year} is {round(average_life_expectancy,2)}")
                                    min_life_expectancy = min(life_expectancy_list)
                                    min_life_expectancy_country = ''
                                    max_life_expectancy = max(life_expectancy_list)
                                    max_life_expectancy_country = ''
                                    with open("life-expectancy.csv", "r") as f:
                                        reader = csv.DictReader(f)
                                        for row in reader:
                                            if row['Year'] == year:
                                                life_expectancy_list.append(float(row['Life expectancy (years)']))
                                        if not life_expectancy_list:
                                            print(f"No data found for the year {year}")
                                        else:
                                            average_life_expectancy = sum(life_expectancy_list) / len(life_expectancy_list)
                                            print(f"The average life expectancy for {year} is {round(average_life_expectancy,2)}")
                                            min_life_expectancy = min(life_expectancy_list)
                                            min_life_expectancy_country = ''
                                            max_life_expectancy = max(life_expectancy_list)
                                            max_life_expectancy_country = ''
                                            with open("life-expectancy.csv", "r") as f:
                                                reader = csv.DictReader(f)
                                                for row in reader:
                                                    if row['Year'] == year:
                                                        if float(row['Life expectancy (years)']) == min_life_expectancy:
                                                            min_life_expectancy_country = row['Entity']
                                                        if float(row['Life expectancy (years)']) == max_life_expectancy:
                                                            max_life_expectancy_country = row['Entity']
                                            print(f"The min life expectancy was in {min_life_expectancy_country} with {min_life_expectancy}")
                                            print(f"The max life expectancy was in {max_life_expectancy_country} with {max_life_expectancy}")
                        elif selection == 4:
                            # Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country
                            country = input("Enter the country of interest: ")
                            life_expectancy_list = []
                            with open("life-expectancy.csv", "r") as f:
                                reader = csv.DictReader(f)
                                for row in reader:
                                    if row['Entity'] == country:
                                        life_expectancy_list.append(float(row['Life expectancy (years)']))
                            if not life_expectancy_list:
                                print(f"No data found for {country}")
                            else:
                                average_life_expectancy = sum(life_expectancy_list) / len(life_expectancy_list)
                                print(f"The average life expectancy for {country} is {round(average_life_expectancy,2)}")
                                min_life_expectancy = min(life_expectancy_list)
                                max_life_expectancy = max(life_expectancy_list)
                                print(f"The min life expectancy for {country} was {min_life_expectancy}")
                                print(f"The max life expectancy for {country} was {max_life_expectancy}")
                        elif selection == 5:
                            # Identify the year and country that has the largest drop from one year to the next
                            largest_drop = 0
                            largest_drop_year = ""
                            largest_drop_country = ""
                            with open("life-expectancy.csv", "r") as f:
                                reader = csv.DictReader(f)
                                prev_row = next(reader)
                                for row in reader:
                                    if row['Entity'] == prev_row['Entity']:
                                        current_drop = float(prev_row['Life expectancy (years)']) - float(row['Life expectancy (years)'])
                                        if current_drop > largest_drop:
                                            largest_drop = current_drop
                                            largest_drop_year = row['Year']
                                            largest_drop_country = row['Entity']
                                    prev_row = row
                            print(f"The largest drop from one year to the next is {round(largest_drop,2)} from {largest_drop_country} in {largest_drop_year}")
                        elif selection == 6:
                            # Allow the user to select a range of years, and then show the average, minimum and maximum life expectancy for that range of years
                            start_year = input("Enter the starting year: ")
                            end_year = input("Enter the ending year: ")
                            life_expectancy_list = []
                            with open("life-expectancy.csv", "r") as f:
                                reader = csv.DictReader(f)
                                for row in reader:
                                    if int(row['Year']) >= int(start_year) and int(row['Year']) <= int(end_year):
                                        life_expectancy_list.append(float(row['Life expectancy (years)']))
                            if not life_expectancy_list:
                                print(f"No data found for the range of years from {start_year} to {end_year}")
                            else:
                                average_life_expectancy = sum(life_expectancy_list) / len(life_expectancy_list)
                                print(f"The average life expectancy for the range of years from {start_year} to {end_year} is {round(average_life_expectancy,3)}")
                                min_life_expectancy = min(life_expectancy_list)
                                max_life_expectancy = max(life_expectancy_list)
                                print(f"The min life expectancy for the range of years from {start_year} to {end_year} was {min_life_expectancy}")
                                print(f"The max life expectancy for the range of years from {start_year} to {end_year} was {max_life_expectancy}")
                                # Additional functionality to show the country with min and max life expectancy for this range of years
                                min_life_expectancy_country = ''
                                max_life_expectancy_country = ''
                                with open("life-expectancy.csv", "r") as f:
                                    reader = csv.DictReader(f)
                                    for row in reader:
                                        if int(row['Year']) >= int(start_year) and int(row['Year']) <= int(end_year):
                                            if float(row['Life expectancy (years)']) == min_life_expectancy:
                                                min_life_expectancy_country = row['Entity']
                                            if float(row['Life expectancy (years)']) == max_life_expectancy:
                                                max_life_expectancy_country = row['Entity']
                                print(f"The country with the min life expectancy for the range of years from {start_year} to {end_year} is {min_life_expectancy_country}")
                                print(f"The country with the max life expectancy for the range of years from {start_year} to {end_year} is {max_life_expectancy_country}")
                        elif selection == 7:
                            # Read the csv file and store the data in a variable
                            with open("life-expectancy.csv") as file:
                                data = list(csv.reader(file))
                            # Get the user input for the countries and year range to compare
                            countries = input("Enter the countries to compare, separated by commas: ").split(",")
                            start_year = int(input("Enter the start year for the comparison: "))
                            end_year = int(input("Enter the end year for the comparison: "))

                            # Validate the user input for the countries
                            while not all(country.strip() in data.Entity.unique() for country in countries):
                                print("Invalid country entered. Please enter valid countries.")
                                countries = input("Enter the countries to compare, separated by commas: ").split(",")

                            # Validate the user input for the year range
                            while start_year > end_year or start_year < data.Year.min() or end_year > data.Year.max():
                                print("Invalid year range entered. Please enter a valid year range.")
                                start_year = int(input("Enter the start year for the comparison: "))
                                end_year = int(input("Enter the end year for the comparison: "))

                            # Define the compare_countries function to compare the life expectancy of multiple countries over a specified year range
                            def compare_countries(data, countries, start_year, end_year):
                                # Filter the data for the specified countries and year range
                                filtered_data = data[(data.Entity.isin(countries)) & (data.Year >= start_year) & (data.Year <= end_year)]

                                # Group the data by country and year and calculate the mean life expectancy
                                grouped_data = filtered_data.groupby(['Entity', 'Year'])['Life expectancy (years)'].mean().reset_index()
                                
                                # Create an empty dictionary to store the data for each country
                                country_data = {}
                                
                                # Iterate through each country in the list
                                for country in countries:
                                    # Get the data for the current country
                                    country_data[country] = grouped_data[grouped_data['Entity'] == country]
                                
                                # Print the data for each country in a tabulated format
                                for country, data in country_data.items():
                                    print(f"Life expectancy for {country} from {start_year} to {end_year}:")
                                    print(tabulate(data, headers='keys', tablefmt='pretty'))
                                    print()
                        else:
                            print("Invalid selection. Please try again.")
            except FileNotFoundError:
                # Display a load error message
                print("\nError: The file 'life-expectancy.csv' was not found. \nPlease make sure the file is in the correct location and try again.")
                print("Or download the file using this url: 'https://byui-cse.github.io/cse110-course/lesson11/life-expectancy.csv'")
                choice = input("\nWould you like to try again? (yes/no): ")
                if choice == "yes":
                    # Display a loading message
                    print("\nLoading DataSet = 'Life-Expectancy'\n", end="")

                    # Create a loading animation
                    for i in range(11):
                        print(" . ", end="", flush=True)
                        time.sleep(.5)
                    main()
                else:
                    print("Exiting program.")
                    exit()
            except:
                # Display a error message
                print("\nError: An unknown error occurred while trying to open the file 'life-expectancy.csv'.")
            else:
                # Display a load success message
                print("\n-- DataSet Successfully Loaded --\n", end="")

                # Create a loading delay
                for i in range(5):
                    print(" ", end="", flush=True)
                    time.sleep(1)
if __name__ == '__main__':
    main()


"""
Features:
Loading animation
Success, Fail, or Error Messages when loading the dataset
Giving an option to run again or Close the program on Fail or Error Messages when loading the dataset
Input validation when an invalid selection is chosen
Giving options for the user on a specific feature they would like to use:
    Find the year and country that has the lowest life expectancy in the dataset
    Find the year and country that has the highest life expectancy in the dataset
    Allow the user to type in a year, then find the average life expectancy for that year. Then find the country with the minimum and the one with the maximum life expectancies for that year.
    Allow the user to type in a year range, then find the average life expectancy for that range. Then find the country with the minimum and the one with the maximum life expectancies for that range.
    Allow the user to type in a country, then find the average life expectancy for that country over time.
    Allow the user to type in a year range, then find the average life expectancy for that range across all countries.
    Compare the life expectancy of two or more countries over time
"""