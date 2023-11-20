import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import haversine as hs

class Dbscan:
    __data_firms: pd.DataFrame
    __distance: float = 0.5 / 6371.0088

    def __init__(self) -> None:
        self.__data_firms = pd.DataFrame(pd.read_csv('SUOMI_VIIRS_C2_South_America_24h.csv'))

    def get_data_firms(self) -> pd.DataFrame:
        return self.__data_firms

    def __get_results__(self) -> pd.DataFrame:
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

        df['centroid_distance'] = 0.0
        for cluster in df['cluster'].unique():
            mask = df['cluster'] == cluster
            center_lat, center_lon = df.loc[mask, ['latitude', 'longitude']].mean()
            df.loc[mask, 'centroid_distance'] = [self.calculate_distance(center_lat, center_lon, lat, lon) \
                for lat, lon in zip(df.loc[mask, 'latitude'], df.loc[mask, 'longitude'])]

        return df

    def count_clusters(self) -> int:
        df = self.__get_results__()
        return len(df['cluster'].unique())

    def generate_csv(self) -> None:
        df = self.__get_results__()
        df.to_csv('./data/dbscan.csv', index=False)

    def calculate_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        return hs.haversine((lat1, lon1), (lat2, lon2))
