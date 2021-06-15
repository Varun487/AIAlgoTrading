<template>
  <p class="note">
    <b>NOTE:</b> Base URL for all REST API endpoints is <Code codetext="/api" />
  </p>
</template>

<script>
import Code from "../Common/Code.vue";

export default {
  name: "Note",
  components: {
    Code,
  },
};
</script>

<style scoped>
.note {
  text-align: center;
}
</style>

