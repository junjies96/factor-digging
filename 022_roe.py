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

        # Read data from Database
        fin_indicator = data.get_variable('AShareFinancialIndicator', 's_fa_roe')
        roe = fin_indicator.pivot(index='REPORT_PERIOD', columns='WIND_CODE', values='S_FA_ROE')

        ref_table = data.get_variable('O_price')

        roe = roe.loc[, ref_table.columns].reindex(ref_table.index, method='ffill').fillna(0)

        return roe