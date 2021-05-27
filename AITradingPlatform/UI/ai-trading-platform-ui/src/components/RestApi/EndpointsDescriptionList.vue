<template>
  <div class="Endpoints">
    <h2>REST API Endpoints</h2>
    <hr />
    <EndpointDescriptionItem heading="Data Feeder" :apis="DataFeederApis" />
    <EndpointDescriptionItem heading="Strategies" :apis="StrategiesApis" />
    <EndpointDescriptionItem heading="Back Tester" :apis="BackTesterApis" />
    <EndpointDescriptionItem heading="Paper Trader" :apis="PaperTraderApis" />
  </div>
</template>

<script>
import EndpointDescriptionItem from "./EndpointDescriptionItem.vue";

export default {
  name: "EndpointsDescriptionList",
  components: {
    EndpointDescriptionItem,
  },
  data() {
    return {
      DataFeederApis: [
        {
          type: "GET",
          code: "/datafeeder/{string}",
          link: "example-datafeeder",
          description:
            "An example api to test the working of the Data Feeder component of the project.",
          parameters: [
            {
              name: "string",
              type: "String",
              desc: "Enter any string in the url above",
            },
          ],
          req_url: "/datafeeder/hello-datafeeder",
          req_body: ``,
          correct_output: `{
    "name": "hello-datafeeder"
}`,
          failed_output: `{}`,
        },
        {
          type: "GET",
          code: "/datafeeder/listcompanies/",
          link: "list-companies",
          description: "Returns all companies data present in the database.",
          parameters: false,
          req_url: "/datafeeder/listcompanies/",
          req_body: ``,
          correct_output: `[
    {
        "name": "TCS BSE",
        "ticker": "TCS.BO",
        "sector": "Technology"
    },
    {
        "name": "TCS NSE",
        "ticker": "TCS.NS",
        "sector": "Technology"
    }
]`,
          failed_output: `{}`,
        },
        {
          type: "POST",
          code: "/datafeeder/dataondemand/",
          link: "data-ondemand",
          description:
            "Sources data (historical) within date range on demand from Yahoo! finance or AlphaVantage.",
          parameters: [
            {
              name: "companies",
              type: "Array of Strings",
              desc:
                "An array of strings mentioning the stock tickers to collect data from",
            },
            {
              name: "start_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to start collecting data for the list of stock tickers provided above.",
            },
            {
              name: "end_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to end collecting data for the list of stock tickers provided above.",
            },
            {
              name: "provider",
              type: "String",
              desc:
                "Data provider to source data from. Can only take values of 'Yahoo' and 'Alpha'",
            },
            {
              name: "time_period",
              type: "String",
              desc:
                "Mentions the time period of data to be collected. If sourcing from Yahoo finance, then value has to be 'daily'. Else, if sourcing from Alpha Vantage, can take any of the following values ['1min', '5min', '15min', '30min', '60min']",
            },
            {
              name: "slice",
              type: "String",
              desc:
                "Is applicable only for Alpha vantage, can take values in range('year1month1' to 'year1month12') and range('year2month1' to 'year2month12'). Even though the slice is not required for Yahoo Finance, it must be present and take a valid value for the request to be valid",
            },
          ],
          req_url: "/datafeeder/dataondemand/",
          req_body: `{
    "companies": ["TCS.NS", "TCS.BO"],
    "start_date": "2021-05-1 00:00:00",
    "end_date": "2021-05-15 00:00:00",
    "provider": "Yahoo",
    "time_period": "daily",
    "slice": "year1month1"
}`,
          correct_output: `{
    "status": "valid",
    "collected_data": [
        "TCS.NS",
        "TCS.BO"
    ],
    "data_not_found": [],
    "provider": "Yahoo"
}`,
          failed_output: `{
    "status": "Invalid request, please check the documentation for the correct request format."
}`,
        },
        {
          type: "POST",
          code: "/datafeeder/derivecandle/",
          link: "derive-candle",
          description: "Deriving the candlestick for a particular time range.",
          parameters: [
            {
              name: "company",
              type: "String",
              desc: "A String mentioning the stock ticker to collect data from",
            },
            {
              name: "start_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to start collecting data for the list of stock tickers provided above.",
            },
            {
              name: "end_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to end collecting data for the list of stock tickers provided above.",
            },
            {
              name: "provider",
              type: "String",
              desc:
                "Data provider to source data from. Can only take values of 'Yahoo' and 'Alpha'",
            },
            {
              name: "original_time_period",
              type: "String",
              desc:
                "Mentions the time period of data to be collected. If sourcing from Yahoo finance, then value has to be 'daily'. Else, if sourcing from Alpha Vantage, can take any of the following values ['1min', '5min', '15min', '30min', '60min']",
            },
            {
              name: "calculate_time_period",
              type: "Int",
              desc:
                "Mentions the aggregation time period or time window of the candle stick.",
            },
            {
              name: "slice",
              type: "String",
              desc:
                "Is applicable only for Alpha vantage, can take values in range('year1month1' to 'year1month12') and range('year2month1' to 'year2month12'). Even though the slice is not required for Yahoo Finance, it must be present and take a valid value for the request to be valid",
            },
          ],
          req_url: "/datafeeder/derivecandle/",
          req_body: `{
    "company": "TCS.BO",
    "start_date": "2021-04-1 00:00:00",
    "end_date": "2021-04-30 00:00:00",
    "provider": "Yahoo",
    "original_time_period": "daily",
    "calculate_time_period": 7,
    "slice": "year1month1"
}`,
          correct_output: `{
    "status": "Candle Sticks have been derived"
}`,
          failed_output: `{
    "status": "invalid request, please check the documentation for this request here"
}`,
        },
        {
          type: "POST",
          code: "/datafeeder/getderivecandlestick/",
          link: "get-derive-candlestick",
          description: "Lists the derived data in candlestick table.",
          parameters: [
            {
              name: "company",
              type: "String",
              desc: "A String mentioning the stock ticker to collect data from",
            },
            {
              name: "start_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to start collecting data for the list of stock tickers provided above.",
            },
            {
              name: "end_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to end collecting data for the list of stock tickers provided above.",
            },
            {
              name: "provider",
              type: "String",
              desc:
                "Data provider to source data from. Can only take values of 'Yahoo' and 'Alpha'",
            },
            {
              name: "original_time_period",
              type: "String",
              desc:
                "Mentions the time period of data to be collected. If sourcing from Yahoo finance, then value has to be 'daily'. Else, if sourcing from Alpha Vantage, can take any of the following values ['1min', '5min', '15min', '30min', '60min']",
            },
            {
              name: "calculate_time_period",
              type: "Int",
              desc:
                "Mentions the aggregation time period or time window of the candle stick.",
            },
            {
              name: "slice",
              type: "String",
              desc:
                "Is applicable only for Alpha vantage, can take values in range('year1month1' to 'year1month12') and range('year2month1' to 'year2month12'). Even though the slice is not required for Yahoo Finance, it must be present and take a valid value for the request to be valid",
            },
          ],
          req_url: "/datafeeder/getderivecandlestick/",
          req_body: `{
    "company": "TCS.BO",
    "start_date": "2021-04-1 00:00:00",
    "end_date": "2021-04-30 00:00:00",
    "provider": "Yahoo",
    "original_time_period": "daily",
    "calculate_time_period": 7,
    "slice": "year1month1"
}`,
          correct_output: `{
    "status": "valid",
    "company": {
        "name": "TCS BSE",
        "ticker": "TCS.BO",
        "sector": "Tech"
    },
    "data": [
        {
            "open": 3190.0,
            "low": 3146.0,
            "high": 3358.800048828125,
            "close": 3217.75,
            "volume": 1606737,
            "company": {
                "id": 2,
                "name": "TCS BSE",
                "ticker": "TCS.BO",
                "sector": "Tech"
            },
            "time_stamp": "2021-04-12T00:00:00Z",
            "time_period": "daily_7"
        }
    ]
}`,
          failed_output: `{
    "error": "No data present that fits all conditions. Please try sourcing the data or computing 
              indicators."
}`,
        },
        {
          type: "POST",
          code: "/datafeeder/indicatorsdata/",
          link: "indicators-data",
          description:
            "Lists the indicators data present in the database after filtering according to conditions provided.",
          parameters: [
            {
              name: "name",
              type: "String",
              desc:
                "The name of the indicator in the form {name}_{column}_{time_period}. example: 'SMA_Close_5'",
            },
            {
              name: "value_range_lower",
              type: "Integer",
              desc: "The lower value of range of indicator values to return.",
            },
            {
              name: "value_range_higher",
              type: "Integer",
              desc: "The higher value of range of indicator values to return.",
            },
            {
              name: "column",
              type: "String",
              desc:
                "The column on which indicator was computed. Can take values in ['Close', 'Open', 'High', 'Low', 'Volume'].",
            },
            {
              name: "indicator_time_period",
              type: "Integer",
              desc: "The time period of the indicator to list.",
            },
            {
              name: "company",
              type: "String",
              desc:
                "Stock ticker of company for which you want to list indicator data.",
            },
            {
              name: "candle_stick_period",
              type: "String",
              desc:
                "Mentions the time period of original immutable data collected for the company. Can take values in ['1min', '5min', '15min', '30min', '60min', 'daily']",
            },
            {
              name: "start_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes beginning the datetime for listing indicators data.",
            },
            {
              name: "end_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the last datetime for listing indicators data.",
            },
          ],
          req_url: "/datafeeder/indicatorsdata/",
          req_body: `{
    "name": "SMA_Close_5",
    "value_range_lower": 3000,
    "value_range_higher": 4000,
    "column": "Close",
    "indicator_time_period": 5,
    "company": "TCS.NS",
    "candle_stick_period": "daily",
    "start_date": "2021-05-1 00:00:00",
    "end_date": "2021-05-20 00:00:00"
}`,
          correct_output: `{
    "status": "valid",
    "indicator": "SMA_Close_5",
    "company": {
        "name": "TCS NSE",
        "ticker": "TCS.NS",
        "sector": "Technology"
    },
    "data": [
        {
            "value": 3084.050048828125,
            "name": "SMA_Close_5",
            "column": "Close",
            "indicator_time_period": 5,
            "candle_stick": {
                "id": 590,
                "open": 3100.0,
                "high": 3124.0,
                "low": 3078.0,
                "close": 3088.800048828125,
                "volume": 2098538,
                "time_stamp": "2021-05-18T00:00:00Z",
                "time_period": "daily",
                "company": 2
            }
        },
        {
            "value": 3075.930029296875,
            "name": "SMA_Close_5",
            "column": "Close",
            "indicator_time_period": 5,
            "candle_stick": {
                "id": 591,
                "open": 3084.0,
                "high": 3118.0,
                "low": 3067.10009765625,
                "close": 3082.0,
                "volume": 1986041,
                "time_stamp": "2021-05-19T00:00:00Z",
                "time_period": "daily",
                "company": 2
            }
        },
        {
            "value": 3070.410009765625,
            "name": "SMA_Close_5",
            "column": "Close",
            "indicator_time_period": 5,
            "candle_stick": {
                "id": 592,
                "open": 3067.10009765625,
                "high": 3088.800048828125,
                "low": 3052.10009765625,
                "close": 3060.0,
                "volume": 2329027,
                "time_stamp": "2021-05-20T00:00:00Z",
                "time_period": "daily",
                "company": 2
            }
        }
    ]
}`,
          failed_output: `{
    "error": "No data present that fits all conditions. Please try sourcing the data or computing indicators."
}`,
        },
        {
          type: "POST",
          code: "/datafeeder/derivedindicatorcalc/",
          link: "derived-indicator-calc",
          description:
            "Derive Indicator values for different time periods by calculating the standard deviation and simple moving average.",
          parameters: [
            {
              name: "company",
              type: "Array of Strings",
              desc:
                "An array of strings mentioning the stock tickers to collect data from",
            },
            {
              name: "start_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to start collecting data for the list of stock tickers provided above.",
            },
            {
              name: "end_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to end collecting data for the list of stock tickers provided above.",
            },
            {
              name: "provider",
              type: "String",
              desc:
                "Data provider to source data from. Can only take values of 'Yahoo' and 'Alpha'",
            },
            {
              name: "time_period",
              type: "String",
              desc:
                "Mentions the time period of data to be collected. If sourcing from Yahoo finance, then value has to be 'daily'. Else, if sourcing from Alpha Vantage, can take any of the following values ['1min', '5min', '15min', '30min', '60min']",
            },
            {
              name: "slice",
              type: "String",
              desc:
                "Is applicable only for Alpha vantage, can take values in range('year1month1' to 'year1month12') and range('year2month1' to 'year2month12'). Even though the slice is not required for Yahoo Finance, it must be present and take a valid value for the request to be valid",
            },
            {
              name: "column",
              type: "Array of Strings",
              desc:
                "An array of strings that can take values ['Open','Low','Close','Volume','High']",
            },
            {
              name: "indicator_time_period",
              type: "Integer",
              desc: "An integer mentioning the indicator time period",
            },
            {
              name: "name",
              type: "Array of Strings",
              desc:
                "An array of strings  that can take values ['SMA','Std_Dev','BB_down','BB_up']",
            },
          ],
          req_url: "/datafeeder/derivedindicatorcalc/",
          req_body: `{
    "company": "TCS.NS",
    "start_date": "2021-05-1 00:00:00",
    "end_date": "2021-05-15 00:00:00",
    "provider": "Yahoo",
    "time_period": "daily",
    "slice": "year1month1",
    "column": "Volume",
    "indicator_time_period":4,
    "name":"SMA"
}`,
          correct_output: `{
    "status": "sucess",
    "validation_status": "sucess",
    "collected_data": [
        "TCS.NS"
    ],
    "data_not_found": [],
    "retrieval_status": "sucess",
    "convert_dataframe_status": "sucess",
    "calculated_indicators_status": "sucess",
    "pushed_status": "sucess"
}`,
          failed_output: `{
    "status": "Invalid request, please check the documentation for the correct request format."
}`,
        },
        {
          type: "POST",
          code: "/datafeeder/listimmutable/",
          link: "list-immutable",
          description:
            "List all the immutable data that are filtered according to open, high, low, close, volume, company, time period values DONE",
          parameters: [
            {
              name: "company",
              type: "Array of Strings",
              desc:
                "An array of strings mentioning the stock tickers to collect data from",
            },
            {
              name: "start_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to start collecting data for the list of stock tickers provided above.",
            },
            {
              name: "end_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to end collecting data for the list of stock tickers provided above.",
            },

            {
              name: "time_period",
              type: "String",
              desc:
                "Mentions the time period of data to be collected. If sourcing from Yahoo finance, then value has to be 'daily'. Else, if sourcing from Alpha Vantage, can take any of the following values ['1min', '5min', '15min', '30min', '60min']",
            },
          ],
          req_url: "/datafeeder/listimmutable/",
          req_body: `{
    "company": "TCS.NS",
    "start_date": "2021-05-1 00:00:00",
    "end_date": "2021-05-15 00:00:00",
    "time_period": "daily"
    
}`,
          correct_output: `
    "validation_status": "sucess",
    "company": {
        "name": "tcs nse",
        "ticker": "TCS.NS",
        "sector": "tech"
    },
    "immutable": [
        {
            "open": 3024.89990234375,
            "low": 3004.0,
            "high": 3055.0,
            "close": 3037.0,
            "volume": 1545831,
            "company": {
                "id": 2,
                "name": "tcs nse",
                "ticker": "TCS.NS",
                "sector": "tech",
                "data_provider": "Yahoo"
            },
            "time_stamp": "2021-05-03T00:00:00Z",
            "time_period": "daily"
        },
        {
            "open": 3062.800048828125,
            "low": 3035.0,
            "high": 3090.0,
            "close": 3049.75,
            "volume": 1990777,
            "company": {
                "id": 2,
                "name": "tcs nse",
                "ticker": "TCS.NS",
                "sector": "tech",
                "data_provider": "Yahoo"
            },
            "time_stamp": "2021-05-04T00:00:00Z",
            "time_period": "daily"
        },
        {
            "open": 3070.0,
            "low": 3052.39990234375,
            "high": 3099.39990234375,
            "close": 3095.699951171875,
            "volume": 1939289,
            "company": {
                "id": 2,
                "name": "tcs nse",
                "ticker": "TCS.NS",
                "sector": "tech",
                "data_provider": "Yahoo"
            },
            "time_stamp": "2021-05-05T00:00:00Z",
            "time_period": "daily"
        },
        {
            "open": 3105.5,
            "low": 3074.0,
            "high": 3134.0,
            "close": 3111.449951171875,
            "volume": 1791671,
            "company": {
                "id": 2,
                "name": "tcs nse",
                "ticker": "TCS.NS",
                "sector": "tech",
                "data_provider": "Yahoo"
            },
            "time_stamp": "2021-05-06T00:00:00Z",
            "time_period": "daily"
        },
        {
            "open": 3133.0,
            "low": 3111.800048828125,
            "high": 3159.85009765625,
            "close": 3132.89990234375,
            "volume": 1912540,
            "company": {
                "id": 2,
                "name": "tcs nse",
                "ticker": "TCS.NS",
                "sector": "tech",
                "data_provider": "Yahoo"
            },
            "time_stamp": "2021-05-07T00:00:00Z",
            "time_period": "daily"
        },
        {
            "open": 3145.949951171875,
            "low": 3125.0,
            "high": 3164.199951171875,
            "close": 3145.5,
            "volume": 2137153,
            "company": {
                "id": 2,
                "name": "tcs nse",
                "ticker": "TCS.NS",
                "sector": "tech",
                "data_provider": "Yahoo"
            },
            "time_stamp": "2021-05-10T00:00:00Z",
            "time_period": "daily"
        },
        {
            "open": 3125.0,
            "low": 3091.14990234375,
            "high": 3128.10009765625,
            "close": 3122.60009765625,
            "volume": 2415625,
            "company": {
                "id": 2,
                "name": "tcs nse",
                "ticker": "TCS.NS",
                "sector": "tech",
                "data_provider": "Yahoo"
            },
            "time_stamp": "2021-05-11T00:00:00Z",
            "time_period": "daily"
        },
        {
            "open": 3120.0,
            "low": 3070.60009765625,
            "high": 3120.0,
            "close": 3087.60009765625,
            "volume": 1978558,
            "company": {
                "id": 2,
                "name": "tcs nse",
                "ticker": "TCS.NS",
                "sector": "tech",
                "data_provider": "Yahoo"
            },
            "time_stamp": "2021-05-12T00:00:00Z",
            "time_period": "daily"
        },
        {
            "open": 3098.5,
            "low": 3040.0,
            "high": 3098.5,
            "close": 3051.5,
            "volume": 2043935,
            "company": {
                "id": 2,
                "name": "tcs nse",
                "ticker": "TCS.NS",
                "sector": "tech",
                "data_provider": "Yahoo"
            },
            "time_stamp": "2021-05-14T00:00:00Z",
            "time_period": "daily"
        }
    ],
    "filtering status": "sucess"
}`,
          failed_output: `{
    "status": "Invalid request, please check the documentation for the correct request format."
}`,
        },
        {
          type: "POST",
          code: "/datafeeder/companydetails/",
          link: "company-details",
          description:
            "Returns a particular company's details that is present in the database.",
          parameters: [
            {
              name: "company",
              type: "String",
              desc: "A string mentioning the stock ticker to collect data from",
            },
          ],
          req_url: "/datafeeder/companydetails/",
          req_body: `{
    "company": "TCS.BO"
}`,
          correct_output: `[
    {
        "status": "valid",
        "company": {
            "name": "TCS BSE",
            "ticker": "TCS.BO",
            "sector": "Tech"
    }
]`,
          failed_output: `{'error': 'No such data present. Please enter a valid company name.'}`,
        },

        {
          type: "POST",
          code: "/datafeeder/filtercompany/",
          link: "filter-company",
          description: "Filters companies according to the sector.",
          parameters: [
            {
              name: "sector",
              type: "String",
              desc:
                "A string mentioning the sector according to which the data is filtered",
            },
          ],
          req_url: "/datafeeder/filtercompany/",
          req_body: `{
    "sector": "Tech"
}`,
          correct_output: `{
    "status": "valid",
    "data": [
        {
            "name": "Apple",
            "ticker": "AAPL",
            "sector": "Tech"
        },
        {
            "name": "TCS BSE",
            "ticker": "TCS.BO",
            "sector": "Tech"
        },
        {
            "name": "TCS NSE",
            "ticker": "TCS.NS",
            "sector": "Tech"
        },
        {
            "name": "Microsoft",
            "ticker": "MC",
            "sector": "Tech"
        }
    ]
}`,
          failed_output: `{
    'status': 'invalid'
}`,
        },
        {
          type: "POST",
          code: "/datafeeder/addcompany/",
          link: "add-company",
          description:
            "Adds a new company to the database if it doesn't already exist.",
          parameters: [
            {
              name: "name",
              type: "String",
              desc: "A string mentioning the name of the company.",
            },
            {
              name: "sector",
              type: "String",
              desc: "A string mentioning the sector of the company.",
            },
            {
              name: "ticker",
              type: "String",
              desc: "A string mentioning the stock ticker of the company.",
            },
          ],
          req_url: "/datafeeder/addcompany/",
          req_body: `{
    "name": "TCS BSE",
    "sector": "Tech",
    "ticker": "TCS.BO"
    
}`,
          correct_output: `{
    'status': 'Valid request. Company added successfully.'
}`,
          failed_output: `{
    'status': 'Invalid request. Company already exists in Database.'
}`,
        },
        {
          type: "POST",
          code: "/datafeeder/deletecompany/",
          link: "delete-company",
          description: "Deletes a company from the database if it exists.",
          parameters: [
            {
              name: "company",
              type: "String",
              desc: "A string mentioning the stock ticker to collect data from",
            },
          ],
          req_url: "/datafeeder/deletecompany/",
          req_body: `{
    "company": MS"
}`,
          correct_output: `{
    'data_deleted': 'success'
}`,
          failed_output: `{
    'error': 'No such data present. Please enter a valid company ticker.'
}`,
        },
        {
          type: "POST",
          code: "/datafeeder/modifycompanyattr/",
          link: "modify-company-attr",
          description:
            "Modifies the attributes of a company if it exists in the database.",
          parameters: [
            {
              name: "name",
              type: "String",
              desc:
                "A string mentioning the name of the company to modify attributes.",
            },
            {
              name: "new_name",
              type: "String",
              desc: "A string mentioning the updated name of the company.",
            },
            {
              name: "new_sector",
              type: "String",
              desc: "A string mentioning the updated sector of the company.",
            },
            {
              name: "new_ticker",
              type: "String",
              desc:
                "A string mentioning the updated stock ticker of the company.",
            },
          ],
          req_url: "/datafeeder/indicatorsdata/",
          req_body: `{
    "name": "TCS BSE",
    "new_name": "TCS BSE",
    "new_sector": "Tech",
    "new_ticker": "TCS",
}`,
          correct_output: `{
   'update': 'success'
}`,
          failed_output: `{
    'data':'Invalid request. Company does not exist in Database.'
}`,
        },
      ],
      StrategiesApis: [
        {
          type: "GET",
          code: "/strategies/{string}",
          link: "example-strategies",
          description:
            "An example api to test the working of the Strategies component of the project.",
          parameters: [
            {
              name: "string",
              type: "String",
              desc: "Enter any string in the url above",
            },
          ],
          req_url: "/strategies/hello-strategies",
          req_body: ``,
          correct_output: `{
    "name": "hello-strategies"
}`,
          failed_output: `{}`,
        },
        {
          type: "GET",
          code: "/strategies/getstrategies/",
          link: "get-strategies/",
          description: "Returns all the Strategies in the db.",
          parameters: false,
          req_url: "/strategies/getstrategies/",
          req_body: ``,
          correct_output: `{
    "status": "valid",
    "data": [
        {
            "name": "Simple Bollinger Bands Strategy",
            "desc": "Bollinger Bands consist of three bands—an upper, middle and lower band—that are 
                      used to spotlight extreme short-term prices in a security.",
            "sector": "Tech"
        }
    ]
}`,
          failed_output: `res = {
            'error': 'No data present in the db.'
        }`,
        },
        {
          type: "POST",
          code: "/strategies/runstrategy",
          link: "run-strategy",
          description:
            "Executes code to source data and calculate indicators then run a strategy on that data to generate orders.",
          parameters: [
            {
              name: "strategy",
              type: "String",
              desc:
                "Enter the name of the strategy to run. The only accepted value as of now is 'Simple Bollinger Bands Strategy'.",
            },
            {
              name: "candle_stick_data",
              type: "JSON object",
              desc:
                "Contains data about the candlesticks to source and run the strategy on.",
            },
            {
              name: "indicators_data",
              type: "JSON object",
              desc:
                "Contains data about the indicators to calculate and run the strategy on.",
            },
            {
              name: "company",
              type: "String",
              desc:
                "Mentions the stock ticker on which to run the strategy and generate orders.",
            },
            {
              name: "start_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to start running the stategy for the stock ticker.",
            },
            {
              name: "end_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to end running of the stategy for the stock ticker.",
            },
            {
              name: "provider",
              type: "String",
              desc:
                "Data provider to source data from. Can only take values of 'Yahoo' and 'Alpha'",
            },
            {
              name: "time_period",
              type: "String",
              desc:
                "Mentions the time period of data to be collected. If sourcing from Yahoo finance, then value has to be 'daily'. Else, if sourcing from Alpha Vantage, can take any of the following values ['1min', '5min', '15min', '30min', '60min']",
            },
            {
              name: "slice",
              type: "String",
              desc:
                "Is applicable only for Alpha vantage, can take values in range('year1month1' to 'year1month12') and range('year2month1' to 'year2month12'). Even though the slice is not required for Yahoo Finance, it must be present and take a valid value for the request to be valid",
            },
            {
              name: "column",
              type: "String",
              desc:
                "The column on which indicator was computed. Can take values in ['Close', 'Open', 'High', 'Low', 'Volume'].",
            },
            {
              name: "time_period",
              type: "Integer",
              desc: "The time period of the indicator to run the strategy on.",
            },
            {
              name: "sigma",
              type: "Integer",
              desc:
                "The standard deviations above and below the SMA to consider while running the 'Simple Bollinger Bands Strategy'.",
            },
          ],
          req_url: "/strategies/runstrategy",
          req_body: `{
    "strategy": "Simple Bollinger Bands Strategy",
    "candlestick_data": {
        "company": "TCS.BO",
        "provider": "Yahoo",
        "start_date": "2021-05-1 00:00:00",
        "end_date": "2021-05-20 00:00:00",
        "time_period": "daily",
        "slice": "year1month1"
    },
    "indicators_data": {
        "column": "Close",
        "time_period": 5,
        "sigma": 1
    }
}`,
          correct_output: `{
    "status": "success, orders created",
    "strategy": "Simple Bollinger Bands Strategy",
    "collected_data": [
        "TCS.BO"
    ],
    "data_not_collected": []
}`,
          failed_output: `{
    "error": "invalid request, please check the documentation for the correct request format"
}`,
        },
      ],
      BackTesterApis: [
        {
          type: "GET",
          code: "/backtester/{string}",
          link: "example-backtester",
          description:
            "An example api to test the working of the Back tester component of the project.",
          parameters: [
            {
              name: "string",
              type: "String",
              desc: "Enter any string in the url above",
            },
          ],
          req_url: "/backtester/hello-backtester",
          req_body: ``,
          correct_output: `{
    "name": "hello-backtester"
}`,
          failed_output: `{}`,
        },
        {
          type: "POST",
          code: "/backtester/generatereport/",
          link: "generate-report",
          description:
            "It takes a parameterised strategy and data over the period of the back test as input. It generates orders over the previous data according to the strategy's rules and pushes the report to the db.",
          parameters: [
            {
              name: "risk_ratio",
              type: "String",
              desc:
                "The risk ratio marks the prospective reward an investor can earn for every rupee they risk on an investment.",
            },
            {
              name: "max_risk",
              type: "float",
              desc:
                "The max risk risk percent is the one where the investor risks no more than the max risk percent of their available capital on any single trade.",
            },
            {
              name: "initial_acc",
              type: "float",
              desc:
                "It is the initial account balance before the order get generated. It is assummed to be in rupees.",
            },

            {
              name: "strategy",
              type: "String",
              desc:
                "Enter the name of the strategy to run. The only accepted value as of now is 'Simple Bollinger Bands Strategy'.",
            },
            {
              name: "candle_stick_data",
              type: "JSON object",
              desc:
                "Contains data about the candlesticks to source and run the strategy on.",
            },
            {
              name: "indicators_data",
              type: "JSON object",
              desc:
                "Contains data about the indicators to calculate and run the strategy on.",
            },
            {
              name: "company",
              type: "String",
              desc:
                "Mentions the stock ticker on which to run the strategy and generate orders.",
            },
            {
              name: "start_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to start running the stategy for the stock ticker.",
            },
            {
              name: "end_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to end running of the stategy for the stock ticker.",
            },
            {
              name: "provider",
              type: "String",
              desc:
                "Data provider to source data from. Can only take values of 'Yahoo' and 'Alpha'",
            },
            {
              name: "time_period",
              type: "String",
              desc:
                "Mentions the time period of data to be collected. If sourcing from Yahoo finance, then value has to be 'daily'. Else, if sourcing from Alpha Vantage, can take any of the following values ['1min', '5min', '15min', '30min', '60min']",
            },
            {
              name: "slice",
              type: "String",
              desc:
                "Is applicable only for Alpha vantage, can take values in range('year1month1' to 'year1month12') and range('year2month1' to 'year2month12'). Even though the slice is not required for Yahoo Finance, it must be present and take a valid value for the request to be valid",
            },
            {
              name: "column",
              type: "String",
              desc:
                "The column on which indicator was computed. Can take values in ['Close', 'Open', 'High', 'Low', 'Volume'].",
            },
            {
              name: "time_period",
              type: "Integer",
              desc: "The time period of the indicator to run the strategy on.",
            },
            {
              name: "sigma",
              type: "Integer",
              desc:
                "The standard deviations above and below the SMA to consider while running the 'Simple Bollinger Bands Strategy'.",
            },
          ],
          req_url: "/backtester/generatereport/",
          req_body: `{
    "risk_ratio" : "10:10",
    "max_risk" : 2,
    "initial_acc" : 1000000,
    "strategy": "Simple Bollinger Bands Strategy",
    "candlestick_data": {
        "company": "TCS.NS",
        "provider": "Yahoo",
        "start_date": "2021-05-1 00:00:00",
        "end_date": "2021-05-20 00:00:00",
        "time_period": "daily",
        "slice": "year1month1"
    },
    "indicators_data": {
        "column": "Close",
        "time_period": 5,
        "sigma": 1
    }
    
}`,
          correct_output: `{
    "status": "Valid"
}`,
          failed_output: `{
    "error": "invalid request, please check the documentation for this request here"
}`,
        },
        {
          type: "GET",
          code: "/backtester/viewallreports/",
          link: "view-all-reports",
          description:
            "Returns all the backtest reports present in the database.",
          parameters: false,
          req_url: "/backtester/viewallreports",
          req_body: ``,
          correct_output: `{
            "start_date_time": "2021-05-01T00:00:00Z",
            "end_date_time": "2021-05-20T00:00:00Z",
            "risk_ratio": "10:10",
            "max_risk": 2.0,
            "initial_account_size": 1000000.0,
            "final_account_size": 1001073.9985351562,
            "total_profit_loss": 1073.99853515625,
            "company": {
                  "id": 1,
                  "name": "TCS BSE",
                  "ticker": "TCS.BO",
                  "sector": "Technology",
                  "data_provider": "Yahoo"
              },
            "strategy": {
                  "id": 1,
                  "name": "Simple Bollinger Bands Strategy",
                  "desc": "Follows a simple algorithm:\r\n\r\nIf stock price > 'n' sigma above SMA, then create a  'SHORT' order\r\nIf stock price crosses SMA, then 'GET OUT OF ALL CURRENT POSITIONS'\r\nIf stock price < 'n' sigma above SMA, then create a  'BUY' order\r\nelse Don't create any order",
                  "sector": "All"
              },
            "column": "Close",
            "indicator_time_period": 5,
            "sigma": 1
          }`,
          failed_output: `{}`,
        },
        {
          type: "POST",
          code: "/backtester/filterreport/",
          link: "filter-report",
          description:
            "Returns backtest reports that are filtered according to start date, end date, risk ratio, max risk, initial account size, final account size, total profit loss, company, strategy",
          parameters:[
            {
              name: "start_date_time",
              type: "Date time string",
              desc: "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to start collecting data for the list of stock tickers.",
            },
            {
              name: "end_date_time",
              type: "Date time string",
              desc: "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to end collecting data for the list of stock tickers.",
            },
            {
              name: "risk_ratio",
              type: "String",
              desc: "The risk ratio marks the prospective reward an investor can earn for every rupee they risk on an investment.",
            },
            {
              name: "max_risk",
              type: "Float",
              desc: "The max risk risk percent is the one where the investor risks no more than the max risk percent of their available capital on any single trade.",
            },
            {
              name: "initial_account_size",
              type: "Float",
              desc: "It is the initial account balance before the order get generated.",
            },
            {
              name: "final_account_size",
              type: "Float",
              desc: "It is the final account balance after the order is generated.",
            },
            {
              name: "total_profit_loss",
              type: "Float",
              desc: "Indicates whether the order generated resulted in a profit or a loss. The order generated by using the strategy.",
            },
            {
              name: "company",
              type: "String",
              desc: "Mentions the stock ticker for which to generate report.",
            },
            {
              name: "strategy",
              type: "String",
              desc: "A string mentioning the name of the strategy associated with the order. The only accepted value as of now is 'Simple Bollinger Bands Strategy'.",
            },
            {
              name: "column",
              type: "String",
              desc: "The column on which indicator was computed. Can take values in ['Close', 'Open', 'High', 'Low', 'Volume'].",
            },
            {
              name: "indicator_time_period ",
              type: "String",
              desc: "A string mentioning the name of the strategy stored in the database.",
            },
            {
              name: "sigma ",
              type: "String",
              desc: "The standard deviations above and below the SMA to consider while running the 'Simple Bollinger Bands Strategy'.",
            },
          ],
          req_url: "/backtester/filterreport",
          req_body: `{
            "start_date_time": "2021-05-01 00:00:00",
            "end_date_time": "2021-05-20 00:00:00",
            "risk_ratio": "10:10",
            "max_risk": 2.0,
            "initial_account_size": 1000000.0,
            "company": "TCS.BO",
            "strategy": "Simple Bollinger Bands Strategy",
            "column": "Close",
            "indicator_time_period": 5,
            "sigma": 1
          }`,
          correct_output: `{
          "status": "Valid request",
    "data": [
        {
            "start_date_time": "2021-05-01T00:00:00Z",
            "end_date_time": "2021-05-20T00:00:00Z",
            "risk_ratio": "10:10",
            "max_risk": 2.0,
            "initial_account_size": 1000000.0,
            "final_account_size": 1001073.9985351562,
            "total_profit_loss": 1073.99853515625,
            "company": {
                "id": 1,
                "name": "TCS BSE",
                "ticker": "TCS.BO",
                "sector": "Technology",
                "data_provider": "Yahoo"
            },
            "strategy": {
                "id": 1,
                "name": "Simple Bollinger Bands Strategy",
                "desc": "Follows a simple algorithm:\r\n\r\nIf stock price > 'n' sigma above SMA, then create a  'SHORT' order\r\nIf stock price crosses SMA, then 'GET OUT OF ALL CURRENT POSITIONS'\r\nIf stock price < 'n' sigma above SMA, then create a  'BUY' order\r\nelse Don't create any order",
                "sector": "All"
            },
            "column": "Close",
            "indicator_time_period": 5,
            "sigma": 1
          }`,
          failed_output: `{'status':'Invalid request, please check the documentation for the appropriate request here'}`,
        },
        {
          type: "GET",
          code: "/backtester/getorders/",
          link: "get-orders",
          description: "Lists all backtested orders of a particular report",
          parameters: [
            {
              name: "strategy",
              type: "String",
              desc:
                "Enter the name of the strategy backtested in the report. The only accepted value as of now is 'Simple Bollinger Bands Strategy'.",
            },
            {
              name: "company",
              type: "String",
              desc:
                "Mentions the stock ticker on which to run the strategy and generate orders.",
            },
            {
              name: "start_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to start running the stategy for the stock ticker.",
            },
            {
              name: "end_date",
              type: "Date time string",
              desc:
                "A string in the format of yyyy-mm-dd hh:MM:ss. It denotes the datetime to end running of the stategy for the stock ticker.",
            },
            {
              name: "column",
              type: "String",
              desc:
                "The column on which indicator was computed. Can take values in ['Close', 'Open', 'High', 'Low', 'Volume'].",
            },
            {
              name: "indicator_time_period",
              type: "Integer",
              desc: "The time period of the indicator to run the strategy on.",
            },
            {
              name: "sigma",
              type: "Integer",
              desc:
                "The standard deviations above and below the SMA to consider while running the backtest for 'Simple Bollinger Bands Strategy'.",
            },
            {
              name: "max_risk",
              type: "Float",
              desc: "The max risk percent of the backtest report.",
            },
          ],
          req_url: "/backtester/getorders/",
          req_body: `{
    "company": "TCS.BO",
    "start_date": "2021-05-1 00:00:00",
    "end_date": "2021-05-20 00:00:00",
    "strategy":"Simple Bollinger Bands Strategy",
    "column": "Close",
    "indicator_time_period":5,
    "sigma":1,
    "max_risk":2.0
}`,
          correct_output: `{
    "backtestorders": [
        {
            "order": {
                "id": 18,
                "order_type": "G",
                "order_category": "M",
                "time_stamp": "2021-05-12T00:00:00Z",
                "profit_loss": 0.0,
                "quantity": 0,
                "company": 1
            },
            "backtestreport": {
                "id": 2,
                "start_date_time": "2021-05-01T00:00:00Z",
                "end_date_time": "2021-05-20T00:00:00Z",
                "max_risk": 2.0,
                "risk_ratio": "10:10",
                "initial_account_size": 1000000.0,
                "final_account_size": 1001073.9985351562,
                "total_profit_loss": 1073.99853515625,
                "column": "Close",
                "indicator_time_period": 5,
                "sigma": 1,
                "company": 1,
                "strategy": 1
            },
            "account_size": 1001001.0991210938
        },
        {
            "order": {
                "id": 19,
                "order_type": "B",
                "order_category": "M",
                "time_stamp": "2021-05-14T00:00:00Z",
                "profit_loss": 12.14990234375,
                "quantity": 6,
                "company": 1
            },
            "backtestreport": {
                "id": 2,
                "start_date_time": "2021-05-01T00:00:00Z",
                "end_date_time": "2021-05-20T00:00:00Z",
                "max_risk": 2.0,
                "risk_ratio": "10:10",
                "initial_account_size": 1000000.0,
                "final_account_size": 1001073.9985351562,
                "total_profit_loss": 1073.99853515625,
                "column": "Close",
                "indicator_time_period": 5,
                "sigma": 1,
                "company": 1,
                "strategy": 1
            },
            "account_size": 982582.298828125
        },
    ],
    "status": "Sucess"
}`,
          failed_output: `{
    "status": "invalid request, please check the documentation for the correct reqiest format"
}`,
        },
      ],
      PaperTraderApis: [
        {
          type: "GET",
          code: "/papertrader/{string}",
          link: "example-papertrader",
          description:
            "An example api to test the working of the Paper Trader component of the project.",
          parameters: [
            {
              name: "string",
              type: "String",
              desc: "Enter any string in the url above",
            },
          ],
          req_url: "/papertrader/hello-papertrader",
          req_body: ``,
          correct_output: `{
    "name": "hello-papertrader"
}`,
          failed_output: `{}`,
        },
        {
          type: "GET",
          code: "/papertrader/getstrategies",
          link: "get-strategies",
          description:
            "An api for  listing all currently  papertraded strategies",
          parameters:false,
          req_url: "/papertrader/getstrategies/",
          req_body: ``,
          correct_output: `{
    "status": "Sucess",
    "Strategies": [
        {
            "strategy": {
                "id": 1,
                "name": "Simple Bollinger Bands Strategy",
                "desc": "jhvweifhawigf/DJ/uv/P;JQHidasb;ojWKCBDJL",
                "sector": "all"
            },
            "company": {
                "id": 3,
                "name": "tcs bse",
                "ticker": "TCS.BO",
                "sector": "tech",
                "data_provider": "Yahoo"
            },
            "column": "Close",
            "time_period": 5,
            "sigma": 1,
            "name": "tcs bse bb close 5 1"
        }
    ]
}`,
          failed_output: `{}`,
        },
      ],
    };
  },
};
</script>

<style scoped>
.Endpoints {
  margin: auto;
  width: 50%;
  padding-top: 20px;
}
</style>
