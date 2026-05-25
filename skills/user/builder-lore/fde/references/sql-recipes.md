# SQL Recipes
# Common patterns for FDE analytics and reporting work.
## Filter rows
```sql
SELECT id, name, email
FROM users
WHERE status = 'active'
  AND created_at > '2024-01-01';
```
## Join two tables
```sql
SELECT orders.id, users.name, orders.total
FROM orders
JOIN users ON orders.user_id = users.id
WHERE orders.status = 'completed';
```
## Aggregate (count, sum, average)
```sql
SELECT status, COUNT(*) AS count, SUM(total) AS revenue
FROM orders
GROUP BY status
ORDER BY count DESC;
```
## Find duplicates
```sql
SELECT email, COUNT(*) AS occurrences
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```
## Date filtering
```sql
-- Last 30 days
WHERE created_at >= NOW() - INTERVAL '30 days'
-- Specific month
WHERE DATE_TRUNC('month', created_at) = '2024-03-01'
-- Between dates
WHERE created_at BETWEEN '2024-01-01' AND '2024-03-31'
```
## CTE (readable multi-step query)
```sql
WITH active_users AS (
  SELECT id, name FROM users WHERE status = 'active'
),
their_orders AS (
  SELECT user_id, COUNT(*) AS order_count FROM orders GROUP BY user_id
)
SELECT active_users.name, their_orders.order_count
FROM active_users
JOIN their_orders ON active_users.id = their_orders.user_id;
```
## Window function (rank rows within a group)
```sql
SELECT
  name,
  total,
  ROW_NUMBER() OVER (PARTITION BY region ORDER BY total DESC) AS rank
FROM sales;
```
