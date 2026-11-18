-- 1. Consultar todos os pagamentos
SELECT *
FROM transactions
ORDER BY transaction_id;

-- 2. Contar o total de pagamentos
SELECT COUNT(*) AS total_pagamentos
FROM transactions;

-- 3. Identificar pagamentos com valor elevado
SELECT *
FROM transactions
WHERE amount >= 1000
ORDER BY amount DESC;

-- 4. Calcular o valor total dos pagamentos
SELECT SUM(amount) AS valor_total
FROM transactions;

-- 5. Quantidade de pagamentos por status
SELECT status, COUNT(*) AS quantidade
FROM transactions
GROUP BY status;

-- 6. Valor total por cartão
SELECT card_id, SUM(amount) AS total_por_cartao
FROM transactions
GROUP BY card_id
ORDER BY total_por_cartao DESC;