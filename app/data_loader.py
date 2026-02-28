import pandas as pd
import os

def load_data():
    data_path = os.path.join(os.path.dirname(__file__),"..","data")

    #loading Dataset
    customers = pd.read_csv(os.path.join(data_path, "olist_customers_dataset.csv"))
    orders = pd.read_csv(os.path.join(data_path, "olist_orders_dataset.csv"))
    order_items = pd.read_csv(os.path.join(data_path, "olist_order_items_dataset.csv"))
    payments = pd.read_csv(os.path.join(data_path, "olist_order_payments_dataset.csv"))
    products = pd.read_csv(os.path.join(data_path, "olist_products_dataset.csv"))
    sellers = pd.read_csv(os.path.join(data_path, "olist_sellers_dataset.csv"))
    category_translation = pd.read_csv(os.path.join(data_path, "product_category_name_translation.csv"))

    #Converting date column
    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"],errors="coerce")
    orders["order_delivered_customer_date"] = pd.to_datetime(orders["order_delivered_customer_date"],errors="coerce")

    #Merge Datasets
    df = orders.merge(customers, on="customer_id", how="left")
    df = df.merge(order_items, on="order_id", how="left")
    df = df.merge(payments, on="order_id", how="left")
    df = df.merge(products, on="product_id", how="left")
    df = df.merge(category_translation,on="product_category_name",how="left")
    df = df.merge(sellers, on="seller_id", how="left")

    df["revenue"] = df["price"] + df["freight_value"]

    #Relevant columns for AI analytics
    df = df[
        [
        "order_purchase_timestamp",
        "customer_state",
        "revenue",
        "price",
        "freight_value"
        ]
    ]
    return df
