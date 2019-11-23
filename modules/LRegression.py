from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression


class LR:
    def __init__(self, obj):
        self.obj = obj

    def run(self, scaled=False):
        xtrain = self.obj.X_train
        ytrain = self.obj.y_train
        xtest = self.obj.X_test
        ytest = self.obj.y_test

        if scaled is True:
            xtrain = self.obj.X_train_scaled
            ytrain = self.obj.y_train_scaled
            xtest = self.obj.X_test_scaled
            ytest= self.obj.y_test_scaled

        reg = LinearRegression().fit(xtrain, ytrain)
        self.obj.coef_ = reg.coef_
        self.obj.intercept_ = reg.intercept_
        self.obj.lr_pred = reg.predict(xtest)
        self.obj.lr_mse = mean_squared_error(ytest, self.obj.lr_pred)
