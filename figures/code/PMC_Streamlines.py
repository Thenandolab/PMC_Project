import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Apply Seaborn style to make the plot look better
sns.set_style("whitegrid")


data = {
    'CG_left': [34564, 34291, 19534, 31373, 27116, 34762, 20725, 28523, 22043, 24560, 29532, 19731, 26249, 29611, 24205, 21542, 30943, 22405, 28772, 33903, 27124, 44474, 20382, 39386, 30108, 26793, 25493, 32429, 35316, 39610, 26485, 34651, 41944, 25071, 34906, 26693, 35491, 36142, 38459, 42814],
    'CC_5': [7323, 12183, 7815, 10108, 12550, 9358, 6779, 7284, 7233, 6736, 13830, 5390, 6052, 12358, 9309, 9217, 6868, 6525, 7761, 10073, 4419, 11324, 10877, 8639, 8205, 9918, 10331, 11582, 6575, 12894, 9579, 8873, 13230, 8429, 19681, 9838, 13575, 14980, 13577,8873],
    'CC_7': [3052, 3889, 2787, 3859, 4938, 3190, 2392, 2631, 2745, 2352, 3923, 1787, 2325, 5058, 3886, 2784, 1743, 1961, 3822, 3373, 1492, 3726, 4165, 2618, 4175, 4157, 3790, 3588, 1846, 3148, 3490, 3021, 3859, 3565, 5687, 4928, 4216, 3754, 4373, 2894],
    'MLF_left': [2011, 3516, 2700, 3407, 1833, 2636, 2028, 1532, 2525, 1369, 4854, 928, 2617, 3453, 4221, 1926, 2490, 2117, 2016, 4069, 1605, 3337, 3110, 4783, 3933, 3228, 4206, 4203, 1665, 2918, 2663, 1272, 3222, 1751, 6632, 1434, 1920, 4756, 4123, 2958],
    'T_PAR_left': [1798, 3112, 2119, 5704, 2664, 3149, 1261, 2035, 2446, 1839, 3312, 1072, 2026, 2741, 2897, 2579, 2392, 3307, 2295, 2829, 1714, 3014, 3970, 3884, 2346, 2416, 2927, 4510, 1388, 5427, 2330, 1756, 3009, 2041, 7777, 1077, 3064, 2097, 2993, 4052],
    'ST_OCC_left': [1833, 3106, 2309, 4711, 2021, 2376, 1651, 1563, 2282, 1828, 3033, 1044, 2234, 2847, 2547, 2269, 2025, 2159, 2325, 3751, 1414, 3456, 3456, 3994, 2401, 2995, 3299, 4037, 1589, 4485, 2350, 1584, 2975, 1764, 6286, 1356, 2221, 2698, 3028, 3818],
    'SLF_I_left': [658, 1517, 1475, 3128, 1651, 778, 64, 1014, 444, 1045, 203, 825, 265, 415, 386, 610, 151, 632, 2000, 1639, 1103, 1332, 3042, 1059, 2571, 5130, 3458, 1561, 586, 2843, 724, 187, 966, 313, 4064, 2162, 2664, 780, 744, 1541],
    'CC_4': [1590, 1054, 1321, 1205, 1435, 1577, 573, 2104, 1745, 380, 1700, 1328, 1054, 3000, 943, 1016, 250, 792, 1207, 1091, 1086, 1605, 830, 1245, 579, 1103, 967, 1451, 1128, 280, 1909, 1748, 3008, 1115, 3012, 1559, 1742, 2530, 1623, 1441],
    'CC_6': [1156, 2491, 346, 367, 444, 979, 80, 275, 1598, 17, 163, 286, 849, 443, 265, 620, 27, 750, 303, 118, 186, 1152, 1555, 1535, 1332, 1072, 1395, 632, 646, 187, 394, 452, 1919, 2199, 713, 9066, 747, 1829, 2603, 337],
    'POPT_left': [274, 797, 548, 1834, 1062, 292, 399, 223, 642, 206, 617, 52, 303, 459, 137, 367, 203, 684, 1200, 1646, 518, 849, 2644, 822, 1219, 1573, 776, 1419, 361, 1579, 220, 258, 706, 97, 3152, 589, 1698, 1127, 572, 1012]
}



# Create a DataFrame from the data and reshape it
data_list = []
for bundle, values in data.items():
    for value in values:
        data_list.append((bundle, value))
        
df = pd.DataFrame(data_list, columns=['Bundles', 'Values'])

fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(x='Bundles', y='Values', data=df, ax=ax, palette="tab10", linewidth=1.5)
sns.stripplot(x='Bundles', y='Values', data=df, jitter=True, color="black", size=4, alpha=0.9)

# Aesthetic modifications
ax.set_ylabel('Streamlines', fontsize=14)
ax.set_ylim(0, 45000)
ax.set_xlabel('Bundles', fontsize=14)
ax.set_title('The number of streamlines that touch the postero medial cortex (PMC) for each bundle.', fontsize=16)
plt.xticks(rotation=15, fontsize=12, ha='right')
plt.yticks(fontsize=12)
sns.despine(left=True, bottom=True)


# Add figure caption
caption = ("")


# Show the plot
plt.show()
