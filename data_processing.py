from dataclasses import dataclass
import pandas as pd
from datetime import datetime


@dataclass
class DatatablePreprocess:
  def __init__(self, raw_data: str):
    self.raw_data = raw_data

  def read_in_raw_data(self) -> pd.DataFrame:
    
    custom_date_parser = lambda x: datetime.strptime(x, "%d/%m/%Y")
    raw_data = pd.read_csv(self.raw_data, parse_dates=['DATE_CREATED', 'DATE_MODIFIED'], date_parser= custom_date_parser)
    col_names = ['id', 'seq', 'origin', 'Project', 'DATE_CREATED', 'DATE_MODIFIED', 'SEQUENCE_TYPE', 'PROTEIN_ID.1', 'LAST_UPDATER.1', 'Format', 'Isotype']
    
    if not set(col_names).issubset(raw_data.columns):
      raise ValueError("Make sure correct file is selected and the column names are correct")
    

    raw_data = raw_data[col_names]

    column_names = ['id', 'seq', 'origin', 'project', 'date_created', 'date_modified', 'sequence_type', 'protein_id', 'last_updated', 'format', 'isotype']
    old_column_names = raw_data.columns.to_list()
    raw_data.rename(columns={i:j for i,j in zip(old_column_names,column_names)}, inplace=True)

    return raw_data

  def drop_duplicates_and_null(self) -> pd.DataFrame:

    raw_data = self.read_in_raw_data()
    tidy_df = raw_data.dropna(subset=['id','seq', 'project', 'format']).drop_duplicates(subset=['id', 'isotype'])

    return tidy_df

  def create_unique_index(self, df: pd.DataFrame) -> pd.DataFrame:

    df['unique_id'] = df['id'] + '_' + df['isotype']

    return df
  
  def run_datatable_preprocess(self) -> pd.DataFrame:

    tidy_df = self.drop_duplicates_and_null()
    df = self.create_unique_index(tidy_df)

    return df