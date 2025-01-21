import pandas as pd

def update_stock(data, product_id, quantity_sold):
    if product_id in data.index:
        data.loc[product_id, 'stock'] -= quantity_sold
        if data.loc[product_id, 'stock'] < 0:
            print(f"Stock for {product_id} is below zero!")
        return data
    else:
        print("Product not found!")
        return data

def add_product(data, product_id, product_name, initial_stock):
    data.loc[product_id] = [product_name, initial_stock]
    return data
