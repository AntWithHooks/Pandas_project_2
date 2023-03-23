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
full_data = user_data.merge(logs, on='client', how='inner')

# data research
top_client = success_operation('client')
top_platform = success_operation('platform')

platform_for_premium = full_data\
    .query('premium == True')\
    .groupby('platform').premium.count()\
    .reset_index()

operation_quantity = full_data\
    .query('success == 1')\
    .client.value_counts()

computer_operation = full_data\
    .query('platform == "computer" & success == 1')


# data review
sns.color_palette()
fig, ax = plt.subplots(nrows=3, ncols=1)
fig.tight_layout(h_pad=2)

sns.barplot(data=platform_for_premium, x='platform', y='premium', ax=ax[0], palette='Set2')
ax[0].set(title='Premium\'s prefers',
                xlabel='Type of platform',
                ylabel='Quantity')

sns.histplot(full_data.query('premium == True').age,
             label='premium', stat="density", binwidth=3, ax=ax[1], color='plum')
sns.histplot(full_data.query('premium == False').age,
             label='no premium', stat="density", binwidth=3, ax=ax[1], color='sandybrown')
ax[1].set(title='Frequency of client by age',
                xlabel='Age',
                ylabel='Frequency')
ax[1].legend()


sns.countplot(x=computer_operation.age, ax=ax[2], color='salmon')
ax[2].set(title='Quantity',
          xlabel='Age',
          ylabel='Quantity')

plt.show()
