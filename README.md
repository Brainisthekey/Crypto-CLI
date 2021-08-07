# CryptoCLI

Simple CLI application written in Python allowing users to perform operations on [Binance](https://binance.com/), [Bitfinex](https://www.bitfinex.com/) CryptoCurrency Exchange directly from CLI.

## v0.1 scope

### Functional requirements

As a **user** you can do: 
- configure CLI application
  - set credentials of the exchange (apiKey, secretKey)
  - set default timeframe (e.g 1D, 4H, 1H)
  - set default quote currency (e.g USDT, BUSD) 
- display popular coins (displayed on the main page) 
- show last N timeframes of specified currency
    - if N is not specified - use default value
    - pprint results (colors are welcomed)
    - export results to file (csv/json)

### Non functional requirements
- all the code has to be documented
- the code must be well-structured
    - three main layers
        - API calls layer
        - business logic layer
        - CLI interface layer
    - [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
- code has to be formatted

## Technologies & tools
- Python3.8+
- [Binance API](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md)
- [Click](https://click.palletsprojects.com/en/7.x/) (CLI app implementation)
- [requests](https://requests.readthedocs.io/en/master/) (to perform Binance API requests)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) or other web scraping library
- [jq](https://pypi.org/project/jq/) or similar to pprint the results
- [black](https://github.com/psf/black/blob/master/docs/the_black_code_style.md) or similar for code formatting

## Installation process
The application can be installed from [GitLab PyPI private package registry](https://docs.gitlab.com/ee/user/packages/pypi_repository/). All the required dependencies are downloaded automatically.

## Additional information

[these](https://www.conventionalcommits.org/en/v1.0.0/#summary) is used to commit message guidelines.

