from methods.price_to_float import price_to_float
from methods.remove_outlier_by_column import remove_outlier_from_column


class DataCleaning:
    def __init__(self, obj):
        self.obj = obj

    def remove_static_columns(self):
        for column in self.obj.df.columns:
            if self.obj.df[column].nunique() <= 1:
                self.obj.df = self.obj.df.drop(columns=column)
        print(self.obj.df.shape)

    def remove_custom(self, columns):
        self.obj.df = self.obj.df.drop(columns=columns)
        print(self.obj.df.shape)

    def price_to_float(self):
        self.obj.df['price'] = self.obj.df['price'].map(price_to_float)

    def remove_nan(self):
        self.obj.df.dropna(inplace=True)
        print(self.obj.df.shape)

    def numeric(self):
        check = lambda a: type(a) == str and a.isnumeric()
        for x in self.obj.df.columns:
            if self.obj.df[x].map(check).any() is not False:
                self.obj.df[x] = self.obj.df[x].map(float)

    def remove_outlier(self):
        number = lambda a: isinstance(a, (int, float)) and not isinstance(a, (bool, str))
        for x in self.obj.df.columns:
            if self.obj.df[x].map(number).any() is not False:
                self.obj.df = remove_outlier_from_column(self.obj.df, x)
