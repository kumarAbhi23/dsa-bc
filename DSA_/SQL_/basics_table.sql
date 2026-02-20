CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    created_at DATETIME
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    amount DECIMAL(10,2),
    updated_at DATETIME
);

CREATE TABLE CDC_Metadata (
    table_name VARCHAR(50),
    last_watermark DATETIME
);

CREATE TABLE Audit_Log (
    error_message VARCHAR(200),
    log_time DATETIME
);
