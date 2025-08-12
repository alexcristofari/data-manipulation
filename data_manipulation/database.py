# database.py

import numpy as np

def get_grouped_mean():
    # __define-ocg__ - Load and process iris data for grouped mean calculation
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris_data = np.genfromtxt(url, delimiter=',', dtype='object')
    
    sepal_width = iris_data[:, 1].astype(float)
    species = iris_data[:, 4]
    unique_species = np.unique(species)
    varOcg = []
    
    for sp in unique_species:
        varFiltersCg = (species == sp)
        mean_val = np.mean(sepal_width[varFiltersCg])
        varOcg.append([sp, mean_val])
    
    return varOcg

if __name__ == "__main__":
    grouped_mean = get_grouped_mean()
    for item in grouped_mean:
        print(item)