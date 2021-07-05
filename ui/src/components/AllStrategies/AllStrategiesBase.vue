<template>
    <div class="main-container">
        <SBase v-if="$store.getters.getAllStrategiesMainPage"/>
        <StrategyPageBase v-else/>
    </div>
</template>

<script>
import SBase from './StrategiesMain/SBase.vue'
import StrategyPageBase from '../StrategyPage/StrategyPageBase.vue'

export default {
    name: 'AllStrategiesBase',
    components: {
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
    top: 0px;
    margin-top:10px;
}
</style>