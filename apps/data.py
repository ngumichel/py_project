import pandas as pd
from pandas import DataFrame

def read_csv_file(data_file, columns, separator, header):
    return pd.read_csv(data_file, names=columns, sep=separator, header=header, low_memory=False)

def sort_data_by_column(data, column):
    return data.sort_values(column, ascending=False)

def select_data_range(data, range):
    return data.head(range)

def narrow_data_column(data, columns):
    return DataFrame(data, columns=columns)

def show_data_in_graph(data, range, x, y, kind):
    return data.head(range).plot(x=x, y=y, kind=kind)

def merge_data(cities, schools, column):
    return pd.merge(cities, schools, on=column)

def save_data_into_database(data, model):
    data_dict = data.to_dict('records')
    return model.insert_many(data_dict).execute()
    