DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS customer_order;

CREATE TABLE customer(
    id INT(11) NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(300) NOT NULL DEFAULT '',
    last_name VARCHAR(300) NOT NULL DEFAULT '',
    email VARCHAR(300) NOT NULL DEFAULT '',
    status VARCHAR(300) NOT NULL DEFAULT '',
    PRIMARY KEY (id)
);


CREATE TABLE customer_order (
    id INT(11) NOT NULL AUTO_INCREMENT,
    customer_id INT(11) NOT NULL,
    item_name VARCHAR(300) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

