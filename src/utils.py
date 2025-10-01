import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# Function to download and prepare stock data
def dl_combined_data(tickers, start, end, debug=None):
    '''Download stock data for multiple tickers and return a clean DataFrame'''
    all_data = []

    for ticker in tickers:
        if debug: print(f'Downloading {ticker}...')
        data = yf.download(ticker, start, end, auto_adjust=False)

        # Flatten MultiIndex columns by removing the ticker level
        data.columns = data.columns.droplevel(1)
        data = data.reset_index()  # Make Date a regular column
        data['Ticker'] = ticker
        globals()[ticker] = data
        all_data.append(data)
    # Combine all stocks
    combined_df = pd.concat(all_data, ignore_index=True)
    # Reorder columns to put Date and Ticker first
    cols = ['Date', 'Ticker'] + [col for col in combined_df.columns if col not in ['Date', 'Ticker']]
    combined_df = combined_df[cols]

    return combined_df
def plotting_var(df,index,var = 'Adj Close'):
    plt.figure(figsize=(15, 10))
    plt.subplots_adjust(top=1.25, bottom=1.2)
    # Create subplots for each company
    for i, (ticker, company_name) in enumerate(index.items()):
        plt.subplot(3, 2, i+1)  # i+1 because subplot indexing starts at 1
        company_data = df[df['company_name'] == company_name]
        company_data[var].plot()
        plt.ylabel(var)
        plt.xlabel(None)
        plt.title(f"{var} of {company_name}")

    plt.tight_layout()


#Creating the sequences for testing the model
def create_sequences(data, seq_length):
    """Create sequences for LSTM training"""
    xs, ys = [], []
    for i in range(seq_length, len(data)):
        xs.append(data[i - seq_length:i])
        ys.append(data[i])
    return np.array(xs), np.array(ys)

def pairgrid(df):
    # Set up our figure by naming it returns_fig, call PairPLot on the DataFrame
    returns_fig = sns.PairGrid(df)
    # Using map_upper we can specify what the upper triangle will look like.
    returns_fig.map_upper(plt.scatter,color='purple')
    # We can also define the lower triangle in the figure, inclufing the plot type (kde) or the color map (BluePurple)
    returns_fig.map_lower(sns.kdeplot,cmap='cool_d')
    # Finally we'll define the diagonal as a series of histogram plots of the daily return
    returns_fig.map_diag(plt.hist,bins=30)
    return returns_fig

pairgrid(closing_df)