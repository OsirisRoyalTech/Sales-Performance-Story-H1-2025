import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Constants for synthetic data generation
regions = ["North America", "Europe", "Asia-Pacific", "South America"]
sales_reps = ["Jane Thompson", "Lars Mueller", "Aisha Rahman", "Carlos Mendoza", "Emily Zhang", "Noah Davis"]
products = ["Software Suite A", "Software Suite B", "Software Suite C", "Hardware Kit A", "Hardware Kit B", "Hardware Kit C"]
client_types = ["Enterprise", "SMB"]
start_date = datetime(2025, 1, 1)

# Generate 1000 rows
num_rows = 1000
data = []

for i in range(1001, 1001 + num_rows):
    date = start_date + timedelta(days=random.randint(0, 180))
    region = random.choice(regions)
    rep = random.choice(sales_reps)
    product = random.choice(products)
    units_sold = random.randint(20, 250)
    unit_price = random.randint(150, 600)
    total_revenue = units_sold * unit_price
    client_type = random.choice(client_types)
    quarter = f"Q{((date.month - 1) // 3) + 1}"

    data.append([
        i, date.strftime('%Y-%m-%d'), region, rep, product,
        units_sold, unit_price, total_revenue, client_type, quarter
    ])

# Create DataFrame
columns = ["Order ID", "Date", "Region", "Sales Rep", "Product",
           "Units Sold", "Unit Price ($)", "Total Revenue ($)", "Client Type", "Quarter"]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("company_sales_data.csv", index=False)
