-- creates second_table
CREATE TABLE IF NOT EXISTS second_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    score INT 
);

INSERT INTO second_table (id, name, score)
(1, "John", 10),
(2, "Alex", 30),
(3, "Bob", 14),
(4, "George", 8);