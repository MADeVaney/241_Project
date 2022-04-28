import pandas as pd
import seaborn as sns
import plotly.express as px
# Reading in data
data2016 = pd.read_csv('2016_2700s.csv', low_memory=False)[['contributor_state', 'committee_name']].dropna()
data2020 = pd.read_csv('2020_2800s.csv', low_memory=False)[['contributor_state', 'committee_name']].dropna()
# Dictionary of the political party for 2016 campaigns
parties2016 = {
'MARCO RUBIO FOR PRESIDENT':'R',
'JUDD WEISS CAMPAIGN COMMITTEE':'L',
'CRUZ FOR PRESIDENT':'D',
'SCOTT WALKER INC':'R',
'KASICH FOR AMERICA INC':'R',
'HILLARY FOR AMERICA':'D',
"O'MALLEY FOR PRESIDENT":'D',
'PATAKI FOR PRESIDENT INC':'R',
'GILMORE FOR AMERICA LLC':'R',
'JINDAL FOR PRESIDENT':'R',
'LINDSEY GRAHAM 2016':'R',
'DONALD J. TRUMP FOR PRESIDENT, INC.':'R',
'CHRIS CHRISTIE FOR PRESIDENT INC':'R',
'JEB 2016, INC.':'R',
'SANTORUM FOR PRESIDENT 2016':'R',
'HUCKABEE FOR PRESIDENT, INC.':'R',
'ROCKY 2016 LLC':'I',
'CARLY FOR PRESIDENT':'R',
'GARY JOHNSON 2016':'L',
'CARSON AMERICA': 'R',
'RAND PAUL FOR PRESIDENT, INC.':'R',
'JEFF GEORGE FOR PRESIDENT':'I',
'MARKFORAMERICA, INC.':'R',
'BERNIE 2016': 'D',
'WEBB 2016': 'D',
'PETERSEN FOR PRESIDENT 2016 LLC':'R',
'PERRY FOR PRESIDENT INC':'R',
'CHAFEE 2016': 'D',
"MCAFEE '16":'L',
'JILL STEIN FOR PRESIDENT':'G',
'CASTLE2016':'I',
'MCMULLIN FOR PRESIDENT COMMITTEE INC.':'I',
'PEOPLE FOR ROBBY WELLS':'I',
'WILLIE WILSON 2016':'D'
}
# Adding parties to the dataframe
party2016 = [parties2016[name] for name in data2016['committee_name']]
data2016['party'] = party2016
# Adding Democrat percentage for each state to the dataframe
dem_percents_2016 = {}
for state in data2016['contributor_state'].unique():
    state_data = data2016[data2016['contributor_state']==state]
    percent = len(state_data[state_data['party']=='D']) / len(state_data)
    dem_percents_2016[state] = percent
data2016['percent_dem'] = [dem_percents_2016[state] for state in data2016['contributor_state']]
# Graphing 2016 Democrat data
fig = px.choropleth(data2016, locations='contributor_state', locationmode='USA-states', scope='usa', color='percent_dem', color_continuous_scale = 'Blues', labels={'percent_dem':'Democrat Ratio'})
fig.update_layout(title_text='2016 Ratio of Maximum Donations in Each State Given To Democrats', title_x=0.5, title_font_size = 24, geo=dict(bgcolor='rgba(0,0,0,0)'))
fig.show()

# Dictionary of the political party for 2020 campaigns
parties2020 = {
    'HICKENLOOPER 2020':'D',
    'BIDEN FOR PRESIDENT':'D',
    'BERNIE 2020':'D',
    'WIN THE ERA PAC':'D',
    'FRIENDS OF ANDREW YANG':'D',
    'WHITNEY 2020 INC.':'R',
    'JACOB HORNBERGER FOR PRESIDENT CAMPAIGN COMMITTEE':'L',
    'HOWIE HAWKINS FOR OUR FUTURE':'G',
    'BULLOCK FOR PRESIDENT':'D',
    'WELD 2020 PRESIDENTIAL CAMPAIGN COMMITTEE, INC.':'R',
    'AMY FOR AMERICA':'D',
    'MARIANNE WILLIAMSON FOR PRESIDENT':'D',
    'MARIANNE WILLIAMSON FOR PRESIDENT, INC.':'D',
    'WARREN FOR PRESIDENT, INC.':'D',
    'DONALD J. TRUMP FOR PRESIDENT, INC.':'R',
    'MATERN 2020':'R',
    'CORY 2020':'D',
    'ADAM KOKESH AMERICAN REFERENDUM PROJECT':'L',
    'ROCKY 101 LLC':'R',
    'TOM STEYER 2020':'D',
    'JO JORGENSEN FOR PRESIDENT':'L',
    'INSLEE FOR AMERICA':'D',
    'WAYNE MESSAM FOR AMERICA, INC.':'D',
    'KANYE 2020':'I',
    'ROSS FOR MAINE':'D',
    'JEN2020':'D',
    'GILLIBRAND 2020':'D',
    'DE BLASIO 2020':'D',
    'BENNET FOR AMERICA':'D',
    'FRIENDS OF JOHN PHILLIPS JR':'L',
    'COMMITTEE TO ELECT CHRIS FLORQUIST PRESIDENT':'D',
    'SETH MOULTON FOR AMERICA, INC.': 'D',
    'SWALWELL FOR AMERICA':'D',
    'TIM RYAN FOR AMERICA':'D',
    'KAMALA HARRIS FOR THE PEOPLE':'D',
    'FRIENDS OF JOHN DELANEY':'D',
    'BROCK PIERCE FOR PRESIDENT':'I',
    'THOM TILLIS COMMITTEE':'R',
    'HICKENLOOPER FOR COLORADO':'D',
    'WALSH FOR PRESIDENT':'R',
    'GLEIB 2020':'D',
    'KEAN VICTORY FUND':'R',
    'JOE SESTAK FOR PRESIDENT':'D',
    'COMMITTEE TO ELECT KIM RUFF':'L',
    'COMMITTEE TO ELECT MARK CHARLES FOR PRESIDENT':'I',
    'COMMITTEE TO ELECT JOSEPH KISHORE':'I',
    'ALYSE FOR ALASKA':'I',
    'JOHN COWAN FOR CONGRESS, INC.':'R'
}
# Adding parties to the dataframe
party2020 = [parties2020[name] for name in data2020['committee_name']]
data2020['party'] = party2020
# Adding Democrat percentage for each state to the dataframe
dem_percents_2020 = {}
for state in data2020['contributor_state'].unique():
    state_data = data2020[data2020['contributor_state']==state]
    percent = len(state_data[state_data['party']=='D']) / len(state_data)
    dem_percents_2020[state] = percent
data2020['percent_dem'] = [dem_percents_2020[state] for state in data2020['contributor_state']]
# Graphing 2020 Democrat data
fig = px.choropleth(data2020, locations='contributor_state', locationmode='USA-states', scope='usa', color='percent_dem', color_continuous_scale = 'Blues', labels={'percent_dem':'Democrat Ratio'})
fig.update_layout(title_text='2020 Ratio of Maximum Donations in Each State Given To Democrats', title_x=0.5, title_font_size = 24, geo=dict(bgcolor='rgba(0,0,0,0)'))
fig.show()

# Adding the change in Democrat percentage from 2016 to 2020 to the dataframe
small2016 = data2016[['contributor_state', 'percent_dem']].drop_duplicates()
small2020 = data2020[['contributor_state', 'percent_dem']].drop_duplicates()
databoth = small2016.merge(small2020, on='contributor_state')
databoth['change'] = databoth['percent_dem_y'] - databoth['percent_dem_x']
# Graphing the change in Democrat percentage from 2016 to 2020
fig = px.choropleth(databoth, locations='contributor_state', locationmode='USA-states', scope='usa', color='change', color_continuous_scale = 'RdBu', labels={'change':'Change in Ratio'})
fig.update_layout(title_text='2016 to 2020 Change in Ratio of Maximum Donations in Each State Given To Democrats', title_x=0.5, title_font_size = 26, geo=dict(bgcolor='rgba(0,0,0,0)'))
fig.show()




# Adding third-party percentage for each state in 2016 to the dataframe
third_percents_2016 = {}
for state in data2016['contributor_state'].unique():
    state_data = data2016[data2016['contributor_state']==state]
    percent = (len(state_data[state_data['party']=='L']) + len(state_data[state_data['party']=='G']) + len(state_data[state_data['party']=='I']))/ len(state_data)
    third_percents_2016[state] = percent
data2016['percent_third'] = [third_percents_2016[state] for state in data2016['contributor_state']]
# Graphing the third-party percentages for 2016
fig = px.choropleth(data2016, locations='contributor_state', locationmode='USA-states', scope='usa', color='percent_third', color_continuous_scale = 'tempo', labels={'percent_third':'Third-Party Ratio'})
fig.update_layout(title_text='2016 Ratio of Maximum Donations in Each State Given To Third-Party Candidates', title_x=0.5, title_font_size = 24, geo=dict(bgcolor='rgba(0,0,0,0)'))
fig.show()

# Adding third-party percentage for each state in 2020 to the dataframe
third_percents_2020 = {}
for state in data2020['contributor_state'].unique():
    state_data = data2020[data2020['contributor_state']==state]
    percent = (len(state_data[state_data['party']=='L']) + len(state_data[state_data['party']=='G']) + len(state_data[state_data['party']=='I']))/ len(state_data)
    third_percents_2020[state] = percent
data2020['percent_third'] = [third_percents_2020[state] for state in data2020['contributor_state']]
# Graphing the third-party percentages for 2020
fig = px.choropleth(data2020, locations='contributor_state', locationmode='USA-states', scope='usa', color='percent_third', color_continuous_scale = 'tempo', labels={'percent_third':'Third-Party Ratio'})
fig.update_layout(title_text='2020 Ratio of Maximum Donations in Each State Given To Third-Party Candidates', title_x=0.5, title_font_size = 24, geo=dict(bgcolor='rgba(0,0,0,0)'))
fig.show()