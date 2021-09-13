<template>
    <div class="main-pt">
        <Navbar />
        <PapertradesMain />
        <FooterBase />
    </div>
</template>
<script>
import PapertradesMain from "./PaperTradesMain.vue"
import Navbar from "../TopNavbar/NavPostLogin.vue"
import FooterBase from "../Footer/FooterBase.vue"

export default {
    name: "PaperTradesBase",
    components: {
        Navbar,
        PapertradesMain,
        FooterBase,
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
