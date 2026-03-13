CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    city VARCHAR(50)
);

CREATE TABLE medicines (
    medicine_id SERIAL PRIMARY KEY,
    medicine_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT,
    supplier_id INT,
    FOREIGN KEY (supplier_id)
    REFERENCES suppliers(supplier_id)
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    phone VARCHAR(15),
    city VARCHAR(50)
);

CREATE TABLE purchases (
    purchase_id SERIAL PRIMARY KEY,
    medicine_id INT,
    supplier_id INT,
    quantity INT,
    purchase_date DATE,
    FOREIGN KEY (medicine_id)
    REFERENCES medicines(medicine_id),
    FOREIGN KEY (supplier_id)
    REFERENCES suppliers(supplier_id)
);

CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    medicine_id INT,
    customer_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (medicine_id)
    REFERENCES medicines(medicine_id),
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);



SELECT table_name
FROM information_schema.tables
WHERE table_schema='public';