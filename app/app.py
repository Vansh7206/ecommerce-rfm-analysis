import streamlit as st
from data_loader import load_data
from ai_query_engine import generate_intent
from analytics_engine import execute_intent
from ai_explainer import explain_result
import pandas as pd

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AI-Powered E-commerce Analytics",
    page_icon="🤖",
    layout="centered"
)

@st.cache_data
def get_data():
    return load_data()

df = get_data()

# ─────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────
st.title("📊 AI-Powered E-commerce Analytics")
st.caption("Ask natural language questions. Get instant data insights.")

st.divider()

# ─────────────────────────────────────────────
# Query Input Form
# ─────────────────────────────────────────────
with st.form("query_form"):
    user_query = st.text_input(
        "Ask your question",
        placeholder="e.g. Top 5 states by revenue"
    )
    run = st.form_submit_button("Analyze", type="primary")

# ─────────────────────────────────────────────
# Example Queries Section
# ─────────────────────────────────────────────
st.markdown("### 🚀 Try Example Questions")

examples = [
    "Top 5 states by revenue",
    "Monthly orders last year",
    "Avg order by category",
    "Best selling products"
]

cols = st.columns(2)

for i, example in enumerate(examples):
    if cols[i % 2].button(example, use_container_width=True):
        user_query = example
        run = True

# ─────────────────────────────────────────────
# Run Query
# ─────────────────────────────────────────────
if run:

    if not user_query.strip():
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Analyzing your question..."):
        try:
            intent = generate_intent(user_query)
            result = execute_intent(intent, df)
        except Exception as e:
            st.error(f"Query failed: {e}")
            st.stop()

    st.divider()

    # ── Extracted Intent ─────────────────────
    with st.expander("🧠 What the AI Interpreted"):
        st.json(intent)

    # ── Result Section ───────────────────────
    st.subheader("📊 Result")

    if isinstance(result, (int, float)):
        st.metric("Total Value", f"{result:,.2f}")

    elif isinstance(result, pd.Series):
        st.dataframe(
            result.reset_index(),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.dataframe(
            result,
            use_container_width=True,
            hide_index=True
        )

    # ── Insight Section ──────────────────────
    st.markdown("### 💡 AI Insight")

    with st.spinner("Generating insight..."):
        try:
            explanation = explain_result(user_query, result)
            st.success(explanation)
        except Exception as e:
            st.warning(f"Couldn't generate insight: {e}")