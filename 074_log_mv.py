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
    
        import numpy as np
        
        # Read data from Database
        data.get_variable('AShareEODDerivativeIndicator', 's_val_mv')
        # Deal with NaN value
        data.deal_exception_value(('AShareEODDerivativeIndicator', 's_val_mv'), 'constant', 1)
        # Get data after pre-process
        mv = data.get_variable('AShareEODDerivativeIndicator', 's_val_mv')
        trade_days = data.get_variable('O_price').index

        return np.log(mv.loc[trade_days])