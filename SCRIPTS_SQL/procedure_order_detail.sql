DELIMITER //
CREATE PROCEDURE sp_create_orders_detail(IN pOrder_id INT, IN pProduct_id INT, pQuantity DECIMAL,pTotal Decimal)
BEGIN
    INSERT INTO purchase_order_detail (purchase_order_id, product_id, quantity,total,created_at)
    VALUES (pOrder_id,pProduct_id,pQuantity,pTotal,CURRENT_TIMESTAMP);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_show_order_detail(IN id INT)
BEGIN
	 SELECT oDetail.id, prd.name, prd.description,
			cat.name, cat.description,
			oDetail.quantity, oDetail.total, 
			Orders.id as ID_ORDER, Orders.date, Orders.total,
			prov.name as provider_name,prov.full_address as provider_address
	FROM purchase_order_detail oDetail
	INNER JOIN (
		SELECT Orders.id, Orders.date, Orders.total, Orders.provider_id
		FROM purchase_orders Orders
	)Orders ON oDetail.purchase_order_id = Orders.id
	INNER JOIN (
		SELECT prov.id, prov.name, prov.full_address
		FROM providers prov
	)prov ON Orders.provider_id = prov.id
	INNER JOIN (
		SELECT prd.id, prd.name, prd.description, prd.category_id
		FROM products as prd 
	)prd  ON oDetail.product_id = prd.id
	INNER JOIN (
		SELECT cat.id, cat.name, cat.description
		FROM categories as cat
	)cat ON prd.category_id = cat.id
	WHERE oDetail.id = id;
END //
DELIMITER ;



DELIMITER //
CREATE PROCEDURE sp_index_order_detail()
BEGIN
	SELECT det.id, det.purchase_order_id as order_id, pd.name, det.quantity, det.total,det.created_at
    FROM purchase_order_detail det
    INNER JOIN store.products pd ON det.product_id = pd.id;
END //
DELIMITER ;



DELIMITER //
CREATE PROCEDURE sp_delete_order_detail(IN id INT)
BEGIN
    DELETE FROM purchase_order_detail WHERE purchase_order_detail.id = id;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_update_order_detail(IN id INT, pQuantity DECIMAL,pTotal Decimal)
BEGIN
    UPDATE purchase_order_detail
    SET quantity  = pQuantity, total = pTotal
    WHERE purchase_order_detail.id = id;
END //
DELIMITER ;
