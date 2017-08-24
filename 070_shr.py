class UserSignal(Signal):

	def __init__(self):
		self._LRImportance = 0
		self._treeImportance = 0
		self._correlation = 0
		self._decay = 0
		self._annual_return = 0
		self._annual_vol = 0
		self._sharpe_ratio = 0
		self._max_drawdown = 0
		self._return_risk_ratio = 0
		self._data_ret = 0

    def dig(self, data):
    
        # Read data from Database
        data.get_variable('AShareEODDerivativeIndicator', 'tot_shr_today')
        # Deal with NaN value
        data.deal_exception_value(('AShareEODDerivativeIndicator', 'tot_shr_today'), 'constant', 0)
        # Get data after pre-process
        shr = data.get_variable('AShareEODDerivativeIndicator', 'tot_shr_today')
        trade_days = data.get_variable('O_price').index

        return shr.loc[trade_days]