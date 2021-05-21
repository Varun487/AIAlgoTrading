<template>
  <div>
    <router-link class="link" :to="link"> {{ name }} </router-link>
  </div>
</template>

<script>
export default {
  name: "Link",
  props: {
    link: String,
    name: String,
  },
};
</script>

<style scoped>
.link{
	text-decoration: none;
	padding: 10px;
	font-size: 20px;
	opacity: 0.5;
	color: white;
}

.router-link-exact-active{
	opacity: 1.0;
}

</style>
