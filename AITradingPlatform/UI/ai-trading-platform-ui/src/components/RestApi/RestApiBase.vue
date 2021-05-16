<template>
  <div>
    <Title />
    <Note />
    <EndpointsOverviewList />
  </div>
</template>

<script>
import Title from "./Title.vue";
import EndpointsOverviewList from "./EndpointsOverviewList.vue";
import Note from "./Note.vue";

export default {
  name: "RestApiBase",
  components: {
    Title,
    Note,
    EndpointsOverviewList,
  },
};
</script>

<style scoped>
.note {
  text-align: center;
}
</style>
