import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import pandas as pd

# data
data = pd.read_csv('student-enrollment.csv')
data

#initialize Dash app
app = dash.Dash(__name__)

#Create a simple bar chart for enrollment rate
students = px.histogram(data,x='Enrolment',y='State',color='State')
students
# Create Layout
app.layout = html.Div([
    html.H1('Education Dash app',style={'textAlign':'center','color':'#FFFFF','font-size':40}),


dcc.Tabs([
    #pie plot - Tab-1
    dcc.Tab(label="No.of students enrolled",children=[
        html.Div([
            html.H3("bar Chart : Enrolled Students"),
            dcc.Graph(figure=students)
        ])
    ]),
 ])
 ])

if __name__ == '__main__':
    app.run_server()



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)