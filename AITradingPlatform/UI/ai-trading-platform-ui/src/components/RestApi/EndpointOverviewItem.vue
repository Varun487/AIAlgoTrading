<template>
  <div>
    <h3>{{ heading }}</h3>
    <ul v-for="link in links" :key="link.code">
      <li>
        <a class="reflink" :href="link.link"><Code :codetext="link.code" /></a>
      </li>
    </ul>
  </div>
</template>

<script>
import Code from "../Common/Code.vue";

export default {
  name: "EndpointOverviewItem",
  components: {
    Code,
  },
  props: {
    heading: String,
    links: Array,
  },
};
</script>

<style scoped>
h3 {
  opacity: 90%;
}

a{
	color: #3291FF;
	opacity: 80%;
	font-size: 13px;
}
</style>
