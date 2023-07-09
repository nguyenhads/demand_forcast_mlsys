from datetime import datetime
from typing import Optional

import pandas as pd
from src.dataset.data_manager import load_df_from_csv
from src.dataset.schema import BASE_SCHEMA

class DataReTriver:
    def __init__(self):
        pass

    def retrieve_data(
            self, 
            file_path: str,
            date_from: Optional[datetime] = None,
            date_to: Optional[datetime] = None,
            item: str = "ALL",
            store: str = "ALL"
            ) -> pd.DataFrame:
        
        raw_df = load_df_from_csv(csv_path=file_path)
        raw_df["date"] = pd.to_datetime(raw_df["date"]).dt.date

        if date_from is not None:
            raw_df = raw_df[raw_df["date"] >= date_from]
        if date_to is not None:
            raw_df = raw_df[raw_df["date"] <= date_to]
        
        if item is not None and item!= "ALL":
            raw_df = raw_df[raw_df["item"] == item]
        if store is not None and store!= "ALL":
            raw_df = raw_df[raw_df["store"] == store]

        raw_df = BASE_SCHEMA.validate(raw_df)

        return raw_df
        
if __name__ == '__main__':
    
    # print(BASE_SCHEMA)
    csv_path = "../../data/data/item_sales_records_train_2020_52.csv"
    date_from = pd.to_datetime("2017-01-01")
    date_to = pd.to_datetime("2020-12-13")

    test_df = DataReTriver().retrieve_data(
        file_path=csv_path,
        date_from=date_from,
        date_to=date_to,
        )
    
    print(test_df.head())

