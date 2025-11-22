# Import package
import matplotlib.pyplot as plt
import seaborn as sns
from Step1_read_data import df

# Plot the data and name the variable(s) in x and/or y
file = sns.countplot(data=df, x='smoker', hue='sex')
file.set_xticklabels(file.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()

file = sns.histplot(data=df, x='bmi')
plt.xlabel('BMI')
plt.show() 

file = sns.boxplot(data=df, x='region', y='expenses')
plt.show()

file = sns.scatterplot(data=df, x='age', y='expenses')
plt.show()
