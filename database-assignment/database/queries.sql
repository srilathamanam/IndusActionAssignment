--- Fetch the top 3 customers with the highest number of orders.
--- Used join operation between customer and orders to count total orders per customer
--- Used Gropuby clause to get orders for each customer
--- Used order by clause to get orders in descending order and from that getting top 3 records using limit 
SELECT 
    c.indus_customer_id,
    c.indus_customer_name,
    COUNT(o.indus_customer_order_id) AS total_orders
FROM indus_customers c
JOIN indus_customer_orders o
ON c.indus_customer_id = o.indus_customer_id
GROUP BY c.indus_customer_id, c.indus_customer_name
ORDER BY total_orders DESC
LIMIT 3;


--- Retrieve orders placed in the last 30 days.
--- Used where clause to filter orders using current time using now() and subtracting with 30 days.
SELECT *
FROM indus_customer_orders
WHERE indus_customer_order_time >= NOW() - INTERVAL '30 days'
ORDER BY indus_customer_order_time DESC;


--- Calculate total revenue for each product
--- Revenue calculated by adding sum of  quantity with product unit price 
--- Used Groupby clause for getteing revencu for each product
SELECT 
    p.indus_product_id,
    p.indus_product_name,
    SUM(opd.ordered_quantity * opd.product_unit_price) AS total_revenue
FROM indus_products p
JOIN indus_customer_order_product_details opd
ON p.indus_product_id = opd.indus_products_product_id
GROUP BY p.indus_product_id, p.indus_product_name
ORDER BY total_revenue DESC;


