<template>
  <div>
    <h2>ACCOUNT SIZE</h2>
    <hr />
    <div v-if="$store.getters.getBacktestsAccountSizeLoading">Loading ...</div>
    <AccountSizeChart
      v-else
      class="AccountSize"
      :labels="$store.getters.getBacktestsTimeStamps"
      :data="$store.getters.getBacktestsAccountSizes"
    />
  </div>
</template>

<script>
import AccountSizeChart from "./AccountSizeChart.vue";

export default {
  name: "AccountSize",
  components: {
    AccountSizeChart,
  },
  mounted() {
    this.$store.dispatch("setOrdersData", this.$store.getters.getBacktestId);
  },
};
</script>

<style scoped>
h2 {
  opacity: 0.9;
}

.AccountSize {
  font-size: 20px;
  width: 100%;
  margin: auto;
  padding: 0px;
  padding-top: 100px;
  padding-bottom: 100px;
}
</style>
