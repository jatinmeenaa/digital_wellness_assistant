-- Drop database if already exists
DROP DATABASE IF EXISTS digital_wellness;

-- Create database
CREATE DATABASE digital_wellness;
USE digital_wellness;

-- Drop table if already exists
DROP TABLE IF EXISTS app_usage_logs;

-- Create table to store app usage logs
CREATE TABLE app_usage_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    app_name VARCHAR(100),
    start_time DATETIME,
    end_time DATETIME,
    duration_sec INT,
    log_date DATE
);
