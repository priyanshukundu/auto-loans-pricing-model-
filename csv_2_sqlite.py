import pandas as pd
import sqlite3

# Step 1: Load the CSV
df = pd.read_csv("credit_risk_dataset.csv")

# Step 2: Connect to SQLite (creates file if it doesn't exist)
conn = sqlite3.connect("credit_risk.db")

# Step 3: Export the DataFrame to SQLite
df.to_sql("credit_data", conn, if_exists="replace", index=False)

# Step 4: (Optional) Verify it worked
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM credit_data")
print("Total rows inserted:", cursor.fetchone()[0])

# Step 5: Close connection
conn.close()
