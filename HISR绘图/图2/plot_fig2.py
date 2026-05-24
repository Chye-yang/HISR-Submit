from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['font.family'] = 'Times New Roman'

markersize = 6
fontsize = 14
color_hisr = [213/255, 38/255, 36/255]

memory = np.array([40, 60, 80, 100, 120])

# 子图1: AAE
AAE = {
    'ALSketch':      [1.9807126511932005, 1.0660346518470087, 0.6430205949656751, 0.4687806472703498, 0.34390323635174896],
    'ML-Sketch':     [1.5675913660929226, 0.722767839900572, 0.4735606690566109, 0.3301217014511335, 0.2641441033688508],
    'TalentSketch':  [1.4717339472896953, 1.469539179058393, 1.501696657222562, 1.6491516905307926, 1.6488538699315318],
    'DeepSketch':    [2.080366332143613, 2.0752655727171985, 2.0733922538744856, 2.072257527575535, 2.071696023997157],
    'ZoomSynth-GTT': [4.859332228844834, 4.482083299417985, 4.355904851796854, 4.444720518592916, 4.473352005373384],
    'UCL-ML':        [4.289009111617312, 2.832289293849658, 2.042995444191344, 1.3294419134396356, 1.9951594533029613],
    'HISR':          [0.8811818940020718, 0.37714517782017326, 0.27266161615336537, 0.20335189475550408, 0.13463808420516063],
}

# 子图2: ARE
ARE = {
    'ALSketch':      [1.5028406957000482, 0.7798371178113542, 0.43378588268265234, 0.29955474221671724, 0.19930274930525538],
    'ML-Sketch':     [1.0785393746074983, 0.46587810532634394, 0.3502680523731163, 0.23366725175860376, 0.17059656760154707],
    'TalentSketch':  [0.8528414450097808, 0.2508552760072342, 0.2548739025063962, 0.36940303451807543, 0.3689251304842825],
    'DeepSketch':    [1.072425881486902, 1.0683219268760604, 1.066151957434122, 1.0648730314155654, 1.0644900237504376],
    'ZoomSynth-GTT': [3.4948864374330597, 3.1935557020992773, 3.1870059913943045, 3.2753861361774397, 3.271034392676117],
    'UCL-ML':        [3.3294738389540597, 2.3235747462319085, 1.7070684533059586, 1.1285737088757728, 1.641563795669456],
    'HISR':          [0.6643378171589354, 0.2840040073845404, 0.1939138380413901, 0.1538623137258687, 0.10166175590329898],
}

# 子图3: WMRD
WMRD = {
    'ALSketch':      [0.8078666666666666, 0.4348, 0.26226666666666665, 0.1912, 0.14026666666666668],
    'ML-Sketch':     [0.6393682651837667, 0.2947929096341133, 0.19314961155255636, 0.13464563796520232, 0.10773557496070862],
    'TalentSketch':  [0.6002712193012237, 0.5993760464986165, 0.6124920099258423, 0.6726340028444926, 0.6725125317494075],
    'DeepSketch':    [0.8485120813369751, 0.8464316515922546, 0.8456675872802735, 0.8452047702471415, 0.844975751654307],
    'ZoomSynth-GTT': [1.9819596384048461, 1.8280923750559488, 1.7766283922195434, 1.812853342183431, 1.8245311712582906],
    'UCL-ML':        [0.8702660542508016, 0.6666219884059914, 0.529266403570243, 0.37960892719216227, 0.5195180722891566],
    'HISR':          [0.30195095610841044, 0.13156632888689368, 0.09535399087447625, 0.07110506401323405, 0.04712665845324743],
}

methods_style = {
    'ALSketch':      {'marker': '^', 'color': 'orange'},
    'ML-Sketch':     {'marker': 'D', 'color': 'saddlebrown'},
    'TalentSketch':  {'marker': 's', 'color': 'indigo'},
    'DeepSketch':    {'marker': 'H', 'color': 'green'},
    'ZoomSynth-GTT': {'marker': 'h', 'color': 'royalblue'},
    'UCL-ML':        {'marker': 'v', 'color': 'darkgoldenrod'},
    'HISR':          {'marker': 'o', 'color': color_hisr},
}

datasets = [('AAE', AAE), ('ARE', ARE), ('WMRD', WMRD)]
subtitles = ['(a) AAE', '(b) ARE', '(c) WMRD']

figure = plt.figure(figsize=(12, 3.5))

for idx, (metric_name, data) in enumerate(datasets):
    ax = plt.subplot(1, 3, idx + 1)
    for method, values in data.items():
        style = methods_style[method]
        plt.plot(memory, values, marker=style['marker'], color=style['color'],
                 markersize=markersize, lw=1.5, label=method)
    plt.grid(ls='--')
    plt.xticks(memory, [str(m) for m in memory], fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.xlabel('Memory Size (KB)', fontsize=fontsize)
    plt.ylabel(metric_name, fontsize=fontsize)

for idx, subtitle in enumerate(subtitles):
    axes = figure.axes[idx]
    axes.text(0.5, -0.32, subtitle, transform=axes.transAxes,
              fontsize=14, ha='center', va='top')

figure.legend(list(methods_style.keys()), prop={'size': 11}, ncol=7,
              loc='upper center', bbox_to_anchor=(0.51, 0.99), frameon=False)
plt.tight_layout(rect=[0, 0.08, 1, 0.92])
figure.subplots_adjust(left=0.07, right=0.98, bottom=0.18, top=0.88, wspace=0.32)

plt.savefig("fig2_kosarak.png", format='png', dpi=800, bbox_inches='tight')
plt.savefig("fig2_kosarak.pdf", format='pdf', dpi=800, bbox_inches='tight')
print("图2已保存: fig2_kosarak.png / fig2_kosarak.pdf")
