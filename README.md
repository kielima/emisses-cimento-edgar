# Emissões Globais de CO₂ — Produção de Cimento (EDGAR, 1970–2024)

Código e gráficos utilizados na dissertação de mestrado para visualização dos dados de emissões globais de CO₂ provenientes da produção de cimento, com base na base de dados EDGAR (Emissions Database for Global Atmospheric Research).

---

## Fonte dos dados

> European Commission, Joint Research Centre (JRC). **EDGAR Community GHG Database**, version EDGAR_2025_GHG (2025).
> Disponível em: [https://edgar.jrc.ec.europa.eu/dataset_ghg2025](https://edgar.jrc.ec.europa.eu/dataset_ghg2025)
> Licença: Creative Commons Attribution 4.0 International (CC BY 4.0)

Código IPCC 2006 utilizado: **2.A.1 — Cement production**
Unidade: Gg CO₂ eq (GWP₁₀₀ AR5)
Cobertura: 164 países, 1970–2024

---

## Gráficos gerados

| Arquivo | Descrição |
|---|---|
| `graficos_dissertacao/fig1_serie_temporal_global.png` | Emissões globais de CO₂ do cimento (1970–2024) |
| `graficos_dissertacao/fig2_top15_paises_2024.png` | Top 15 maiores emissores em 2024 |
| `graficos_dissertacao/fig3_linhas_paises.png` | Emissões por país selecionado — série histórica |

---

## Como reproduzir

### 1. Baixe os dados brutos

Acesse [https://edgar.jrc.ec.europa.eu/dataset_ghg2025](https://edgar.jrc.ec.europa.eu/dataset_ghg2025) e baixe o arquivo:

```
EDGAR_AR5_GHG_1970_2024.xlsx
```

Coloque-o na pasta `EDGAR_AR5_GHG_1970_2024/`.

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o script

```bash
python gerar_graficos_cimento.py
```

Os gráficos serão salvos automaticamente na pasta `graficos_dissertacao/`.

---

## Dados-chave

| Indicador | Valor |
|---|---|
| Emissões globais em 1970 | 0,30 Gt CO₂ eq |
| Emissões globais em 2024 | 1,47 Gt CO₂ eq |
| Crescimento 1970–2024 | +396% |
| Maior emissor (2024) | China — 627 Mt CO₂ eq |
| Brasil (2024) | 24 Mt CO₂ eq |

---

## Citação recomendada (ABNT)

```
EUROPEAN COMMISSION; JOINT RESEARCH CENTRE. EDGAR Community GHG Database
(Emissions Database for Global Atmospheric Research): version EDGAR_2025_GHG.
Luxembourg: Publications Office of the European Union, 2025.
Disponível em: https://edgar.jrc.ec.europa.eu/dataset_ghg2025. Acesso em: abr. 2025.
```
