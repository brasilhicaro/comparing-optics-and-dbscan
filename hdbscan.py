import pandas as pd
import numpy as np
from sklearn.cluster import HDBSCAN

class Hdbscan:
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

        hdbscan = HDBSCAN(
                    min_cluster_size=2,
                    min_samples=1,
                    cluster_selection_epsilon=self.__distance,
                    metric='haversine',
                    algorithm='balltree'
                ).fit(np.radians(df))
        clusters_labels = hdbscan.labels_
        df['cluster'] = clusters_labels
        return df
    
    def count_clusters(self)->int:
        df = self.__get_results__()
        return len(df['cluster'].unique()) - 1
    
    def generate_csv(self)->None:
        df = self.__get_results__()
        df.to_csv('./data/hdbscan.csv', index=False)
    