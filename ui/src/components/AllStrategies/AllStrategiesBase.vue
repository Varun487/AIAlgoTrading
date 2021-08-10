<template>
    <div class="main-container">
        <Navbar />
        <SBase v-if="$store.getters.getAllStrategiesMainPage"/>
        <StrategyPageBase v-else/>
    </div>
</template>

<script>
import SBase from './StrategiesMain/SBase.vue'
import StrategyPageBase from '../StrategyPage/StrategyPageBase.vue'
import Navbar from "../TopNavbar/NavPostLogin.vue"

export default {
    name: 'AllStrategiesBase',
    components: {
        Navbar,
        SBase,
        StrategyPageBase,
    }
}
</script>
<style scoped>
.main-container {
    position: absolute;
    width: 100%;
    height: 160%;
    left: 0px;
    top: 80px;
}
</style>