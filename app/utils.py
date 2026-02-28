import pandas as pd

def format_result_for_display(result):

    if isinstance(result, (int, float)):
        return f"{result:,.2f}"

    if isinstance(result, pd.Series):
        return result.reset_index()

    return result