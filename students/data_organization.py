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
    data.to_csv(r'../simulated_dataset/cleaned_stu_df.csv', index=False)

cleaned_data = None
score = None
def load_cleaned_df():
    global cleaned_data
    cleaned_data = pd.read_csv(r'../simulated_dataset/cleaned_stu_df.csv')
    print(cleaned_data.info())

def load_scores():
    global score
    # score = pd.read_csv(r'../simulated_dataset/raw_scores.csv')
    #
    # # type convertion from object to string
    # score['Period'] = score['Period'].astype('string')
    #
    # # update period -> January, February, March
    # for index, row in score.iterrows():
    #    if row['Period'] == 'Q1_2024':
    #        score.at[index, 'Period'] = 'January'
    #    elif row['Period'] == 'Q2_2024':
    #         score.at[index, 'Period'] = 'February'
    #    else:
    #        score.at[index, 'Period'] = 'March'
    #
    # score.to_csv(r'../simulated_dataset/cleaned_scores_df.csv', index=False)
    score = pd.read_csv(r'../simulated_dataset/cleaned_scores_df.csv')


def map_student_id_between_2_df():

    # this works until the student_ID value matches stu_id value
    # merged_df = pd.merge(score, cleaned_data,left_on='Student_ID', right_on='stu_id', how='left')

    print("")
    # to prevent auto generated column 'Unnamed'
    # score.to_csv(r'../simulated_dataset/cleaned_scores_df.csv', index=False)

def analyze_score():
    # to select multi columns we use [[]]
    # score['Total'] = score.iloc[:, 2:6].sum(axis=1)
    # score.to_csv(r'../simulated_dataset/cleaned_scores_df.csv', index=False)
    print(score)

if __name__ == '__main__':
    # load_data()
    # organize_data()
    load_cleaned_df()
    load_scores()
    # print(score)
    map_student_id_between_2_df()
    analyze_score()