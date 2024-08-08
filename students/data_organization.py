import pandas as pd

data = None
def load_data():
    # remember that never work directly with raw data
    global data
    raw_data = pd.read_csv(r'../simulated_dataset/generated_students.csv')
    data = raw_data.copy()

def organize_data():

    # 1. Inspection
    print(f'All records ::: \n {data}')
    print(f'Head ::: \n {data.head()}')

    # 2. check data types and null
    print(data.info())

    # 3, Summary  statistics
    # count: count missing values
    # mean: the average of values
    # std: measure the standard deviation (variation or dispersion of the values)
    # min: the smallest value
    # max: the greatest value
    # 25%(25% percentile): 25% of data is below the SPECIFIC VALUE
    print(data.describe())

    # 4. Handle missing value
    print(f'Missing value ::: {data.isnull().sum()}')
    # null data:::
    # stu_id 0
    # stu_name 0
    # dob 4 there are 4 rows that contains no data
    # country 3 there are 3 rows that contains no data
    # dtype: int64

    # fill missing data with the default value
    # be careful when fill missing data as dob
    default_dob = pd.Timestamp('1990-01-01')
    data['dob'] = data['dob'].fillna(default_dob.date())
    data['country'] = data['country'].fillna("Country not found")
    print(data)

    # 5. Find and Drop duplicate row if is there any duplicate rows
    print(f'Duplicate rows::: \n {data.duplicated().sum()}')

    # 6. Datatype conversion (optional)
    print(f'DOB column before converting ::: \n {data['dob'].dtypes}')
    data['dob'] = pd.to_datetime(data['dob'])
    print(f'Convert String to date in DOB col::: \n {data['dob'].dtypes}')

    # to be continue

if __name__ == '__main__':
    load_data()
    organize_data()
