import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates    # more date formats
from functions.data_samples import load_data_yahoo_finance

# =============================================================================
# LOAD DATA - SET TIME INDEX - DATA CLEANING & SELECTION
# =============================================================================


# ===== LOAD DATA

path = 'A.csv'
df_MSFT = pd.read_csv(path)


# ===== SET TIME INDEX

# Convert 'Date' col from string to datetime
"""
- pd.to_datetime() usually recognizes format
- with unusual formatting, format='' can be used
- check documentation for formatting codes
"""
df_MSFT['Date'] = pd.to_datetime(df_MSFT['Date'], format='%m/%d/%Y')

# Set index to date
df_MSFT.set_index('Date', inplace=True)

# Verify that index is datetime object (try it out without converting 'Date' col to datetime
df_MSFT.index.month
df_MSFT.index.day_name()


# ===== DATA CLEANING & SELECTION

# Drop unnecessary entries (Selection via boolean masking otherwise)
df_MSFT = df_MSFT.dropna()                                    # get rid of all NaN rows
df_MSFT = df_MSFT.drop(pd.Timestamp('2012-08-06 00:00:00'))   # by row, timestamp object
df_MSFT = df_MSFT.drop(pd.Timestamp('2012-08-07'))            # also possible


# Slice dataframe based on time series index if needed
df_MSFT['2013':'2014']                      # By year
df_MSFT['2013-01':'2014-07']                # By month
df_MSFT['2013-01-01':'2014-07-06']          # By day

df_MSFT.loc['2015-05-05']                   # for a single day



# =============================================================================
# BASIC DESCRIPTIVE STATISTICS - CONDITIONAL SELECTION - RESAMPLING
# =============================================================================


# ===== BASIC DESCRIPTIVE STATISTICS

df_MSFT.mean()
df_MSFT.min()
df_MSFT.max()


# ===== CONDITIONAL SELECTION

# Find index given value
close_adj = df_MSFT['Adj Close'].min()
df_MSFT[df_MSFT['Adj Close'] == close_adj].index.tolist()

df_MSFT['Adj Close'].idxmin()   # alternatively

# Filter dataframe by values
open_mean = df_MSFT['Adj Close'].mean()
df_MSFT[df_MSFT['Adj Close'] > open_mean]


# ===== RESAMPLING

# Basically a time-based groupby function, need datetime(!)

df_MSFT['Adj Close'].resample('D').mean()       # doesn't make sense ofc
df_MSFT['Adj Close'].resample('M').median()
df_MSFT['Adj Close'].resample('Y').max()

df_MSFT.resample(rule='W').first()              # Sample last day of the week, i.e. sunday
df_MSFT.resample(rule='M').mean()               # Sample mean of each month
df_MSFT.resample(rule='Y').last()               # Sample last day of the year


"""
# Other possibilities: rule='5d', partition in 5 day intervals and pick e.g. first()
df_MSFT.resample('5d').first()  # Sample last day of the year

# Simultaneous operations using .agg()
df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})
"""



# =============================================================================
# IDENTIFYING DIFFERENCES BETWEEN TIME SERIES
# =============================================================================

# Load Data: Microsoft and Amazon Stocks
df_AMZN = load_data_yahoo_finance('00_data_source/yf_AMZN.csv')

# Find Differences of Dataframes as sets
set_MSFT = set(df_MSFT.index)
set_AMZN = set(df_AMZN.index)
diff_set = (set_AMZN - set_MSFT)      # Note: AMZN contains much more data then MSFT


# TO DO: MERGING two time series with the same column



# =============================================================================
# PLOTTING TIME SERIES
# =============================================================================

# Variant 1
plt.plot(df_AMZN['Open'])
plt.show()


# Variant 2
plt.plot_date(df_AMZN.index, df_AMZN['Open'], df_AMZN['Close'],
              linestyle='solid', linewidth=1, markersize=0.5)
plt.gcf().autofmt_xdate()
plt.show()


# Change date formatting
plt.plot(df_AMZN['Open'], label='Open')
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)        # gca(!) not gcf
plt.show()



# =============================================================================
# METHODS
# ============================================================================

df_AMZN = load_data_yahoo_finance('00_data_source/yf_AMZN.csv')
df_BMW = load_data_yahoo_finance('00_data_source/BMW.csv')

# exercise: Truncate both dataframes such that both have the same index
same_index = list(set(df_AMZN.index).intersection(set(df_BMW.index)))
df_AMZN = df_AMZN.loc[same_index]
df_BMW = df_BMW.loc[same_index]

# Percentage Change
df_AMZN_returns = df_AMZN.pct_change()
df_BMW_returns = df_BMW.pct_change()

# Drop NaNs
df_AMZN_returns = df_AMZN_returns.dropna()
df_BMW_returns = df_BMW_returns.dropna()

# Calculate 1st differences
df_AMZN_diff_lag1 = df_AMZN_returns.diff(1)
df_AMZN_diff_lag2 = df_AMZN_returns.diff(2)
df_AMZN_diff_lag_m1 = df_AMZN_returns.diff(-1)
df_AMZN_diff_lag_m2 = df_AMZN_returns.diff(-2)



# ======== EXERCISE
"""
1) Given the CSV file, check for missing values and delete the rows
2) Compute the returns with the corresponding formula
3) Plot the price and the returns
    3.1) In two separate plots
    3.2) In one figure with two axes
4) Display the mean and median of each month in a lineplot
5) Returning to the returns plots only
    5.1) Mark every yearly maximum and minimum with a red marker and black marker respectively
    5.2) Draw a horizontal line of the yearly mean
6) Plot the histogram of the returns
"""
