import pandas as pd

def create_features(df):
    
    #Dilevery time in days
    df["delivery_days"] = (df["order_delivered_customer_date"] - df["order_purchase_timestamp"]).dt.days

    #Month and Year
    df["order_year"] = df["order_purchase_timestamp"].dt.year
    df["order_month"] = df["order_purchase_timestamp"].dt.month

    #Month Name
    df["order_month_name"] = df["order_purchase_timestamp"].dt.month_name()

    return df