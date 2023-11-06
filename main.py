from dbscan import Dbscan
import pandas as pd
from optics import Optics

if __name__ == '__main__':
    dbscan = Dbscan()
    optics = Optics()
    df_dbscan = dbscan.generate_csv()
    df_optics = optics.generate_csv()

