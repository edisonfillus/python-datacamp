import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/gapminder.csv')

# Print the number of countries reported in 2015
print(df['2015'].count())

# Print the 5th and 95th percentiles
print(df.quantile([0.05, 0.95]))

# Generate a box plot
years = ['1800', '1850', '1900', '1950', '2000']
df[years].plot(kind='box')
plt.show()


quantiles = df.iloc[:,1:].quantile([0.05, 0.95])
quantiles = pd.pivot_table(quantiles, columns=['5%','95%'])
quantiles.index = pd.to_numeric(quantiles.index)
quantiles.plot()
plt.show()