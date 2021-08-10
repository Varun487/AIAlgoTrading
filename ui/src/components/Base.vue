<template>
  <div>
    <router-view id="main-content" :class="{ sidenavactive: $store.getters.getSideNavToggle }" />
  </div>
</template>

<script>

export default {
  name: "Base",
  components: {
  },
};
</script>

<style scoped>

#main-content {
  margin-top: 10px;
  padding-top: 10px;
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
}
.sidenavactive{
	margin-left: 150px;
	transition: all 0.5s;
}
/* 
#main-content {
  margin-top: 100px;
}
.sidenavactive{
	margin-left: 150px;
	transition: all 0.5s;
}
*/
</style>
