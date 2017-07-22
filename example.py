class UserSignal(Signal):
    def dig(self, data): # data should be a object from Data Class.
    """
    This method is the main method that a user should implement.
    :param data:
    :return:
    """
        # Read data from Database
        data.get_variable('AshareEODPrices', 's_dq_adjclose')
        # Deal with NaN value
        data.deal_exception_value(('AshareEODPrices', 's_dq_adjclose'), 'constant', 0)
        data.deal_exception_value('O_price', 'constant', 0)
        # Get data after pre-process
        close = data.get_variable('AshareEODPrices', 's_dq_adjclose')
        # Get data from built-in data
        open = data.get_variable('O_price')
        return close + open