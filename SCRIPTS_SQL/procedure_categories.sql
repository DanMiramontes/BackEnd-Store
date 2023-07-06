DELIMITER //
CREATE PROCEDURE sp_create_category(IN pName VARCHAR(50), IN pDescription VARCHAR(255))
BEGIN
    INSERT INTO store.categories (name, description,created_at)
    VALUES (pName, pDescription,CURRENT_TIMESTAMP);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_index_category()
BEGIN
    SELECT * FROM store.categories ;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_show_category(IN id INT)
BEGIN
    SELECT * FROM store.categories WHERE categories.id = id;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_delete_category(IN id INT)
BEGIN
    DELETE FROM store.categories WHERE categories.id = id;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_update_category(IN id INT, IN pName VARCHAR(50), IN pDescription VARCHAR(255))
BEGIN
    UPDATE store.categories
    SET name = pName , description = pDescription
    WHERE categories.id = id;
END //
DELIMITER ;

