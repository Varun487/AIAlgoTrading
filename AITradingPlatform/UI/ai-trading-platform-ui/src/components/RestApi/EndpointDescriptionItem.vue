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
  opacity: 90%;
  padding-top: 20px;
}

a {
  color: #3291ff;
  opacity: 80%;
  font-size: 13px;
}

ul {
  list-style-type: none;
}

hr {
  opacity: 20%;
}

.DescItem {
  padding: 20px;
}
</style>
