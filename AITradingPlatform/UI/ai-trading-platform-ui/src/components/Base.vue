<template>
	<div>
		<NavbarBase />
		<router-view />
	</div>
</template>

<script>
import NavbarBase from "./Navbar/NavbarBase.vue";

export default {
  name: "Base",
  components: {
    NavbarBase,
  },
};
</script>

<style scoped>
</style>
