import pandas as pd

# Load the raw dataset
raw_data = pd.read_csv('/Users/mustafa/Desktop/Coding Projects/Video Games Sales Analysis/Video_Games.csv')

# Make a copy of the raw data to work on
df = raw_data.copy()

# Drop the 'Year_of_Release' column
df.drop('Year_of_Release', axis=1, inplace=True)

# Save the 'Name' column for later use
df_name = df['Name']

# Select the numeric columns for cleaning
numeric_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales',
                   'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']
df = df[numeric_columns]

# Replace 'tbd' values in the 'User_Score' column with NaN
df['User_Score'].replace('tbd', pd.NA, inplace=True)
df['User_Score'] = pd.to_numeric(df['User_Score'])

# Fill missing values with the median of the respective columns
df['Critic_Score'].fillna(df['Critic_Score'].median(), inplace=True)
df['Critic_Count'].fillna(df['Critic_Count'].median(), inplace=True)
df['User_Score'].fillna(df['User_Score'].median(), inplace=True)
df['User_Count'].fillna(df['User_Count'].median(), inplace=True)

# Add the 'Name' column back to the dataframe
df['Name'] = df_name

# Save the cleaned dataframe to a .csv file
df.to_csv('/Users/mustafa/Desktop/Coding Projects/Video Games Sales Analysis/cleaned_video_game_sales_withname.csv', index=False)


