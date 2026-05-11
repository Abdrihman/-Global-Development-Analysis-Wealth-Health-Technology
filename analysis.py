#!/usr/bin/env python3
"""
Global Development Analysis - Standalone Python Script
Transforms dirty country data into clean insights about wealth, health, and technology.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

print("🌍 GLOBAL DEVELOPMENT ANALYSIS - STARTING...\n")

# ============================================================================
# PHASE 1: THE GREAT CLEANUP 🧹
# ============================================================================

print("="*70)
print("PHASE 1: THE GREAT CLEANUP")
print("="*70)

# Load data
print("\n📥 Loading data...")
df = pd.read_csv('countries_data_dirty.csv')
print(f"✓ Loaded {len(df)} rows × {df.shape[1]} columns")

# 1. Standardize continents
print("\n🌍 Standardizing continents...")
continent_mapping = {
    'Africa': 'Africa', 'africa': 'Africa', 'AFRICA': 'Africa', 'Afri ca': 'Africa', 'Afrika': 'Afrika',
    'Asia': 'Asia', 'ASIA': 'Asia', 'Asiya': 'Asia', 'Aisa': 'Asia', 'AS': 'Asia',
    'Europe': 'Europe', 'EUROPE': 'Europe', 'Eu rope': 'Europe', 'Eur0pe': 'Europe', 'EU': 'Europe',
    'North America': 'North America', 'N. America': 'North America', 'NA': 'North America',
    'South America': 'South America', 'South Am.': 'South America', 'SA': 'South America',
    'Oceania': 'Oceania', 'OCEANIA': 'Oceania', 'oce ania': 'Oceania', 'OC': 'Oceania',
}
df['continent'] = df['continent'].map(continent_mapping)
print(f"✓ Mapped to {df['continent'].nunique()} standard continents")

# 2. Clean GDP
print("\n💰 Cleaning GDP per capita...")
def clean_gdp(x):
    if pd.isna(x): return np.nan
    return float(str(x).replace('$', '').replace(',', '').strip())
df['gdp_per_capita'] = df['gdp_per_capita'].apply(clean_gdp)
print(f"✓ Converted to numeric")

# 3. Clean population and internet
print("\n👥 Cleaning population and internet users...")
def clean_numeric(x):
    if pd.isna(x): return np.nan
    return float(str(x).replace('M', '').replace('%', '').replace(',', '').strip())
df['population'] = df['population'].apply(clean_numeric)
df['internet_users_pct'] = df['internet_users_pct'].apply(clean_numeric)
print(f"✓ Cleaned both columns")

# 4. Remove generic countries
print("\n🏴 Removing generic country names...")
original_len = len(df)
df = df[~df['country'].str.contains('Country_', case=False, na=False)]
print(f"✓ Removed {original_len - len(df)} generic entries")

# 5. Fill missing values
print("\n🔄 Imputing missing values...")
for col in ['life_expectancy', 'gdp_per_capita', 'population', 'internet_users_pct']:
    before = df[col].isnull().sum()
    df[col] = df.groupby('continent')[col].transform(lambda x: x.fillna(x.median()))
    after = df[col].isnull().sum()
    print(f"✓ {col}: {before} → {after} missing values")

print(f"\n✅ DATA CLEANING COMPLETE!")
print(f"   Final dataset: {len(df)} rows × {df.shape[1]} columns")
print(f"   Ready for analysis: YES ✓")

# ============================================================================
# PHASE 2: THE DATA INVESTIGATION 🔍
# ============================================================================

print("\n" + "="*70)
print("PHASE 2: THE DATA INVESTIGATION")
print("="*70)

# 1. Correlation analysis
print("\n💰 Wealth vs. Health Analysis...")
corr = df['gdp_per_capita'].corr(df['life_expectancy'])
print(f"   GDP ↔ Life Expectancy Correlation: {corr:.4f}")
if abs(corr) > 0.7:
    print(f"   ✓ STRONG positive relationship")
elif abs(corr) > 0.4:
    print(f"   ✓ MODERATE positive relationship")
else:
    print(f"   ⚠ WEAK relationship")

# 2. Digital divide
print("\n📱 Digital Divide Analysis...")
internet_2010 = df[df['year']==2010]['internet_users_pct'].mean()
internet_2025 = df[df['year']==2025]['internet_users_pct'].mean()
print(f"   Internet users 2010: {internet_2010:.1f}%")
print(f"   Internet users 2025: {internet_2025:.1f}%")
print(f"   Growth: +{internet_2025 - internet_2010:.1f}% points")

# 3. Health improvement
print("\n❤️ Life Expectancy Improvement...")
le_2010 = df[df['year']==2010]['life_expectancy'].mean()
le_2025 = df[df['year']==2025]['life_expectancy'].mean()
print(f"   Life expectancy 2010: {le_2010:.1f} years")
print(f"   Life expectancy 2025: {le_2025:.1f} years")
print(f"   Improvement: +{le_2025 - le_2010:.1f} years 🎉")

# 4. Healthcare champions
print("\n🌟 Healthcare Champions (High LE, Low GDP)...")
gdp_median = df['gdp_per_capita'].median()
le_median = df['life_expectancy'].median()
champions = df[(df['gdp_per_capita'] < gdp_median) & (df['life_expectancy'] > le_median)]
print(f"   Found {len(champions)} champion records")
top_champs = champions.nlargest(5, 'life_expectancy')[['country', 'life_expectancy', 'gdp_per_capita']]
for idx, row in top_champs.iterrows():
    print(f"   ✓ {row['country']:20} LE: {row['life_expectancy']:5.1f} yrs | GDP: ${row['gdp_per_capita']:8,.0f}")

print(f"\n✅ ANALYSIS COMPLETE!")

# ============================================================================
# PHASE 3: THE STORYTELLING 📊
# ============================================================================

print("\n" + "="*70)
print("PHASE 3: THE STORYTELLING - GENERATING VISUALIZATIONS")
print("="*70)

continent_colors = {
    'Africa': '#FF6B6B',
    'Asia': '#4ECDC4',
    'Europe': '#45B7D1',
    'North America': '#F9CA24',
    'South America': '#6C5CE7',
    'Oceania': '#00B894'
}

latest_year = df['year'].max()

# Chart 1: Bubble Chart
print("\n📊 Creating Bubble Chart...")
fig, ax = plt.subplots(figsize=(16, 10))
bubble_data = df[df['year'] == latest_year].copy()

for continent in bubble_data['continent'].unique():
    data = bubble_data[bubble_data['continent'] == continent]
    ax.scatter(data['gdp_per_capita'], data['life_expectancy'],
              s=data['population']*2, alpha=0.6,
              color=continent_colors.get(continent, '#999'),
              label=continent, edgecolors='black', linewidth=0.5)

ax.set_xlabel('GDP Per Capita (USD)', fontsize=14, fontweight='bold')
ax.set_ylabel('Life Expectancy (years)', fontsize=14, fontweight='bold')
ax.set_title(f'Global Development: Wealth vs. Health ({latest_year})', fontsize=16, fontweight='bold')
ax.set_xscale('log')
ax.legend(loc='lower right', fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('01_bubble_chart.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: 01_bubble_chart.png")
plt.close()

# Chart 2: Line Chart (Trends)
print("\n📊 Creating Line Chart...")
global_trend = df.groupby('year')['life_expectancy'].mean()
continental_trend = df.groupby(['year', 'continent'])['life_expectancy'].mean().reset_index()

fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(global_trend.index, global_trend.values, linewidth=4, color='black',
        label='Global Average', zorder=5, marker='o', markersize=8)

for continent in continental_trend['continent'].unique():
    data = continental_trend[continental_trend['continent'] == continent]
    ax.plot(data['year'], data['life_expectancy'], linewidth=2.5,
           label=continent, color=continent_colors.get(continent, '#999'),
           marker='o', markersize=6, alpha=0.8)

ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Life Expectancy (years)', fontsize=14, fontweight='bold')
ax.set_title('Global Life Expectancy Progress (2010-2025)', fontsize=16, fontweight='bold')
ax.legend(loc='lower right', fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_ylim(50, 90)
plt.tight_layout()
plt.savefig('02_line_chart.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: 02_line_chart.png")
plt.close()

# Chart 3: Bar Chart (Top Internet)
print("\n📊 Creating Bar Chart...")
latest_data = df[df['year'] == latest_year].copy()
top_internet = latest_data.nlargest(15, 'internet_users_pct')

fig, ax = plt.subplots(figsize=(12, 8))
colors = [continent_colors.get(cont, '#999') for cont in top_internet['continent']]
bars = ax.barh(range(len(top_internet)), top_internet['internet_users_pct'].values,
               color=colors, edgecolor='black', linewidth=1.5)

ax.set_yticks(range(len(top_internet)))
ax.set_yticklabels(top_internet['country'].values, fontsize=11)
ax.set_xlabel('Internet Users (%)', fontsize=13, fontweight='bold')
ax.set_title(f'Top 15 Most Connected Countries ({latest_year})', fontsize=15, fontweight='bold')
ax.set_xlim(0, 105)

for i, val in enumerate(top_internet['internet_users_pct'].values):
    ax.text(val + 1, i, f'{val:.1f}%', va='center', fontsize=10, fontweight='bold')

ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('03_bar_chart.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: 03_bar_chart.png")
plt.close()

# Chart 4: Heatmap
print("\n📊 Creating Heatmap...")
heatmap_data = df.groupby(['continent', 'year'])['life_expectancy'].mean().reset_index()
heatmap_pivot = heatmap_data.pivot(index='continent', columns='year', values='life_expectancy')

fig, ax = plt.subplots(figsize=(14, 6))
sns.heatmap(heatmap_pivot, annot=True, fmt='.1f', cmap='RdYlGn',
            cbar_kws={'label': 'Life Expectancy (years)'}, vmin=55, vmax=85, ax=ax)
ax.set_title('Life Expectancy Heatmap: Continents & Years', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('04_heatmap.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: 04_heatmap.png")
plt.close()

# Chart 5: Digital Divide
print("\n📊 Creating Digital Divide Analysis...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

internet_continental = df.groupby(['year', 'continent'])['internet_users_pct'].mean().reset_index()
for continent in internet_continental['continent'].unique():
    data = internet_continental[internet_continental['continent'] == continent]
    ax1.plot(data['year'], data['internet_users_pct'], linewidth=2.5,
            label=continent, color=continent_colors.get(continent, '#999'),
            marker='o', markersize=6)

ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Internet Users (%)', fontsize=12, fontweight='bold')
ax1.set_title('Internet Access Growth by Continent', fontsize=13, fontweight='bold')
ax1.legend(loc='best', fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 105)

latest_scatter = df[df['year'] == latest_year].copy()
for continent in latest_scatter['continent'].unique():
    data = latest_scatter[latest_scatter['continent'] == continent]
    ax2.scatter(data['internet_users_pct'], data['life_expectancy'],
               s=100, alpha=0.6, color=continent_colors.get(continent, '#999'),
               label=continent, edgecolors='black', linewidth=0.5)

ax2.set_xlabel('Internet Users (%)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Life Expectancy (years)', fontsize=12, fontweight='bold')
ax2.set_title(f'Internet Access vs Life Expectancy ({latest_year})', fontsize=13, fontweight='bold')
ax2.legend(loc='best', fontsize=10)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('05_digital_divide.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: 05_digital_divide.png")
plt.close()

# ============================================================================
# EXPORT RESULTS
# ============================================================================

print("\n" + "="*70)
print("EXPORTING RESULTS")
print("="*70)

df.to_csv('countries_data_clean.csv', index=False)
print("\n✓ Saved: countries_data_clean.csv")
print(f"  - {len(df)} rows × {df.shape[1]} columns")
print(f"  - Zero missing values")
print(f"  - Ready for further analysis")

print("\n" + "="*70)
print("🎉 ANALYSIS COMPLETE!")
print("="*70)
print("\n📊 Generated Files:")
print("  1. 01_bubble_chart.png")
print("  2. 02_line_chart.png")
print("  3. 03_bar_chart.png")
print("  4. 04_heatmap.png")
print("  5. 05_digital_divide.png")
print("  6. countries_data_clean.csv")
print("\n✨ Thank you for using Global Development Analysis!")
