
--- following 5 tables are created for order management
--- 1. indus_customers have all customer details
--- 2. indus_products have all prodcut details
--- 3. indus_customer_orders have orders associated with each customer so it has realtion ship with indus_customer table
--- 4. indus_customer_order_product_details have product and order details , product and orders are in many to many realtionship so created seprate table
--- 5. indus_customer_payments have payment details, each order have one payment

CREATE TABLE indus_customers (
    indus_customer_id SERIAL PRIMARY KEY,
    indus_customer_name VARCHAR(20) NOT NULL,
    indus_customer_email VARCHAR(30) UNIQUE NOT NULL,
    indus_customer_phone_no VARCHAR(15),
    indus_customer_city VARCHAR(50),
    indus_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE indus_products (
    indus_product_id SERIAL PRIMARY KEY,
    indus_product_name VARCHAR(100) NOT NULL,
    indus_product_category VARCHAR(50),
    indus_product_price DECIMAL(10,2) NOT NULL,
    indus_total_product_stock INT DEFAULT 0
);


CREATE TABLE indus_customer_orders (
    indus_customer_order_id SERIAL PRIMARY KEY,
    indus_customer_id INT REFERENCES indus_customers(indus_customer_id),
    indus_customer_order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    indus_customer_order_status VARCHAR(20) DEFAULT 'PENDING'
);

CREATE TABLE indus_customer_order_product_details (
    indus_customer_order_product_id SERIAL PRIMARY KEY,
    indus_customer_order_id INT REFERENCES indus_customer_orders(indus_customer_order_id),
    indus_products_product_id INT REFERENCES indus_products(indus_product_id),
    ordered_quantity INT NOT NULL,
    product_unit_price DECIMAL(10,2) NOT NULL
);

CREATE TABLE indus_customer_payments (
    indus_customer_payment_id SERIAL PRIMARY KEY,
    indus_customer_order_id INT UNIQUE REFERENCES indus_customer_orders(indus_customer_order_id),
    payment_mode VARCHAR(30),
    order_payment_amount DECIMAL(10,2),
    order_payment_status VARCHAR(20) DEFAULT 'SUCCESS',
    order_payment_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);