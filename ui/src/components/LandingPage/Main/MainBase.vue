<template>
    <div class="landing">
        <MainLanding />
        <About />
    </div>
</template>

<script>
import MainLanding from "./MainLanding.vue"
import About from "./About.vue"

export default {
    name: "LandingPageMain",
    components: {
        MainLanding,
        About,
    },
};
</script>

<style scoped>
.landing {
    margin:0px;
}
</style>