import pandas as pd
import matplotlib.pyplot as plt

def analyze_trends(data):
    sales_trends = data.groupby('month')['sales'].sum()
    sales_trends.plot(kind='bar')
    plt.title("Sales Trends")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.show()
