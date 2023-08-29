import numpy as np

def model(dbt, session):
    df = dbt.ref("stg_orders")
    dfx = df.to_pandas()
    dfx['ROLLING'] = dfx['CUSTOMER_ID'].rolling(5).mean()
    dfx['LOG'] = dfx['CUSTOMER_ID'].apply(lambda x: np.log(x) if x != 0 else 0)
    return dfx
