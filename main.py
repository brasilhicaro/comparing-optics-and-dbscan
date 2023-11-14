from dbscan import Dbscan
import pandas as pd
from hdbscan import Hdbscan
from optics import Optics
import matplotlib.pyplot as plt

if __name__ == '__main__':
    dbscan = Dbscan()
    optics = Optics()
    hdbscan = Hdbscan()
    
    # Tempo para o DBSCAN
    horario_inicial = pd.Timestamp.now()
    df_dbscan = dbscan.generate_csv()
    horario_final = pd.Timestamp.now()
    print(f"tempo dbscan: {horario_final - horario_inicial}")
    df_dbscan = pd.read_csv('./data/dbscan.csv')
    print(f"dbscan: {dbscan.count_clusters()}")
    
    # Tempo para o OPTICS
    horario_inicial = pd.Timestamp.now()
    df_optics = optics.generate_csv()
    horario_final = pd.Timestamp.now()
    print(f"tempo optics: {horario_final - horario_inicial}")
    df_optics = pd.read_csv('./data/optics.csv')
    print(f'optics: {optics.count_clusters()}')
    
    # Tempo para o HDBSCAN
    horario_inicial = pd.Timestamp.now()
    df_hdbscan = hdbscan.generate_csv()
    horario_final = pd.Timestamp.now()
    print(f"tempo hdbscan: {horario_final - horario_inicial}")
    df_hdbscan = pd.read_csv('./data/hdbscan.csv')
    print(f'hdbscan: {hdbscan.count_clusters()}')
    
    # Salvando os gráficos
    plt.scatter(df_dbscan['latitude'], df_dbscan['longitude'], c=df_dbscan['cluster'], cmap='Paired')
    plt.savefig('./imgs/dbscan.png')
    
    plt.scatter(df_optics['latitude'], df_optics['longitude'], c=df_optics['cluster'], cmap='Paired')
    plt.savefig('./imgs/optics.png')
    
    plt.scatter(df_hdbscan['latitude'], df_hdbscan['longitude'], c=df_hdbscan['cluster'], cmap='Paired')
    plt.savefig('./imgs/hdbscan.png')
