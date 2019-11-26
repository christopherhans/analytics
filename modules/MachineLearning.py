import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


class ML:
    def __init__(self, obj):
        self.obj = obj

    def one_hot_encoding(self, columns, drop_first):
        self.obj.df = pd.get_dummies(data=self.obj.df, columns=columns, drop_first=drop_first)

    def train_test(self, y, ratio, state):
        X = self.obj.df.drop(columns=[y])
        y = self.obj.df[y].values
        self.obj.X_train, self.obj.X_test, self.obj.y_train, self.obj.y_test = train_test_split(X, y, test_size=ratio,
                                                                                                random_state=state)
        print(self.obj.X_train)

    def scaler(self):
        min_max_scaler = preprocessing.MinMaxScaler()
        if len(self.obj.df.columns) <= 2:
            self.obj.X_train_scaled = min_max_scaler.fit_transform(self.obj.X_train.to_numpy().reshape(-1,1))
            self.obj.X_test_scaled = min_max_scaler.fit_transform(self.obj.X_test.to_numpy().reshape(-1,1))
        else:
            self.obj.X_train_scaled = min_max_scaler.fit_transform(self.obj.X_train)
            self.obj.X_test_scaled = min_max_scaler.fit_transform(self.obj.X_test)
        self.obj.y_train_scaled = min_max_scaler.fit_transform(self.obj.y_train.reshape(-1, 1))
        self.obj.y_test_scaled = min_max_scaler.fit_transform(self.obj.y_test.reshape(-1, 1))
