import os
import pandas as pd
from classes.Data import Data
from modules.DataCleaning import DataCleaning
from modules.MachineLearning import ML
from modules.KNN import KNN
from modules.LRegression import LR
from methods.report import report
from methods.print_debug import print_debug


def analytics_run(scope=None):
    print_debug('run')
    # Import dataframe from file.
    print_debug(os.environ['INVENTORY'])
    df = pd.read_csv(os.environ['INVENTORY'])
    # Initialize data object (data == the dataframe, which we wanna use for further testing).
    data = Data(df[scope])

    # Some debug output
    print_debug(data.df.head())
    print_debug('Before cleaning: ')
    print_debug(data.df.shape)

    # Some cleaning steps.
    # You can remove additional columns by running the remove_custom function.
    print_debug(data.df.head())
    data_cleaning = DataCleaning(data)
    data_cleaning.remove_static_columns()
    data_cleaning.remove_nan()
    data_cleaning.price_to_float()
    # data_cleaning.numeric()
    data_cleaning.remove_outlier()
    # data_cleaning.property_type_()

    # some debug output
    print_debug('After cleaning: ')
    # print_debug(data.df.shape)
    # print_debug(data.df.isna().any())

    print_debug(data.df.head())
    # Preprocess dataframe for ML scenarios.
    data_ml = ML(data)
    # data_ml.one_hot_encoding(columns=['property_type'], drop_first=True)
    data_ml.train_test(y='price', ratio=0.33, state=42)
    # data_ml.scaler()

    # Run k-Nearest-Neighbor.
    # You can specify the amount of neighbors and whether you want to use scaled train/test data.
    data_knn = KNN(data)
    data_knn.run(neighbors=1, scaled=False)

    # Run Linear Regression. You can specify whether you want to use scaled train/test data.
    # If you want, you can also set a specific feature.
    data_lr = LR(data)
    data_lr.run(scaled=False)

    # Print a basic report for the final results.
    if os.environ['REPORT'] == '1':
        report(data)

    print_debug('Finished.')
