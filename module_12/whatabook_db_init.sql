DROP USER IF EXISTS 'whatabook_user'@'localhost';
DROP DATABASE IF EXISTS whatabook;
-- create the database and associated user
create database whatabook;
use whatabook;
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';
-- create required tables
CREATE TABLE user(
	user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
);
CREATE TABLE book(
	book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    details VARCHAR(500),
    author VARCHAR(500) NOT NULL,
    PRIMARY KEY(book_id)
);
CREATE TABLE store(
	store_id INT NOT NULL,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY(store_id)
);
CREATE TABLE wishlist(
	wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
		REFERENCES user(user_id),
	CONSTRAINT fk_book
    FOREIGN KEY (book_id)
		REFERENCES book(book_id)
);
-- insert user records
INSERT INTO user(first_name, last_name)
	VALUES ('Hakari', 'Kinji');
INSERT INTO user(first_name, last_name)
	VALUES ('Scott', 'Fitzgerald');
INSERT INTO user(first_name, last_name)
	VALUES ('Millie', 'Valentine');
-- insert book records
INSERT INTO book(book_name, author, details)
	VALUES ('Naruto Box Set 1', 'Masashi Kishimoto', 'Contains volumes 1-27 of the Naruto manga');
INSERT INTO book(book_name, author, details)
	VALUES('Naruto Box Set 2', 'Masashi Kishimoto', 'Contains volumes 28-48 of the Naruto manga');
INSERT INTO book(book_name, author, details)
	VALUES ('Naruto Box Set 3', 'Masashi Kishimoto', 'Contains volumes 49-72 of the Naruto manga');
INSERT INTO book(book_name, author)
	VALUES('It Ends With us', 'Colleen Hoover');
INSERT INTO book(book_name, author)
	VALUES ('Hatchet', 'Gary Paulsen');
INSERT INTO book(book_name, author)
	VALUES ('Atomic Habits', 'James Clear');
INSERT INTO book(book_name, author, details)
	VALUES ('Fourth Wing', 'Rebecca Yarros', 'First book of the Empryan series');
INSERT INTO book(book_name, author, details)
	VALUES ('Iron Flame', 'Rebecca Yarros', 'Second book of the Empryan series');
INSERT INTO book(book_name, author)
	VALUES ('Unbroken', 'Laura Hillenbrand');
-- insert store record
INSERT INTO store(store_id, locale)
	VALUES ('1', '1200 Ulster Avenue, Kingston, New York 12401');
-- insert wishlist records
INSERT INTO wishlist(user_id, book_id)
	VALUES(
		(SELECT user_id from user where first_name = 'Hakari'),
        (SELECT book_id from book where book_name = 'Naruto Box Set 1')
	);
INSERT INTO wishlist(user_id, book_id)
	VALUES(
		(SELECT user_id from user where first_name = 'Scott'),
        (SELECT book_id from book where book_name = 'Atomic Habits')
	);
INSERT INTO wishlist(user_id, book_id)
	VALUES(
		(SELECT user_id from user where first_name = 'Millie'),
        (SELECT book_id from book where book_name = 'Hatchet')
	);
