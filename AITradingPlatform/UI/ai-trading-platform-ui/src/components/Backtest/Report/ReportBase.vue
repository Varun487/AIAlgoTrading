<template>
  <div class="report-base">
    <BackButton />
    <Title />
    <Summary />
    <AccountSize />
  </div>
</template>

<script>
import BackButton from "./BackButton.vue";
import Title from "./Title.vue";
import Summary from "./Summary.vue";
import AccountSize from "./AccountSize.vue";

export default {
  name: "BacktestReport",
  components: {
    BackButton,
    Title,
    Summary,
    AccountSize,
  },
};
</script>

<style scoped>
.report-base {
  width: 90%;
  margin: auto;
}
</style>
