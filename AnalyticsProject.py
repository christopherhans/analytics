import os
import pandas as pd
from classes.Data import Data
from modules.DataCleaning import DataCleaning
from modules.MachineLearning import ML
from modules.KNN import KNN
from modules.LRegression import LR
from methods.report import report
from methods.print_debug import print_debug


class AnalyticsProject:

    def __init__(self):
        print_debug('init')
        self.inv = os.environ['INVENTORY']
        self.report = os.environ['REPORT']

    def run(self):
        print_debug('run')
        # Import dataframe from file.
        print_debug(self.inv)
        df = pd.read_csv('~/studies/analytics/analytics/bin/activate')
        # Initialize data object (data == the dataframe, which we wanna use for further testing).
        print_debug('Scope:')
        print_debug(os.environ['SCOPE'])
        data = Data(df[['price', 'beds', 'bedrooms', 'room_type']])

        # Some debug output
        print_debug(data.df.head())
        print_debug('Before cleaning: ')
        print_debug(data.df.shape)

        # Some cleaning steps.
        # You can remove additional columns by running the remove_custom function.
        data_cleaning = DataCleaning(data)
        data_cleaning.remove_static_columns()
        data_cleaning.remove_nan()
        data_cleaning.price_to_float()
        data_cleaning.remove_outlier(['price', 'beds', 'bedrooms'])

        # some debug output
        print_debug('After cleaning: ')
        print_debug(data.df.shape)
        print_debug(data.df.isna().any())

        # Preprocess dataframe for ML scenarios.
        data_ml = ML(data)
        data_ml.one_hot_encoding(columns=['room_type'], drop_first=True)
        data_ml.train_test(y='price', ratio=0.33, state=42)
        data_ml.scaler()

        # Run k-Nearest-Neighbor.
        # You can specify the amount of neighbors and whether you want to use scaled train/test data.
        data_knn = KNN(data)
        data_knn.run(neighbors=1, scaled=True)

        # Run Linear Regression. You can specify whether you want to use scaled train/test data.
        # If you want, you can also set a specific feature.
        data_lr = LR(data)
        data_lr.run(scaled=True)

        # Print a basic report for the final results.
        if self.report == '1':
            report(data)

        print_debug('Finished.')
