-- Query (consulta)
-- Comandos SQL para consulta
SELECT *
FROM produtos_produtos


-- Updates
UPDATE produtos_produtos
SET preco = 750
WHERE id = 4;

-- Insert
INSERT INTO produtos_produtos (id, nome, descricao, preco, quantidade)
VALUES (6, 'Bike Cinco', 'Descricao bike 5', 5, 5)

-- Delete
DELETE FROM produtos_produtos
where id = 6

select * from clientes_cliente
where nome = 'Maria'