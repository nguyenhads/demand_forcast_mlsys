from datetime import datetime

from pandera import Check, Column, DataFrameSchema, Index

STORES = [
    "nagoya",
    "shinjuku",
    "osaka",
    "kobe",
    "sendai",
    "chiba",
    "morioka",
    "ginza",
    "yokohama",
    "ueno",
]

ITEMS = [
    "fruit_juice",
    "apple_juice",
    "orange_juice",
    "sports_drink",
    "coffee",
    "milk",
    "mineral_water",
    "sparkling_water",
    "soy_milk",
    "beer",
]

ITEM_PRICES = {
    "fruit_juice": 150,
    "apple_juice": 120,
    "orange_juice": 120,
    "sports_drink": 130,
    "coffee": 200,
    "milk": 130,
    "mineral_water": 100,
    "sparkling_water": 120,
    "soy_milk": 120,
    "beer": 200,
}

WEEKS = [i for i in range(1, 54, 1)]

MONTHS = [i for i in range(1, 13, 1)]

YEARS = [i for i in range(2017, 2031, 1)]

DAYS_OF_WEEK = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

BASE_SCHEMA = DataFrameSchema(
    columns={
        "date": Column(datetime),
        "year": Column(int, required=False),
        "day_of_week": Column(str, checks=Check.isin(DAYS_OF_WEEK)),
        "week_of_year": Column(int, checks=Check.isin(WEEKS)),
        "store": Column(str, checks=Check.isin(STORES)),
        "item": Column(str, checks=Check.isin(ITEMS)),
        "item_price": Column(int, checks=Check.greater_than_or_equal_to(0)),
        "sales": Column(int, checks=Check.greater_than_or_equal_to(0)),
        "total_sales_amount": Column(int, checks=Check.greater_than_or_equal_to(0)),
    },
    index=Index(int),
    strict=True,
    coerce=True,
)

WEEKLY_SCHEMA = DataFrameSchema(
    columns={
        "year": Column(int),
        "week_of_year": Column(int, checks=Check.isin(WEEKS)),
        "month": Column(int, checks=Check.isin(MONTHS)),
        "store": Column(str, checks=Check.isin(STORES)),
        "item": Column(str, checks=Check.isin(ITEMS)),
        "item_price": Column(int, checks=Check.greater_than_or_equal_to(0)),
        "sales": Column(int, checks=Check.greater_than_or_equal_to(0)),
        "total_sales_amount": Column(int, checks=Check.greater_than_or_equal_to(0)),
        "sales_lag_.*": Column(float, checks=Check.greater_than_or_equal_to(0), nullable=True, regex=True),
    },
    index=Index(int),
    strict=True,
    coerce=True,
)

PREPROCESSED_SCHEMA = DataFrameSchema(
    columns={
        "store": Column(str, checks=Check.isin(STORES)),
        "item": Column(str, checks=Check.isin(ITEMS)),
        "year": Column(int, checks=Check.isin(YEARS)),
        "week_of_year": Column(int, checks=Check.isin(WEEKS)),
        "sales.*": Column(
            float,
            checks=Check(lambda x: x >= 0.0 and x <= 5000.0, element_wise=True),
            nullable=True,
            regex=True,
        ),
        "item_price": Column(float, checks=Check(lambda x: x >= 0.0 and x <= 1.0, element_wise=True)),
        "store_.*": Column(float, checks=Check.isin((0, 1)), regex=True),
        "item_.*[^price]": Column(float, checks=Check.isin((0, 1)), regex=True),
        "week_of_year_.*": Column(float, checks=Check.isin((0, 1)), regex=True),
        "month_.*": Column(float, checks=Check.isin((0, 1)), regex=True),
        "year_.*": Column(float, checks=Check.isin((0, 1)), regex=True),
    },
    index=Index(int),
    strict=True,
    coerce=True,
)

X_SCHEMA = DataFrameSchema(
    columns={
        "year": Column(int, checks=Check.isin(YEARS)),
        "week_of_year": Column(int, checks=Check.isin(WEEKS)),
        "sales_.*": Column(
            float,
            checks=Check(lambda x: x >= 0.0 and x <= 5000.0, element_wise=True),
            nullable=True,
            regex=True,
        ),
        "item_price": Column(float, checks=Check(lambda x: x >= 0.0 and x <= 1.0, element_wise=True)),
        "store_.*": Column(float, checks=Check.isin((0, 1)), regex=True),
        "item_.*[^price]": Column(float, checks=Check.isin((0, 1)), regex=True),
        "week_of_year_.*": Column(float, checks=Check.isin((0, 1)), regex=True),
        "month_.*": Column(float, checks=Check.isin((0, 1)), regex=True),
        "year_.*": Column(float, checks=Check.isin((0, 1)), regex=True),
    },
    index=Index(int),
    strict=True,
    coerce=True,
)

Y_SCHEMA = DataFrameSchema(
    columns={
        "sales": Column(
            float,
            checks=Check(lambda x: x >= 0.0 and x <= 5000.0, element_wise=True),
        )
    },
    index=Index(int),
    strict=True,
    coerce=True,
)

RAW_PREDICTION_SCHEMA = DataFrameSchema(
    columns={
        "date": Column(datetime),
        "year": Column(int, required=False),
        "day_of_week": Column(str, checks=Check.isin(DAYS_OF_WEEK)),
        "week_of_year": Column(int, checks=Check.isin(WEEKS)),
        "store": Column(str, checks=Check.isin(STORES)),
        "item": Column(str, checks=Check.isin(ITEMS)),
        "item_price": Column(int, checks=Check.greater_than_or_equal_to(0)),
        "sales": Column(int, checks=Check.equal_to(0), nullable=True),
        "total_sales_amount": Column(int, checks=Check.equal_to(0), nullable=True),
    },
    index=Index(int),
    strict=True,
    coerce=True,
)

WEEKLY_PREDICTION_SCHEMA = DataFrameSchema(
    columns={
        "year": Column(int),
        "week_of_year": Column(int, checks=Check.isin(WEEKS)),
        "store": Column(str, checks=Check.isin(STORES)),
        "item": Column(str, checks=Check.isin(ITEMS)),
        "item_price": Column(int, checks=Check.greater_than_or_equal_to(0)),
        "prediction": Column(float, checks=Check.greater_than_or_equal_to(0)),
    },
    index=Index(int),
    strict=True,
    coerce=True,
)


if __name__ == "__main__":
    print(PREPROCESSED_SCHEMA)
    print(WEEKLY_PREDICTION_SCHEMA)