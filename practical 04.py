
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Sample data: Test scores for two groups (new method and traditional method)
new_method_scores = [85, 90, 88, 92, 87, 91, 89, 90, 86, 93]  # New method group scores
traditional_method_scores = [80, 84, 82, 79, 81, 85, 78, 83, 80, 79]  # Traditional method group scores

# Step 1: Formulate Hypotheses
# H₀: There is no difference between the means of the two groups (μ_new = μ_traditional)
# H₁: The new teaching method results in a higher mean test score (μ_new > μ_traditional)

# Step 2: Perform the t-test
# We will use a one-tailed t-test to test if the new method is better.
t_stat, p_value = stats.ttest_ind(new_method_scores, traditional_method_scores, alternative='greater')

# Step 3: Interpret the result
alpha = 0.05  # Significance level (5%)

# If p-value is less than alpha, reject the null hypothesis
if p_value < alpha:
    result = "Reject the null hypothesis: The new teaching method is more effective."
else:
    result = "Fail to reject the null hypothesis: No significant difference between the methods."

# Step 4: Output the results
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(result)

# Step 5: Plot the distributions of the two groups
plt.figure(figsize=(10, 6))

# Plot the histogram of both groups with different colors
sns.histplot(new_method_scores, kde=True, color='blue', label='New Method', stat="density", linewidth=0)
sns.histplot(traditional_method_scores, kde=True, color='green', label='Traditional Method', stat="density", linewidth=0)

# Customize the plot
plt.title('Distribution of Test Scores for Both Teaching Methods', fontsize=16)
plt.xlabel('Test Scores', fontsize=14)
plt.ylabel('Density', fontsize=14)
plt.legend()

# Show the plot
plt.show()

