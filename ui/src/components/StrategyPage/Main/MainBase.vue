<template>
    <div class="strategy">
        
        <About />
        <MainLanding />
    </div>
</template>

<script>
import MainLanding from "./MainLanding.vue"
import About from "./About.vue"

export default {
    name: "StrategyPageMain",
    components: {
        
        About,
        MainLanding,
    },
};
</script>

<style scoped>
.landing {
    margin:0px;
}
</style>