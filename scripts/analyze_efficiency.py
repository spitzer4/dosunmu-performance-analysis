import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create reports/figures directory if it doesn't exist
figures_dir = Path('reports/figures')
figures_dir.mkdir(parents=True, exist_ok=True)

# Load the cleaned and processed data (ensure the correct path is specified)
data_path = Path('data/processed/dosunmu_cleaned_stats.csv')
df = pd.read_csv(data_path)

# 1. Convert columns to appropriate data types (if necessary)
df['Date'] = pd.to_datetime(df['Date'])  # Ensure the 'Date' column is datetime
df['FG%'] = pd.to_numeric(df['FG%'], errors='coerce')  # Ensure 'FG%' is numeric
df['3P%'] = pd.to_numeric(df['3P%'], errors='coerce')  # Ensure '3P%' is numeric
df['FT%'] = pd.to_numeric(df['FT%'], errors='coerce')  # Ensure 'FT%' is numeric

# 2. Calculate the mean shooting efficiency for each metric
mean_fg = df['FG%'].mean()
mean_3p = df['3P%'].mean()
mean_ft = df['FT%'].mean()

print(f"Mean Field Goal Percentage (FG%): {mean_fg:.2f}")
print(f"Mean 3-Point Percentage (3P%): {mean_3p:.2f}")
print(f"Mean Free Throw Percentage (FT%): {mean_ft:.2f}")

# 3. Visualize shooting efficiency over time
def plot_shooting_efficiency(df):
    plt.figure(figsize=(14, 6))

    # Field Goal Percentage (FG%)
    plt.subplot(1, 3, 1)
    plt.plot(df['Date'], df['FG%'], label='Field Goal %', color='b', marker='o', markersize=5)
    plt.axhline(mean_fg, color='gray', linestyle='--', label=f'Mean FG%: {mean_fg:.2f}')
    plt.title('Field Goal Percentage')
    plt.xlabel('Game Date')
    plt.ylabel('FG%')
    plt.legend(loc='upper left')

    # Three-Point Percentage (3P%)
    plt.subplot(1, 3, 2)
    plt.plot(df['Date'], df['3P%'], label='3-Point %', color='g', marker='o', markersize=5)
    plt.axhline(mean_3p, color='gray', linestyle='--', label=f'Mean 3P%: {mean_3p:.2f}')
    plt.title('3-Point Percentage')
    plt.xlabel('Game Date')
    plt.ylabel('3P%')
    plt.legend(loc='upper left')

    # Free Throw Percentage (FT%)
    plt.subplot(1, 3, 3)
    plt.plot(df['Date'], df['FT%'], label='Free Throw %', color='r', marker='o', markersize=5)
    plt.axhline(mean_ft, color='gray', linestyle='--', label=f'Mean FT%: {mean_ft:.2f}')
    plt.title('Free Throw Percentage')
    plt.xlabel('Game Date')
    plt.ylabel('FT%')
    plt.legend(loc='upper left')

    plt.tight_layout()

    # Save the figure
    plt.savefig(figures_dir / 'shooting_efficiency_over_time.png')
    plt.close()

# Call the function to visualize shooting efficiency
plot_shooting_efficiency(df)

# 4. Visualizing Field Goal Percentage against Points Scored
def plot_fg_vs_pts(df):
    plt.figure(figsize=(10, 6))

    sns.scatterplot(x=df['FG%'], y=df['PTS'], color='b')
    plt.title('Field Goal Percentage vs Points Scored')
    plt.xlabel('Field Goal Percentage')
    plt.ylabel('Points Scored')
    plt.tight_layout()

    # Save the figure
    plt.savefig(figures_dir / 'fg_vs_pts.png')
    plt.close()

# Call the function to visualize FG% vs PTS
plot_fg_vs_pts(df)

# 5. Free Throw Attempts (FTA) and Free Throw Percentage (FT%)
def plot_fta_vs_ft(df):
    plt.figure(figsize=(10, 6))

    sns.scatterplot(x=df['FTA'], y=df['FT%'], color='r')
    plt.title('Free Throw Attempts vs Free Throw Percentage')
    plt.xlabel('Free Throw Attempts')
    plt.ylabel('Free Throw Percentage')
    plt.tight_layout()

    # Save the figure
    plt.savefig(figures_dir / 'fta_vs_ft.png')
    plt.close()

# Call the function to visualize FTA vs FT%
plot_fta_vs_ft(df)

# 6. Efficiency trends based on shooting accuracy (e.g., correlation analysis)
def analyze_efficiency_trends(df):
    # Calculate correlation matrix
    corr_matrix = df[['FG%', '3P%', 'FT%', 'PTS', 'TRB', 'AST']].corr()

    print("\nEfficiency Correlation Matrix:")
    print(corr_matrix)

    # Visualize correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix of Efficiency Metrics')
    plt.tight_layout()

    # Save the figure
    plt.savefig(figures_dir / 'efficiency_correlation_matrix.png')
    plt.close()

# Call the function to analyze and visualize efficiency correlations
analyze_efficiency_trends(df)
