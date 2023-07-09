import pandas as pd
from src.dataset.schema import BASE_SCHEMA
from src.utils.logger import configure_logger

logger = configure_logger(__name__)

def load_df_from_csv(csv_path: str) -> pd.DataFrame:
    logger.info(f"Loading data from {csv_path}")

    df = pd.read_csv(csv_path)
    df = BASE_SCHEMA.validate(df)
    return df

def save_df_to_csv(df: pd.DataFrame, csv_path: str):
    logger.info(f"Saving data to {csv_path}")
    df.to_csv(csv_path, index=False)
    

if __name__ == "__main__":
    
    df = load_df_from_csv("../../master_data/item_sales_records_2017_2021.csv")
    print(df.head())


# print(logger)