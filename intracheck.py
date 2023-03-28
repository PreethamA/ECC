
import psycopg2
import pandas as pd
import numpy as np

def connect(query):
    # Connect to the database
    conn = psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_username",
        password="your_password"
    )

    # Execute the query and fetch the results as a list of tuples
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    # Close the database connection
    cur.close()
    conn.close()
    return results

CI050_result=connect( """
    SELECT * FROM CI050
    WHERE timeofday IN
    (SELECT MIN(timeofday)
    FROM CI050
    GROUP BY margin_type)
    """)
CI050_df = pd.DataFrame(CI050_result, columns=['date', 'timeofday', 'clearing_member', 'account','margin_type', 'margin'])

CC050_result=connect("""
SELECT * FROM CC050
WHERE date IN
(SELECT MAX(date)
FROM CC050
GROUP BY margin_type)
""")

# Convert the results to a Pandas DataFrame
CC050_df = pd.DataFrame(CC050_result, columns=['date', 'clearing_member', 'account','margin_type', 'margin'])




# filtering to check intraday margins match or not
df=pd.concat([CC050_df, CI050_df],axis=1, keys = ['cc', 'ci'])

df['margindifference']=np.where(df['cc']['margin_type']==df['ci']['margin_type'],
                    (df['cc']['margin']-df['ci']['margin']),
                    0)

filtered_df = df.loc[(df['margindifference'] > 0) & (df['margindifference'] < 0)]