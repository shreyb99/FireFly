# Importing Required Libraries
import nest_asyncio
import pandas as pd
import matplotlib.pyplot as plt

# Importing dataset
df = pd.read_csv(r'csv files to be input')
print(df.dtypes)

# Displaying Connection Strength
power = df['Power'].value_counts()
print(power)
df['Power'].value_counts().plot(kind='barh', figsize=(15, 10))

# Displaying Packets sent per Connection
packets = df[['packets']].value_counts()
print(packets)
df['packets'].value_counts().plot(kind='barh', figsize=(15, 10))

# Displaying Histogram of Dataset
plt.figure(figsize=(9, 9))
df.hist()
plt.show()
