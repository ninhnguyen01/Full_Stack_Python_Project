# import package
from urllib.request import urlretrieve

# retrieve file
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

urlretrieve(url,'winequality-white.csv')
