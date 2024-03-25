#Question 3: Basic on Data insights (programming perspective)

import matplotlib.pyplot as plt
import pandas as pd

#3.1 Write a program that will load the “football.csv” dataset into a dataframe called “foot_ball”.
file_path = "C:\Users\HP\Downloads\dataset - 2020-09-24.csv"

# Loading the dataset into a DataFrame
foot_ball = pd.read_csv(file_path)

#3.2 inspect the dataframe by listing and displaying the last 7 rows of the dataframe using a single python statement.
# Printing the last 7 rows of the DataFrame
print(foot_ball.tail(7))

#3.3.1 Access and display the "Nationality" and "Club" columns for the first all players
# Display the "Nationality" and "Club" columns for the first 5 rows of the DataFrame
print(foot_ball[['Nationality', 'Club']].head(5))

#3.3.2 Access and display the data for the tenth player in the dataset using row index
# Displaying the tenth row of the DataFrame
print(foot_ball.loc[9])


#3.3.3 Access and display the "Goals" and "Appearances" for players with index positions 100 to 110
print(foot_ball[100:111][['Goals', 'Appearances']])

#3.3.4 Add a new column named "Goals per Appearance" that is calculated by dividing
#"Goals" by "Appearances"; and display the first 5 rows of the updated dataset. 
foot_ball['Goals per Appearance'] = foot_ball['Goals'] / foot_ball['Appearances']
# Displaying the first 5 rows of the updated foot_ball DataFrame
print(foot_ball.head())

#3.3.6 Perform a filtering operation to display players who have scored more than 5. 
print(foot_ball[foot_ball["Goals"]>6])


