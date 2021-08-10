<template>
    <div>
        <Navbar />
        <LandingPageMain/>
    </div>
</template>

<script>
import LandingPageMain from "./Main/MainBase.vue"
import Navbar from "../TopNavbar/NavPreLogin.vue"

export default {
    name: "LandingPageBase",
    components: {
        Navbar,
        LandingPageMain,
    },
};
</script>
<style scoped>
</style>