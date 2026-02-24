-- Day 1: Advanced Database Schema for Retail & Performance Analytics
-- Focus: Data Integrity, Primary Keys, Foreign Keys, and ML-Ready Constraints

-- Creating a table for Customer Demographics
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    Location VARCHAR(50),
    JoinDate DATE NOT NULL
);

-- Creating a table for Sales Transactions (linking to your Sales Analysis project)
CREATE TABLE Sales_Transactions (
    TransactionID INT PRIMARY KEY,
    CustomerID INT,
    ProductCategory VARCHAR(50) NOT NULL,
    SaleAmount DECIMAL(10, 2) CHECK (SaleAmount > 0), -- Ensuring data integrity
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Technical Note: This relational structure is designed to support 
-- Exploratory Data Analysis (EDA) and future Machine Learning Regression models.
