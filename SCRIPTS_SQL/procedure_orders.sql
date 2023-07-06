DELIMITER //
CREATE PROCEDURE sp_create_orders(IN pProvider_id INT, IN pTotal DECIMAL)
BEGIN
    INSERT INTO store.purchase_orders (provider_id, date,total,created_at)
    VALUES (pProvider_id,CURRENT_DATE,pTotal,CURRENT_TIMESTAMP);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_index_orders()
BEGIN
	SELECT * FROM store.purchase_orders;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_show_order(IN id INT)
BEGIN
	SELECT ord.id, ord.provider_id,prov.name, prov.full_address,ord.date, ord.total, ord.created_at
    FROM store.purchase_orders ord
    INNER JOIN (
       SELECT prov.id, prov.name, prov.full_address
       FROM providers prov
    )prov  ON ord.provider_id = prov.id
    WHERE ord.id = id;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_delete_order(IN id INT)
BEGIN
    DELETE FROM store.purchase_orders WHERE purchase_orders.id = id;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_update_order(IN id INT, IN pProvider_id INT, IN pTotal DECIMAL)
BEGIN
    UPDATE store.purchase_orders
    SET provider_id  = pProvider_id, total = pTotal
    WHERE purchase_orders.id = id;
END //
DELIMITER ;