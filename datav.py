import pandas as pd 
import plotly.graph_objects as go

data = pd.read_csv('./data.csv')

students = data.loc[ data['student_id'] == 'TRL_987']
level = students.groupby('level')
meanlevel = level['attempt'].mean()
graph = go.Figure(go.Bar(x = meanlevel , y = ['Level 1 ' , 'Level 2 ' , 'Level 3 ' , 'Level 4 '] , orientation = 'h'))
graph.show()