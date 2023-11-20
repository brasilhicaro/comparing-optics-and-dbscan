import pandas as pd
import numpy as np
from sklearn.cluster import OPTICS
import haversine as hs

class Optics:
    __distance: float = 0.5 / 6371.0088
    __data_firms: pd.DataFrame

    def __init__(self)->None:
        self.__data_firms = pd.DataFrame(pd.read_csv(
            'SUOMI_VIIRS_C2_South_America_24h.csv'))
        
    def get_data_firms(self)->pd.DataFrame:
        return self.__data_firms
    
    def __get_results__(self)->pd.DataFrame:
        df = pd.DataFrame(self.__data_firms, columns=['latitude', 'longitude'])

        df = df.dropna()

        optics = OPTICS(
                    min_samples=2,
                    max_eps=self.__distance,
                    metric='haversine',
                    cluster_method='dbscan',
                    algorithm='ball_tree'
                ).fit(np.radians(df))
        clusters_labels = optics.labels_
        df['cluster'] = clusters_labels
        
        df['centroid_distance'] = 0.0
        for cluster in df['cluster'].unique():
            mask = df['cluster'] == cluster
            center_lat, center_lon = df.loc[mask, ['latitude', 'longitude']].mean()
            df.loc[mask, 'centroid_distance'] = [self.calculate_distance(center_lat, center_lon, lat, lon) \
                for lat, lon in zip(df.loc[mask, 'latitude'], df.loc[mask, 'longitude'])]

        return df
    def calculate_distance(self, lat1: float, lon1: float, lat2: float, lon2: float)->float:
        return hs.haversine((lat1, lon1), (lat2, lon2))
    
    def generate_csv(self)->None:
        df = self.__get_results__()
        df.to_csv('./data/optics.csv', index=False)
        
    def count_clusters(self)->int:
        df = self.__get_results__()
        return len(df['cluster'].unique()) - 1
    
    def get_clusters(self)->pd.DataFrame:
        df = self.__get_results__()
        return df['cluster'].unique()
    
    def get_clusters_count(self)->pd.DataFrame:
        df = self.__get_results__()
        return df['cluster'].value_counts()
