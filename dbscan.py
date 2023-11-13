import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import haversine as hs


class Dbscan:

    __data_firms: pd.DataFrame
    __distance: float = 0.5 / 6371.0088


    def __init__(self)->None:
        self.__data_firms = pd.DataFrame(pd.read_csv(
            'SUOMI_VIIRS_C2_South_America_24h.csv'))
        
    def get_data_firms(self)->pd.DataFrame:
        return self.__data_firms
    
    def __get_results__(self)->pd.DataFrame:
        df: pd.DataFrame = pd.DataFrame(self.__data_firms, columns=['latitude', 'longitude'])

        df = df.dropna()

        dbscan = DBSCAN(
                    eps=self.__distance,
                    min_samples=1,
                    algorithm='ball_tree',
                    metric='haversine'
                ).fit(np.radians(df))
        clusters_labels = dbscan.labels_
        df['cluster'] = clusters_labels
        distances = []
        for i in range(len(df['cluster']) + 1):
            for j in range(len(df['cluster']) + 1):
                if df['cluster'][i] == df['cluster'][j] and (df['latitude'][i] != df['latitude'][j] or df['longitude'][i] != df['longitude'][j]):
                    distancia = self.calculate_distance(
                        df['latitude'][i],
                        df['longitude'][i],
                        df['latitude'][j],
                        df['longitude'][j]
                    )
                    distances.append(distancia)
                    print(distancia)
        print(len(distances))
        df['distance'] = distances
        distances.clear()
        return df
    
    def count_clusters(self)->int:
        df = self.__get_results__()
        return len(df['cluster'].unique()) - 1
    
    def generate_csv(self)->None:
        df = self.__get_results__()
        df.to_csv('./data/dbscan.csv', index=False)
        
    def calculate_distance(self, lat1: float, lon1: float, lat2: float, lon2: float)->float:
        return hs.haversine((lat1, lon1), (lat2, lon2))