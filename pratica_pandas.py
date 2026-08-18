import numpy as np
import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).with_name('data.csv')


def load_data(path: Path = DATA_FILE) -> pd.DataFrame:
    """Load the semicolon-separated dataset used by the exercise."""
    return pd.read_csv(path, sep=';', engine='python', encoding='utf-8')


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy without changing the original DataFrame."""
    cleaned = df.copy()
    cleaned['Calories'] = cleaned['Calories'].fillna(0)

    dates = cleaned['Date'].astype('string').str.strip("'")
    dates = dates.replace({'20201226': '2020/12/26', '1900/01/01': np.nan})
    cleaned['Date'] = pd.to_datetime(
        dates,
        format='%Y/%m/%d',
        errors='coerce',
    )

    return cleaned.dropna(subset=['Date']).reset_index(drop=True)


def main() -> None:
    df = load_data()

    print('--- Informações gerais ---')
    df.info()
    print('\n--- Primeiras 10 linhas ---')
    print(df.head(10))
    print('\n--- Últimas 10 linhas ---')
    print(df.tail(10))

    cleaned = clean_data(df)
    print('\n--- DataFrame final ---')
    print(cleaned)


if __name__ == '__main__':
    main()
