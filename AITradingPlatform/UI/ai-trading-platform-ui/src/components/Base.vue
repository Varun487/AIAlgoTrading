<template>
  <div>
    <div id="nav">
      <router-link to="/" />
      <router-link to="/home">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/api">REST API documentation</router-link> 
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "Base",
};
</script>

<style scoped>
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: white;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>