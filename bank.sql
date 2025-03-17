CREATE DATABASE IF NOT EXISTS bank;

CREATE TABLE IF NOT EXISTS account (
    id_account INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    fname VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL,
    id_transaction INT,
    PRIMARY KEY (id_account),
    FOREIGN KEY (id_transaction) REFERENCES transaction(id_transaction) ON DELETE CASCADE
)

CREATE TABLE IF NOT EXISTS transaction (
    id_transaction INT AUTO_INCREMENT,
    description VARCHAR(200) NOT NULL,
    amount INT NOT NULL,
    date DATE NOT NULL,
    type VARCHAR(10) NOT NULL
    receiving_account INT,
    PRIMARY KEY (id_transaction),
    FOREIGN KEY (receiving_account) REFERENCES account(id_account) ON DELETE CASCADE
)