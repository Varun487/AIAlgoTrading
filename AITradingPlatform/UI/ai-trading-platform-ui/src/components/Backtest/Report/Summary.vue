<template>
  <div>
    <h2>SUMMARY</h2>
    <hr />
    <div v-if="$store.getters.getBacktestsSummaryLoading">Loading ...</div>
    <div v-else class="summary">
      <br /><br />
      <span class="date-time">From: </span>
      {{
        $store.getters.getBacktestReportData.start_date_time.split("T")[0] +
        "  " +
        $store.getters.getBacktestReportData.start_date_time
          .split("T")[1]
          .slice(0, -1)
      }}
      <br />
      <span class="date-time">To: </span>
      {{
        $store.getters.getBacktestReportData.end_date_time.split("T")[0] +
        "  " +
        $store.getters.getBacktestReportData.end_date_time
          .split("T")[1]
          .slice(0, -1)
      }}
      <br /><br />
      <span class="company">Company: </span>
      {{ $store.getters.getBacktestReportData.company.name }}
      <br />
      <span class="company">Ticker: </span>
      {{ $store.getters.getBacktestReportData.company.ticker }}
      <br />
      <span class="company">Sector: </span>
      {{ $store.getters.getBacktestReportData.company.sector }}
      <br />
      <span class="company">Data provider: </span>
      {{ $store.getters.getBacktestReportData.company.data_provider }}
      <br /><br />
      <span class="backtest">Max risk: </span>
      {{ $store.getters.getBacktestReportData.max_risk }}%
      <br />
      <span class="backtest">Initial account size: </span> ₹
      {{ $store.getters.getBacktestReportData.initial_account_size }}
      <br />
      <span class="backtest">Total profit: </span> ₹
      {{ Math.round($store.getters.getBacktestReportData.total_profit_loss) }}
      <br /><br />
      <span class="backtest-heading">Strategy: </span>
      {{ $store.getters.getBacktestReportData.strategy.name }}
      <br />
      <span class="backtest-heading">Column: </span>
      {{ $store.getters.getBacktestReportData.column }}
      <br />
      <span class="backtest-heading">Indicator time period: </span>
      {{ $store.getters.getBacktestReportData.indicator_time_period }}
      <br />
      <span class="backtest-heading">Sigma: </span>
      {{ $store.getters.getBacktestReportData.sigma }}
      <br /><br />
    </div>
  </div>
</template>

<script>
export default {
  name: "Summary",
  mounted() {
    this.$store.dispatch("setReportInfo", this.$store.getters.getBacktestId);
  },
};
</script>

<style scoped>
h2 {
  opacity: 0.9;
}

.summary {
  font-size: 20px;
}

.backtest-heading {
  color: lightblue;
}

.date-time {
  opacity: 0.8;
}

.company {
  color: #fa8072;
}

.backtest {
  color: lightgreen;
}
</style>
