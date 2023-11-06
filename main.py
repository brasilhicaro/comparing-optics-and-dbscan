from dbscan import Dbscan
import pandas as pd
from optics import Optics
import matplotlib.pyplot as plt

if __name__ == '__main__':
    dbscan = Dbscan()
    optics = Optics()
    df_dbscan = dbscan.generate_csv()
    df_dbscan = pd.read_csv('dbscan.csv')
    print(dbscan.count_clusters())
    df_optics = optics.generate_csv()
    df_optics = pd.read_csv('optics.csv')
    print(optics.count_clusters())
    
    plt.scatter(df_dbscan['latitude'], df_dbscan['longitude'], c=df_dbscan['cluster'], cmap='Paired')
    plt.show()    
    plt.scatter(df_optics['latitude'], df_optics['longitude'], c=df_optics['cluster'], cmap='Paired')
    plt.show()
    
    

