import pandas as pd

def create_features(df):
    #Revenue column
    df["revenue"] = df["price"] + df["freight_value"]

    #Dilevery time in days
    df["delivery_days"] = (df["order_delivered_customer_date"] - df["order_purchase_timestamp"]).dt.days

    #Month and Year
    df["order_year"] = df["order_purchase_timestamp"].dt.year
    df["order_year"] = df["order_purchase_timestamp"].dt.month

    #Month Name
    df["order_year"] = df["order_purchase_timestamp"].dt.month_name()

    return df