CREATE DATABASE IF NOT EXISTS users_db;
USE users_db;
CREATE ROLE 'service';
GRANT SELECT, INSERT, UPDATE, INSERT, DELETE ON users_db.* to 'service';
CREATE USER 'accessor'@'%' IDENTIFIED BY 'accessor' DEFAULT ROLE 'service';
FLUSH PRIVILEGES;
ALTER USER 'root'@'%' IDENTIFIED BY 'root';
FLUSH PRIVILEGES;


-- CREATE TABLE IF NOT EXISTS User (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     telephone VARCHAR(15)
-- );

-- CREATE TABLE IF NOT EXISTS Preference (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     preference VARCHAR(100) UNIQUE NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS User_Preferences (
--     user_id INT,
--     preference_id INT,
--     FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
--     FOREIGN KEY (preference_id) REFERENCES Preference(id) ON DELETE CASCADE,
--     PRIMARY KEY (user_id, preference_id)
-- );

-- INSERT INTO User (name, telephone) VALUES ('Anton', '0557712411');
-- INSERT INTO Preference (preference) VALUES ('politics'), ('hight-tech'), ('stock market');
-- INSERT INTO User_Preferences (user_id, preference_id) VALUES
--     (1, 1),
--     (1, 2);
