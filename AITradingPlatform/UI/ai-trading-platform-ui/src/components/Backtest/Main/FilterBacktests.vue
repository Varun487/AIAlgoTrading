<template>
  <div>
    <h2>FILTER BACKTESTS</h2>
    <hr />
    <div class="filter-text">
      You can filter all backtests according to the following criteria
      <div class="filter-item">
        <label>Start date</label>
        <input
          class="inp"
          type="date"
          v-model="start_date"
          @change="filterBacktests"
        />
      </div>
      <div class="filter-item">
        <label>End date</label>
        <input
          class="inp"
          type="date"
          v-model="end_date"
          @change="filterBacktests"
        />
      </div>
      <div class="filter-item">
        <label>Maximum risk </label>
        <input
          class="inp"
          type="number"
          v-model="max_risk"
          @change="filterBacktests"
        />
        %
      </div>
      <div class="filter-item">
        <label>Company</label>
        <select
          name="Company"
          class="inp"
          v-model="company"
          @change="filterBacktests"
        >
          <option value="Any">Any</option>
          <option value="Apple">Apple</option>
          <option value="TCS NSE">TCS NSE</option>
          <option value="TCS BSE">TCS BSE</option>
        </select>
      </div>
      <div class="filter-item">
        <label>Strategy</label>
        <select
          name="Strategy"
          class="inp"
          v-model="strategy"
          @change="filterBacktests"
        >
          <option value="Any">Any</option>
          <option value="Simple Bollinger Bands Strategy">
            Simple Bollinger Bands Strategy
          </option>
        </select>
      </div>
      <div class="filter-item">
        <label>Dimension</label>
        <select
          name="Dimension"
          class="inp"
          v-model="dimension"
          @change="filterBacktests"
        >
          <option value="Any">Any</option>
          <option value="Close">Close</option>
          <option value="Open">Open</option>
          <option value="High">High</option>
          <option value="Low">Low</option>
        </select>
      </div>
      <div class="filter-item">
        <label>Time period</label>
        <input
          class="inp"
          type="number"
          v-model="time_period"
          @change="filterBacktests"
        />
      </div>
      <button class="reset-button" @click="reset">RESET</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "FilterBacktests",
  data: function () {
    return {
      start_date: "",
      end_date: "",
      max_risk: "",
      time_period: "",
      company: "",
      strategy: "",
      dimension: "",
    };
  },
  methods: {
    reset() {
      this.start_date = "";
      this.end_date = "";
      this.max_risk = "";
      this.time_period = "";
      this.company = "";
      this.strategy = "";
      this.dimension = "";
      this.$store.dispatch("resetFilteredBacktestReports");
    },
    filterBacktests() {
      let filtered_bt = this.$store.getters.getBacktestsReports;

      if (this.start_date != "") {
        const start_dt = new Date(this.start_date);
        filtered_bt = filtered_bt.filter((report) => {
          const report_start_dt = new Date(report.start_date_time);
          return report_start_dt >= start_dt;
        });
      }

      if (this.end_date != "") {
        const end_dt = new Date(this.end_date);
        filtered_bt = filtered_bt.filter((report) => {
          const report_end_dt = new Date(report.end_date_time);
          return report_end_dt <= end_dt;
        });
      }

      if (this.max_risk != "" && this.max_risk != "0") {
        const max_risk = Number(this.max_risk);
        filtered_bt = filtered_bt.filter((report) => {
          const report_max_risk = Number(report.max_risk);
          return report_max_risk == max_risk;
        });
      }

      if (this.company != "" && this.company != "Any") {
        filtered_bt = filtered_bt.filter((report) => {
          const report_company = report.company.name;
          return report_company == this.company;
        });
      }

      if (this.strategy != "" && this.strategy != "Any") {
        filtered_bt = filtered_bt.filter((report) => {
          const report_strategy = report.strategy.name;
          return report_strategy == this.strategy;
        });
      }

      if (this.dimension != "" && this.dimension != "Any") {
        filtered_bt = filtered_bt.filter((report) => {
          const report_column = report.column;
          return report_column == this.dimension;
        });
      }

      if (this.time_period != "" && this.time_period != "0") {
        filtered_bt = filtered_bt.filter((report) => {
          const report_time_period = Number(report.indicator_time_period);
          return report_time_period == this.time_period;
        });
      }

      this.$store.dispatch("setFilteredBacktestsReports", filtered_bt);
    },
  },
};
</script>

<style scoped>
h2 {
  opacity: 0.9;
}

.filter-text {
  font-size: 20px;
  padding: 20px;
  opacity: 0.9;
}

.filter-item {
  padding-top: 20px;
}

label {
  padding-right: 20px;
}

.inp {
  background-color: transparent;
  color: white;
  border-color: lightblue;
  border-radius: 7px;
}

.reset-button {
  color: lightblue;
  background-color: transparent;
  border-radius: 20px;
  font-size: 20px;
  margin-top: 30px;
  padding: 10px;
  border-color: #fa8072;
}
</style>
