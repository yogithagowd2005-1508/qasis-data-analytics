# 📊 OASIS INFOBYTE — SUMMER INTERNSHIP PROGRAM (OIBSIP)

## 📌 Repository: `OIBSIP`
**Domain / Track:** Data Analytics  
**Status:** Completed (Eligible for Certificate of Completion & Letter of Recommendation - LOR)  
**Execution Environment:** Python 3.10+, Jupyter Notebook, scikit-learn, pandas  

---

## 👨‍💻 Intern Profile
- **Intern Name:** `[Your Full Name]`
- **Domain Track:** Data Analytics
- **Batch / Cohort:** `[Your Cohort / Month]`
- **GitHub Repository:** `https://github.com/[YourUsername]/OIBSIP`
- **LinkedIn Profile:** `[Your LinkedIn Profile Link]`

---

## 🏆 Project Portfolio & Track Matrix

Per the **Domain Track Matrix** in the Oasis Infobyte SIP Task List:
> *Track: Data Analytics (7 tasks across 2 levels)*  
> *Minimum to Complete: At least 3 tasks from Level 1 or Level 2 combined.*  
> *To be eligible for a Letter of Recommendation (LOR), complete maximum tasks from both levels.*

This repository provides **4 complete, end-to-end projects** covering both **Level 1** and **Level 2**, fulfilling all completion thresholds and qualifying for the **Letter of Recommendation (LOR)**.

| Level | Task ID | Folder Name | Project Title | Primary Technologies | Status |
| :---: | :---: | :--- | :--- | :--- | :---: |
| **Level 1** | **Task 1** | [`DataAnalytics-L1-EDARetailSales/`](DataAnalytics-L1-EDARetailSales/) | **EDA on Retail Sales Data** | Python, pandas, seaborn, matplotlib | ✅ Completed |
| **Level 1** | **Task 2** | [`DataAnalytics-L1-CustomerSegmentation/`](DataAnalytics-L1-CustomerSegmentation/) | **Customer Segmentation Analysis** | Python, scikit-learn (K-Means), RFM | ✅ Completed |
| **Level 1** | **Task 3** | [`DataAnalytics-L1-CleaningData/`](DataAnalytics-L1-CleaningData/) | **Data Cleaning & Quality Remediation** | Python, pandas, numpy, IQR Outlier Capping | ✅ Completed |
| **Level 2** | **Task 1** | [`DataAnalytics-L2-HousePricePrediction/`](DataAnalytics-L2-HousePricePrediction/) | **Predicting House Prices with Linear Regression** | Python, scikit-learn, OLS, Ridge, Lasso | ✅ Completed |

---

## 📂 Strict Folder Hierarchy (`OIBSIP/[TrackName]-[Level/Task]-[ProjectName]/`)

Every project is organized in accordance with the mandatory Oasis Infobyte directory specification:

```text
OIBSIP/
├── README.md                                    # Master Repository Overview & Guidelines
├── requirements.txt                             # Python dependencies
├── run_all_tasks.py                             # Master test execution runner
├── create_title_cards.py                        # 2-Second Title Card Generator for Video Submissions
│
├── DataAnalytics-L1-EDARetailSales/             # [Level 1 - Task 1]
│   ├── README.md                                # Project Documentation & Business Insights
│   ├── EDA_Retail_Sales.ipynb                   # Executed Jupyter Notebook
│   ├── eda_retail_sales.py                      # Standalone CLI Script
│   ├── retail_sales_dataset.csv                 # 2,500-record Omnichannel Sales Dataset
│   └── plots/
│       ├── title_card_task1.png                 # 2-Second Video Title Card Slide
│       ├── monthly_quarterly_sales_trend.png    # Time Series Revenue Plot
│       ├── customer_demographics.png            # Gender Breakdown & Age Distribution
│       ├── top10_products_and_category_revenue.png # Best Sellers & Category Volume
│       ├── correlation_heatmap.png              # Metric Correlation Matrix
│       └── profit_margin_by_age_and_category.png# Non-Obvious Insight Heatmap
│
├── DataAnalytics-L1-CustomerSegmentation/       # [Level 1 - Task 2]
│   ├── README.md                                # Customer Segmentation Architecture & Strategies
│   ├── Customer_Segmentation.ipynb              # Executed RFM Clustering Notebook
│   ├── customer_segmentation.py                 # Standalone Segmentation CLI Pipeline
│   ├── ecommerce_customer_data.csv              # 1,800-customer Behavioral Dataset
│   └── plots/
│       ├── title_card_task2.png                 # 2-Second Video Title Card Slide
│       ├── elbow_method_analysis.png            # Elbow Curve & Silhouette Validation
│       ├── cluster_scatter_plots.png            # Multi-Dimensional Cluster Separation
│       ├── customer_distribution_per_cluster.png# Customer Volume & Share per Cohort
│       └── cluster_profile_comparison.png       # Centroid Metric Comparison
│
├── DataAnalytics-L1-CleaningData/               # [Level 1 - Task 3]
│   ├── README.md                                # Cleaning Audit & Transformation Rationales
│   ├── Data_Cleaning.ipynb                      # Executed Data Remediation Notebook
│   ├── data_cleaning.py                         # Standalone Cleaning Pipeline Script
│   ├── raw_dirty_dataset.csv                    # Messy Raw Dataset with Deliberate Flaws
│   └── outputs/
│       ├── title_card_task3.png                 # 2-Second Video Title Card Slide
│       ├── cleaned_dataset.csv                  # Analysis-Ready Remediated Dataset
│       └── data_cleaning_comparison_summary.csv # Before vs After Quality Audit Report
│
└── DataAnalytics-L2-HousePricePrediction/       # [Level 2 - Task 1]
    ├── README.md                                # Econometric Valuation Model Report
    ├── House_Price_Prediction.ipynb             # Executed Linear Regression Notebook
    ├── house_price_prediction.py                # Standalone Regression Pipeline Script
    ├── housing_price_dataset.csv                # 1,500 Real Estate Transaction Records
    └── plots/
        ├── title_card_task4.png                 # 2-Second Video Title Card Slide
        ├── price_distribution.png               # Target Variable Distribution
        ├── correlation_heatmap.png              # Feature Correlation Matrix
        ├── actual_vs_predicted.png              # Scatter Plot with 45° Fit Line
        ├── residual_plot.png                    # Residual Variance Diagnostics
        ├── feature_coefficients.png             # Marginal Price Contributions
        └── model_comparison.png                 # OLS vs Ridge vs Lasso Benchmark
```

---

## 🛠️ Quickstart & Local Execution

### 1. Clone the Repository
```bash
git clone https://github.com/[YourUsername]/OIBSIP.git
cd OIBSIP
```

### 2. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run All Tasks via Master Automation Runner
```bash
python run_all_tasks.py
```
*This command executes all 4 task pipelines sequentially, generates all diagnostic plots, and validates data integrity with zero errors.*

---

## 🎥 Video Demo Submission Guide (PDF Step 4 Requirement)

Per the **Master Onboarding Checklist (Section 1.2, Step 4 & 1.3)**:
> ⚠️ **Video Title Card:** *The first 2 seconds of each demo video MUST show a static title card containing:*
> 1. Your Full Name
> 2. Your Assigned Track (Data Analytics)
> 3. The Task Title

### Pre-Generated 2-Second Title Cards
Ready-to-use 1080p title card assets are located inside each project's directory:
- Task 1: `DataAnalytics-L1-EDARetailSales/plots/title_card_task1.png`
- Task 2: `DataAnalytics-L1-CustomerSegmentation/plots/title_card_task2.png`
- Task 3: `DataAnalytics-L1-CleaningData/outputs/title_card_task3.png`
- Task 4: `DataAnalytics-L2-HousePricePrediction/plots/title_card_task4.png`

To regenerate or customize them with your name, edit `create_title_cards.py` and run:
```bash
python create_title_cards.py
```

---

## 📢 LinkedIn Post Submission Templates (PDF Step 5 Requirement)

When posting your walkthrough video to LinkedIn, tag **Oasis Infobyte** and include the mandatory hashtags:

```text
🚀 Thrilled to share my project completed during the OASIS INFOBYTE Summer Internship Program (OIBSIP)!

Domain Track: Data Analytics
Project: [Project Name - e.g., Exploratory Data Analysis on Retail Sales Data]
GitHub Repository: https://github.com/[YourUsername]/OIBSIP

In this project, I:
• Analyzed 2,500+ transactional records using Python, Pandas, and Seaborn.
• Uncovered customer demographics, sales seasonality, and category profit margins.
• Formulated actionable data-driven recommendations for commercial growth.

Grateful to Oasis Infobyte for this enriching learning experience! 🌟

#oasisinfobyte #dataanalytics #datascience #python #machinelearning #internship #oibsip
```

---

## 👥 Peer Evaluation Checklist (PDF Step 6 Requirement)
- [ ] Watch LinkedIn demo videos of at least 2 cohort peers.
- [ ] Post a constructive, substantive comment on each (ask a question or provide analytical observations).
- [ ] Save screenshot evidence for your final submission form.

---

## 📬 Final Task Submission Form (PDF Step 7)
When the submission form opens, submit your public GitHub repository URL:
`https://github.com/[YourUsername]/OIBSIP`
