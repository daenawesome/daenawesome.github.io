
-- Q1
INSERT INTO clients 
    (clientFirstname, clientLastname, clientEmail, clientPassword, comment)
VALUES 
    ('Tony', 'Stark', 'tony@starkent.com', 'Iam1ronM@n', '"I am the real Ironman"')

-- Q2
UPDATE 
    clients 
SET 
    clientLevel = 3 
WHERE 
    clientFirstname = 'Tony'

-- Q3
UPDATE 
    inventory 
SET 
    invDescription = replace(invDescription, 'small interiors', 'spacious interior')
WHERE 
    invId = 12

-- Q4
SELECT 
    invModel 
FROM 
    inventory i
INNER JOIN carclassification c ON i.classificationId = c.classificationId
WHERE i.classificationId = 1;

-- Q5
DELETE 
FROM 
    inventory 
WHERE 
    invModel = 'Wrangler'

-- Q6
UPDATE 
    inventory 
SET 
    invImage = CONCAT("/phpmotors", invImage), 
    invThumbnail = CONCAT("/phpmotors", invThumbnail)