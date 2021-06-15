<template>
    <div class="go-back" @click="$store.dispatch('flipBacktestsMainPage')">
      <b>←</b> BACK
    </div>
</template>

<script>
export default {
  name: "BackButton",
};
</script>

<style scoped>
.go-back {
  font-size: 20px;
  cursor: pointer;
}

.go-back:hover {
  font-size: 22px;
  color: lightblue;
  cursor: pointer;
}
</style>
