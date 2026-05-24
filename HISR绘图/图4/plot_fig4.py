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
variants = ["L1 only", "L1+L2", "Full"]
key_aae = [0.17630673390802612, 0.1620952005153881, 0.11127616481432087]
key_are = [0.15690439095888187, 0.14200504486838345, 0.09069976957913667]
key_wmrd = [0.1680757927914335, 0.15252465165726176, 0.10930082696155848]

# =========================
# 子图2数据: prefix16_are, prefix24_are, prefix32_are
# =========================
prefix16_are = [0.17043888073405572, 0.1577451454127471, 0.07550034543091085]
prefix24_are = [0.16533267604635637, 0.14963853595508603, 0.08288805630792652]
prefix32_are = [0.16152139545836072, 0.14635988894865348, 0.08365118499594229]

# =========================
# 配色
# =========================
colors = ["#9E3C36", "#ECEAE0", "#B1D3E0"]

# =========================
# 布局
# =========================
fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.2), gridspec_kw={"wspace": 0.25})
plt.subplots_adjust(left=0.08, right=0.98, top=0.80, bottom=0.28)

w = 0.25
x = np.arange(len(variants))

# 子图1
ax1 = axes[0]
ax1.bar(x - w, key_aae, width=w, label="Key AAE", color=colors[0], edgecolor="black", linewidth=0.8)
ax1.bar(x, key_are, width=w, label="Key ARE", color=colors[1], edgecolor="black", linewidth=0.8)
ax1.bar(x + w, key_wmrd, width=w, label="Key WMRD", color=colors[2], edgecolor="black", linewidth=0.8)
ax1.set_xticks(x)
ax1.set_xticklabels(variants)
ax1.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=3,
           frameon=False, fontsize=11, handlelength=1.2, handletextpad=0.2, columnspacing=0.4)
ax1.set_title("(a) Key-level Metrics", fontsize=12, y=-0.30)
style_axis(ax1)

# 子图2
ax2 = axes[1]
ax2.bar(x - w, prefix16_are, width=w, label="Prefix16 ARE", color=colors[0], edgecolor="black", linewidth=0.8)
ax2.bar(x, prefix24_are, width=w, label="Prefix24 ARE", color=colors[1], edgecolor="black", linewidth=0.8)
ax2.bar(x + w, prefix32_are, width=w, label="Prefix32 ARE", color=colors[2], edgecolor="black", linewidth=0.8)
ax2.set_xticks(x)
ax2.set_xticklabels(variants)
ax2.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=3,
           frameon=False, fontsize=11, handlelength=1.2, handletextpad=0.2, columnspacing=0.4)
ax2.set_title("(b) Prefix-level ARE", fontsize=12, y=-0.30)
style_axis(ax2)

plt.savefig("fig4_ablation_loss.png", dpi=600, bbox_inches="tight")
plt.savefig("fig4_ablation_loss.pdf", dpi=600, bbox_inches="tight")
print("图4已保存: fig4_ablation_loss.png / fig4_ablation_loss.pdf")
