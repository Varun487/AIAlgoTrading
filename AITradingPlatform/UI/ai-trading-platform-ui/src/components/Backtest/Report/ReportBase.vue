<template>
  <div class="report-base">
    <div class="go-back" @click="$store.dispatch('flipBacktestsMainPage')">
      <b>←</b> BACK
    </div>
    <h1>Backtest Report page</h1>
  </div>
</template>

<script>
export default {
  name: "BacktestReport",
};
</script>

<style scoped>
.report-base {
  width: 90%;
  margin: auto;
}

.go-back {
  font-size: 20px;
  cursor: pointer;
}

.go-back:hover {
  font-size: 22px;
  color: lightblue;
  cursor: pointer;
}
</style>
