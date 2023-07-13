-- script to create a table
-- must not fail if exists uses enum
CREATE TABLE IF NOT EXISTS `users` (`id` INT NOT NULL AUTO_INCREMENT, `email` VARCHAR(255) NOT NULL UNIQUE, `name` VARCHAR(255), `country` ENUM('US', 'CO', 'TN') DEFAULT 'US', PRIMARY KEY(`id`));
