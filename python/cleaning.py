import pandas as pd


def clean_data(df):
    """
    Clean procurement dataset.
    """

    # Copy dataframe
    df = df.copy()

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Rename columns
    df.rename(columns={
        "tender_no.": "tender_no",
        "tender_detail_status": "status"
    }, inplace=True)

    # Convert award_date
    df["award_date"] = pd.to_datetime(
        df["award_date"],
        dayfirst=True,
        errors="coerce"
    )

    # Remove leading/trailing spaces
    text_columns = [
        "tender_description",
        "agency",
        "supplier_name",
        "status"
    ]

    for col in text_columns:
        df[col] = df[col].str.strip()

    # Award amount cannot be negative
    df = df[df["awarded_amt"] >= 0]

    return df