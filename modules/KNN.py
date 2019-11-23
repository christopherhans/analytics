from sklearn.neighbors import NearestNeighbors, KNeighborsRegressor
from sklearn.metrics import mean_squared_error


class KNN:
    def __init__(self, obj):
        self.obj = obj

    def run(self, neighbors, scaled=False):
        xtrain = self.obj.X_train
        ytrain = self.obj.y_train
        xtest = self.obj.X_test
        ytest = self.obj.y_test

        if scaled is True:
            xtrain = self.obj.X_train_scaled
            ytrain = self.obj.y_train_scaled
            xtest = self.obj.X_test_scaled
            ytest = self.obj.y_test_scaled

        knn = KNeighborsRegressor(n_neighbors=neighbors)
        knn.fit(xtrain, ytrain)
        self.obj.knn_pred = knn.predict(xtest)
        self.obj.knn_mse = mean_squared_error(ytest, self.obj.knn_pred)
