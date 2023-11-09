from dbscan import Dbscan
import pandas as pd
from hdbscan import Hdbscan
from optics import Optics
import matplotlib.pyplot as plt

if __name__ == '__main__':
    dbscan = Dbscan()
    optics = Optics()
    hdbscan = Hdbscan()
    
    df_dbscan = dbscan.generate_csv()
    df_dbscan = pd.read_csv('./data/dbscan.csv')
    print(f"dbscan: {dbscan.count_clusters()}")
    
    df_optics = optics.generate_csv()
    df_optics = pd.read_csv('./data/optics.csv')
    print(f'optics: {optics.count_clusters()}')
    
    df_hdbscan = hdbscan.generate_csv()
    df_hdbscan = pd.read_csv('./data/hdbscan.csv')
    print(f'hdbscan: {hdbscan.count_clusters()}')
    
    plt.scatter(df_dbscan['latitude'], df_dbscan['longitude'], c=df_dbscan['cluster'], cmap='Paired')
    plt.savefig('./imgs/dbscan.png')
    
    plt.scatter(df_optics['latitude'], df_optics['longitude'], c=df_optics['cluster'], cmap='Paired')
    plt.savefig('./imgs/optics.png')
    
    plt.scatter(df_hdbscan['latitude'], df_hdbscan['longitude'], c=df_hdbscan['cluster'], cmap='Paired')
    plt.savefig('./imgs/hdbscan.png')
    
