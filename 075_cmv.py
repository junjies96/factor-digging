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
        data.get_variable('AShareEODDerivativeIndicator', 's_dq_mv')
        # Deal with NaN value
        data.deal_exception_value(('AShareEODDerivativeIndicator', 's_dq_mv'), 'constant', 0)
        # Get data after pre-process
        cmv = data.get_variable('AShareEODDerivativeIndicator', 's_dq_mv')
        trade_days = data.get_variable('O_price').index

        return cmv.loc[trade_days]