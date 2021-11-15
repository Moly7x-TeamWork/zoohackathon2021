CREATE TABLE user (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username   VARCHAR(30),
    `password` VARCHAR(182)
)

CREATE TABLE groupReport (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    linkGroup VARCHAR(4096),
    summary TEXT,
    `status` ENUM('Pre-pending', 'Pending', 'True', 'False'),
    idUser INT UNSIGNED,
    reviewTime DATETIME,
    FOREIGN KEY (idUser) REFERENCES user(id)
)

CREATE TABLE dataML (
    idGroup INT UNSIGNED,
    linkUser VARCHAR(4096),
    linkFull VARCHAR(4096),
    `hash` NVARCHAR(256) UNIQUE,
    content TEXT,
    FOREIGN KEY (idGroup) REFERENCES groupReport(id)
)

select * from information_schema.tables

TRUNCATE TABLE dataML;
Select * from dataML;


TRUNCATE TABLE groupReport;

SELECT gr.id, gr.linkgroup, gr.status, user.username, gr.reviewTime
FROM groupReport gr
JOIN user ON user.id = gr.idUser;

SELECT gr.id, gr.linkgroup, gr.status, user.username, gr.reviewTime FROM groupReport gr JOIN user ON user.id = gr.idUser

SELECT dataML.linkUser, dataML.linkFull
FROM groupReport gr
JOIN dataML ON dataML.idGroup = gr.id
WHERE gr.id = 3 AND dataML.linkUser IS NOT NULL AND dataML.linkFull IS NOT NULL;