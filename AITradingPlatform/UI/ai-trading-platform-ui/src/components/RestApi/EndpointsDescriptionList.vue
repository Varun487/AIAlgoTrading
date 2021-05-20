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
          link: "https://aialgotrader.xyz/api/",
          description:
            "An example api to test the working of the Data Feeder component of the project.",
          parameters: [],
        },
        {
          type: "GET",
          code: "/datafeeder/listcompanies/",
          link: "https://aialgotrader.xyz/api/",
          description: "Returns all companies data present in the database.",
          parameters: [],
        },
        {
          type: "POST",
          code: "/datafeeder/dataondemand/",
          link: "https://aialgotrader.xyz/api/",
          description:
            "Sources data (historical) on demand from Yahoo! finance or AlphaVantage.",
          parameters: [],
        },
      ],
      StrategiesApis: [
        {
          type: "GET",
          code: "/strategies/hello-strategies",
          link: "https://aialgotrader.xyz/api/",
          description:
            "An example api to test the working of the Strategies component of the project.",
          parameters: [],
        },
      ],
      BackTesterApis: [
        {
          type: "GET",
          code: "/backtester/hello-backtester",
          link: "https://aialgotrader.xyz/api/",
          description:
            "An example api to test the working of the Back tester component of the project.",
          parameters: [],
        },
      ],
      PaperTraderApis: [
        {
          type: "GET",
          code: "/papertrader/hello-papertrader",
          link: "https://aialgotrader.xyz/api/",
          description:
            "An example api to test the working of the Paper Trader component of the project.",
          parameters: [],
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
