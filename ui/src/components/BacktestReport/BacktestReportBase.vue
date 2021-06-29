<template>
  <div id="main_frame">

  </div>

  
    
</template>


<script>
export default {
  name: "LoginBase",

  data() {
    return {
      
    };
  },
  methods: {
    async login() {
      this.$router.push("/Login");
      
    },
  },
};

</script>

<style>
#main_frame{
	top: 0px;
	left: 50px;
	width: 143522222222222px;
	height: 42702222222222222px;
	background:white
}

</style>

