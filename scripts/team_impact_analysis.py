import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create reports/figures directory if it doesn't exist
figures_dir = Path('reports/figures')
figures_dir.mkdir(parents=True, exist_ok=True)

# Load the cleaned data
data_path = Path('data/processed/dosunmu_cleaned_stats.csv')
df = pd.read_csv(data_path)

# Load the Bulls' game results data
game_results_path = Path('data/raw/chicago_bulls_game_stats.csv')
game_results_df = pd.read_csv(game_results_path)

# 1. Convert columns to appropriate data types (if necessary)
df['Date'] = pd.to_datetime(df['Date'])  # Ensure 'Date' is in datetime format
df['PTS'] = pd.to_numeric(df['PTS'], errors='coerce')
df['AST'] = pd.to_numeric(df['AST'], errors='coerce')
df['TRB'] = pd.to_numeric(df['TRB'], errors='coerce')
df['FG%'] = pd.to_numeric(df['FG%'], errors='coerce')
df['+/-'] = pd.to_numeric(df['+/-'], errors='coerce')

# 2. Load and clean the game results data
game_results_df['Date'] = pd.to_datetime(game_results_df['Date'], format='%a, %b %d, %Y')  # Ensure proper date format
game_results_df['Opponent'] = game_results_df['Opponent'].str.strip()  # Clean opponent names if necessary

# 3. Merge Ayo's performance data with the game results data based on Date and Opponent
merged_df = pd.merge(df, game_results_df[['Date', 'Opponent', 'W', 'L']], how='left', left_on=['Date', 'Opp'], right_on=['Date', 'Opponent'])

# 4. Create a new 'Result' column based on 'W'/'L' values from the game results
merged_df['Result'] = merged_df['L'].apply(lambda x: 'Loss' if pd.notna(x) else 'Win')

# 5. Analyze performance in wins vs losses
performance_wins = merged_df[merged_df['Result'] == 'Win']
performance_losses = merged_df[merged_df['Result'] == 'Loss']

# 6. Calculate and display averages for wins and losses
average_performance_wins = performance_wins[['PTS', 'AST', 'TRB', 'FG%', '+/-']].mean()
average_performance_losses = performance_losses[['PTS', 'AST', 'TRB', 'FG%', '+/-']].mean()

print("Average Performance in Wins:")
print(average_performance_wins)
print("\nAverage Performance in Losses:")
print(average_performance_losses)

# 7. Visualizing performance in wins vs losses
def plot_performance_comparison(wins_data, losses_data):
    # Create a comparison bar chart for performance metrics
    metrics = ['PTS', 'AST', 'TRB', 'FG%', '+/-']
    
    # Plot performance comparison for each metric
    plt.figure(figsize=(10, 6))

    # Plot wins
    wins_values = [wins_data[metric] for metric in metrics]
    plt.bar(metrics, wins_values, width=0.4, label='Wins', align='center', color='g')

    # Plot losses
    losses_values = [losses_data[metric] for metric in metrics]
    plt.bar(metrics, losses_values, width=0.4, label='Losses', align='edge', color='r')

    # Title and labels
    plt.title('Ayo Dosunmu Performance Comparison: Wins vs Losses')
    plt.xlabel('Metrics')
    plt.ylabel('Average Value')
    plt.legend()

    # Save the figure
    plt.tight_layout()
    plt.savefig(figures_dir / 'performance_comparison_wins_vs_losses.png')
    plt.close()

# Call function to generate comparison bar chart
plot_performance_comparison(average_performance_wins, average_performance_losses)

# 8. Correlation between Ayo's performance and team success
def analyze_performance_correlation(df):
    # Correlation between Ayo's performance and team success
    correlation_df = df[['PTS', 'AST', 'TRB', 'FG%', '+/-']]
    correlation_matrix = correlation_df.corr()

    print("\nCorrelation Matrix for Ayo's Performance and Team Success:")
    print(correlation_matrix)

    # Visualize the correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix: Ayo Dosunmu Performance vs Team Success')
    plt.tight_layout()

    # Save the figure
    plt.savefig(figures_dir / 'performance_correlation_matrix.png')
    plt.close()

# Call the function to visualize performance correlations
analyze_performance_correlation(merged_df)

# 9. Analyze Ayo's impact on team +/-
def plot_impact_on_plus_minus(df):
    # Scatter plot to show Ayo's points vs team +/- to visualize his impact
    plt.figure(figsize=(10, 6))

    sns.scatterplot(x=df['PTS'], y=df['+/-'], color='b')
    plt.title('Ayo Dosunmu: Points Scored vs Team Impact (+/-)')
    plt.xlabel('Points Scored')
    plt.ylabel('Team Impact (+/-)')
    plt.tight_layout()

    # Save the figure
    plt.savefig(figures_dir / 'points_vs_plus_minus.png')
    plt.close()

# Call the function to visualize Ayo's impact on team +/- 
plot_impact_on_plus_minus(merged_df)

