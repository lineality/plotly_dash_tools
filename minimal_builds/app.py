"""
For Plolty Dash: Minimal Deploy Test MVP "hello world" dash app.

run with: $ python3 app.py

May need to run requirements.txt with package versions removed to install all newest versions:


# Use a python environment:
    use: python3 -m venv env; source env/bin/activate

The only required python package is dash

(env) $ pip install dash

"""

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1("Hello World!")
    ])

if __name__ == '__main__':
    app.run_server()
