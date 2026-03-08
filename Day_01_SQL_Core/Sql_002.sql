----Supplier-----------------
CREATE TABLE suppliers(
supplier_id SERIAL PRIMARY KEY,
supplier_name VARCHAR(100),
phone VARCHAR(20),
city VARCHAR(50)
);

---Medicines--------------------------
CREATE TABLE medicines(
medicine_id SERIAL PRIMARY KEY,
medicine_name VARCHAR(100),
category VARCHAR(50),
price INT,
stock_quantity INT,
expiry_date DATE,
supplier_id INT
);


ALTER TABLE medicines
ADD CONSTRAINT fk_supplier
FOREIGN KEY (supplier_id)
REFERENCES suppliers(supplier_id);


