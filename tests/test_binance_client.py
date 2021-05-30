from exchange_processors.binance.binance_client import BinanceClient

def test_binance_client():
    client = BinanceClient(
                        apiKey='test_api_key',
                        secretKey='test_secret_key',
                        BASE_PATH='test_base_patch',
                        suported_codes=[777]
    )
    assert client.__getattribute__('secretKey') == 'test_secret_key'
    assert client.__getattribute__('BASE_PATH') == 'test_base_patch'
    assert client.__getattribute__('suported_codes') == [777]
    assert client.__getattribute__('headers') == {"X-MBX-APIKEY" : 'test_api_key'}

def test_get_signature():
    secretKey = 'test_signature'
    client = BinanceClient(secretKey=secretKey)
    return_value = '3f9168044ce99b6e1e6544c7e148626a4454b54a67675b8bf14e684916a57ee7'
    assert client.get_signature({"test_signature": "777"}) == return_value



