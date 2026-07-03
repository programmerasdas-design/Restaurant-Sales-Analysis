import pandas as pd 
import matplotlib.pyplot as plt 
data=pd.read_csv("Restaurant Sales Analysis.csv")
print(data.tail())
print(data.head())
plt.figure()
plt.plot(data["Day"],data["Revenue"],color=("purple"),marker="o")
plt.title("Total Revenue Over Time")
plt.xlabel("Days")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()
plt.figure()
products=["Burger","Pizza","Pasta","Cola","Coffee","Cake"]
data1=[data[data["Item"]=="Burger"]["Revenue"].sum(),
    data[data["Item"]=="Pizza"]["Revenue"].sum(),
    data[data["Item"]=="Pasta"]["Revenue"].sum(),
    data[data["Item"]=="Cola"]["Revenue"].sum(),
    data[data["Item"]=="Coffee"]["Revenue"].sum(),
    data[data["Item"]=="Cake"]["Revenue"].sum()]
plt.bar(products,data1,color=["black","Red","blue","green","skyblue","yellow"])
plt.title("Total Revenue by Product")
plt.xlabel("products")
plt.ylabel("Revenue")
plt.show()
plt.figure()
products=["Burger","Pizza","Pasta","Cola","Coffee","Cake"]
Quantity_sold=[data[data["Item"]=="Burger"]["Quantity_Sold"].sum(),
    data[data["Item"]=="Pizza"]["Quantity_Sold"].sum(),
    data[data["Item"]=="Pasta"]["Quantity_Sold"].sum(),
    data[data["Item"]=="Cola"]["Quantity_Sold"].sum(),
    data[data["Item"]=="Coffee"]["Quantity_Sold"].sum(),
    data[data["Item"]=="Cake"]["Quantity_Sold"].sum()]
plt.bar(products,Quantity_sold,color=["black","Red","blue","green","skyblue","yellow"])
plt.title("Total Quantity Sold by Product")
plt.xlabel("products")
plt.ylabel("Quantity sold")
plt.show()
plt.figure()
products=["Main Course","Beverages","Dessert"]
Quantity_sold=[data[data["Category"]=="Main Course"]["Revenue"].sum(),
    data[data["Category"]=="Beverages"]["Revenue"].sum(),
    data[data["Category"]=="Dessert"]["Revenue"].sum(),
]
plt.bar(products,Quantity_sold,color=["black","Red","green"])
plt.title("Total Revenue by Category")
plt.xlabel("Categories")
plt.ylabel("Revenue")
plt.show()
plt.figure()
plt.scatter(data["Price"],data["Quantity_Sold"],color=("red"))
plt.title("Price vs Quantity Sold Analysis")
plt.xlabel("Price")
plt.ylabel("Quantity sold")
plt.show()
