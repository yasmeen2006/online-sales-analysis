#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd         
import numpy as np          
import matplotlib.pyplot as plt  
import seaborn as sns     

# Reading the Dataset
df = pd.read_csv("online_sales_dataset.csv")

# Display the First 5 Rows
print("🔹 Head:")
print(df.head())


# In[6]:


import pandas as pd         # for data manipulation and analysis
import numpy as np          # for numerical operations
import matplotlib.pyplot as plt  # for data visualization
import seaborn as sns       # for enhanced data visualization

#  Reading the Dataset
df = pd.read_csv("online_sales_dataset.csv")

print("\n🔹 Tail:")
print(df.tail())


# In[8]:


import pandas as pd         # for data manipulation and analysis
import numpy as np          # for numerical operations
import matplotlib.pyplot as plt  # for data visualization
import seaborn as sns       # for enhanced data visualization

# Reading the Dataset
df = pd.read_csv("online_sales_dataset.csv")

print("\n🔹 Size:")
print(df.size)


# In[10]:


import pandas as pd         # for data manipulation and analysis
import numpy as np          # for numerical operations
import matplotlib.pyplot as plt  # for data visualization
import seaborn as sns       # for enhanced data visualization

#  Reading the Dataset
df = pd.read_csv("online_sales_dataset.csv")

print("\n🔹 Shape:")
print(df.shape)


# In[12]:


import pandas as pd         # for data manipulation and analysis
import numpy as np          # for numerical operations
import matplotlib.pyplot as plt  # for data visualization
import seaborn as sns       # for enhanced data visualization

#  Reading the Dataset
df = pd.read_csv("online_sales_dataset.csv")

print("\n🔹 Columns:")
print(df.columns.tolist())


# In[14]:


import pandas as pd         # for data manipulation and analysis
import numpy as np          # for numerical operations
import matplotlib.pyplot as plt  # for data visualization
import seaborn as sns       # for enhanced data visualization

#  Reading the Dataset
df = pd.read_csv("online_sales_dataset.csv")

print("\n🔹 Info:")
print(df.info())


# In[16]:


import pandas as pd         # for data manipulation and analysis
import numpy as np          # for numerical operations
import matplotlib.pyplot as plt  # for data visualization
import seaborn as sns       # for enhanced data visualization

#  Reading the Dataset
df = pd.read_csv("online_sales_dataset.csv")

print("\n🔹 Describe:")
print(df.describe())


# In[18]:


import pandas as pd         # for data manipulation and analysis
import numpy as np          # for numerical operations
import matplotlib.pyplot as plt  # for data visualization
import seaborn as sns       # for enhanced data visualization

#  Reading the Dataset
df = pd.read_csv("online_sales_dataset.csv")

print("\n🔹 Describe (Include Object):")
print(df.describe(include='object'))


# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

purchased_df = pd.read_csv("online_sales_dataset.csv")  

category_purchase_df = purchased_df["Category"].value_counts().reset_index() 
category_purchase_df.columns = ["Category", "PurchaseCount"]

# Plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=category_purchase_df, x="Category", y="PurchaseCount", marker="o", linewidth=2.5, color='teal')
plt.title("Purchase Rate by Product Category (Line Graph)", fontsize=16)
plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Number of Purchases", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

purchased_df = pd.read_csv("online_sales_dataset.csv")  

# Plot a pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_purchase_df["PurchaseCount"], labels=category_purchase_df["Category"], autopct='%1.1f%%', 
        startangle=140, colors=sns.color_palette("viridis", len(category_purchase_df)))
plt.title("Purchase Distribution by Product Category (Pie Chart)", fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures the pie is circular
plt.show()


# In[42]:


import seaborn as sns
import matplotlib.pyplot as plt

purchased_df = pd.read_csv("online_sales_dataset.csv")  

# Group and count purchases by country using your dataset
country_purchase_counts = df["Country"].value_counts().reset_index() 
country_purchase_counts.columns = ["Country", "PurchaseCount"]

# Plot a pie chart of the top 10 countries
plt.figure(figsize=(8, 8))
plt.pie(country_purchase_counts["PurchaseCount"].head(10),
        labels=country_purchase_counts["Country"].head(10),
        autopct='%1.1f%%',
        startangle=140,
        colors=sns.color_palette("mako", 10))  # Nice blue-green color palette
plt.title("Purchase Frequency by Country (Top 10)", fontsize=16)
plt.axis('equal')  # Keeps the pie chart as a circle
plt.tight_layout()
plt.show()



# In[36]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("online_sales_dataset.csv")  

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Extract month
df['Month'] = df['InvoiceDate'].dt.to_period('M')

# Count number of months each CustomerID appeared in
customer_months = df.groupby('CustomerID')['Month'].nunique()

# Identify repeat customers (appeared in more than 1 month)
repeat_customers = customer_months[customer_months > 1].index #The .index part extracts the CustomerIDs

# Add flag for whether each record is from a repeat customer
df['IsRepeatCustomer'] = df['CustomerID'].isin(repeat_customers)

# Group by month and calculate repeat rate
monthly_repeat_rate = df.groupby('Month')['IsRepeatCustomer'].mean().reset_index()

# Convert Month back to timestamp for plotting
monthly_repeat_rate['Month'] = monthly_repeat_rate['Month'].dt.to_timestamp()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(monthly_repeat_rate['Month'], 
         monthly_repeat_rate['IsRepeatCustomer'], 
         marker='o', color='b', linestyle='-', linewidth=2)
plt.title("Monthly Repeat Customer Rate")
plt.xlabel("Month")
plt.ylabel("Repeat Customer Rate")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




# In[38]:


import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("online_sales_dataset.csv")  

# Categorize discount into levels
def categorize_discount(value):
    if value < 0.1:
        return 'Low'
    elif value < 0.3:
        return 'Medium'
    else:
        return 'High'

df['DiscountLevel'] = df['Discount'].apply(categorize_discount)

# Identify repeat customers
customer_counts = df['CustomerID'].value_counts()
repeat_customers = customer_counts[customer_counts > 1].index #The .index part extracts the CustomerIDs
df['IsRepeatCustomer'] = df['CustomerID'].isin(repeat_customers)

# Group by DiscountLevel and calculate repeat rate
repeat_rate_by_discount = df.groupby('DiscountLevel', observed=True)['IsRepeatCustomer'].mean().reset_index()

# Plotting
plt.figure(figsize=(8,6))
plt.bar(repeat_rate_by_discount['DiscountLevel'], 
        repeat_rate_by_discount['IsRepeatCustomer'], 
        color='green')
plt.xlabel("Discount Level")
plt.ylabel("Repeat Customer Rate")
plt.title("Repeat Customer Rate by Discount Level")
plt.tight_layout()
plt.show()


# In[44]:


import pandas as pd
import matplotlib.pyplot as plt

#Create a copy of the DataFrame
df_copy = df.copy()

#Create DiscountLevel based on Discount percentage
df_copy['DiscountLevel'] = pd.cut(df_copy['Discount'], #pd.cut() is used to categorize the Discount column into discrete intervals 
                                  bins=[-1, 0, 10, 25, 100],
                                  labels=['No Discount', 'Low', 'Medium', 'High'])

#Identify repeat customers (customers who appear more than once)
repeat_customers = df_copy['CustomerID'].value_counts()
repeat_ids = repeat_customers[repeat_customers > 1].index #The .index part extracts the CustomerIDs 
df_copy['IsRepeatCustomer'] = df_copy['CustomerID'].isin(repeat_ids)

# Group by DiscountLevel
repeat_rate_by_discount = df_copy.groupby('DiscountLevel', observed=True)['IsRepeatCustomer'].mean().reset_index()

#Sort by DiscountLevel
repeat_rate_sorted = repeat_rate_by_discount.sort_values('DiscountLevel')

# Plot
plt.figure(figsize=(8,6))
plt.plot(repeat_rate_sorted['DiscountLevel'], repeat_rate_sorted['IsRepeatCustomer'],
         marker='o', linestyle='-', color='purple')
plt.xlabel("Discount Level")
plt.ylabel("Customer Retention Rate")
plt.title("Trend: Discount Level vs Customer Retention")
plt.ylim(0, 1)
plt.grid(True)
plt.tight_layout()
plt.show()

