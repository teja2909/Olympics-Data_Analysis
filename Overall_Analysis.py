def data_overtime(df, col):
    nations_overtime = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('Year')
    nations_overtime.rename(columns={'Year':'Editions', 'count': col}, inplace=True)
    return nations_overtime

def most_successful(df, sport):
    temp_df = df.dropna(subset=['Medal'])
    if sport !='Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]
    top_athletes = temp_df['Name'].value_counts().reset_index().head(15)
    top_athletes.columns = ['Name', 'Medal Count']
    result = top_athletes.merge(df[['Name', 'Sport', 'region']], on='Name', how='left').drop_duplicates()
    return result