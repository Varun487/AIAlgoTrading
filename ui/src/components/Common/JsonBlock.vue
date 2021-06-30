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
  color: #FFFFFF;
	padding: 20px;
  border: 1px solid #000000;
  border-radius: 10px;
  width: 600px;
}
</style>
