import pandas as pd

def homework_pandas():
    adv1_df = pd.read_csv('data_set/advertising_1.csv', index_col='Number')
    adv2_df = pd.read_csv('data_set/advertising_2.csv', index_col='Number')
    adv3_df = pd.read_csv('data_set/advertising_3.csv', index_col='Number')
    users_df = pd.read_csv('data_set/users.csv')

    # 1
    print(adv1_df.head(10))
    # 2
    print(adv1_df.shape)
    # 3
    print(adv1_df.loc[8, 'Daily Internet Usage'])
    # 4
    print(adv2_df.loc[533:536])
    # 5
    print(adv2_df.describe())
    print(adv2_df.shape)
    # Clicked on Ad

    # 6
    adv12_df = adv1_df._append(adv2_df)
    print(adv12_df)

    # 7
    print(adv12_df['Daily Time Spent on Site'].mean())

    # 8
    print(adv12_df[adv12_df['Daily Time Spent on Site'].isna()])

    # 9
    print(adv3_df[['Ad Topic Line', 'Clicked on Ad']])

    # 10
    adv123_df = pd.concat([adv12_df, adv3_df], axis=0)
    print(adv123_df)

    # 11
    success_adv_df = adv123_df[adv123_df['Clicked on Ad'] == 1]
    print(success_adv_df)

    # 12
    print(users_df, users_df.describe(), sep='\n')

    # 13
    print(users_df['Age'].min())
    print(users_df['Area Income'].max())
    print(users_df['Age'].mean())
    # -------------------------------
    print('-----------------', '\n', 'задание 13-4', )
    print(users_df[users_df['Male'] != 'Nan'].shape[0])
    print('Или')
    print(users_df['Male'].count())
    print('Где правда?')
    print('\n', '-----------------', '\n')
    print(users_df['Number'].min())

    # 14
    success_adv_df = success_adv_df.reset_index()
    success_full_df = pd.merge(left=success_adv_df, right=users_df, how='inner', on='Number')
    print(success_full_df)

    # 15
    print(success_full_df[['Ad Topic Line', 'City', 'Country']].describe())

    # 16
    print(success_full_df['Country'].value_counts())

    # 17
    # 'Ethiopia'
    print(success_full_df[success_full_df['Country'] == 'Ethiopia'])

    # 18
    ''
    filtered_df = success_full_df.loc[(success_full_df["Country"] == 'Ethiopia') &
                                      (success_full_df["Age"] < 30) &
                                      (success_full_df["Daily Internet Usage"] > 120)]
    print(filtered_df)

    # 19
    filtered_df2 = filtered_df.loc[
        (filtered_df["Daily Time Spent on Site"].isnull()) | (filtered_df["Daily Time Spent on Site"] > 55)]
    print(filtered_df2)


bank_df = pd.read_csv('bank-full.csv', sep=';', index_col='id')

print(bank_df.day.describe())
print(bank_df.day)



