import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.stats.multicomp as mc
from statsmodels.formula.api import ols

def perform_anova():
    # Define four groups of data
    data = {
        'A': [23, 25, 27, 29, 31],
        'B': [20, 21, 22, 23, 24],
        'C': [30, 32, 34, 36, 38],
        'D': [15, 17, 19, 21, 23]
    }
    
    # Create DataFrame
    df = pd.DataFrame({
        'values': sum(data.values(), []),
        'group': [group for group, values in data.items() for _ in values]
    })
    
    # Perform One-Way ANOVA
    f_stat, p_value = stats.f_oneway(data['A'], data['B'], data['C'], data['D'])
    print(f"\nOne-Way ANOVA Results:\nF-statistic: {f_stat:.4f}, P-value: {p_value:.4f}")
    
    # Tukey-Kramer Post-Hoc Test
    tukey = mc.MultiComparison(df['values'], df['group'])
    tukey_results = tukey.tukeyhsd()
    print("\nTukey-Kramer Post-Hoc Test Results:\n", tukey_results)

if __name__ == "__main__":
    perform_anova()

