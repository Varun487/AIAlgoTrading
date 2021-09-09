<template>
    <div>
        
        <!-- <div v-for="strategy in $store.getters.getAllStrategies"
                :key="strategy.id"
            >
            <h1>{{ strategy.id }}</h1>
            <div @onload="showStrategy(strategy.id)">Go</div>
        </div> -->
        <Navbar/>
        <BacktesterMain />
    </div>
</template>

<script>
import BacktesterMain from "./main/MainBase.vue"
import Navbar from "../TopNavbar/NavPostLogin.vue"

export default {
  name: "BacktestReportBase",
  components: {
    Navbar,
    BacktesterMain,
  },
  methods: {
    // addRows(){
    //   this.$store.commit('incrementRows',5);
    // }
  },
    mounted() {
    // this.$store.dispatch("setBacktestReportdata",21);
    // this.$store.dispatch("setTradeVisualization",21);
    // this.$store.dispatch("setTrades",21);
    // this.$store.dispatch("incrementRows",5);
    this.$store.dispatch("setAllBacktests",this.$store.getters.getStrategyId);
    this.$store.dispatch("setBacktestReportdata",this.$store.getters.getBacktestsId);
    this.$store.dispatch("setTradeVisualization",this.$store.getters.getBacktestsId);
    this.$store.dispatch("setTrades",this.$store.getters.getBacktestsId);
  },
}
</script>
<style scoped>
</style>