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
    this.$store.dispatch("setSelectedStrategy",31);
  },
};
</script>
<style scoped>
</style>