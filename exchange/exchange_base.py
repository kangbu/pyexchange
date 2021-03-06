# -*- coding: utf-8 -*-
class ExchangeBase:
    """
    Base class of Exchange
    """

    def __init__(self, name, version, url=None):
        '''
        Constructor
        :param str name:name of exchange
        :param str version: API version
        :param str url: API url
        '''
        self._name = name
        self._version = version
        self._url = url

    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version

    @property
    def url(self):
        return self._url

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        return NotImplementedError()

    def get_ticker(self, currency_pair):
        '''
        Gets last price
        :param CurrencyPair currency_pair: currency pair
        :return: ticker
        :rtype: Ticker
        '''
        return NotImplementedError()

    def get_orderbook(self, currency_pair):
        '''
        Gets orderbook information
        :param CurrencyPair currency_pair: currency pair
        :return: orderbook
        :rtype: Orderbook
        '''
        return NotImplementedError()
