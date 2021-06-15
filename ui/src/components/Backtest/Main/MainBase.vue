<template>
  <div class="backtestmain">
    <Title />
    <About />
    <FilterBacktests />
    <AllBacktests />
  </div>
</template>

<script>
import Title from "./Title.vue";
import About from "./About.vue";
import FilterBacktests from "./FilterBacktests.vue";
import AllBacktests from "./AllBacktests.vue";

export default {
  name: "BacktestMain",
  components: {
    Title,
    About,
    FilterBacktests,
    AllBacktests,
  },
};
</script>

<style scoped>
.backtestmain {
  margin: auto;
  width: 90%;
}
</style>
