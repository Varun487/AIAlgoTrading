<template>
  <div>
    <BacktestMain v-if="$store.getters.getBacktestsMainPage" />
    <BacktestReport v-else />
  </div>
</template>

<script>
import BacktestMain from "./Main/MainBase.vue";
import BacktestReport from "./Report/ReportBase.vue";

export default {
  name: "BacktestBase",
  components: {
    BacktestMain,
    BacktestReport,
  },
};
</script>

<style scoped>
</style>
