import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load cleaned and processed data 
data_path = Path('data/processed/dosunmu_cleaned_stats.csv')
df = pd.read_csv(data_path)

# 1. Convert columns to appropriate data types (if necessary)
df['Date'] = pd.to_datetime(df['Date'])  # Ensure the 'Date' column is datetime
df['PTS'] = pd.to_numeric(df['PTS'], errors='coerce')  # Ensure 'PTS' is numeric
df['Game'] = df['G']  # Using 'G' as the game number or use 'Date' for chronological order

# 2. Calculate rolling averages (e.g., 3-game rolling average for points, assists, and rebounds)
df['Rolling_PTS'] = df['PTS'].rolling(window=3).mean()
df['Rolling_AST'] = df['AST'].rolling(window=3).mean()
df['Rolling_REB'] = df['TRB'].rolling(window=3).mean()

# 3. Plot the performance trends over time
def plot_performance_trends(df):
    plt.figure(figsize=(14, 10))

    # Plot Points
    plt.subplot(3, 1, 1)
    plt.plot(df['Game'], df['PTS'], label='Points', color='b', marker='o', markersize=5)
    plt.plot(df['Game'], df['Rolling_PTS'], label='3-Game Rolling Avg', color='orange', linestyle='--')
    plt.title('Points per Game')
    plt.xlabel('Game')
    plt.ylabel('Points')
    plt.legend(loc='upper right')

    # Plot Assists
    plt.subplot(3, 1, 2)
    plt.plot(df['Game'], df['AST'], label='Assists', color='g', marker='o', markersize=5)
    plt.plot(df['Game'], df['Rolling_AST'], label='3-Game Rolling Avg', color='purple', linestyle='--')
    plt.title('Assists per Game')
    plt.xlabel('Game')
    plt.ylabel('Assists')
    plt.legend(loc='upper right')

    # Plot Rebounds
    plt.subplot(3, 1, 3)
    plt.plot(df['Game'], df['TRB'], label='Rebounds', color='r', marker='o', markersize=5)
    plt.plot(df['Game'], df['Rolling_REB'], label='3-Game Rolling Avg', color='yellow', linestyle='--')
    plt.title('Rebounds per Game')
    plt.xlabel('Game')
    plt.ylabel('Rebounds')
    plt.legend(loc='upper right')

    plt.tight_layout()
    
	# Save the figure
    plt.savefig('reports/figures/performance_trends.png')
    plt.close()

# Call the plotting function
plot_performance_trends(df)

# 4. Analyze shooting efficiency (FG%, 3P%, FT%) - This can give insights into overall efficiency
def plot_shooting_efficiency(df):
    plt.figure(figsize=(12, 6))
    
    # Field Goal Percentage (FG%)
    plt.subplot(1, 3, 1)
    plt.plot(df['Game'], df['FG%'], label='Field Goal %', color='b', marker='o', markersize=5)
    plt.title('Field Goal Percentage')
    plt.xlabel('Game')
    plt.ylabel('FG%')
    plt.ylim(0, 1)
    plt.legend(loc='upper right')

    # Three-Point Percentage (3P%)
    plt.subplot(1, 3, 2)
    plt.plot(df['Game'], df['3P%'], label='3-Point %', color='g', marker='o', markersize=5)
    plt.title('3-Point Percentage')
    plt.xlabel('Game')
    plt.ylabel('3P%')
    plt.ylim(0, 1)
    plt.legend(loc='upper right')

    # Free Throw Percentage (FT%)
    plt.subplot(1, 3, 3)
    plt.plot(df['Game'], df['FT%'], label='Free Throw %', color='r', marker='o', markersize=5)
    plt.title('Free Throw Percentage')
    plt.xlabel('Game')
    plt.ylabel('FT%')
    plt.ylim(0, 1)
    plt.legend(loc='upper right')

    plt.tight_layout()
    
	# Save the figure
    plt.savefig('reports/figures/shooting_efficiency.png')
    plt.close()

# Call the shooting efficiency function
plot_shooting_efficiency(df)

# 5. Detecting performance streaks based on points scored (e.g., 20+ points in 3 consecutive games)
def detect_streaks(df, metric, threshold=20):
    streaks = []
    current_streak = 0

    for i, value in enumerate(df[metric]):
        if value >= threshold:
            current_streak += 1
        else:
            if current_streak >= 3:
                streaks.append((i - current_streak, i - 1))
            current_streak = 0

    # Check if the last streak was a long one
    if current_streak >= 3:
        streaks.append((len(df) - current_streak, len(df) - 1))

    return streaks

# Detect streaks where Ayo scored more than 20 points
streaks = detect_streaks(df, 'PTS', threshold=20)

# Print detected streaks
if streaks:
    print(f"Found streaks where points exceeded 20:")
    for start, end in streaks:
        print(f"Game {start + 1} to Game {end + 1}")
else:
    print("No performance streaks above the threshold were found.")
