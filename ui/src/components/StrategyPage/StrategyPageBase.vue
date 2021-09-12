<template>
    <div>
        
        <!-- <div v-for="strategy in $store.getters.getAllStrategies"
                :key="strategy.id"
            >
            <h1>{{ strategy.id }}</h1>
            <div @onload="showStrategy(strategy.id)">Go</div>
        </div> -->
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
    methods: {
        showStrategy(id) {
            this.$store.dispatch("setSelectedStrategy",id);
        this.$store.dispatch("setAllBacktests",id);
        this.$store.dispatch("setAllPapertrades",id);
    },
  },
    mounted() {
        this.$store.dispatch("setAllStrategies");
        // console.log(this.$store.getters.getStrategyId);
        this.$store.dispatch("setSelectedStrategy",this.$store.getters.getStrategyId);
        this.$store.dispatch("setAllBacktests",this.$store.getters.getStrategyId);
        this.$store.dispatch("setAllPapertrades",this.$store.getters.getStrategyId);
  },
};
</script>
<style scoped>
</style>