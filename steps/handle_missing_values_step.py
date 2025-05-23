import sys
import os

current_file_path = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(current_file_path, '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
import pandas as pd
from source.handle_missing_values import DropMissingValuesStrategy,FillMissingValuesStrategy,MissingValueHandler

from zenml import step

@step
def handle_missing_values_step(df:pd.DataFrame,strategy:str="mean")->pd.DataFrame:
    if strategy=="drop":
        handler=MissingValueHandler(DropMissingValuesStrategy(zxis=0))
    elif strategy in ['mean','median','mode','constant']:
        handler=MissingValueHandler(FillMissingValuesStrategy(method=strategy))
    else:
        raise ValueError(f"unsupported missing value handling strategy : {strategy}")
    
    cleaned_df=handler.handle_missing_values(df)
    return cleaned_df