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
        },
        {
          type: "GET",
          code: "/datafeeder/listcompanies/",
          link: "https://aialgotrader.xyz/api/",
        },
        {
          type: "POST",
          code: "/datafeeder/dataondemand/",
          link: "https://aialgotrader.xyz/api/",
        },
      ],
      StrategiesApis: [
        {
          type: "GET",
          code: "/strategies/hello-strategies",
          link: "https://aialgotrader.xyz/api/",
        },
      ],
      BackTesterApis: [
        {
          type: "GET",
          code: "/backtester/hello-backtester",
          link: "https://aialgotrader.xyz/api/",
        },
      ],
      PaperTraderApis: [
        {
          type: "GET",
          code: "/papertrader/hello-papertrader",
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
