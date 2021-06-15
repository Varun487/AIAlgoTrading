<template>
  <div>
    <TopBanner />
    <router-view id="main-content" :class="{ sidenavactive: $store.getters.getSideNavToggle }" />
  </div>
</template>

<script>
import TopBanner from "./TopBanner/TopBanner.vue";

export default {
  name: "Base",
  components: {
    TopBanner,
  },
};
</script>

<style scoped>
#main-content {
  margin-top: 100px;
}
.sidenavactive{
	margin-left: 150px;
	transition: all 0.5s;
}
</style>
