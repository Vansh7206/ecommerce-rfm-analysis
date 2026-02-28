# 📊 AI-Powered E-Commerce Business Intelligence System

An end-to-end Business Intelligence project combining SQL analytics, RFM customer segmentation, and an AI-powered natural language query engine built with Streamlit.
This system transforms raw e-commerce data into executive-level insights and allows users to query business metrics using natural language.

## 🚀 Project Overview  
This project analyzes a large-scale Brazilian e-commerce dataset to:
1. Identify key revenue drivers
2. Evaluate operational efficiency
3. Analyze customer purchasing behavior
4. Perform RFM-based segmentation
5. Detect geographic revenue concentration
6. Understand payment behavior
7. Enable AI-driven business querying
8. It combines traditional data analysis with a lightweight AI intent engine to simulate a business intelligence assistant.

🎥 Demo & Application Preview

![App Preview](media/Working_video.mp4)

## 🧠 AI-Powered Analytics Engine   
Users can type natural language questions such as:

a. “Total revenue”      
b. “Revenue by state”   
c. “Top 5 states by revenue”    
d. “Orders by payment type”     
e. “Average order value”    
f. “Revenue by customer segment”    

### How It Works
1. User Input
Natural language query is entered in the Streamlit interface.

2. Intent Detection (ai_query_engine.py)
The system extracts:

- Metric (revenue, orders, AOV)
- Dimension (state, category, payment type)
- Aggregation type (sum, average, count)
- Top-N condition (if specified)
- Execution Engine (analytics_engine.py)
- Performs aggregation using Pandas
- Applies grouping
- Applies Top-N sorting
- Returns structured results
- AI Explainer (ai_explainer.py)
- Generates human-readable business insights
- Highlights patterns and leaders

This removes the need to manually write SQL queries.

## ✅ Supported Capabilities
1. Revenue aggregation
2. Order count analysis
3. Average order value (AOV)
4. Group-by analysis (state, category, payment type)
5. Top-N queries (e.g., Top 5 states by revenue)
6. AI-generated result explanation
7. Modular backend architecture

## ❌ Current Limitations
1. Month-based filtering (e.g., “Monthly revenue in 2018”)
2. Time-series trend detection
3. Year-over-year comparison
4. Advanced multi-condition queries
5. The system uses a rule-based intent engine and does not yet support advanced time-intelligence logic.

## 📊 Business Performance Analysis 
### Key Metrics
- 96K+ Customers
- 99K+ Orders
- 15.8M Total Revenue
- 97% Delivery Success Rate
- Major Insights
- Revenue scaled consistently from 2016–2018
- Business operates in a mass-market model (low AOV)
- Revenue heavily concentrated in São Paulo
- Delivery reliability strong but delivery speed slow
- Majority customers purchase only once

## 👥 RFM Customer Segmentation 
Customers segmented using:
- Recency
- Frequency
- Monetary

#### Segments identified:
1. Champion
2. Loyal
3. Regular
4. Lost

#### Key Findings
1. Loyal customers contribute the highest revenue
2. Majority customers purchase only once
3. Revenue follows Pareto principle
4. Retention improvement presents major growth opportunity

### 🛠 Tech Stack
a. SQL (Data extraction & joins)
b. Python
c. Pandas & NumPy
d. Matplotlib
e. Streamlit
f. Modular AI intent engine
g. RFM scoring model

### 💼 Business Value Demonstrated
1. Revenue concentration analysis
2. Customer intelligence modeling
3. Operational performance evaluation
4. Data-driven strategic recommendations
5. AI-enhanced analytics automation