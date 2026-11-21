CREATE TABLE IF NOT EXISTS lab_messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO lab_messages (message) VALUES ('The lab database is ready');
