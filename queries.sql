-- OLIST E-COMMERCE SQL ANALYSIS
-- Dataset: Brazilian E-Commerce Public Dataset (Kaggle)
-- Scope: 99,000+ orders | 96,000+ customers | R$15.8M revenue
-- Sections: Sales Performance | Customer Behaviour |
--           Product Performance | Seller Effectiveness

-- 1. SALES PERFORMANCE
-------------------------------------------------------------------

-- What is the monthly revenue trend over the dataset period?
SELECT
    DATE_TRUNC('month', o.order_purchase_timestamp) AS order_month,
    SUM(oi.price + oi.freight_value) AS total_revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY order_month
ORDER BY order_month;


-- What is the total revenue per year?
SELECT
    DATE_TRUNC('year', o.order_purchase_timestamp) AS order_year,
    SUM(oi.price + oi.freight_value) AS total_revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY order_year
ORDER BY order_year;


-- Which Brazilian states generate the most revenue?
SELECT
    c.customer_state,
    SUM(oi.price + oi.freight_value) AS total_revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_state
ORDER BY total_revenue DESC;


-- Which product categories drive the most revenue? (Top 10)
SELECT
    ct.product_category_name_english,
    SUM(oi.price + oi.freight_value) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN category_translation ct ON p.product_category_name = ct.product_category_name
GROUP BY ct.product_category_name_english
ORDER BY total_revenue DESC
LIMIT 10;

-- 2. CUSTOMER BEHAVIOUR
-------------------------------------------------------------------

-- Extract raw transaction data for RFM scoring
-- (Recency, Frequency, Monetary value per customer)
SELECT
    c.customer_unique_id,
    o.order_id,
    o.order_purchase_timestamp,
    SUM(oi.price + oi.freight_value) AS total_revenue
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN customers c ON c.customer_id = o.customer_id
GROUP BY c.customer_unique_id, o.order_id, o.order_purchase_timestamp;


-- What payment methods do customers prefer?
SELECT
    payment_type,
    COUNT(*) AS total_transactions
FROM order_payments
GROUP BY payment_type
ORDER BY total_transactions DESC;


-- How are customers distributed across installment ranges?
-- Helps understand financing behaviour and credit reliance
SELECT
    CASE
        WHEN payment_installments BETWEEN 1 AND 4  THEN '1-4 installments'
        WHEN payment_installments BETWEEN 5 AND 8  THEN '5-8 installments'
        WHEN payment_installments BETWEEN 9 AND 12 THEN '9-12 installments'
        ELSE '13+ installments'
    END AS installment_group,
    COUNT(*) AS total_payments
FROM order_payments
GROUP BY installment_group
ORDER BY installment_group;

-- 3. PRODUCT PERFORMANCE
-------------------------------------------------------------------

-- Which product categories have the highest number of listings? (Top 10)
-- Revenue vs volume comparison — high listings ≠ high revenue
SELECT
    ct.product_category_name_english AS category,
    COUNT(*) AS total_products
FROM products p
JOIN category_translation ct ON p.product_category_name = ct.product_category_name
GROUP BY ct.product_category_name_english
ORDER BY total_products DESC
LIMIT 10;

-- 4. SELLER EFFECTIVENESS
-------------------------------------------------------------------

-- Which cities have the highest concentration of sellers? (Top 10)
SELECT
    seller_city,
    COUNT(*) AS seller_count
FROM sellers
GROUP BY seller_city
ORDER BY seller_count DESC
LIMIT 10;


-- How long does delivery actually take? Bucketed distribution
-- Identifies whether slow delivery is an edge case or systemic issue
SELECT
    CASE
        WHEN (order_delivered_customer_date - order_purchase_timestamp)
             BETWEEN INTERVAL '1 day'  AND INTERVAL '4 days'  THEN '1-4 days'
        WHEN (order_delivered_customer_date - order_purchase_timestamp)
             BETWEEN INTERVAL '5 days' AND INTERVAL '8 days'  THEN '5-8 days'
        WHEN (order_delivered_customer_date - order_purchase_timestamp)
             BETWEEN INTERVAL '9 days' AND INTERVAL '12 days' THEN '9-12 days'
        ELSE '12+ days'
    END AS delivery_bucket,
    COUNT(*) AS total_orders
FROM orders
WHERE order_delivered_customer_date IS NOT NULL
GROUP BY delivery_bucket
ORDER BY delivery_bucket;