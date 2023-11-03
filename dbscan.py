import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN


class Dbscan:

    __data_firms: pd.DataFrame
    __distance: float = 0.5 / 6371.0088


    def __init__(self):
        self.__data_firms = pd.read_csv('SUOMI_VIIRS_C2_South_America_24h.csv')
        
    def get_data_firms(self):
        return self.__data_firms
    
    def get_results(self):
        df = pd.DataFrame(self.__data_firms, columns=['latitude', 'longitude'])

        df = df.dropna()

        dbscan = DBSCAN(
                    eps== self.__distance,
                    min_samples=1,
                    algorithm='ball_tree',
                    metric='haversine'
                ).fit(np.radians(df))
        clusters_labels = dbscan.labels_
        df['cluster'] = clusters_labels
        return df