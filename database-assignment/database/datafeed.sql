--- Feeding data into indus_customers table
INSERT INTO indus_customers (indus_customer_name, indus_customer_email, indus_customer_phone_no, indus_customer_city)
VALUES 
('Arun', 'arun@gmail.com', '9876543210', 'Hyderabad'),
('Kiran', 'kiran@gmail.com', '9876543211', 'Vijayawada'),
('Meena', 'meena@gmail.com', '9876543212', 'Chennai'),
('Ravi', 'ravi@gmail.com', '9876543213', 'Bangalore'),
('Sita', 'sita@gmail.com', '9876543214', 'Hyderabad');

--- Feeding data into indus_products
INSERT INTO indus_products (indus_product_name, indus_product_category, indus_product_price, indus_total_product_stock)
VALUES
('Laptop', 'Electronics', 55000, 10),
('Mobile', 'Electronics', 20000, 25),
('Headphones', 'Accessories', 1500, 50),
('Keyboard', 'Accessories', 1200, 30);


--- Feeding data into indus_customer_orders
INSERT INTO indus_customer_orders (indus_customer_id, indus_customer_order_time, indus_customer_order_status)
VALUES
(1, NOW() - INTERVAL '5 days', 'COMPLETED'),
(1, NOW() - INTERVAL '10 days', 'COMPLETED'),
(2, NOW() - INTERVAL '2 days', 'PENDING'),
(2, NOW() - INTERVAL '20 days', 'COMPLETED'),
(3, NOW() - INTERVAL '15 days', 'COMPLETED'),
(3, NOW() - INTERVAL '1 days', 'COMPLETED'),
(4, NOW() - INTERVAL '25 days', 'PENDING'),
(4, NOW() - INTERVAL '3 days', 'COMPLETED'),
(5, NOW() - INTERVAL '12 days', 'COMPLETED'),
(5, NOW() - INTERVAL '7 days', 'COMPLETED');

--- Feeding data into indus_customer_order_product_details 
INSERT INTO indus_customer_order_product_details 
(indus_customer_order_id, indus_products_product_id, ordered_quantity, product_unit_price)
VALUES
(1, 1, 1, 55000),
(2, 2, 2, 20000),
(3, 3, 3, 1500),
(4, 4, 1, 1200),
(5, 1, 1, 55000),
(6, 2, 1, 20000),
(7, 3, 5, 1500),
(8, 4, 2, 1200),
(9, 1, 1, 55000),
(10, 2, 1, 20000);

--- Feeding data into indus_customer_payments
INSERT INTO indus_customer_payments 
(indus_customer_order_id, payment_mode, order_payment_amount, order_payment_status)
VALUES
(1, 'UPI', 55000, 'SUCCESS'),
(2, 'CARD', 40000, 'SUCCESS'),
(3, 'UPI', 4500, 'PENDING'),
(4, 'CASH', 1200, 'SUCCESS'),
(5, 'UPI', 55000, 'SUCCESS'),
(6, 'CARD', 20000, 'SUCCESS'),
(7, 'UPI', 7500, 'SUCCESS'),
(8, 'CASH', 2400, 'SUCCESS'),
(9, 'UPI', 55000, 'SUCCESS'),
(10, 'CARD', 20000, 'SUCCESS');