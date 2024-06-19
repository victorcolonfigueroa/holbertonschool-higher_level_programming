-- creates the user_0d_1_pwd and gives privileges
CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1_pwd;