import os
import seaborn as sns
import matplotlib.pyplot as plt


def report(obj):
    print(obj.df)
    if 'KNN' in os.environ:
        print(f'KNN Neighbors: {obj.neighbors}')
        print(f'KNN Mean-Squared-Error: {obj.knn_mse}')
    if 'LINEAR_REGRESSION' in os.environ:
        print(f'Linear Regression Mean-Squared-Error: {obj.lr_mse}')
        print(f'Linear Regression: f(x) = {obj.coef_} * x + {obj.intercept_}')

        try:
            plt.figure(figsize=(20, 5))
            plt.scatter(obj.X_train['beds'].to_numpy().reshape(-1, 1), obj.y_train, color='black')
            plt.plot(obj.X_test['beds'].to_numpy().reshape(-1, 1), obj.lr_pred, color='blue', linewidth=3)
            plt.xlabel('Linear Regression')
            plt.xticks(())
            plt.yticks(())

            plt.show()
        except:
            pass
