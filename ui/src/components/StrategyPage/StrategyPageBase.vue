<template>
    <div>
        <Navbar/>
        <StrategyPageMain />
    </div>
</template>

<script>
import StrategyPageMain from "./Main/MainBase.vue"
import Navbar from "../TopNavbar/NavPostLogin.vue"

export default {
    name: "StrategyPageBase",
    components: {
        Navbar,
        StrategyPageMain,
    },
    mounted() {
    this.$store.dispatch("setSelectedStrategy",31);
  },
};
</script>
<style scoped>
</style>