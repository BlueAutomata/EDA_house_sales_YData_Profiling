import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('House_sales.csv', sep=";")
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("house_sales_report.html")