def process_property_type(df):
    property_count = df.property_type.value_counts().to_dict()
    avg = df.price.mean()
    avg_prices = dict()
    for i in property_count.keys():
        sum_price = 0
        for p in df.price[df['property_type'] == i]:
            sum_price = sum_price + p
        avg_prices[i] = sum_price / len(df.price[df['property_type'] == i])

    def categorize_by_avg_price(df, avg_price, avgp):
        very_low = ['very_low']
        low = ['low']
        high = ['high']
        very_high = ['very_high']
        categories = [very_low, low, high, very_high]
        for i in avg_price:
            if avg_price[i] < (avgp / 2):
                very_low.append(i)
            elif avg_price[i] < avgp:
                low.append(i)
            elif avg_price[i] > (avgp * 1.5):
                very_high.append(i)
            elif avg_price[i] > avgp:
                high.append(i)
        for d in df['property_type']:
            for c in categories:
                if d in c:
                    df['property_type'][df['property_type'] == d] = c[0]
        return df

    df = categorize_by_avg_price(df, avg_prices, avg)

    return df
