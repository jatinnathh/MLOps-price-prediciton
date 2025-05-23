import sys
import os

current_file_path = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(current_file_path, '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pandas as pd
from source.ingest_data import DataIngestorFactory
from zenml import step

@step 
def data_ingestion_step(file_path:str)->pd.DataFrame:

    file_extension=".zip"
    data_ingestor=DataIngestorFactory.get_data_ingestor(file_extension)

    df=data_ingestor.ingest(file_path)
    return df