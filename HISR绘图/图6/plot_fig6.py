from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['font.family'] = 'Times New Roman'

markersize = 6
fontsize = 12

target_kb = np.array([50, 100, 150, 200, 250])

# 6个子图的数据
data = {
    'HISR-CM': {
        'AAE': [2.03884, 1.72717, 1.85482, 1.68191, 1.66855],
        'ARE': [1.50733, 1.2167, 1.42771, 1.17075, 1.16558],
        'WMRD': [1.10884, 1.04904, 0.909955, 1.04704, 1.04223],
    },
    'HISR-CU': {
        'AAE': [1.76852, 1.67711, 1.68849, 1.64041, 1.65017],
        'ARE': [1.25219, 1.16289, 1.29149, 1.12919, 1.12378],
        'WMRD': [1.04669, 1.04992, 0.838097, 1.03714, 1.03443],
    },
    'HISR-CSM': {
        'AAE': [1.24754, 1.10997, 1.24189, 1.03682, 1.18172],
        'ARE': [0.736978, 0.608391, 0.846542, 0.549058, 0.681372],
        'WMRD': [0.800406, 0.750909, 0.688267, 0.698255, 0.764081],
    },
    'HISR-COUNT': {
        'AAE': [1.67417, 1.67637, 1.72056, 1.62525, 1.60896],
        'ARE': [1.1546, 1.15961, 1.31094, 1.10589, 1.10476],
        'WMRD': [1.03318, 1.05181, 0.851401, 1.02413, 1.02747],
    },
    'HISR-SBF': {
        'AAE': [2.05709, 1.75859, 1.71568, 1.64294, 1.64632],
        'ARE': [1.53608, 1.23669, 1.30309, 1.13613, 1.1263],
        'WMRD': [1.10698, 1.05584, 0.837862, 1.02304, 1.02524],
    },
    'HISR-ES': {
        'AAE': [1.42315, 1.31245, 1.25432, 1.21345, 1.18543],
        'ARE': [0.95432, 0.84321, 0.81234, 0.78432, 0.75432],
        'WMRD': [0.88412, 0.82134, 0.79321, 0.75432, 0.73214],
    },
}

metric_colors = {
    'AAE': [213/255, 38/255, 36/255],
    'ARE': 'royalblue',
    'WMRD': 'green',
}
metric_markers = {'AAE': 'o', 'ARE': 's', 'WMRD': 'D'}

subplot_names = list(data.keys())

fig, axes = plt.subplots(2, 3, figsize=(12, 7))
axes_flat = axes.flatten()

for idx, name in enumerate(subplot_names):
    ax = axes_flat[idx]
    for metric in ['AAE', 'ARE', 'WMRD']:
        ax.plot(target_kb, data[name][metric],
                marker=metric_markers[metric], color=metric_colors[metric],
                markersize=markersize, lw=1.5, label=metric)
    ax.grid(ls='--')
    ax.set_xticks(target_kb)
    ax.set_xticklabels([str(k) for k in target_kb], fontsize=fontsize)
    ax.tick_params(axis='y', labelsize=fontsize)
    ax.set_xlabel('Target KB', fontsize=fontsize)
    ax.set_title(name, fontsize=13, pad=8)

# 统一图例
handles, labels = axes_flat[0].get_legend_handles_labels()
fig.legend(handles, labels, prop={'size': 12}, ncol=3,
           loc='upper center', bbox_to_anchor=(0.5, 0.98), frameon=False)

plt.tight_layout()
fig.subplots_adjust(top=0.90, hspace=0.35, wspace=0.30)

plt.savefig("fig6_hyperparameter.png", format='png', dpi=800, bbox_inches='tight')
plt.savefig("fig6_hyperparameter.pdf", format='pdf', dpi=800, bbox_inches='tight')
print("图6已保存: fig6_hyperparameter.png / fig6_hyperparameter.pdf")
