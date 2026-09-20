import pandas as pd
import numpy as np

# Read Flipkart dataset
df = pd.read_csv(
    "marketing_sample_for_flipkart_com-ecommerce__20191101_20191130__15k_data.csv",
    engine="python",
    on_bad_lines="skip"
)


print("Dataset Loaded Successfully!")
print(df.head())
print(df.shape)
print(df.columns)

#checking missing values
print("/n Missing Values Before Cleaning:")
print(df.isnull().sum())



# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing Product Description
df["Product Description"] = df["Product Description"].fillna("No Description Available")

# Fill missing Quantity Or Pack Size
df["Quantity Or Pack Size"] = df["Quantity Or Pack Size"].fillna("Not Mentioned")

# Fill missing Offers
df["Offers"] = df["Offers"].fillna("No Offer")

# Fill missing Combo Offers
df["Combo Offers"] = df["Combo Offers"].fillna("No Combo Offer")

# Fill missing Image URL
df["Image Url"] = df["Image Url"].fillna("No Image")

print("\nData Cleaning Completed Successfully!")
print("New Shape:", df.shape)

df["Mrp"] = df["Mrp"].astype(str).str.replace(",", "")
df["Price"] = df["Price"].astype(str).str.replace(",", "")

df["Mrp"] = pd.to_numeric(df["Mrp"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Calculate Discount Amount
df["Discount Amount"] = df["Mrp"] - df["Price"]

# Calculate Discount Percentage
df["Discount Percentage"] = (
    (df["Discount Amount"] / df["Mrp"]) * 100
).round(2)

print("\nDiscount Columns Created Successfully!")
print(df[["Product Title", "Mrp", "Price","Discount Amount", "Discount Percentage"]].head())


df. to_csv("flipkart_cleaned.csv",index=False)




