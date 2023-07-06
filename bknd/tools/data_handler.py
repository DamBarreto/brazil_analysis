# https://www.bcb.gov.br/controleinflacao/historicotaxasjuros -> testar usar pandas.read_table

from abc import ABC, abstractmethod
from typing import Union, Dict, List
from pandas import DataFrame, Series


from . import extractor, transformer, loader

class DataHandler(ABC):
    """
    data: Dataframe | Series
    """
    data: Union[DataFrame, Series]

    def __init__(self):
        pass

    @abstractmethod
    def __load_data(self):
        pass


class WageDataHandle(DataHandler):
    pass

class BasicBasketDataHandler(DataHandler):
    pass



dframe = pd.read_csv("../../datasets/wage/wage.csv", sep=";")

def month_str_to_int(month)->int:
    dict_mount_str = {
        "Jan": 1,
        "Fev": 2,
        "Mar": 3,
        "Abr": 4,
        "Mai": 5,
        "Jun": 6,
        "Jul": 7,
        "Ago": 8,
        "Set": 9,
        "Out": 10,
        "Nov": 11,
        "Dez": 12
    }

    return dict_mount_str[month[0:3]]

dframe["month_#"] = dframe.month.apply(month_str_to_int)

dframe.sort_index(ascending=False)
