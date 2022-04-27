import pandas as pd
import seaborn as sns
import plotly.express as px

data2016 = pd.read_csv('2016_2700s.csv', low_memory=False)[['contributor_state', 'committee_name']].dropna()
data2020 = pd.read_csv('2020_2800s.csv', low_memory=False)[['contributor_state', 'committee_name']].dropna()

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

party2016 = [parties2016[name] for name in data2016['committee_name']]

data2016['party'] = party2016

dem_percents_2016 = {}

for state in data2016['contributor_state'].unique():
    state_data = data2016[data2016['contributor_state']==state]
    percent = len(state_data[state_data['party']=='D']) / len(state_data)
    dem_percents_2016[state] = percent

data2016['percent_dem'] = [dem_percents_2016[state] for state in data2016['contributor_state']]

fig = px.choropleth(data2016, locations='contributor_state', locationmode='USA-states', scope='usa', color='percent_dem', color_continuous_scale = 'Blues', labels={'percent_dem':'Democrat Ratio'})
fig.update_layout(title_text='2016 Ratio of Maximum Donations in Each State Given To Democrats', title_x=0.5, title_font_size = 24, geo=dict(bgcolor='rgba(0,0,0,0)'))
fig.show()


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

party2020 = [parties2020[name] for name in data2020['committee_name']]

data2020['party'] = party2020

dem_percents_2020 = {}

for state in data2020['contributor_state'].unique():
    state_data = data2020[data2020['contributor_state']==state]
    percent = len(state_data[state_data['party']=='D']) / len(state_data)
    dem_percents_2020[state] = percent

data2020['percent_dem'] = [dem_percents_2020[state] for state in data2020['contributor_state']]

fig = px.choropleth(data2020, locations='contributor_state', locationmode='USA-states', scope='usa', color='percent_dem', color_continuous_scale = 'Blues', labels={'percent_dem':'Democrat Ratio'})
fig.update_layout(title_text='2020 Ratio of Maximum Donations in Each State Given To Democrats', title_x=0.5, title_font_size = 24, geo=dict(bgcolor='rgba(0,0,0,0)'))
fig.show()


small2016 = data2016[['contributor_state', 'percent_dem']].drop_duplicates()
small2020 = data2020[['contributor_state', 'percent_dem']].drop_duplicates()
databoth = small2016.merge(small2020, on='contributor_state')
databoth['change'] = databoth['percent_dem_y'] - databoth['percent_dem_x']

fig = px.choropleth(databoth, locations='contributor_state', locationmode='USA-states', scope='usa', color='change', color_continuous_scale = 'RdBu', labels={'change':'Change in Ratio'})
fig.update_layout(title_text='2016 to 2020 Change in Ratio of Maximum Donations in Each State Given To Democrats', title_x=0.5, title_font_size = 26, geo=dict(bgcolor='rgba(0,0,0,0)'))
fig.show()