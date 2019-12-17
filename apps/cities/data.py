import pandas as pd
from pandas import DataFrame

def read_csv_file(file, columns, separator, header):
    return pd.read_csv(file, names=columns, sep=separator, header=header, low_memory=False)

def sort_data_by_column(data, column):
    return data.sort_values(column, ascending=False)

def select_data_range(data, range):
    return data.head(range)

def narrow_data_column(data, columns):
    return DataFrame(data, columns=columns)

def show_first_ten_data_in_graph(cities, x, y, kind):
    return cities.head(10).plot(x=x, y=y, kind=kind)

def merge_data(cities, schools, column):
    return pd.merge(cities, schools, on=column)