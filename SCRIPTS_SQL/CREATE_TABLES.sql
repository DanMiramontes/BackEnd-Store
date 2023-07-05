DROP DATABASE IF EXISTS store;
CREATE DATABASE store;
USE store;

CREATE TABLE categories (
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY(id),
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255) NOT NULL,
    created_at DATETIME NULL,
    created_by TINYINT NULL
);

-- RELATION ONE TO MANY CATEGORIES TO PRODUCTS
CREATE TABLE products (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
    description VARCHAR(255) NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY( category_id) REFERENCES categories(id),
	created_at DATETIME NULL,
    created_by TINYINT NULL
);

CREATE TABLE providers (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	full_address VARCHAR(255) NOT NULL,
	created_at DATETIME NULL,
    created_by TINYINT NULL,
    PRIMARY KEY(id)
);

-- RELACION ONE TO MANY providers to purchase_orders
CREATE TABLE purchase_orders (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    provider_id INT NOT NULL,
	FOREIGN KEY( provider_id) REFERENCES providers(id),
    date TIMESTAMP NOT NULL,
    total DECIMAL UNSIGNED,
	created_at DATETIME NULL,
    created_by TINYINT NULL
);

DROP TABLE purchase_order_detail;
CREATE TABLE purchase_order_detail (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    purchase_order_id INT NOT NULL UNIQUE,
    FOREIGN KEY( purchase_order_id) REFERENCES purchase_orders(id),
    product_id INT NOT NULL,
    FOREIGN KEY( product_id ) REFERENCES products(id),
    quantity DECIMAL UNSIGNED,
    total DECIMAL,
	created_at DATETIME NULL,
    created_by TINYINT NULL
);









