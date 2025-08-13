# Sales-Analysis

Product Sales Analysis Dashboard

Overview
This project is a Streamlit-based interactive dashboard for analyzing product sales data. It processes Excel datasets, generates key business insights, and provides dynamic visualizations to help track sales performance and trends. The dashboard is designed for business owners, analysts, and decision-makers to quickly visualize sales performance without needing technical expertise.

Features
Automatic Data Loading – Reads sales data from a local Excel file (bundled with the app).

Interactive Charts – Supports Bar, Pie, and Line charts.

KPI Highlights – Displays total sales, quantity sold, and top products.

Dynamic Filters – Filter by date, category, or region.

Multi-Chart Support – Choose preferred visualization type.

Business Insights – Detects trends and patterns.

Project Structure
bash
Copy
Edit
Product_Salesdata/
│── product_sales.py        # Main Streamlit app
│── requirements.txt        # Dependencies
│── sales_data_store1.xlsx  # Sample dataset (included in repo)
│── README.md               # Documentation
Installation & Setup

Clone the repo

pip install -r requirements.txt
Run the app locally

streamlit run product_sales.py
