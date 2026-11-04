# ONLINE STORE PRODUCT INVENTORY ANALYSIS SYSTEM
# QUESTION 2 (a) - (f)

# Import libraries
import streamlit as st
import numpy as np
import pandas as pd

# QUESTION 2(a)
# Streamlit Interface

st.title("Online Store Product Inventory Analysis System")

product_name = st.text_input("Product Name")

category = st.selectbox(
    "Product Category",
    ["Electronics", "Clothing", "Accessories"]
)

stock_quantity = st.text_input("Stock Quantity")

# QUESTION 2(b) and 2(f)
# Input Validation and Session State

if "products" not in st.session_state:
    st.session_state.products = []

if st.button("Process Inventory"):

    try:

        if product_name.strip() == "":
            st.error("Product Name cannot be empty!")

        else:

            quantity = int(stock_quantity)

            if quantity < 0:
                st.error("Stock Quantity cannot be negative!")

            else:

                product = {
                    "Product Name": product_name,
                    "Category": category,
                    "Quantity": quantity
                }

                st.session_state.products.append(product)

                st.success("Product information added successfully!")

    except ValueError:
        st.error("Please enter a valid Stock Quantity!")

# QUESTION 2(c) and 2(f)
# NumPy Inventory Analysis

st.header("Inventory Analysis")

if len(st.session_state.products) > 0:

    quantities = np.array([
        p["Quantity"] for p in st.session_state.products
    ])

    total_stock = np.sum(quantities)

    minimum_stock = np.min(quantities)

    low_stock_count = np.sum(quantities < 20)

    st.write("Total Stock Quantity:", total_stock)

    st.write("Minimum Stock Quantity:", minimum_stock)

    st.write("Products Below 20 Units:", low_stock_count)

# QUESTION 2(d) and 2(f)
# Pandas DataFrame

if len(st.session_state.products) > 0:

    df = pd.DataFrame(st.session_state.products)

    def classify_stock(quantity):

        if quantity >= 20:
            return "Sufficient"

        elif quantity >= 1:
            return "Low Stock"

        else:
            return "Out of Stock"

    df["Stock Status"] = df["Quantity"].apply(classify_stock)

    st.header("Complete Product Inventory")

    st.dataframe(df)

    # Filter products below 20 units

    st.subheader("Low Stock Products")

    low_stock = df[df["Quantity"] < 20]

    st.dataframe(low_stock)

    # QUESTION 2(e) and 2(f)
    # Category-Based Inventory Analysis

    st.header("Category Inventory Analysis")

    category_summary = df.groupby(
        "Category"
    )["Quantity"].sum().reset_index()

    st.write("Grouped Inventory Data")

    st.dataframe(category_summary)

    # Bar Chart

    st.subheader("Total Stock Quantity by Category")

    chart_data = category_summary.set_index("Category")

    st.bar_chart(chart_data)
