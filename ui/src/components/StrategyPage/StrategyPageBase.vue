<template>
    <div>
        <StrategyPageMain />
    </div>
</template>

<script>
import StrategyPageMain from "./Main/MainBase.vue"
export default {
    name: "StrategyPageBase",
    components: {
        StrategyPageMain,
    },
    mounted() {
    this.$store.dispatch("setSelectedStrategy",2);
    this.$store.dispatch("setAllBacktests",2);
  },
};
</script>
<style scoped>
</style>