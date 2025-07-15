import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Apply Seaborn style to make the plot look better
sns.set(style="whitegrid", palette="Set2", color_codes=True)

# Set the font style for the plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Arial'

data = {
    'CG': [67, 52, 50, 56, 59, 72, 72, 53, 63, 54, 74, 57, 66, 65, 60, 65, 60, 77, 56, 62, 59, 58, 58, 61, 49, 53, 61, 67, 58, 51, 67, 62, 54, 56, 66, 60, 59, 72, 64, 66],
    'CC_5': [18, 20, 21, 22, 17, 10, 11, 18, 14, 20, 15, 19, 16, 14, 15, 13, 16, 13, 19, 14, 19, 20, 19, 16, 21, 15, 16, 12, 17, 22, 17, 16, 19, 21, 14, 15, 21, 12, 13, 17],
    'CC_7': [5, 7, 8, 6, 6, 4, 4, 7, 4, 7, 4, 6, 5, 7, 7, 4, 7, 4, 8, 5, 7, 5, 6, 8, 6, 6, 6, 6, 7, 8, 4, 5, 8, 7, 5, 5, 6, 4, 4, 7],
    'T_PAR': [5, 6, 7, 5, 6, 5, 3, 8, 6, 6, 2, 5, 5, 4, 5, 6, 4, 2, 5, 5, 4, 3, 5, 2, 8, 10, 6, 3, 4, 6, 7, 6, 7, 5, 5, 5, 6, 5, 8, 2],
    'MLF': [1, 5, 5, 6, 2, 2, 1, 3, 5, 4, 1, 3, 2, 2, 4, 3, 3, 1, 2, 4, 3, 4, 2, 0, 5, 4, 3, 2, 3, 2, 1, 2, 6, 4, 2, 4, 2, 2, 4, 0],
    'CC_4': [1, 2, 3, 2, 3, 2, 2, 2, 3, 5, 2, 5, 1, 4, 1, 2, 2, 2, 5, 2, 3, 6, 3, 3, 4, 2, 3, 2, 4, 3, 1, 2, 2, 3, 4, 4, 2, 2, 2, 3],
    'ST_OCC': [1, 3, 2, 2, 2, 1, 2, 3, 2, 3, 1, 3, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 3, 3, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 3, 1],
    'CC_6': [0, 3, 1, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 0, 2, 1, 1, 0, 5, 2, 3, 2, 0, 7, 0, 0, 2, 3, 3, 1, 0, 1, 0, 0, 0, 2, 1, 0, 1, 3],
    'POPT': [0, 1, 2, 1, 3, 1, 0, 4, 1, 0, 0, 1, 1, 1, 2, 2, 3, 0, 0, 2, 1, 1, 2, 1, 2, 3, 1, 1, 1, 3, 1, 1, 0, 2, 0, 1, 1, 0, 2, 0],
    'SLF_I': [1, 2, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 2, 1, 3, 0, 0, 3, 0, 0, 2, 1, 2, 4, 0, 1, 0, 2, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
}


normalized_data = {}
for key, values in data.items():
    normalized_data[key] = [value / 100 for value in values]

# Create a DataFrame from the normalized data and reshape it
data_list = []
for bundle, values in normalized_data.items():
    for value in values:
        data_list.append((bundle, value))

df = pd.DataFrame(data_list, columns=['Bundles', 'Values'])

fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(x='Bundles', y='Values', data=df, ax=ax, palette="viridis", linewidth=2)
sns.stripplot(x='Bundles', y='Values', data=df, jitter=True, color="black", size=5, alpha=0.9)

# Aesthetic modifications
ax.set_ylabel('Percent (%)', fontsize=16, fontweight='bold')
ax.set_ylim(0, 1)
ax.set_xlabel('Bundles', fontsize=16, fontweight='bold')
ax.set_title('PMC Connectivity Across Different Fiber Bundles', fontsize=20, fontweight='bold', pad=20)
plt.xticks(rotation=15, fontsize=14, ha='right', fontweight='bold')
plt.yticks(fontsize=14, fontweight='bold')
sns.despine(left=True, bottom=True)

# Create legend
legend_labels = {
    'CG': 'Cingulum',
    'CC_5': 'Posterior midbody (Primary Somatosensory)',
    'CC_7': 'Splenium',
    'MLF': 'Middle longitudinal fascicle',
    'T_PAR': 'Thalamo-parietal',
    'ST_OCC': 'Striato-occipital',
    'SLF_I': 'Superior longitudinal fascicle I',
    'CC_4': 'Anterior midbody (Primary Motor)',
    'CC_6': 'Isthmus',
    'POPT': 'Parieto-occipital pontine'
}

legend_patches = [plt.plot([],[], marker="s", ls="", mec=None, color=sns.color_palette("viridis", len(legend_labels))[i], 
           label="{}: {}".format(key, label))[0] for i, (key, label) in enumerate(legend_labels.items())]

plt.legend(handles=legend_patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=12)

# Save the plot as an HD image
plt.savefig('PMCStreamlinesProportionRelativeToTotal_.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()







