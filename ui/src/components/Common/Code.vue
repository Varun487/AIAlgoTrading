<template>
  <code>{{ codetext }}</code>
</template>

<script>
export default {
  name: "Code",
  props: {
    codetext: String,
  },
};
</script>

<style scoped>
code {
  background-color: #333333;
  padding: 5px;
  border: 1px solid var(--nc-bg-3);
  border-radius: 6px;
}
</style>
