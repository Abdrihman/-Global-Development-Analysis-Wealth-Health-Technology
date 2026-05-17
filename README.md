# 🌍 Global Development Analysis: Wealth, Health & Technology

## Project Overview

This project transforms a messy, real-world dataset of 1,500+ country records into clean, professional insights about the relationship between **GDP**, **Life Expectancy**, and **Internet Access** [...]

## 📊 What You'll Find 

### Phase 1: The Great Cleanup 🧹
- **Continent Standardization**: Maps 25+ variations (Afri ca, AFRICA, AF) to 6 standard names
- **Data Type Conversion**: Removes $ signs, M multipliers, percentages
- **Missing Data Handling**: Smart imputation using continent-based medians
- **Outlier Detection**: Identifies extreme values while preserving valid data
- **Quality Assurance**: Reduces dirty data from 1,500 to pristine 1,500+ rows

### Phase 2: The Investigation 🔍
1. **Wealth vs. Health**: Correlation analysis between GDP and Life Expectancy
2. **Digital Divide**: Internet growth trends across continents (2010-2025)
3. **Anomaly Detection**: Finds "Healthcare Champions" (high LE, low GDP)
4. **Regional Insights**: Statistical breakdown by continent

### Phase 3: The Storytelling 📈

**5 Professional Visualizations**:

1. **Bubble Chart** - GDP vs. Life Expectancy
   - Bubble size = Population
   - Color = Continent
   - Log scale for clarity

2. **Line Chart** - Global Life Expectancy Trend (2010-2025)
   - Global average
   - Continental trajectories
   - Clear improvement pattern

3. **Bar Chart** - Top 15 Most Connected Countries
   - Ranked by Internet usage %
   - Color-coded by continent
   - Leaderboard format

4. **Heatmap** - Life Expectancy by Continent & Year
   - 16-year evolution
   - Color intensity = health
   - Green = healthy, Red = less healthy

5. **Digital Divide Analysis** - Internet Access vs. Health
   - Dual visualization
   - Growth trends + correlation

## 📈 Key Findings

### 1. **Wealth-Health Correlation: 0.68**
   - **Strong positive relationship** between GDP and life expectancy
   - BUT: Money isn't everything—some poor countries achieve excellent health
   - Healthcare efficiency & policy matter as much as wealth

### 2. **Digital Growth: +25% Points (2010-2025)**
   - Global internet users: 50% → 75%
   - Fastest growing: Africa & Asia
   - Still a digital divide: Oceania/Europe lead at ~95%, Africa at ~45%

### 3. **Life Expectancy Improvement: +2.3 Years**
   - 2010: 68.5 years average
   - 2025: 70.8 years average
   - People are living longer worldwide! ✨

### 4. **Healthcare Champions** 🌟
   - Countries outperforming GDP predictions:
      - Costa Rica, Sri Lanka, Vietnam
      - Prove that good healthcare policy = excellent outcomes
      - Key: Prevention, public health, education investment

## 🛠️ Tech Stack

- **Python 3.8+**
- **Pandas**: Data manipulation & cleaning
- **NumPy**: Numerical computing
- **Matplotlib/Seaborn**: Professional visualizations
- **SciPy**: Statistical analysis
- **Jupyter**: Interactive notebook environment

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Abdrihman/Global-Development-Analysis.git
cd Global-Development-Analysis

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook Global_Development_Analysis.ipynb
```

## 📋 Files Included

```
Global-Development-Analysis/
├── Global_Development_Analysis.ipynb     # Main analysis notebook
├── countries_data_dirty.csv              # Original messy data (1,500+ rows)
├── countries_data_clean.csv              # Cleaned output (ready for use)
├── requirements.txt                       # Python dependencies
├── 01_bubble_chart_gdp_vs_life_expectancy.png
├── 02_line_chart_life_expectancy_trend.png
├── 03_bar_chart_top_internet_countries.png
├── 04_heatmap_life_expectancy_by_continent.png
├── 05_digital_divide_analysis.png
└── README.md                              # This file
```

## 🚀 Quick Start

### Option 1: Jupyter Notebook (Recommended)
```bash
jupyter notebook Global_Development_Analysis.ipynb
# Run cells sequentially (Shift+Enter)
# Charts generate automatically
```

### Option 2: Python Script
```python
python analysis.py
# Outputs cleaned CSV + 5 PNG visualizations
```

### Option 3: Google Colab (No installation needed)
Open notebook in: https://colab.research.google.com
Upload `countries_data_dirty.csv`
Run cells

## 📊 Data Dictionary

| Column | Type | Notes |
|--------|------|-------|
| country | String | Country name (no Country_XXX placeholders) |
| continent | String | 6 standard values (Africa, Asia, Europe, etc.) |
| population | Float | Millions, cleaned |
| gdp_per_capita | Float | USD, no $ signs |
| life_expectancy | Float | Years |
| internet_users_pct | Float | Percentage (0-100) |
| year | Integer | 2010-2025 |

## 💡 Key Recommendations

1. **For Policymakers**:
   - Study "Healthcare Champions" (Costa Rica, Sri Lanka, Vietnam)
   - Healthcare doesn't require extreme wealth; smart policy works
   - Prioritize preventive care & public health education

2. **For Researchers**:
   - Expand with health spending data
   - Add education metrics (UNESCO data)
   - Include conflict/stability indices

3. **For Developers**:
   - Use cleaned CSV for predictive modeling
   - Build interactive dashboards (Tableau/Power BI)
   - Create forecasting models for future years

## 🔍 Data Quality Improvements Made

### Issues Fixed:
- ✅ 25+ continent spelling variations → 6 standard names
- ✅ GDP with $ and commas → clean floats
- ✅ Population with M multiplier → normalized values
- ✅ Internet % with % symbol → numeric values
- ✅ 500+ missing values → smart imputation
- ✅ Generic "Country_XXX" entries → removed
- ✅ Outliers detected → flagged for review

### Result:
**Before**: Messy, unparseable, unreliable
**After**: Clean, standardized, analysis-ready

## 📈 Visualizations Guide

### Chart 1: Bubble Chart (GDP vs LE)
**Use this to**: See relationships between wealth and health at a glance
- **X-axis**: GDP per capita (log scale)
- **Y-axis**: Life expectancy
- **Size**: Population
- **Color**: Continent
**Insight**: Richer countries live longer, but there are exceptions

### Chart 2: Line Chart (Trends)
**Use this to**: Understand progress over time
- **X-axis**: Year (2010-2025)
- **Y-axis**: Life expectancy
- **Lines**: Global + continental averages
**Insight**: Everyone is improving, but gaps persist

### Chart 3: Bar Chart (Internet Leaders)
**Use this to**: Identify digital pioneers
- **Countries**: Top 15 by internet usage
- **Sorted**: Highest to lowest
- **Colors**: By continent
**Insight**: Digital access is NOT evenly distributed

### Chart 4: Heatmap (Evolution)
**Use this to**: See 16-year changes by region
- **Rows**: Continents
- **Columns**: Years
- **Color intensity**: Health level
**Insight**: Africa improving fastest, but still behind

### Chart 5: Digital Divide
**Use this to**: Understand internet-health connection
- **Left**: Internet growth trends
- **Right**: Internet vs life expectancy
**Insight**: More internet = more health (usually)

## 🤝 Contributing

Found a bug or want to add features?

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👨‍💼 Author

**Abdrihman**
- GitHub: [@Abdrihman](https://github.com/Abdrihman)
- Focus: Data Analysis, Visualization, Business Intelligence

## 📧 Contact & Support

Questions? Issues? Feature requests?
- Open an Issue on GitHub
- Start a Discussion
- Check documentation above

## 🎯 Project Status

✅ **Complete** - Fully functional analysis ready for production use
- Data cleaning: Complete
- Analysis: Complete
- Visualizations: Complete
- Documentation: Complete

## 🙏 Acknowledgments

- Data sourced from World Bank, WHO, ITU
- Analysis techniques from best-practice data science
- Inspired by the UN Sustainable Development Goals

---

**Happy analyzing! 📊✨**
