import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path("graficos_dissertacao")
OUTPUT_DIR.mkdir(exist_ok=True)

PATH = "EDGAR_AR5_GHG_1970_2024/EDGAR_AR5_GHG_1970_2024.xlsx"
df = pd.read_excel(PATH, sheet_name="IPCC 2006", header=9)
cement = df[df["ipcc_code_2006_for_standard_report"] == "2.A.1"].copy()

year_cols = [c for c in df.columns if str(c).startswith("Y_")]
years = [int(c.replace("Y_", "")) for c in year_cols]

global_total_gg = cement[year_cols].sum()
global_total_gt = global_total_gg / 1e6  # Gg → Gt

FONTE = "Fonte: EDGAR GHG Community Database v2025 (JRC/CE, 2025). Código IPCC 2006: 2.A.1."
CITATION_STYLE = dict(fontsize=7, color="#555555", style="italic")
TITLE_STYLE = dict(fontsize=13, fontweight="bold", pad=12)

# ── Figura 1: Série temporal global ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5.5))

ax.fill_between(years, global_total_gt, alpha=0.18, color="#c0392b")
ax.plot(years, global_total_gt, color="#c0392b", linewidth=2.5, zorder=3)

peak_idx = global_total_gt.values.argmax()
ax.annotate(
    f"Pico: {global_total_gt.values[peak_idx]:.2f} Gt ({years[peak_idx]})",
    xy=(years[peak_idx], global_total_gt.values[peak_idx]),
    xytext=(years[peak_idx] - 8, global_total_gt.values[peak_idx] + 0.04),
    arrowprops=dict(arrowstyle="->", color="#333333", lw=1.2),
    fontsize=9,
)

ax.set_title("Emissões globais de CO₂ da produção de cimento (1970–2024)", **TITLE_STYLE)
ax.set_xlabel("Ano", fontsize=10)
ax.set_ylabel("Emissões (Gt CO₂ eq, GWP₁₀₀ AR5)", fontsize=10)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f"))
ax.set_xlim(1970, 2024)
ax.grid(axis="y", linestyle="--", alpha=0.5)
ax.tick_params(labelsize=9)
fig.text(0.01, -0.02, FONTE, **CITATION_STYLE, transform=ax.transAxes)
plt.tight_layout()
fig.savefig(OUTPUT_DIR / "fig1_serie_temporal_global.png", dpi=300, bbox_inches="tight")
plt.close()
print("Figura 1 salva.")

# ── Figura 2: Top 15 países em 2024 ─────────────────────────────────────────
top15 = (
    cement[["Name", "Y_2024"]]
    .dropna()
    .sort_values("Y_2024", ascending=False)
    .head(15)
)
top15["Y_2024_Mt"] = top15["Y_2024"] / 1e3  # Gg → Mt

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(
    top15["Name"][::-1],
    top15["Y_2024_Mt"][::-1],
    color=["#c0392b" if n in ("China", "India") else "#e67e73" for n in top15["Name"][::-1]],
    edgecolor="white",
    linewidth=0.5,
)

for bar, val in zip(bars, top15["Y_2024_Mt"][::-1]):
    ax.text(bar.get_width() + 3, bar.get_y() + bar.get_height() / 2,
            f"{val:.0f}", va="center", fontsize=8.5)

ax.set_title("Maiores emissores de CO₂ da produção de cimento em 2024 (Top 15)", **TITLE_STYLE)
ax.set_xlabel("Emissões (Mt CO₂ eq, GWP₁₀₀ AR5)", fontsize=10)
ax.tick_params(labelsize=9)
ax.grid(axis="x", linestyle="--", alpha=0.5)
ax.set_xlim(0, top15["Y_2024_Mt"].max() * 1.18)
fig.text(0.01, -0.02, FONTE, **CITATION_STYLE, transform=ax.transAxes)
plt.tight_layout()
fig.savefig(OUTPUT_DIR / "fig2_top15_paises_2024.png", dpi=300, bbox_inches="tight")
plt.close()
print("Figura 2 salva.")

# ── Figura 3: Emissões por país selecionado — gráfico de linhas ──────────────
REGIOES = {
    "China":                      ("#c0392b", "-",  2.8),
    "India":                      ("#e67e22", "-",  2.2),
    "Viet Nam":                   ("#d4ac0d", "--", 1.8),
    "United States":              ("#2980b9", "-",  1.8),
    "Turkey":                     ("#27ae60", "--", 1.8),
    "Brazil":                     ("#8e44ad", "-",  1.8),
    "Iran, Islamic Republic of":  ("#16a085", "--", 1.8),
}

fig, ax = plt.subplots(figsize=(10, 5.5))

for country, (color, ls, lw) in REGIOES.items():
    row = cement[cement["Name"] == country]
    if row.empty:
        continue
    vals = row[year_cols].iloc[0] / 1e3  # Gg → Mt
    label = "Irã" if country == "Iran, Islamic Republic of" else country
    ax.plot(years, vals, color=color, linewidth=lw, linestyle=ls, label=label)

ax.set_title("Emissões de CO₂ da produção de cimento por país selecionado (1970–2024)", **TITLE_STYLE)
ax.set_xlabel("Ano", fontsize=10)
ax.set_ylabel("Emissões (Mt CO₂ eq, GWP₁₀₀ AR5)", fontsize=10)
ax.legend(loc="upper left", fontsize=9, framealpha=0.95,
          edgecolor="#cccccc", title="País", title_fontsize=9)
ax.set_xlim(1970, 2024)
ax.grid(axis="y", linestyle="--", alpha=0.4)
ax.tick_params(labelsize=9)
fig.text(0.01, -0.02, FONTE, **CITATION_STYLE, transform=ax.transAxes)
plt.tight_layout()
fig.savefig(OUTPUT_DIR / "fig3_linhas_paises.png", dpi=300, bbox_inches="tight")
plt.close()
print("Figura 3 salva.")

print(f"\nTodos os gráficos salvos em: {OUTPUT_DIR.resolve()}")
print("\nResumo dos dados:")
print(f"  Global 1970: {global_total_gt['Y_1970']:.2f} Gt CO2eq")
print(f"  Global 2024: {global_total_gt['Y_2024']:.2f} Gt CO2eq")
print(f"  Crescimento: {(global_total_gt['Y_2024']/global_total_gt['Y_1970'] - 1)*100:.0f}%")
