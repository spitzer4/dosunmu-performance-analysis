import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
	# Step 1: Load the cleaned data
	ayo_stats_df = pd.read_csv('data/processed/dosunmu_cleaned_stats.csv')
	
	# Step 2: Group by 'Home/Away' and calculate average points
	avg_points = ayo_stats_df.groupby('Home/Away')['PTS'].mean().reset_index()
	print("Average Points by Home/Away:\n", avg_points)
	
	# Step 3: Create visualizations
	
	# Bar plot for average points
	plt.figure(figsize=(8, 6))
	sns.barplot(x='Home/Away', y='PTS', data=avg_points, palette='Blues')
	plt.title("Average Points: Home vs Away Games")
	plt.ylabel("Average Points")
	plt.xlabel("Game Location")
	plt.savefig("reports/figures/average_points_home_vs_away.png")
	plt.show()
	
	# Points distribution by game location
	plt.figure(figsize=(10, 6))
	sns.boxplot(x='Home/Away', y='PTS', data=ayo_stats_df, palette='coolwarm')
	plt.title("Points Distribution: Home vs Away Games")
	plt.ylabel("Points")
	plt.xlabel("Game Location")
	plt.savefig("reports/figures/points_distribution_home_vs_away.png")
	plt.show()

except Exception as e:
	print(f"An error occurred during analysis: {e}")

