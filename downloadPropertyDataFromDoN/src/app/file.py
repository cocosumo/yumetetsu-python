import pandas as pd
import os, glob, shutil
from dotenv import load_dotenv

load_dotenv()

project_name = "scrape_donet_bukken"
grouped_folder = "grouped"

def get_process_dir():
  process_path = os.path.join(os.path.join(os.path.dirname(__file__),'dump_files'))
  grouped_path = os.path.join(process_path, grouped_folder)

  if not os.path.exists(grouped_path):
    os.makedirs(grouped_path, exist_ok=False)
  return process_path

def get_grouped_dir(dir = get_process_dir()):
  return os.path.join(dir, grouped_folder)

def get_merged_file_path():
  return os.path.join(get_grouped_dir(), "merged.csv")

def clear_dir(dir = get_process_dir()):
  print("Clearing directory.")
  for f in glob.glob(dir + '\\*.csv'):
    os.remove(os.path.join(dir, f))

def remove_dir(dir = get_process_dir()):
  print("Removing entire directory.")
  try:
    shutil.rmtree(dir)
  except OSError as e:
    print("Error: %s : %s" % (dir, e.strerror))

def save_dt_tocsv(dt, path):
  print("Saving to : ", path)
  dt.to_csv(path, index=False, encoding='cp932')

def merge_files(dir = get_process_dir()):
  print(f"Merging files. {dir}")
  os.chdir(dir)

  all_filenames = [i for i in glob.glob(u'*.csv')]

  merged_df = pd.concat(
      [pd.read_csv(f, encoding="cp932") for f in all_filenames ]
    ).dropna(axis=1,how="all"
    ).drop(columns=['更新者', '登録者'])

  save_dt_tocsv(
    merged_df,
    os.path.join
      (get_grouped_dir(), 'merged.csv'
    )
  )
  return merged_df

def group_by_property_type(dir = get_process_dir()):
  grouped_path = get_grouped_dir()
  for name, group in merge_files(dir).groupby(by=u'物件種別'):
    df = group.dropna(axis=1,how="all")
    print(f'{len(df.columns)}列数\t => \t{name}')
    save_dt_tocsv(df, os.path.join(grouped_path, f'{len(df.columns)}_{name}.csv'))


def process_files():
  merge_files()

def insert_str (source_str, insert_str):
  pos = source_str.find('.csv')
  return ''.join([source_str[:pos], insert_str, source_str[pos:]])

def rename_file(from_path, filename):
  os.rename(from_path, insert_str(from_path, filename))