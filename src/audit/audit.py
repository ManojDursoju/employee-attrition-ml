
from pathlib import Path
import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    """Load an approved CSV or Excel dataset."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    suffix = path.suffix.lower()

    if suffix == ".csv":
        return pd.read_csv(path)

    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path)

    raise ValueError("Supported formats: CSV, XLSX, XLS")


def profile_dataset(df: pd.DataFrame) -> None:
    """Print basic dataset information."""
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")

    print("\nColumn types:")
    print(df.dtypes.to_string())

    print("\nMissing values:")
    print(df.isna().sum().to_string())

    print("\nDuplicate rows:", df.duplicated().sum())


if __name__ == "__main__":
    print("Employee Attrition Data Audit")
    print("Waiting for the approved dataset.")
