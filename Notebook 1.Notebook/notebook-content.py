# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# PARAMETERS CELL ********************

start_date = '2026-01-01'
end_date = '2026-09-01'

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import datetime
import pandas as pd
import json

notebookutils.notebook.exit(json.dumps(
    pd.period_range(
        start = start_date, end = end_date, freq='M')
        .astype('str').tolist()
            )
        )

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
