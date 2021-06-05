from src.exchange_processors.models import GetAccount
from src.exchange_processors.binance.binance_exchange_processor import BinanceExchangeProcessor
import pytest
from src.clients.binance_main_client.binance_client import BinanceClient
from tests.data import json_get_account_200


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
                    return json_get_account_200
            return CorrectResponse()
           

    mocker.patch("src.clients.binance_main_client.binance_client.BinanceClient.request", mock_request)


    mocker.patch("src.clients.binance_main_client.binance_client.BinanceClient.get_signature", mock_good_signature)

    assert test_binance_exchange_processor.get_account() == GetAccount(balances={'BNB': '0.00024951'})

    mocker.patch("src.clients.binance_main_client.binance_client.BinanceClient.get_signature", mock_bad_signature)
    
    with pytest.raises(KeyError):
        test_binance_exchange_processor.get_account() == GetAccount(balances={'BNB': '0.00024951'})
    
    