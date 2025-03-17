import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import preprocessor, Medal_Tally, Overall_Analysis, Countrywise_Analysis, Athletewise_Analysis
df = pd.read_csv("athlete_events.csv")
region_df = pd.read_csv("noc_regions.csv")

df = preprocessor.preprocess(df, region_df)

st.sidebar.title("Olympics Analysis")
st.sidebar.image('https://stillmed.olympic.org/media/Images/OlympicOrg/IOC/The_Organisation/The-Olympic-Rings/Olympic_rings_TM_c_IOC_All_rights_reserved_1.jpg')

user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years, country = Medal_Tally.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = Medal_Tally.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title('Overall Tally')
    elif selected_year == 'Overall':
        st.title(f'{selected_country} Overall performance')
    elif selected_country == 'Overall':
        st.title(f'Medal Tally in {selected_year} Olympics')
    else:
        st.title(f'{selected_country} performance in {selected_year} Olympics')

    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title('Top Statistics')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)
    with col2:
        st.header('Nations')
        st.title(nations)
    with col3:
        st.header('Athletes')
        st.title(athletes)

    # Countries
    st.markdown("<br><br>", unsafe_allow_html=True)
    nations_overtime = Overall_Analysis.data_overtime(df, 'region')
    st.title('Trend of Participating Nations Over the Years')
    # Line plot
    fig = px.line(
        nations_overtime,
        x='Editions',
        y='region',
        markers=True,  # Add markers to highlight data points
        line_shape='spline',  # Smooth curve instead of straight lines
        template='plotly_dark',  # Dark theme for a modern look
    )

    # Customize hover text
    fig.update_traces(
       # hoverinfo="text",
        #hovertext=nations_overtime.apply(lambda row: f"Year: {row['Editions']}<br>Countries: {row['region']}", axis=1),
        marker=dict(size=8, color='red') , # Custom marker size and color
        line = dict(width=3, color='royalblue')
    )

    # Update layout to add **subtle grid lines**
    fig.update_layout(
        xaxis_title="<b>Olympic Editions</b>",
        yaxis_title="<b>Number of Nations</b>",
        font=dict(family="Arial, sans-serif", size=20),
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        paper_bgcolor="rgba(0,0,0,0)",

        # X-axis customization
        xaxis=dict(
            showgrid=True,
            gridcolor='gray',
            gridwidth=0.5,
            zeroline=False,
            showline=True,
            linewidth=2,
            linecolor='white'
        ),

        # Y-axis customization
        yaxis=dict(
            showgrid=True,
            gridcolor='gray',
            gridwidth=0.5,
            zeroline=False,
            showline=True,
            linewidth=2,
            linecolor='white'
        ),

        # **Adding a box around the entire graph**
        shapes=[
            dict(
                type="rect",
                xref="paper", yref="paper",
                x0=0, y0=0, x1=1, y1=1,  # Cover the full plot area
                line=dict(color="gray", width=10)  # White box border
            )
        ]
    )

    st.plotly_chart(fig)

    # Events
    st.markdown("<br><br>", unsafe_allow_html=True)
    events_overtime = Overall_Analysis.data_overtime(df, 'Event')
    st.title('Trend of Events Over the Years')
    # Line plot
    fig = px.line(
        events_overtime,
        x='Editions',
        y='Event',
        markers=True,  # Add markers to highlight data points
        line_shape='spline',  # Smooth curve instead of straight lines
        template='plotly_dark',  # Dark theme for a modern look
    )

    # Customize hover text
    fig.update_traces(
        # hoverinfo="text",
        # hovertext=nations_overtime.apply(lambda row: f"Year: {row['Editions']}<br>Countries: {row['region']}", axis=1),
        marker=dict(size=10, color='red'),  # Custom marker size and color
        line=dict(width=3, color='royalblue')
    )

    # Update layout to add **subtle grid lines**
    fig.update_layout(
        xaxis_title="<b>Olympic Editions</b>",
        yaxis_title="<b>Number of Events</b>",
        font=dict(family="Arial, sans-serif", size=20),
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        paper_bgcolor="rgba(0,0,0,0)",

        # X-axis customization
        xaxis=dict(
            showgrid=True,
            gridcolor='gray',
            gridwidth=0.5,
            zeroline=False,
            showline=True,
            linewidth=2,
            linecolor='white'
        ),

        # Y-axis customization
        yaxis=dict(
            showgrid=True,
            gridcolor='gray',
            gridwidth=0.5,
            zeroline=False,
            showline=True,
            linewidth=2,
            linecolor='white'
        ),

        # **Adding a box around the entire graph**
        shapes=[
            dict(
                type="rect",
                xref="paper", yref="paper",
                x0=0, y0=0, x1=1, y1=1,  # Cover the full plot area
                line=dict(color="gray", width=10)  # White box border
            )
        ]
    )

    st.plotly_chart(fig)

    # Athletes
    st.markdown("<br><br>", unsafe_allow_html=True)
    athletes_overtime = Overall_Analysis.data_overtime(df, 'Name')
    st.title('Trend of Athletes Over the Years')
    # Line plot
    fig = px.line(
        athletes_overtime,
        x='Editions',
        y='Name',
        markers=True,  # Add markers to highlight data points
        line_shape='spline',  # Smooth curve instead of straight lines
        template='plotly_dark',  # Dark theme for a modern look
    )

    # Customize hover text
    fig.update_traces(
        hoverinfo="text",
        hovertext=athletes_overtime.apply(lambda row: f"Year: {row['Editions']}<br>Countries: {row['Name']}", axis=1),
        marker=dict(size=10, color='red'),  # Custom marker size and color
        line=dict(width=3, color='royalblue')
    )

    # Update layout to add **subtle grid lines**
    fig.update_layout(
        xaxis_title="<b>Olympic Editions</b>",
        yaxis_title="<b>Number of Athletes</b>",
        font=dict(family="Arial, sans-serif", size=20),
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        paper_bgcolor="rgba(0,0,0,0)",

        # X-axis customization
        xaxis=dict(
            showgrid=True,
            gridcolor='gray',
            gridwidth=0.5,
            zeroline=False,
            showline=True,
            linewidth=2,
            linecolor='white'
        ),

        # Y-axis customization
        yaxis=dict(
            showgrid=True,
            gridcolor='gray',
            gridwidth=0.5,
            zeroline=False,
            showline=True,
            linewidth=2,
            linecolor='white'
        ),

        # **Adding a box around the entire graph**
        shapes=[
            dict(
                type="rect",
                xref="paper", yref="paper",
                x0=0, y0=0, x1=1, y1=1,  # Cover the full plot area
                line=dict(color="gray", width=10)  # White box border
            )
        ]
    )

    st.plotly_chart(fig)

    # Year-wise Event Distribution Across Sports
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title('Year-wise Event Distribution Across Sports')
    fig, ax = plt.subplots(figsize=(30, 25))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int),
                annot=True)
    st.pyplot(fig)

    #Most Succesful Athletes
    st.title('Most Successful Athletes')
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    x = Overall_Analysis.most_successful(df, selected_sport)
    st.table(x)

if user_menu == 'Country-wise Analysis':
    st.sidebar.title('Country-wise Analysis')
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country = st.sidebar.selectbox('Select a Country', country_list)
    country_df = Countrywise_Analysis.yearwise_medal_tally(df, selected_country)
    fig = px.line(
        country_df,
        x='Year',
        y='Medal',
        title=f"🏅 {selected_country} Medal Tally Over the Years",
        markers=True,  # Adds markers for clarity
        line_shape='spline',  # Smooth curves instead of sharp angles
        color_discrete_sequence=['#FF5733'],  # Custom color (Orange-Red)
    )

    # Improve layout aesthetics
    fig.update_layout(
        title_font=dict(size=24, family="Arial Black"),  # Bold, large title
        xaxis_title="Year",
        yaxis_title="Number of Medals",
        xaxis=dict(showgrid=True, gridcolor='lightgrey'),  # Light grey grid
        yaxis=dict(showgrid=True, gridcolor='lightgrey'),
        plot_bgcolor="white",  # White background for clarity
        hovermode="x unified",  # Show hover tooltip for all points on the x-axis
    )
    st.plotly_chart(fig, use_container_width=True)  # Expands to full width

     # Heat map
    st.title(f'{selected_country} excels in the following sports')
    pt = Countrywise_Analysis.country_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(30, 25))
    ax = sns.heatmap(pt, annot=True)
    st.pyplot(fig)

    st.title(f'Top 10 Athletes of {selected_country}')
    top10 = Countrywise_Analysis.most_successful_countrywise(df, selected_country)
    st.table(top10)

if user_menu == 'Athlete-wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    x1 = athlete_df['Age'].dropna()

    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    # fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
    #                          show_hist=False, show_rug=False)
    # st.plotly_chart(fig)

    st.title('Age Distribution of Olympic Athletes 🏅')

    colors = ['#636EFA', '#FFD700', '#696969', '#CD7F32']  # Blue, Red, Green, Purple

    fig = ff.create_distplot(
        [x1, x2, x3, x4],
        ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
        show_hist=False, show_rug=False, colors=colors
    )

    fig.update_layout(
        font=dict(size=14),
        legend=dict(
            title='Category',
            orientation="v",  # Vertical legend
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02  # Move legend to the right side
        ),
        xaxis_title="Age",
        yaxis_title="Density",
        template='plotly_white',
        width=900,
        height=700,
        margin = dict(t=100)
    )

    fig.update_xaxes(tickangle=-45)  # Rotate x-axis labels for better visibility
    st.plotly_chart(fig, use_container_width=True)

    x = []
    name = []
    famous_sports = [
        'Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
        'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
        'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
        'Water Polo', 'Hockey', 'Rowing', 'Fencing',
        'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
        'Tennis', 'Golf', 'Softball', 'Archery',
        'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
        'Rhythmic Gymnastics', 'Rugby Sevens',
        'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)
    fig2 = ff.create_distplot(x,name, show_hist=False, show_rug=False)
    st.title('Distribution of Age wrt Sports (Gold Medalists)🏅')
    fig2.update_layout(
        font=dict(size=14),
        legend=dict(
            orientation="v",  # Vertical legend
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02  # Move legend to the right side
        ),
        xaxis_title="Age",
        yaxis_title="Density",
        template='plotly_white',
        width=900,
        height=700
    )

    fig2.update_xaxes(tickangle=-45)  # Rotate x-axis labels for better visibility
    st.plotly_chart(fig2, use_container_width=True)

    st.title('Height and Weight of Athletes in Sport')
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    #st.markdown("<br><br>", unsafe_allow_html=True)
    temp_df = Athletewise_Analysis.weight_vs_height(df, selected_sport)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=temp_df['Weight'], y=temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'], ax=ax, s=60)
    st.pyplot(fig)

    st.title('Men vs Women participation')
    final = Athletewise_Analysis.men_vs_women(df)
    # fig = px.line(final, x='Year', y=['Men', 'Women'])
    # st.plotly_chart(fig)
    fig = px.line(
        final,
        x='Year',
        y=['Men', 'Women'],
        labels={'Men': 'Men Participation', 'Women': 'Women Participation', 'Year': 'Year'},
        line_shape='linear',  # Smooth lines
        markers=True,  # Add markers to each point
        color_discrete_map={'Men': '#1f77b4', 'Women': '#ff7f0e'}  # Distinct colors for lines
    )

    # Update layout for better presentation
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Participation',
        xaxis=dict(tickangle=-45),  # Rotate x-axis labels for better visibility
        yaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
        plot_bgcolor='white',  # Set background to white
        legend_title='Gender',
        legend=dict(title='Gender', x=1.02, y=0.5, xanchor='left', yanchor='middle', orientation='v')
        # Centered legend below the plot
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)