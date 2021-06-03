from exchange_processors.models import GetAccount
from requests.models import Response
from exchange_processors.binance.binance_exchange_processor import BinanceExchangeProcessor
import pytest
from exchange_processors.binance.binance_client import BinanceClient


@pytest.fixture()
def test_binance_exchange_processor():
    yield BinanceExchangeProcessor(BinanceClient())



def test_get_account(test_binance_exchange_processor, mocker):

    def mock_good_signature(*args, **kwargs):
        return "good_signature"
    
    def mock_bad_signature(*args, **kwargs):
        return " "

    def mock_request(*args, **kwargs):
        if kwargs["params"]["signature"] == " ":
            class IncorrectResponse:
                @staticmethod
                def json():
                    return {"error": "Incorrect signature"}
            return IncorrectResponse()
        elif kwargs["params"]["signature"] == "good_signature":
            class CorrectResponse:
                @staticmethod
                def json():
                    return {"amount" : "123"}
            return CorrectResponse()
           

    mocker.patch("exchange_processors.binance.binance_client.BinanceClient.request", mock_request)


    mocker.patch("exchange_processors.binance.binance_client.BinanceClient.get_signature", mock_good_signature)

    #assert test_binance_exchange_processor.get_account() == GetAccount(amount=123.0)

    mocker.patch("exchange_processors.binance.binance_client.BinanceClient.get_signature", mock_bad_signature)
    
    #with pytest.raises(KeyError):
        #test_binance_exchange_processor.get_account() == GetAccount(amount=123.0)
    
    