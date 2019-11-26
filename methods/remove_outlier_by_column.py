def remove_outlier_from_column(df, column):

    df[column] = df[column]._get_numeric_data()
    q1 = df[column].quantile(0.25)
    print(q1)
    q3 = df[column].quantile(0.75)
    print(q3)
    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    df = df.drop(df[df[column] < lower_bound].index)
    df = df.drop(df[df[column] > upper_bound].index)

    return df
