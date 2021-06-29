<template>
  <div id="nav">
    
    <Navbar />
    <!-- <hr class="separator" /> -->
	
  </div>
</template>

<script>
import Navbar from "./Navbar.vue";


export default {
  name: "TopBanner",
  components: {
    Navbar,
    
  },
};
</script>

<style scoped>
#nav {
  background-color: #222222;
  margin-top: 0px;
  padding-top: 0px;
  margin-bottom: 0px;
  margin-left: 0px;
  position: fixed;
  z-index: 100;
  width: 100%;
  top: 0px;
}

.separator {
  opacity: 0.2;
}
</style>
