import pandas as pd

path_to_data = '/Users/benjamin/Data/DSC/DSC2t/'

data = pd.read_csv(path_to_data+'dsc2t.csv', sep=';')

# Remove first record (title names from .csv file)
# rename columns and convert dates to Date objects
data.columns = [u'Day', u'Pageviews']
data = data[1:]
data.Day = pd.to_datetime(data.Day)

# Display the data
figure(1)
plot(data.Day, data.Pageviews, 'b-')
gcf().autofmt_xdate()
xlabel('Day')
ylabel('Pageviews')
grid()

# Create Time Serie
serie = data.Pageviews.apply(float)
serie.index = data.Day

mondays = serie[serie.index.dayofweek == 0]

