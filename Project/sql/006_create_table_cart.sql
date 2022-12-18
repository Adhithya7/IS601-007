CREATE TABLE
    IF NOT EXISTS IS601_S_Cart(
        id int AUTO_INCREMENT PRIMARY KEY,
        quantity int DEFAULT 0,
        unit_price float DEFAULT 99999,
        item_id int,
        user_id int,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        check (quantity >= 0),
        check (unit_price >= 0),
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id),
        FOREIGN KEY(item_id) REFERENCES IS601_S_Items(id),
        UNIQUE KEY (item_id, user_id)
    )