<template>
  <div class="bar">
    <Link link="/" class="bar-element"/>
	<Link link="/home" name="Home" class="bar-element"/>
	<Link link="/about" name="About" class="bar-element"/>
	<Link link="/api" name="REST API Documentation" class="lastbar-element"/>
  </div>
</template>

<script>
import Link from "./Link.vue";

export default {
  name: "Bar",
  components: {
    Link,
  },
};
</script>

<style scoped>
.bar-element{
	display: inline;
}

.lastbar-element{
	display: inline;
	float: right;
	padding-right: 30px;
}

.bar{
	width: 100%;
	height: 30px;
}
</style>
