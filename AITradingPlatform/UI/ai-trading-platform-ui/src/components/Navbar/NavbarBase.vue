<template>
  <div id="nav">
    <Title />
	<hr class="separator"/>
    <Bar />
  </div>
</template>

<script>
import Title from "./Title.vue";
import Bar from "./Bar.vue";

export default {
  name: "Base",
  components: {
    Title,
    Bar,
  },
};
</script>

<style scoped>
#nav {
	background-color: #222222;
	margin-top: 0px;
	padding-top: 0px;
}

.separator{
	opacity: 0.2;
}
</style>
