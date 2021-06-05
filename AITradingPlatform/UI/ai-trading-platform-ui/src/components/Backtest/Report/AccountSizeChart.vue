<template>
  <LineChart :chart-data="datacollection" :height="200" />
</template>

<script>
import LineChart from "./LineChart.js";

export default {
  name: "AccountSizeChart",
  props: {
    labels: Array,
    data: Array,
  },
  components: {
    LineChart,
  },
  data() {
    return {
      datacollection: null,
    };
  },
  mounted() {
    this.fillData();
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: this.labels,
        datasets: [
          {
            label: "Account Size",
            borderColor: "lightblue",
            hoverBackgroundColor: "red",
            pointBackgroundColor: "lightblue",
            pointRadius: "5",
            tension: 0.1,
            spanGaps: true,
            clip: 0,
            data: this.data,
          },
        ],
      };
    },
  },
};
</script>

<style>
</style>
