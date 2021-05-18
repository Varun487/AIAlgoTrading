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
          code: "GET /datafeeder/hello-datafeeder",
          link: "https://aialgotrader.xyz/api/",
        },
        {
          code: "GET /datafeeder/listcompanies/",
          link: "https://aialgotrader.xyz/api/",
        },
        {
          code: "POST /datafeeder/dataondemand/",
          link: "https://aialgotrader.xyz/api/",
        },
      ],
      StrategiesLinks: [
        {
          code: "GET /strategies/hello-strategies",
          link: "https://aialgotrader.xyz/api/",
        },
      ],
      BackTesterLinks: [
        {
          code: "GET /backtester/hello-backtester",
          link: "https://aialgotrader.xyz/api/",
        },
      ],
      PaperTraderLinks: [
        {
          code: "GET /papertrader/hello-papertrader",
          link: "https://aialgotrader.xyz/api/",
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
