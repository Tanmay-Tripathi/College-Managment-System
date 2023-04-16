Table number 1 - user 

CREATE TABLE user (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(30),
  password VARCHAR(30),
  account_type VARCHAR(50)
);


table number 2 - attendance

CREATE TABLE attendance (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(25),
  date VARCHAR(25),
  status VARCHAR(12)
);


if you want to use normalised tables then follow this 

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(30),
  password VARCHAR(30),
  account_type VARCHAR(50)
);

CREATE TABLE user_attendance (
  user_id INT,
  date VARCHAR(25),
  status VARCHAR(12),
  PRIMARY KEY (user_id, date),
  FOREIGN KEY (user_id) REFERENCES users(id)
);
