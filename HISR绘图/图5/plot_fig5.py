import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "Times New Roman",
    "font.size": 12,
    "axes.linewidth": 1.0,
    "xtick.direction": "in",
    "ytick.direction": "in",
})

def style_axis(ax):
    ax.set_axisbelow(True)
    ax.grid(True, axis="y", linestyle=":", linewidth=1.0, alpha=0.6, color="gray")
    ax.tick_params(length=4.0, width=1.0)

# =========================
# 子图1数据: key_aae, key_are, key_wmrd
# =========================
variants = ["HISR-Full", "w/o Bipartite\nEncoder", "w/o Prefix-aware\nBucketization",
            "w/o Specialized\nSplit Decoders", "Single-env\nTraining"]

key_aae = [0.14870394947442337, 0.18205103980981305, 0.17798561330825563, 0.17353145426768565, 0.1641543475138087]
key_are = [0.12801951476100352, 0.1618023127069639, 0.15561123407436697, 0.1534795774511559, 0.1447872333313062]
key_wmrd = [0.13701478698215417, 0.17276070076266464, 0.16919066907510288, 0.16467572031685512, 0.15346987565404974]

# =========================
# 子图2数据: prefix16_are, prefix24_are, prefix32_are, total_mass_rel_error
# =========================
prefix16_are = [0.2545814438280885, 0.17410397119635782, 0.17245241342396952, 0.16811963406405678, 0.156980188455328]
prefix24_are = [0.15113584482705583, 0.17029040624749078, 0.16617680011507072, 0.16039657727930928, 0.2303293060743104]
prefix32_are = [0.14717546350058216, 0.16770123499043194, 0.1626356430731928, 0.15788039701772325, 0.23753757819962598]
total_mass_rel_error = [0.0012389942303444577, 0.0052432055226421664, 0.0038306673537566052, 0.0052451806096711715, 0.03539214718046055]

# =========================
# 配色
# =========================
colors_sub1 = ["#9E3C36", "#ECEAE0", "#B1D3E0"]
colors_sub2 = ["#9E3C36", "#ECEAE0", "#B1D3E0", "#6BAED6"]

# =========================
# 布局
# =========================
fig, axes = plt.subplots(1, 2, figsize=(11, 3.5), gridspec_kw={"wspace": 0.25})
plt.subplots_adjust(left=0.06, right=0.98, top=0.78, bottom=0.32)

x = np.arange(len(variants))

# 子图1: 3 metrics
w = 0.25
ax1 = axes[0]
ax1.bar(x - w, key_aae, width=w, label="Key AAE", color=colors_sub1[0], edgecolor="black", linewidth=0.8)
ax1.bar(x, key_are, width=w, label="Key ARE", color=colors_sub1[1], edgecolor="black", linewidth=0.8)
ax1.bar(x + w, key_wmrd, width=w, label="Key WMRD", color=colors_sub1[2], edgecolor="black", linewidth=0.8)
ax1.set_xticks(x)
ax1.set_xticklabels(variants, fontsize=9)
ax1.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=3,
           frameon=False, fontsize=10, handlelength=1.2, handletextpad=0.2, columnspacing=0.4)
ax1.set_title("(a) Key-level Metrics", fontsize=12, y=-0.42)
style_axis(ax1)

# 子图2: 4 metrics
w2 = 0.2
ax2 = axes[1]
ax2.bar(x - 1.5*w2, prefix16_are, width=w2, label="Prefix16 ARE", color=colors_sub2[0], edgecolor="black", linewidth=0.8)
ax2.bar(x - 0.5*w2, prefix24_are, width=w2, label="Prefix24 ARE", color=colors_sub2[1], edgecolor="black", linewidth=0.8)
ax2.bar(x + 0.5*w2, prefix32_are, width=w2, label="Prefix32 ARE", color=colors_sub2[2], edgecolor="black", linewidth=0.8)
ax2.bar(x + 1.5*w2, total_mass_rel_error, width=w2, label="Mass Rel Error", color=colors_sub2[3], edgecolor="black", linewidth=0.8)
ax2.set_xticks(x)
ax2.set_xticklabels(variants, fontsize=9)
ax2.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=4,
           frameon=False, fontsize=9, handlelength=1.2, handletextpad=0.2, columnspacing=0.3)
ax2.set_title("(b) Prefix-level & Mass Metrics", fontsize=12, y=-0.42)
style_axis(ax2)

plt.savefig("fig5_ablation_module.png", dpi=600, bbox_inches="tight")
plt.savefig("fig5_ablation_module.pdf", dpi=600, bbox_inches="tight")
print("图5已保存: fig5_ablation_module.png / fig5_ablation_module.pdf")
