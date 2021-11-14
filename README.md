**ROUTES**

I. https://aus-exchange-rates-api.herokuapp.com/latest/
[GET]
Fetches the latest exchange rates. Uses the Open Exchange Rates API to do so.

RESPONSE:
200 Ok.

Returns the fetched data. 

Example:
https://aus-exchange-rates-api.herokuapp.com/latest/

Response:

{
    "latest rates": {
        "AED": 3.673,
        "AFN": 91.449995,
        "ALL": 106.8125,
        "AMD": 475.599248,
        "ANG": 1.802601,
        "AOA": 596.901,
        "ARS": 100.23626,
        "AUD": 1.363782,
        "AWG": 1.80025,
        "AZN": 1.700805,
        "BAM": 1.709179,

        ...
    }
}

II. https://aus-exchange-rates-api.herokuapp.com/historical/**some-date**
[GET]

Fetches the historical exchange rates data for the given date.
**Note:** The date must be given in the **MM-DD-YYYY** format only.

Response:
200 Ok.

1. Error message if the entered date format is incompatible.
2. Error message if the entered date is after or is the same as the present date.
3. Returns the fetched data.

Examples:

1. https://aus-exchange-rates-api.herokuapp.com/historical/11-19-2021

{
  'error' : 'The entered date is not valid for a historical lookup.'
}

2. https://aus-exchange-rates-api.herokuapp.com/historical/11:12:2021

{
    'error' : 'Incorrect date format, please enter a date in MM-DD-YYYY.'   
}

3. https://aus-exchange-rates-api.herokuapp.com/historical/11-2-2009

{
    "historical rates": {
        "AED": 3.673,
        "AFN": 91.449995,
        "ALL": 106.8125,
        "AMD": 475.599248,
        "ANG": 1.802601,
        "AOA": 596.901,
        "ARS": 100.23626,
        "AUD": 1.363782,
        "AWG": 1.80025,
        "AZN": 1.700805,
        "BAM": 1.709179,

        ...
    }
}
