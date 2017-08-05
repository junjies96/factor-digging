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
    
        # Get PE
        data.get_variable('AShareEODDerivativeIndicator', 's_val_pe_ttm')
        data.deal_exception_value(('AShareEODDerivativeIndicator', 's_val_pe_ttm'), 'constant', 0)
        pe_ltm = data.get_variable('AShareEODDerivativeIndicator', 's_val_pe_ttm')

        # Get market value
        data.get_variable('AShareEODDerivativeIndicator', 's_val_mv')
        data.deal_exception_value(('AShareEODDerivativeIndicator', 's_val_mv'), 'constant', 0)
        mktVal = data.get_variable('AShareEODDerivativeIndicator', 's_val_mv')

        # Get net profit LTM
        data.get_variable('AShareTTMAndMRQ', 's_fa_profit_ttm')
        data.deal_exception_value(('AShareTTMAndMRQ', 's_fa_profit_ttm'), 'constant', 0)
        netProfit = data.get_variable('AShareTTMAndMRQ', 's_fa_profit_ttm')

        # Get industry class
        indClass = data.get_variable('AShareIndustriesClass','wind_ind_code')
        indClass = indClass.loc[indClass['CUR_SIGN'] == '1']
        classMap = pd.Series(indClass['WIND_IND_CODE'].values, index=indClass['WIND_CODE'])
        
        # Calculate indusrty PE
        mktVal_Ind = mktVal.groupby(classMap, axis=1).sum()
        netProfit_Ind = netProfit.groupby(classMap, axis=1).sum()
        trade_days = data.get_variable('O_price').index



        return pe_ltm.loc[trade_days]