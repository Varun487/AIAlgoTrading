<template>
  <div class="Endpoints">
    <h2>REST API Endpoints Overview</h2>
    <hr />
    <EndpointOverviewItem heading="Data Feeder" :links="DataFeederLinks" />
    <EndpointOverviewItem heading="Strategies" :links="StrategiesLinks" />
    <EndpointOverviewItem heading="Back Tester" :links="BackTesterLinks" />
    <EndpointOverviewItem heading="Paper Trader" :links="PaperTraderLinks" />
  </div>
</template>

<script>
import EndpointOverviewItem from "./EndpointOverviewItem.vue";

export default {
  name: "EndpointsOverviewList",
  components: {
    EndpointOverviewItem,
  },
  data() {
    return {
      DataFeederLinks: [
        {
          code: "GET /datafeeder/{string}",
          link: "#example-datafeeder",
        },
        {
          code: "GET /datafeeder/listcompanies/",
          link: "#list-companies",
        },
        {
          code: "POST /datafeeder/dataondemand/",
          link: "#data-ondemand",
        },
		{
          code: "POST /datafeeder/derivecandle/",
          link: "#derive-candle",
        },
		{
          code: "POST /datafeeder/getderivecandlestick/",
          link: "#get-derive-candlestick",
        },
		{
          code: "POST /datafeeder/derivedindicatorcalc/",
          link: "#derived-indicator-calc",
        },
      ],
      StrategiesLinks: [
        {
          code: "GET /strategies/{string}",
          link: "#example-strategies",
        },
        {
          code: "POST /strategies/getstrategies/",
          link: "#get-strategies/",
        },
      ],
      BackTesterLinks: [
        {
          code: "GET /backtester/{string}",
          link: "#example-backtester",
        },
      ],
      PaperTraderLinks: [
        {
          code: "GET /papertrader/{string}",
          link: "#example-papertrader",
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
