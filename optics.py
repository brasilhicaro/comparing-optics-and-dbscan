import pandas as pd
import numpy as np
from sklearn.cluster import OPTICS

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
                    min_samples=1.0,
                    max_eps=self.__distance,
                    metric='haversine'
                ).fit(np.radians(df))
        clusters_labels = optics.labels_
        df['cluster'] = clusters_labels
        return df
    
    def generate_csv(self)->None:
        df = self.__get_results__()
        df.to_csv('optics.csv', index=False)
    