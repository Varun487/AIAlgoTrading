<template>
  <div>
    <h2>BACKTESTS</h2>
    <hr />
    <p class="no-backtests" v-if="!$store.getters.getBacktestReports.length">
      NO BACKTESTS AVAILABLE
    </p>
    <ul
      v-for="report in $store.getters.getBacktestReports"
      :key="report.start_date + report.end_date"
    >
      <div class="card">
        <h3>
          <span class="backtest-heading">BACKTEST</span>
          {{ report.strategy.name }} - {{ report.company.name }}
        </h3>
        <span class="date-time">From: </span>
        {{
          report.start_date_time.split("T")[0] +
          "  " +
          report.start_date_time.split("T")[1].slice(0, -1)
        }}
        <br />
        <span class="date-time">To: </span>
        {{
          report.end_date_time.split("T")[0] +
          "  " +
          report.end_date_time.split("T")[1].slice(0, -1)
        }}
        <br /><br />
        <span class="company">Company: </span> {{ report.company.name }}
        <br />
        <span class="company">Ticker: </span> {{ report.company.ticker }}
        <br />
        <span class="company">Sector: </span> {{ report.company.sector }}
        <br />
        <span class="company">Data provider: </span>
        {{ report.company.data_provider }}
        <br /><br />
        <span class="backtest">Max risk: </span> {{ report.max_risk }}%
        <br />
        <span class="backtest">Initial account size: </span> ₹
        {{ report.initial_account_size }}
        <br />
        <span class="backtest">Total profit: </span> ₹
        {{ Math.round(report.total_profit_loss) }}
        <br /><br />
        <span class="backtest-heading">Strategy: </span>
        {{ report.strategy.name }}
        <br />
        <span class="backtest-heading">Column: </span> {{ report.column }}
        <br />
        <span class="backtest-heading">Indicator time period: </span>
        {{ report.indicator_time_period }}
        <br />
        <span class="backtest-heading">Sigma: </span> {{ report.sigma }}
        <br /><br />
      </div>
    </ul>
  </div>
</template>

<script>
export default {
  name: "AllBacktests",
  mounted() {
    this.$store.dispatch("setBacktestReports");
  },
};
</script>

<style scoped>
h2 {
  opacity: 0.9;
}

.all-backtests-text {
  font-size: 20px;
  padding: 20px;
  opacity: 0.9;
}

.card {
  width: 25%;
  box-shadow: 0 4px 8px 0 lightblue;
  border-radius: 20px;
  transition: 0.3s;
  padding: 20px;
  opacity: 0.9;
  font-size: 20px;
  float: left;
  margin: 40px;
}

.card:hover {
  box-shadow: 0 4px 16px 0 #fa8072;
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

.no-backtests{
	font-size: 25px;
	opacity: 0.5;
	text-align: center;
	padding: 50px;
}

</style>
