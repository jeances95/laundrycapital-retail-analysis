-- Revenue by service
SELECT 
    s.service_name,
    SUM(f.revenue) AS total_revenue
FROM fact_sales f
JOIN dim_services s ON f.service_id = s.service_id
GROUP BY s.service_name
ORDER BY total_revenue DESC;

-- Top 5 stores
SELECT TOP 5
    st.store_name,
    SUM(f.revenue) AS revenue
FROM fact_sales f
JOIN dim_stores st ON f.store_id = st.store_id
GROUP BY st.store_name
ORDER BY revenue DESC;