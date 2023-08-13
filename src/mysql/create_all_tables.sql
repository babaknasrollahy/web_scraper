CREATE DATABASE stack_mag ;
USE stack_mag ;
CREATE TABLE tags 
(
    tag_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `owner` ENUM('admin', 'bot') ,
    tag VARCHAR(15) NOT NULL UNIQUE,
    `status` ENUM('active', 'pending' , 'completed'),
    `date` DATE
);

CREATE TABLE contents
(
    cont_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    tag_id INT,
    cont_en TEXT ,
    cont_fa TEXT ,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)


);

CREATE TABLE informations
(
    cont_id INT,
    tag_id INT,
    title VARCHAR(100),
    `date` DATE,
    `like` VARCHAR(15),
    writer VARCHAR(50),
    tags VARCHAR(50),
    FOREIGN KEY (cont_id) REFERENCES contents(cont_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)



);