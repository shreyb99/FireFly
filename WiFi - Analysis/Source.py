# Importing Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
from OuiLookup import OuiLookup

# Loading dataset and performing basic data analysis
df = pd.read_csv(r'csv file input')  # 8288x11
print("Shape : ", df.shape, ", \nColmuns and Data Types - \n", df.dtypes)
print("NaN values in BSSID : ", df['BSSID'].isnull().sum())

# Retreiving Vendor for each BSSID using OuiLookup Package
for wmac in df['BSSID']:
    try:
        vendor = OuiLookup().query(wmac)
        print(vendor)
    except:
        print(wmac, " - Possibly Randomized MAC, Unknown")
        continue

# Displaying Different Privacy Standards Used
privacy = df['Privacy'].value_counts()
print(privacy)
df['Privacy'].value_counts().plot(kind='barh', figsize=(10, 10))

# Displaying Ciphers Used
cipher = df[['Cipher']].value_counts()
print(cipher)
df['Cipher'].value_counts().plot(kind='barh', figsize=(10, 10))

# Displaying Types of Wifi Authentication Used
auth = df[['Authentication']].value_counts()
print(auth)
df['Authentication'].value_counts().plot(kind='barh', figsize=(15, 10))

# Displaying Various Connection Speeds Observed
speed = df['Speed'].value_counts()
print(speed)
df['Speed'].value_counts().plot(kind='barh', figsize=(15, 10))

# Displaying Channels Detected
channel = df['channel'].value_counts()
print(channel)
df['channel'].value_counts().plot(kind='barh')

# Displaying Connection Strength Detected
power = df['Power'].value_counts()
print(power)
df['Power'].value_counts().plot(kind='barh', figsize=(15, 10))

# Displaying numbers of ID-Lengths used
id = df['ID-length'].value_counts()
print(id)
df['ID-length'].value_counts().plot(kind='barh', figsize=(15, 10))

# Displaying Number of Beacons Used
beacons = df['beacons'].value_counts()
print(beacons)
df['beacons'].value_counts().plot(kind='barh', figsize=(15, 10))

# Displaying Histogram of Dataset
plt.figure(figsize=(9, 9))
df.hist()
plt.show()
