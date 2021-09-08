<template>
<div>
    
    <Topbanner />
    <MidSection />
    
    
</div>
    
</template>
<script>

import Topbanner from './Topbanner.vue'
import MidSection from './MidSection.vue'



export default {
    name : 'SBase',
    components: {
        
        Topbanner,
        MidSection,
        
        
  }
}
</script>
<style scoped>

</style>