USE flipkart_db;
SELECT COUNT(*) AS Toatl_products FROM flipkart_products;
SELECT `Product Title`, Brand, Mrp
FROM flipkart_products
ORDER BY Mrp DESC
LIMIT 10;
SELECT `Product Title`,
       `Discount Percentage`
FROM flipkart_products
ORDER BY `Discount Percentage` DESC
LIMIT 10;
SELECT `Product Title`, Price
FROM flipkart_products
WHERE Price > 5000;
SELECT Brand,
       ROUND(AVG(Price),2) AS Average_Price
FROM flipkart_products
GROUP BY Brand
ORDER BY Average_Price DESC;
SELECT Brand,
       COUNT(*) AS Total_Products
FROM flipkart_products
GROUP BY Brand
ORDER BY Total_Products DESC;
SELECT Brand,
       ROUND(AVG(`Discount Percentage`),2) AS Avg_Discount
FROM flipkart_products
GROUP BY Brand
ORDER BY Avg_Discount DESC;