import pandas as pd
import json

# Download from: https://tds-llm-analysis.s-anand.net/project2/orders.csv

# Read the CSV
df = pd.read_csv('orders.csv')

print("Original data:")
print(df)
print()

# Sort by order_date
df['order_date'] = pd.to_datetime(df['order_date'])
df = df.sort_values('order_date')

print("Sorted by order_date:")
print(df)
print()

# Calculate running total for each customer
df['running_total'] = df.groupby('customer_id')['amount'].cumsum()

print("With running totals:")
print(df[['order_id', 'customer_id', 'order_date', 'amount', 'running_total']])
print()

# Get the final (highest) running total for each customer
customer_totals = df.groupby('customer_id')['running_total'].last().reset_index()
customer_totals.columns = ['customer_id', 'total']

print("Final totals by customer:")
print(customer_totals)
print()

# Sort by total (highest first) and take top 3
top_3 = customer_totals.nlargest(3, 'total')

print("Top 3 customers by total:")
print(top_3)
print()

# Create JSON output in rank order
result = []
for idx, row in top_3.iterrows():
    result.append({
        "customer_id": row['customer_id'],
        "total": int(row['total'])
    })

json_output = json.dumps(result)

print("="*50)
print("ANSWER (JSON array):")
print(json_output)
print("="*50)