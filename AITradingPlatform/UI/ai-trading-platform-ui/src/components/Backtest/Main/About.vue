<template>
  <div>
    <h2>ABOUT</h2>
    <hr />
    <div class="about-text">
      A back test runs a strategy on historical data and generates orders. It
      then evaluates these orders and generates a report detailing the
      performance of the strategy over that period of time. Backtests are useful
      for determining the future permance of a strategy according to past
      performance.
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
};
</script>

<style scoped>
h2 {
  opacity: 0.9;
}

.about-text {
  font-size: 20px;
  padding: 20px;
  opacity: 0.9;
}
</style>
