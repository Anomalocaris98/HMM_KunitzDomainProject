import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Define confusion matrix manually
TN =286285
FP =1
FN =3
TP =181 
cm = np.array([[TN, FP], [FN, TP]])

# Plot
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Predicted Negative', 'Predicted Positive'],
            yticklabels=['Actual Negative', 'Actual Positive'], ax=ax)
ax.set_xlabel('Prediction')
ax.set_ylabel('Actual')
ax.set_title('PERFORMANCES SET_1 USING E-VALUE THRESHOLD OF SET_2 - FULL SEQUENCES')

# Save image to current directory
output_file = 'full sequence, trained SET2, test SET1.png'
plt.savefig(output_file, bbox_inches='tight')
print(f"Saved confusion matrix as: {output_file}")
