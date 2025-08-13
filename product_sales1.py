import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

st.set_page_config(page_title="Product Sales Dashboard", page_icon="📊", layout="wide")
st.title("📊 Product Sales Analysis Dashboard")

# --- Load Excel (hardcoded path from your notebook) ---
file_path = r"C:\Users\SHAIK BASHEER\Downloads\sales_data_store1.xlsx"
df = pd.read_excel(r"C:\Users\SHAIK BASHEER\Downloads\sales_data_store1.xlsx")


# --- Data Cleaning ---
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
for col in ['Total', 'Price', 'Quantity']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['Month'] = df['Date'].dt.to_period('M').astype(str)

sns.set_theme(style="whitegrid")

# --- KPIs ---
df['OrderCount'] = 1
total_sales = df['Total'].sum()
total_orders = df['OrderCount'].sum()
avg_order_value = total_sales / total_orders if total_orders > 0 else 0
avg_price = df['Price'].mean()
total_qty = df['Quantity'].sum()

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
kpi1.metric("Total Sales", f"${total_sales:,.2f}")
kpi2.metric("Orders", f"{total_orders:,}")
kpi3.metric("Avg Order Value", f"${avg_order_value:,.2f}")
kpi4.metric("Avg Price", f"${avg_price:,.2f}")
kpi5.metric("Total Quantity", f"{total_qty:,}")

st.markdown("---")

# --- Monthly Sales Trend ---
monthly_sales = df.groupby('Month')['Total'].sum().reset_index()
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.lineplot(x='Month', y='Total', data=monthly_sales, marker='o', ax=ax1)
ax1.set_title("Monthly Sales Trend", fontsize=16)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
ax1.set_ylabel("Total Sales")
st.pyplot(fig1)

# --- Top 10 Products by Sales ---
top_products = df.groupby('Product')['Total'].sum().nlargest(10).reset_index()
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x='Total', y='Product', data=top_products, palette='viridis', ax=ax2)
ax2.set_title("Top 10 Products by Sales", fontsize=16)
st.pyplot(fig2)

# --- Top 10 Products by Price ---
top_products_cost = df.groupby('Product')['Price'].mean().nlargest(10).reset_index()
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.barplot(x='Price', y='Product', data=top_products_cost, palette='magma', ax=ax3)
ax3.set_title("Top 10 Products by Price", fontsize=16)
st.pyplot(fig3)

# --- Sales by Category ---
category_sales = df.groupby('Category')['Total'].sum().reset_index()
fig4, ax4 = plt.subplots(figsize=(8, 6))
sns.barplot(x='Category', y='Total', data=category_sales, palette='Set2', ax=ax4)
ax4.set_title("Sales by Category", fontsize=16)
st.pyplot(fig4)

# --- Sales by City ---
city_sales = df.groupby('City')['Total'].sum().reset_index()
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.barplot(
    x='Total', y='City',
    data=city_sales.sort_values(by='Total', ascending=False),
    palette='coolwarm', ax=ax5
)
ax5.set_title("Sales by City", fontsize=16)
st.pyplot(fig5)

# --- Sales by Channel (Pie) ---
channel_sales = df.groupby('Channel')['Total'].sum().reset_index()
fig6, ax6 = plt.subplots(figsize=(6, 6))
ax6.pie(channel_sales['Total'], labels=channel_sales['Channel'], autopct='%1.1f%%', startangle=140)
ax6.set_title("Sales by Channel")
st.pyplot(fig6)

# --- Quantity Distribution ---
fig7, ax7 = plt.subplots(figsize=(8, 6))
sns.histplot(df['Quantity'], bins=20, kde=True, color='orange', ax=ax7)
ax7.set_title("Quantity Distribution", fontsize=16)
st.pyplot(fig7)

# --- Overall Sales Distribution by Category (Pie) ---
fig8, ax8 = plt.subplots(figsize=(8, 8))
ax8.pie(
    category_sales['Total'],
    labels=category_sales['Category'],
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('pastel')[0:len(category_sales)]
)
ax8.set_title("Overall Sales Distribution by Category", fontsize=16)
st.pyplot(fig8)

# --- Interactive Sales Scatter ---
st.subheader("Interactive Sales Dashboard")
fig_scatter = px.scatter(
    df,
    x="Date", y="Total", color="Category", size="Quantity",
    hover_data=["Product", "City", "Channel"],
    title="Interactive Sales Dashboard"
)
st.plotly_chart(fig_scatter, use_container_width=True)

# --- Animated Monthly Top Products ---
df['Month'] = pd.to_datetime(df['Date'], errors='coerce').dt.to_period('M').astype(str)
monthly_top = df.groupby(['Month', 'Product'])['Total'].sum().reset_index()
fig_anim = px.bar(
    monthly_top,
    x='Total', y='Product', color='Product',
    animation_frame='Month',
    range_x=[0, monthly_top['Total'].max()*1.2],
    title="Animated Top Products by Monthly Sales"
)
fig_anim.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig_anim, use_container_width=True)



