import pandas as pd

input_file = 'data/raw/ayo_dosunmu_game_stats.csv'
output_file = 'data/processed/dosunmu_cleaned_stats.csv'

try:
	# Step 1: Load the raw data
	ayo_stats_df = pd.read_csv(input_file)
	
	# Step 2: Drop rows without points data
	ayo_stats_df.dropna(subset=['PTS'], inplace=True)
	
	# Step 3: Convert 'PTS' column to integers
	ayo_stats_df['PTS'] = ayo_stats_df['PTS'].astype(int)
	
	# Step 4: Add 'Home/Away' column
	ayo_stats_df['Home/Away'] = ayo_stats_df['Opp'].apply(lambda x: 'Away' if '@' in x else 'Home')
	
	# Step 5: Save the cleaned data
	ayo_stats_df.to_csv(output_file, index=False)
	print(f"Cleaned data saved to {output_file}")

except Exception as e:
	print(f"An error occurred: {e}")

