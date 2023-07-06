DELIMITER //
CREATE PROCEDURE sp_create_product(IN pName VARCHAR(50), IN pDescription VARCHAR(255), IN pCategory_id INT)
BEGIN
    INSERT INTO store.products (name, description,category_id,created_at)
    VALUES (pName, pDescription,pCategory_id,CURRENT_TIMESTAMP);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_index_product()
BEGIN
	SELECT pd.id, pd.name, pd.description, cat.name as category, pd.created_at
	FROM store.products pd
	INNER JOIN store.categories cat ON pd.category_id = cat.id;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_show_product(IN id INT)
BEGIN
	SELECT pd.id, pd.name, pd.description, cat.name as category, pd.created_at
	FROM store.products pd
	INNER JOIN store.categories cat ON pd.category_id = cat.id
    WHERE pd.id = id;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_delete_product(IN id INT)
BEGIN
    DELETE FROM store.products WHERE products.id = id;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_update_product(IN id INT, IN pName VARCHAR(50), IN pDescription VARCHAR(255),pCategory_id INT)
BEGIN
    UPDATE store.products
    SET name = pName , description = pDescription, category_id = pCategory_id
    WHERE products.id = id;
END //
DELIMITER ;