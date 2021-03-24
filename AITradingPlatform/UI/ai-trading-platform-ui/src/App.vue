<template>
  <div id="app">
    <Base />
  </div>
</template>

<script>
import Base from './components/Base.vue'

export default {
	name: 'App',
	components: {
		Base
	}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;/* #2c3e50;*/
  background-color: black;
}
</style>
