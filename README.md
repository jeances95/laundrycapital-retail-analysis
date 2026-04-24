# laundrycapital-retail-analysis
End-to-end retail analytics project for Laundry Capital, implementing an ETL pipeline that ingests data from Excel files, performs data cleaning and transformation using Python, loads structured data into SQL Server, and connects to Power BI for interactive dashboards and business insights.

## 🔄 Data Pipeline
Excel → Python (ETL) → SQL Server → Power BI

## 📊 Data Model
Star schema with fact_sales and dimension tables

## 🧠 Key Insights
- Most profitable service
- Top performing stores
- Revenue trends

## 🛠️ Tools Used
Python, SQL Server, Power BI

## 🔄 Data Pipeline

![Pipeline](docs/pipeline.png)

## 📈 Dashboard

![Dashboard](docs/dashboard1.png)
![Dashboard](docs/dashboard2.png)

## 💡 Key Insights

- Self Service is the top-performing service, generating approximately $0.50M in revenue, outperforming both Drop-Off and Pick-Up & Delivery services.

- Revenue remains relatively stable throughout 2026, fluctuating between ~$100K and ~$122K monthly, with noticeable peaks around May and October.

- Store performance is fairly concentrated, with the top 5 stores (e.g., Hartford, Worcester, Cleveland) each generating over $42K, indicating consistent high performers across locations.

- Average revenue per store is ~$40.85K and per customer ~$4.36K, showing a balanced distribution of revenue across both locations and customer base.

- Customer activity is strong, with an average of 48 transactions per customer, suggesting a mix of recurring and loyal customers.

- Geographic distribution shows revenue spread across multiple cities, with no single city overwhelmingly dominating, indicating a diversified market presence. 

- Given the strong performance of Self Service, expanding capacity or optimizing pricing for this service could further increase overall revenue.