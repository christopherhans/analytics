class Data:
    def __init__(self, df):
        self.df = df
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.X_train_scaled = None
        self.X_test_scaled = None
        self.y_train_scaled = None
        self.y_test_scaled = None
        self.knn_pred = None
        self.knn_mse = None
        self.lr_pred = None
        self.lr_mse = None
        self.coef_ = None
        self.intercept_ = None
        self.used_features = None
