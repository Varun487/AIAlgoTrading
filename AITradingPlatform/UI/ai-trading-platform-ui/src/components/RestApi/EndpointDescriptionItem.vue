<template>
  <div>
    <h2>{{ heading }}</h2>
    <hr />

    <ul v-for="api in apis" :key="api.code">
      <li class="DescItem">
        <b>{{ api.type }}</b> <Code :codetext="api.code" />
        <br />
        <br />

        {{ api.description }} 
        <br />

		<h4>Parameters: </h4>

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
    apis: Array,
  },
};
</script>

<style scoped>
h2 {
  opacity: 0.9;
  padding-top: 20px;
}

a {
  color: #3291ff;
  opacity: 0.8;
  font-size: 13px;
}

ul {
  list-style-type: none;
}

hr {
  opacity: 0.2;
}

.DescItem {
  padding: 20px;
}
</style>
