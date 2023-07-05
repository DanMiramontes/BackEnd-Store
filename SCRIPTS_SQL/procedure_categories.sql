DELIMITER //
CREATE PROCEDURE sp_create_category(IN pName VARCHAR(50), IN pDescription VARCHAR(255))
BEGIN
    INSERT INTO categories (name, description,created_at)
    VALUES (pName, pDescription,CURRENT_TIMESTAMP);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_index_category()
BEGIN
    SELECT * FROM categories ;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_show_category(IN id INT)
BEGIN
    SELECT * FROM categories WHERE categories.id = id;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_delete_category(IN id INT)
BEGIN
    DELETE FROM categories WHERE categories.id = id;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_update_category(IN id INT, IN pName VARCHAR(50), IN pDescription VARCHAR(255))
BEGIN
    UPDATE categories
    SET name = pName , description = pDescription
    WHERE categories.id = id;
END //
DELIMITER ;

