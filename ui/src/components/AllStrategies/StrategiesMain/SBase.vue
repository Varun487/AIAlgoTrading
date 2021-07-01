<template>
<div>
    
    <Topbanner />
    <MidSection />
    
    <FooterBase />
</div>
    
</template>
<script>

import Topbanner from './Topbanner.vue'
import MidSection from './MidSection.vue'

import FooterBase from '../../Footer/FooterBase.vue'

export default {
    name : 'SBase',
    components: {
        
        Topbanner,
        MidSection,
        
        FooterBase,
  }
}
</script>
<style scoped>

</style>