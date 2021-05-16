<template>
  <div class="Endpoints">
    <h2>Endpoints overview</h2>
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
          link: "http://localhost:8080/api/",
        },
        {
          code: "GET /datafeeder/listcompanies/",
          link: "http://localhost:8080/api/",
        },
        {
          code: "POST /datafeeder/dataondemand/",
          link: "http://localhost:8080/api/",
        },
      ],
      StrategiesLinks: [
        {
          code: "GET /strategies/hello-strategies",
          link: "http://localhost:8080/api/",
        },
      ],
      BackTesterLinks: [
        {
          code: "GET /backtester/hello-backtester",
          link: "http://localhost:8080/api/",
        },
      ],
      PaperTraderLinks: [
        {
          code: "GET /papertrader/hello-papertrader",
          link: "http://localhost:8080/api/",
        },
      ],
    };
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  opacity: 90%;
}

.Endpoints {
  margin: auto;
  width: 50%;
  padding-top: 20px;
}
</style>
