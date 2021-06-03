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
          @change="filterByStartDate"
        />
      </div>
      <div class="filter-item">
        <label>End date</label>
        <input
          class="inp"
          type="date"
          v-model="end_date"
          @change="filterByEndDate"
        />
      </div>
      <div class="filter-item">
        <label>Maximum risk </label>
        <input
          class="inp"
          type="number"
          v-model="max_risk"
          @change="filterByMaxRisk"
        />
        %
      </div>
      <div class="filter-item">
        <label>Company</label>
        <select
          name="Company"
          class="inp"
          v-model="company"
          @change="filterByCompany"
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
          @change="filterByStrategy"
        >
          <option value="Any">Any</option>
          <option value="SBB">Simple bollinger band test strategy</option>
        </select>
      </div>
      <div class="filter-item">
        <label>Dimension</label>
        <select
          name="Column"
          class="inp"
          v-model="dimension"
          @change="filterByDimension"
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
          @change="filterByTimePeriod"
        />
      </div>
      <!-- <button class="filter-button">FILTER</button> -->
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
    filterByStartDate() {
      console.log("Start Date Changed: ", this.start_date);
    },
    filterByEndDate() {
      console.log("End Date Changed: ", this.end_date);
    },
    filterByMaxRisk() {
      console.log("Max Risk Changed: ", this.max_risk);
    },
    filterByCompany() {
      console.log("Company Changed: ", this.company);
    },
    filterByStrategy() {
      console.log("Strategy Changed: ", this.strategy);
    },
    filterByDimension() {
      console.log("Dimension Changed: ", this.dimension);
    },
    filterByTimePeriod() {
      console.log("Time period Changed: ", this.time_period);
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

.filter-button {
  color: lightblue;
  background-color: transparent;
  border-radius: 20px;
  font-size: 20px;
  margin-top: 30px;
  padding: 10px;
  border-color: #fa8072;
}
</style>
