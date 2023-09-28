from flask import Flask, render_template, request
import yfinance as yf
from utils import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import base64
import io
from io import BytesIO
import pandas as pd
from scipy.stats import norm
from sklearn.metrics import mean_squared_error

majors={
       "A": "Choose",
       "CSC": "Computer Science",
       "ENG":"English",
       "MATH": "Mathematics",
       "ECON": "Economics",
       "BUS":"Business",
       "AS":"Actuarial Science",
       "DS": "Data Science",
       "POL": "Politics",
       "MKT": "Marketing",
       "HTL": "Healthcare",
       "ENGI": "Engineering",
       "PSY": "Psychology",
       "HIS": "History",
       "LAW": "Law/Legal",
       "EDUC": "Education",
       "Other": "Other"
       }

myKeys = list(majors.keys())
myKeys.sort()
sorted_dict = {i: majors[i] for i in myKeys}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html',majors = sorted_dict)

@app.route('/stockpred', methods=['GET', 'POST'])
def stockpred():

    sticker_df = pd.read_csv("data/yahoofinance.csv")
    stickers = sticker_df["Symbol"].to_list()
    # if request.method == 'POST':
    #     startday = request.form.get('startday')
    #     endday = request.form.get('endday')
    #     stock_symbol = request.form.get('stock_symbol')
    #     df = get_stock(stock_symbol,startday,endday)
    #     closing_prices = df['Close'].values

    #     # Create a Matplotlib figure
    #     fig = Figure(figsize=(16, 6))
    #     ax = fig.add_subplot(111)
    #     ax.set_title('Model')
    #     ax.set_xlabel('Date', fontsize=18)
    #     ax.set_ylabel('Close Price USD ($)', fontsize=18)
    #     ax.plot(df['Close'])

    #     ax.legend(['Stock Price'], loc='lower left')
    #     canvas = FigureCanvas(fig)
    #     img_buf = io.BytesIO()
    #     canvas.print_png(img_buf)
    #     img_buf.seek(0)
    #     img_base64 = base64.b64encode(img_buf.getvalue()).decode('utf-8')
    #     return render_template('stockpred.html', ticker=stock_symbol, startday='2020-07-19', endday='2023-01-01', image_data=img_base64, listofstickers= stickers)
    return render_template('stockpred.html', ticker=None, startday=None, endday=None, image_data=None, listofstickers= stickers)



@app.route('/casesolver')
def casesolver():
    return render_template('casesolver.html')

if __name__ == '__main__':
    app.run(debug=True)