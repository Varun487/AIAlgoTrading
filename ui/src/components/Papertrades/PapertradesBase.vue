<template>
    <div class="main-pt">
        <Navbar />
        <PapertradesMain />
    </div>
</template>
<script>
import PapertradesMain from "./PaperTradesMain.vue"
import Navbar from "../TopNavbar/NavPostLogin.vue"
export default {
    name: "PaperTradesBase",
    components: {
        Navbar,
        PapertradesMain,
    },
}
</script>
<style scoped>
.main-pt {
    background-color: white;
    width: 100%;
    margin: 0px;
}
</style>