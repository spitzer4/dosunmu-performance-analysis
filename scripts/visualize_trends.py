import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
	# Step 1: Load the cleaned data
	ayo_stats_df = pd.read_csv('data/processed/dosunmu_cleaned_stats.csv')
	
	# Convert the 'Date' column to a datetime object for better time-based analysis
	ayo_stats_df['Date'] = pd.to_datetime(ayo_stats_df['Date'])
	
	# Sort data by date
	ayo_stats_df.sort_values(by='Date', inplace=True)
	
	# Step 2: Plot overall performance trend
	plt.figure(figsize=(12, 6))
	sns.lineplot(x='Date', y='PTS', data=ayo_stats_df, marker='o', label="Overall")
	plt.title("Ayo Dosunmu: Points Scored Over Time")
	plt.ylabel("Points")
	plt.xlabel("Date")
	plt.xticks(rotation=45)
	plt.grid()
	plt.savefig("reports/figures/points_over_time.png")
	plt.show()

except Exception as e:
	print(f"An error occurred during visualization: {e}")

