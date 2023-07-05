DELIMITER //
CREATE PROCEDURE sp_create_providers(IN pName VARCHAR(50), IN pFull_address VARCHAR(255))
BEGIN
    INSERT INTO providers (name, full_address, created_at)
    VALUES (pName, pFull_address,CURRENT_TIMESTAMP);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_index_providers()
BEGIN
	SELECT * FROM providers;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_show_provider(IN id INT)
BEGIN
	SELECT * FROM providers WHERE providers.id = id;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_delete_provider(IN id INT)
BEGIN
    DELETE FROM providers WHERE providers.id = id;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_update_provider(IN id INT, IN pName VARCHAR(50), IN pFull_address VARCHAR(255))
BEGIN
    UPDATE providers
    SET name = pName, full_address = pFull_address
    WHERE providers.id = id;
END //
DELIMITER ;