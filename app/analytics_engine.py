import pandas as pd

def execute_intent(intent, df):

    metric = intent.get("metric", "revenue")
    agg = intent.get("aggregation", "sum")
    group = intent.get("group_by", "none")
    last_n = intent.get("last_n_years")
    top_n = intent.get("top_n")
    sort_order = intent.get("sort_order", "none")
    comparison = intent.get("comparison", "none")

    metric_mapping = {"sales": "revenue","revenue": "revenue","price": "price","freight": "freight_value"}

    metric = metric_mapping.get(metric.lower(), "revenue")

    data = df.copy()

    # Filter last N years
    if last_n:
        max_date = data["order_purchase_timestamp"].max()
        start_date = max_date - pd.DateOffset(years=last_n)
        data = data[data["order_purchase_timestamp"] >= start_date]

    # Grouping
    if group == "year":
        data["year"] = data["order_purchase_timestamp"].dt.year
        grouped = data.groupby("year")[metric]

    elif group == "state":
        grouped = data.groupby("customer_state")[metric]

    else:
        grouped = data[metric]

    # Aggregation
    if agg == "sum":
        result = grouped.sum()
    elif agg == "mean":
        result = grouped.mean()
    elif agg == "count":
        result = grouped.count()
    else:
        result = grouped

    # Sorting
    if sort_order == "asc":
        result = result.sort_values(ascending=True)
    elif sort_order == "desc":
        result = result.sort_values(ascending=False)

    # Top N
    if top_n:
        result = result.head(top_n)

    # Comparison (growth calculation)
    if comparison == "growth" and isinstance(result, pd.Series):
        result = result.pct_change() * 100

    return result