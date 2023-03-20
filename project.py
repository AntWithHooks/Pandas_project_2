import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def success_operation(column):
    top_operation = full_data \
        .query('success == True') \
        .groupby(column).success.count() \
        .reset_index() \
        .sort_values('success', ascending=False)

    max_value = top_operation.success.max()

    return top_operation\
        .query(f'success == {max_value}')\
        [f'{column}'].sort_values().tolist()


# data edit
user_data = pd.read_csv('./user_data.csv')
logs = pd.read_csv('./logs.csv')
full_data = user_data.merge(logs, on='client', how='outer')

# data research
top_client = success_operation('client')
top_platform = success_operation('platform')

platform_for_premium = full_data\
    .query('premium == True')\
    .groupby('platform').premium.count()\
    .reset_index()


# data review
bar_by_premium = sns.barplot(data=platform_for_premium, x='platform', y='premium')
plt.show()
