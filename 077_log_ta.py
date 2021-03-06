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
    
        import pandas as pd
        import numpy as np

        # Read data from Database
        profitx = data.get_variable('AShareProfitExpress', 'tot_assets')
        ta = profitx.pivot(index='REPORT_PERIOD', columns='WIND_CODE', values='TOT_ASSETS')

        ref_table = data.get_variable('O_price')

        ta = ta.loc[:, ref_table.columns].reindex(ref_table.index, method='ffill').fillna(1)

        return np.log(ta)