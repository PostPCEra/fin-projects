
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='6FQ27E5DXFAAADLX', output_format='pandas')

symbols = [ 'EBAY', 'PYPL']
for symbol in symbols:
	data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
	print(symbol, data.shape)
	file = symbol + '.dat'
	data.to_csv(file)
