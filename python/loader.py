import pandas as pd
import pymysql

from config import DB_CONFIG


def load_raw_data(df):

    connection = pymysql.connect(**DB_CONFIG)

    cursor = connection.cursor()

    # Clear table before loading
    cursor.execute("TRUNCATE TABLE raw_procurements")

    sql = """
    INSERT INTO raw_procurements
    (
        tender_no,
        tender_description,
        agency,
        award_date,
        tender_detail_status,
        supplier_name,
        awarded_amt
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    data = df.values.tolist()

    cursor.executemany(sql, data)

    connection.commit()

    print(f"\n✅ Loaded {len(df)} rows into raw_procurements")

    cursor.close()

    connection.close()