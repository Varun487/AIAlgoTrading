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
          code: "POST /datafeeder/indicatorsdata/",
          link: "#indicators-data",
        },
        {
          code: "POST /datafeeder/derivedindicatorcalc/",
          link: "#derived-indicator-calc",
        },
        {
          code: "POST /datafeeder/listimmutable/",
          link: "#list-immutable",
        },
        {
          code: "POST /datafeeder/companydetails/",
          link: "#company-details",
        },
        {
          code: "POST /datafeeder/filtercompany/",
          link: "#filter-company",
        },
        {
          code: "POST /datafeeder/addcompany/",
          link: "#add-company",
        },
        {
          code: "POST /datafeeder/deletecompany/",
          link: "#delete-company",
        },
        {
          code: "POST /datafeeder/modifycompanyattr/",
          link: "#modify-company-attr",
        },
      ],
      StrategiesLinks: [
        {
          code: "GET /strategies/{string}",
          link: "#example-strategies",
        },
        {
          code: "GET /strategies/getstrategies/",
          link: "#get-strategies/",
        },
        {
          code: "POST /strategies/runstrategy/",
          link: "#run-strategy",
        },
      ],
      BackTesterLinks: [
        {
          code: "GET /backtester/{string}",
          link: "#example-backtester",
        },
        {
          code: "GET /strategies/getorders/",
          link: "#get-orders",
        },
        {
          code: "GET /backtester/generatereport/",
          link: "#generate-report",
        },
        {
          code: "GET /backtester/viewallreports",
          link: "#view-all-reports",
        },
        {
          code: "GET /backtester/filterreport",
          link: "#filter-report",
        },
        {
          code: "GET /backtester/getorders/",
          link: "#get-orders",
        },
      ],
      PaperTraderLinks: [
        {
          code: "GET /papertrader/{string}",
          link: "#example-papertrader",
        },
        {
          code: "GET /papertrader/getstrategies",
          link: "#get-strategies",
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
