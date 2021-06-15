<template>
  <div>
    <Title />
    <Note />
    <EndpointsOverviewList />
    <EndpointsDescriptionList />
  </div>
</template>

<script>
import Title from "./Title.vue";
import Note from "./Note.vue";
import EndpointsOverviewList from "./EndpointsOverviewList.vue";
import EndpointsDescriptionList from "./EndpointsDescriptionList.vue";

export default {
  name: "RestApiBase",
  components: {
    Title,
    Note,
    EndpointsOverviewList,
    EndpointsDescriptionList,
  },
};
</script>

<style scoped>
</style>
