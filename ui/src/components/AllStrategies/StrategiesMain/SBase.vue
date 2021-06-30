<template>
<div>
    
    <Topbanner />
    <MidSection />
    
    <Footer />
</div>
    
</template>
<script>

import Topbanner from './Topbanner.vue'
import MidSection from './MidSection.vue'

import Footer from './Footer.vue'

export default {
    name : 'SBase',
    components: {
        
        Topbanner,
        MidSection,
        
        Footer,
  }
}
</script>
<style scoped>

</style>