<template>
  <div id="nav">
    <!--
    <SideNavButton />
    <Title />
    <SideNavBar />
    -->
    <Navbar />
  </div>
</template>

<script>
/*
import Title from "./Title.vue";
import SideNavButton from "./SideNavButton.vue";
import SideNavBar from "../Navbar/SideNavBar.vue";
*/
import Navbar from "./Navbar.vue"
export default {
  name: "TopBanner",
  components: {
    Navbar,
    /*
    Title,
    SideNavButton,
    SideNavBar,
    */
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
