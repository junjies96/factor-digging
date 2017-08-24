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
        in_holder = data.get_variable('AShareInsideHolder', 's_holder_pct')

        ref_table = data.get_variable('O_price')

        in_holder['S_HOLDER_ENDDATE'].fillna(ref_table.index[-1])
        in_holder = in_holder.pivot_table(index='S_HOLDER_ENDDATE', columns=['S_INFO_WINDCODE', 'S_HOLDER_ANAME'], values='S_HOLDER_PCT')
        max_date = in_holder.index.max()

        in_holder = in_holder.loc(axis=1)[ref_table.columns, :].reindex(ref_table.index.union(in_holder.index))
        in_holder = in_holder.fillna(method='bfill')
        maj_holder_pct = in_holder.max(axis=1, level=0).fillna(0)

        return maj_holder_pct.loc[ref_table.index]