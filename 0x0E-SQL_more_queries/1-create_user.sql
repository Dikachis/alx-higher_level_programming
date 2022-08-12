-- This script creates the MySQL server user user_0d_1

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- flush privileges after creating a user or granting a user permissions
FLUSH PRIVILEGES;

-- granting a user all permissions in root
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
