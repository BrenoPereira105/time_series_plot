import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

#here we choose the style for the plot 
matplotlib.style.use('ggplot')

# Import as Dataframe
df = pd.read_csv("covid_data.csv")

#plotting total_cases
df.iloc[2507:2810].plot(x='date', y='total_cases', figsize=(10,5))
plt.title('Australia Covid Total Cases')
plt.show()

