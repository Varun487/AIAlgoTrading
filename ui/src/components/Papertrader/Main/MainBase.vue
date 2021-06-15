<template>
    <div class="papertradermain">
        <Title />
        <About />
        <FilterPaperTrades />
        <AllPaperTrades />
        <FilterBody />
        <AllPaperTradesBody />
    </div>
</template>

<script>
import Title from "./Title.vue"
import About from "./About.vue"
import FilterPaperTrades from "./FilterPaperTrades.vue"
import AllPaperTrades from "./AllPaperTrades.vue"
import FilterBody from "./FilterBody.vue"
import AllPaperTradesBody from "./AllPaperTradesBody.vue"

export default {
    name: "PapertraderMain",
    components: {
        Title,
        About,
        FilterPaperTrades,
        AllPaperTrades,
        FilterBody,
        AllPaperTradesBody,
    },
};
</script>

<style scoped>
.papertradermain {
    margin:0px;
}
</style>