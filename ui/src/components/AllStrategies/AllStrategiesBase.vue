<template>
    <div class="main-container">
        <SBase v-if="$store.getters.getAllStrategiesMainPage"/>
    </div>
</template>

<script>
import SBase from './StrategiesMain/SBase.vue'

export default {
    name: 'AllStrategiesBase',
    components: {
        SBase,
    }
}
</script>
<style scoped>
.main-container {
    position: absolute;
    width: 100%;
    height: 280%;
    left: 0px;
    top: 0px;
    margin-top:10px;
}
</style>