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
              desc: "Is applicable only for Alpha vantage, can take values in range('year1month1' to 'year1month12') and range('year2month1' to 'year2month12'). Even though the slice is not required for Yahoo Finance, it must be present and take a valid value for the request to be valid",
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
          description:
            "Deriving the candlestick for a particular time range.",
          parameters: [
            {
              name: "company",
              type: "String",
              desc:
                "A String mentioning the stock ticker to collect data from",
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
              desc: "Is applicable only for Alpha vantage, can take values in range('year1month1' to 'year1month12') and range('year2month1' to 'year2month12'). Even though the slice is not required for Yahoo Finance, it must be present and take a valid value for the request to be valid",
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
          description:
            "Lists the derived data in candlestick table.",
          parameters: [
            {
              name: "company",
              type: "String",
              desc:
                "A String mentioning the stock ticker to collect data from",
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
              desc: "Is applicable only for Alpha vantage, can take values in range('year1month1' to 'year1month12') and range('year2month1' to 'year2month12'). Even though the slice is not required for Yahoo Finance, it must be present and take a valid value for the request to be valid",
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
          description:
            "Returns all the Strategies in the db.",
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
