create database demo;
use pawan_sanger;
CREATE TABLE stock (
    stock_id INT PRIMARY KEY AUTO_INCREMENT,
    company_name VARCHAR(50),
    ticker_symbol VARCHAR(10),
    price DECIMAL(10,2),
    quantity INT,
    last_updated DATE
);
INSERT INTO stock (company_name, ticker_symbol, price, quantity, last_updated)
VALUES
('Reliance Industries', 'RELI', 2800.50, 100, '2025-08-14'),
('Tata Consultancy Services', 'TCS', 3950.75, 50, '2025-08-14'),
('Infosys', 'INFY', 1600.20, 200, '2025-08-14'),
('HDFC Bank', 'HDFCBANK', 1750.00, 150, '2025-08-14'),
('State Bank of India', 'SBIN', 620.45, 300, '2025-08-14');
-- सभी डेटा देखना
SELECT * FROM stock;

-- सिर्फ कंपनी का नाम और प्राइस
SELECT company_name, price FROM stock;

-- जिनका प्राइस 2000 से ज्यादा है
SELECT * FROM stock WHERE price > 2000;

-- TCS का डेटा
SELECT * FROM stock WHERE ticker_symbol = 'TCS';
-- टॉप 3 सबसे महंगे स्टॉक्स
SELECT * FROM stock ORDER BY price DESC LIMIT 3;

-- Quantity का Total
SELECT SUM(quantity) AS total_quantity FROM stock;

-- Average price
SELECT AVG(price) AS avg_price FROM stock;

-- Price range में स्टॉक्स (BETWEEN का use)
SELECT * FROM stock WHERE price BETWEEN 1500 AND 3000;
use pawan_sanger;
show tables;
desc stock

select * from customer;
create user teamuser identified by "123@";
grant select,insert,update on pawan_sanger.customer to teamuser ;
