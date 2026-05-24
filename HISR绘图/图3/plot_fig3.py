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
    'ALSketch':      [2.028485254691689, 1.103887399463807, 0.6367292225201072, 0.4584450402144772, 0.3475201072386059],
    'ML-Sketch':     [1.5571782885383985, 0.8942634242389541, 0.671504658065117, 0.3231781748280768, 0.271356392721708],
    'TalentSketch':  [1.5565292636686612, 1.5477264812540752, 1.5602834304599915, 1.5600630115847485, 1.5619081127939212],
    'DeepSketch':    [1.7751901538058836, 1.7804684912231588, 1.7793251411844515, 1.7772476244867648, 1.7785636226549226],
    'ZoomSynth-GTT': [4.78462288310956, 4.564019137588966, 4.555839995676327, 4.280888418969137, 4.404242609445276],
    'UCL-ML':        [8.76951566951567, 4.665242165242165, 3.2165242165242165, 2.394301994301994, 3.4068376068376067],
    'HISR':          [1.0571273241114285, 0.4774243828268418, 0.303839715430281, 0.19550178211967406, 0.15081982098522136],
}

# 子图2: ARE
ARE = {
    'ALSketch':      [1.468910409292923, 0.7685256664289188, 0.42882451452687453, 0.28222062499575845, 0.19631461504939268],
    'ML-Sketch':     [1.0353676180641131, 0.5464473752177473, 0.3264927443070301, 0.20649185413759874, 0.17127048163544223],
    'TalentSketch':  [0.27680293923237137, 0.2711416850232215, 0.2808221394752521, 0.27974891438317506, 0.28134761465798236],
    'DeepSketch':    [0.7562120533784435, 0.7637362215197881, 0.7628054178158018, 0.7618905069607831, 0.7626615116176257],
    'ZoomSynth-GTT': [3.268852655433975, 3.2658784119668596, 3.2247024748049764, 2.961726210660798, 3.1485190293377783],
    'UCL-ML':        [6.255110823476092, 3.5559991965837825, 2.49543398834764, 1.9053900747618353, 2.6451912371986332],
    'HISR':          [0.7151235336184842, 0.3110254467963339, 0.21440264516236635, 0.13632769592136162, 0.14493914450079878],
}

# 子图3: WMRD
WMRD = {
    'ALSketch':      [0.8070666666666667, 0.4392, 0.25333333333333335, 0.1824, 0.13826666666666668],
    'ML-Sketch':     [0.6195493350664775, 0.35579760772387187, 0.2671693199555079, 0.12858182315826416, 0.10796366345087687],
    'TalentSketch':  [0.6192911097049714, 0.6157887760082881, 0.6207847675323487, 0.6206970702091853, 0.6214311744769414],
    'DeepSketch':    [0.7062889891942342, 0.7083890637079875, 0.7079341628392537, 0.7071075881958008, 0.7076311800003052],
    'ZoomSynth-GTT': [1.9036419577598571, 1.8158710808753968, 1.8126168729464214, 1.7032228056271872, 1.7523013262112936],
    'UCL-ML':        [1.227239200207324, 0.904921112983891, 0.7229764344262295, 0.5922480620155038, 0.7489665539270951],
    'HISR':          [0.3624996675830587, 0.16583333788877447, 0.10650184593339403, 0.06822675849342766, 0.07023443847802256],
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

plt.savefig("fig3_retail.png", format='png', dpi=800, bbox_inches='tight')
plt.savefig("fig3_retail.pdf", format='pdf', dpi=800, bbox_inches='tight')
print("图3已保存: fig3_retail.png / fig3_retail.pdf")
