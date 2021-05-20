<template>
  <code>
    <pre>{{ text }}</pre>
  </code>
</template>

<script>
export default {
  name: "JsonBlock",
  props: {
    text: String,
  },
};
</script>

<style scoped>
pre{
	background-color: #222222;
	padding: 20px;
}
</style>
