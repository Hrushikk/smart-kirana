import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="Smart Kirana", layout="centered", page_icon="🛒")

# --- Custom CSS for a darker, more vibrant theme ---
st.markdown("""
    <style>
    /* Main container and text */
    body, .stApp {
        background-color: #1a1a1a; /* Dark gray background */
        color: #f0f2f6; /* Light gray text for readability */
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #28a745; /* Green for headings */
    }
    
    /* Side bar */
    .css-1y4-4t3 {
        background-color: #282828; /* Darker sidebar */
        color: #f0f2f6;
    }
    .css-1y4-4t3 .st-eb {
        color: #f0f2f6;
    }
    
    /* Info, Success, Warning boxes */
    .st-bb { /* st.info - Loyalty Wallet */
        background-color: #315875; /* Dark blue background */
        color: #e0f7fa; /* Lighter text color */
        border-left: 5px solid #007bff; /* Blue accent bar */
        border-radius: 8px;
        padding: 15px;
        font-size: 1.2em;
        font-weight: bold;
    }
    .st-at { /* st.warning - Offers & alerts */
        background-color: #6a532d; /* Darker yellow/brown */
        color: #fff3cd; /* Lighter yellow text */
        border-left: 5px solid #ffc107; /* Yellow accent bar */
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
    }
    .st-dg { /* General success/warning messages */
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .st-dg.success {
        background-color: #2b5637; /* Dark green for success */
        color: #d4f0d4;
    }
    .st-dg.error {
        background-color: #6d3a3d; /* Dark red for error */
        color: #f8d7da;
    }
    .st-dg.info {
        background-color: #2d4c6a; /* Dark blue for info */
        color: #d4e7f8;
    }

    /* Buttons */
    .stButton > button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        margin-top: 10px;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }

    /* Text Inputs */
    .st-c3 {
        background-color: #333333; /* Darker input background */
        color: #f0f2f6;
    }
    .st-bd {
        color: #f0f2f6; /* Text input label */
    }
    
    /* Charts */
    .js-plotly-plot .plotly .modebar-container {
        background-color: #282828 !important; /* Plotly modebar */
        color: #f0f2f6 !important;
    }

    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("Smart Kirana")
st.sidebar.markdown("---")
screen = st.sidebar.radio("Navigate", ["Home", "Inventory", "Loyalty Wallet", "Reports"], 
                            format_func=lambda x: {"Home": "🏠 Home", 
                                                   "Inventory": "📦 Inventory", 
                                                   "Loyalty Wallet": "❤️ Loyalty Wallet", 
                                                   "Reports": "📊 Reports"}[x])
st.sidebar.markdown("---")
st.sidebar.info("Developed with Streamlit for a quick prototype.")

# --- Home Screen ---
if screen == "Home":
    st.header("🏠 Home Dashboard")

    st.markdown("### Today’s Sales")
    st.metric(label="Total Sales", value="₹8,250", delta="+₹1,200 vs. Yesterday", delta_color="normal")
    st.markdown("---")

    st.markdown("### 🔔 Inventory Alerts")
    alerts = [
        "Parle-G Biscuits: 2 left",
        "Tata Salt 1kg: 5 left",
        "Maggi Noodles: 1 left"
    ]
    if alerts:
        for item in alerts:
            st.warning(f"• {item}")
    else:
        st.success("No low stock alerts!")
    st.markdown("---")

# --- Inventory Screen ---
elif screen == "Inventory":
    st.header("📦 Inventory Management")

    st.markdown("### Current Stock Levels")
    items_data = [
        {"name": "Parle-G 5 Packs", "stock": 3},
        {"name": "Tata Salt 1kg", "stock": 15},
        {"name": "Maggi Noodles", "stock": 1},
        {"name": "Amul Milk 500ml", "stock": 20},
        {"name": "Detergent Powder", "stock": 8},
    ]

    for item in items_data:
        col1, col2 = st.columns([3, 1])
        with col1:
            if item["stock"] <= 5:
                st.error(f"**{item['name']}** - Stock: {item['stock']} (Low!)")
            else:
                st.info(f"**{item['name']}** - Stock: {item['stock']}")
        with col2:
            if st.button(f"Reorder", key=f"reorder_{item['name']}"):
                st.toast(f"Ordering more {item['name']} via WhatsApp...")
        st.markdown("---", help="Divider")

    st.markdown("### Add New Product")
    with st.form("add_product_form", clear_on_submit=True):
        new_name = st.text_input("Product Name")
        new_stock = st.number_input("Initial Stock", min_value=0, step=1)
        add_button = st.form_submit_button("Add Product")
        if add_button:
            if new_name and new_stock >= 0:
                st.success(f"Successfully added **{new_name}** with stock **{new_stock}**.")
            else:
                st.error("Please enter a valid product name and stock.")
    st.markdown("---")

# --- Loyalty Wallet Screen ---
elif screen == "Loyalty Wallet":
    st.header("❤️ Customer Loyalty Wallet")

    st.markdown("### Your Points Balance")
    current_points = 120
    total_points_for_reward = 200

    st.info(f"**Balance: {current_points} Points**")
    
    st.markdown(f"**Progress to next reward:** {current_points}/{total_points_for_reward} points")
    st.progress(current_points / total_points_for_reward)
    st.caption(f"You need {total_points_for_reward - current_points} more points for your next reward!")
    st.markdown("---")

    st.markdown("### Active Offers")
    
    st.warning("🎁 **Buy 5 Parle-G, Get 1 Free**\n\n_Enrolled: 15 customers | Expires: 15/10/2025_")
    st.warning("💸 **Buy ₹500, Get 10% Off**\n\n_Enrolled: 8 customers | Expires: 20/10/2025_")

    st.markdown("---")
    if st.button("📱 Send WhatsApp Offer to Customers"):
        st.success("Offer sent via WhatsApp to 25 customers!")
    st.markdown("---")

# --- Reports Screen ---
elif screen == "Reports":
    st.header("📊 Business Reports")

    st.markdown("### Daily Sales Overview")
    sales_data = pd.DataFrame({
        'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'Sales (₹)': [8000, 8500, 7500, 9000, 9500, 7000, 8200]
    })
    
    fig_sales = px.line(sales_data, x='Day', y='Sales (₹)', title='Daily Sales Trends',
                        labels={'Sales (₹)': 'Sales in Rupees'}, markers=True)
    fig_sales.update_traces(line_color='#28a745', marker_color='#28a745')
    fig_sales.update_layout(
        plot_bgcolor='#282828',
        paper_bgcolor='#282828',
        font_color='#f0f2f6',
        title_font_color='#f0f2f6'
    )
    st.plotly_chart(fig_sales, use_container_width=True)

    st.markdown("### Payment Breakdown")
    payment_data = pd.DataFrame({
        'Method': ['Digital Payments', 'Cash Payments'],
        'Percentage': [65, 35]
    })
    
    fig_payments = px.pie(payment_data, values='Percentage', names='Method', 
                         title='Payment Methods Distribution',
                         color_discrete_sequence=['#007bff', '#6c757d'])
    fig_payments.update_layout(
        plot_bgcolor='#282828',
        paper_bgcolor='#282828',
        font_color='#f0f2f6',
        title_font_color='#f0f2f6'
    )
    st.plotly_chart(fig_payments, use_container_width=True)
    
    st.info("📊 **This Week Total Revenue:** ₹50,000")
    st.markdown("---")

    st.markdown("### Top 5 Selling Products")
    top_products_data = pd.DataFrame({
        'Product': ["Parle-G Biscuits", "Tata Salt 1kg", "Maggi Noodles", "Amul Milk 500ml", "Cadbury Dairy Milk"],
        'Units Sold': [120, 80, 60, 50, 40]
    })
    
    fig_top_products = px.bar(top_products_data.sort_values('Units Sold', ascending=True), 
                              x='Units Sold', y='Product', orientation='h', 
                              title='Top 5 Products by Units Sold',
                              color_discrete_sequence=['#ffc107'])
    fig_top_products.update_layout(
        plot_bgcolor='#282828',
        paper_bgcolor='#282828',
        font_color='#f0f2f6',
        title_font_color='#f0f2f6'
    )
    st.plotly_chart(fig_top_products, use_container_width=True)
    st.markdown("---")
