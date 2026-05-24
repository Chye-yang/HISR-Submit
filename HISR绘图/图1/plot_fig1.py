from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['font.family'] = 'Times New Roman'

markersize = 6
fontsize = 14
color_hisr = [213/255, 38/255, 36/255]

memory = np.array([50, 100, 150, 200, 250])

# 子图1: AAE
AAE = {
    'ALSketch':      [1.9931718061674009, 0.6936123348017621, 0.3579295154185022, 0.21035242290748898, 0.15198237885462554],
    'ML-Sketch':     [1.4304489605752382, 0.5166480356638652, 0.24314136313446819, 0.27711044164481142, 0.1123686057670526],
    'TalentSketch':  [0.7129638282212917, 0.7121268983979582, 0.6801732700564262, 0.6774948184842055, 0.6760597831614742],
    'DeepSketch':    [0.7744967838741084, 0.7887880112631206, 0.825123257390203, 0.8004974557439661, 0.8013907155276395],
    'ZoomSynth-GTT': [4.241385564089872, 4.375825293946371, 4.492001727866707, 4.556283716010627, 4.703648827622115],
    'UCL-ML':        [7.741471301535974, 1.799029911075182, 1.038965238480194, 0.8554567502021019, 2.7385610347615197],
    'HISR':          [0.6795821972045273, 0.37294130236263306, 0.1833697147879128, 0.13928407056359865, 0.10230183100388067],
}

# 子图2: ARE
ARE = {
    'ALSketch':      [1.8019646891459087, 0.6049336950299912, 0.29346416314327883, 0.15316166567805642, 0.10117399374169708],
    'ML-Sketch':     [1.257508425691884, 0.4328267990240692, 0.19924231967768535, 0.20040749947519455, 0.07289197431139453],
    'TalentSketch':  [1.1482704988153849, 0.64954072432220375, 0.21149358624675133, 0.210845300597015206, 0.1069246194877908],
    'DeepSketch':    [1.21161624154303363, 0.5279520952445184, 0.27061037972241575, 0.24285133746729215, 0.24409338372789247],
    'ZoomSynth-GTT': [3.708303695104174, 3.8448293844991706, 3.9653053513778014, 4.036510259678719, 4.175455939020784],
    'UCL-ML':        [7.325929924465979, 1.7309295021116033, 1.0084347673675302, 0.8291551576680395, 2.6627304981912907],
    'HISR':          [0.9068349621667248, 0.3497234645187795, 0.175662676135665, 0.13250862344393688, 0.05791628960436083],
}

# 子图3: WMRD
WMRD = {
    'ALSketch':      [1.2065333333333332, 0.41986666666666667, 0.21666666666666667, 0.12733333333333333, 0.092],
    'ML-Sketch':     [0.8658984374682108, 0.3127442775885264, 0.14718157181739808, 0.09089085400899252, 0.081967129357655845],
    'TalentSketch':  [0.6315807706832886, 0.43107414916356407, 0.41173155280749, 0.4101101967891057, 0.4092415220737457],
    'DeepSketch':    [0.6688287198384603, 0.4774796761512756, 0.49947461180686953, 0.4845677932103475, 0.4851085131327311],
    'ZoomSynth-GTT': [2.567452061462402, 2.64883291126887, 2.7191583792686465, 2.7580704094250996, 2.8472754236539206],
    'UCL-ML':        [1.4191798686960002, 0.716000128695988, 0.4864864864864865, 0.4184758967058172, 0.9176508830859248],
    'HISR':          [0.5774607777594984, 0.22778130324146478, 0.11255018151412127, 0.08603336932545237, 0.06329952550012985],
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

# 子图标题放在下方
for idx, subtitle in enumerate(subtitles):
    axes = figure.axes[idx]
    axes.text(0.5, -0.32, subtitle, transform=axes.transAxes,
              fontsize=14, ha='center', va='top')

figure.legend(list(methods_style.keys()), prop={'size': 11}, ncol=7,
              loc='upper center', bbox_to_anchor=(0.51, 0.99), frameon=False)
plt.tight_layout(rect=[0, 0.08, 1, 0.92])
figure.subplots_adjust(left=0.07, right=0.98, bottom=0.18, top=0.88, wspace=0.32)

plt.savefig("fig1_caida.png", format='png', dpi=800, bbox_inches='tight')
plt.savefig("fig1_caida.pdf", format='pdf', dpi=800, bbox_inches='tight')
print("图1已保存: fig1_caida.png / fig1_caida.pdf")
