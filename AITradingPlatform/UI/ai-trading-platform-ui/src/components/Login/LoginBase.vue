<template>
  <div class="login">
    <h1>LOGIN</h1>
    <form id="login" method="get" action="" @submit.prevent="login">
      <label><b>User Name</b></label>
      <br /><br />
      <input type="text" name="Username" id="Username" v-model="username" />
      <br /><br />
      <label><b>Password</b></label>
      <br /><br />
      <input type="Password" name="Password" id="Password"  v-model=" password" /> <br /><br /><br />
      <input
        type="button"
        name="log_button"
        id="log_button"
        value="Log In"
        v-on:click="login"
      />
      <br /><br />
    </form>

    <!-- <div>
    <h3 v-if="user"> Welcome {{user.username}}</h3>
    <h3 v-if="!user">You are not logged in!</h3>
    </div> -->
  
  </div>

</template> 

<script>
import axios from 'axios'

export default {
  name: "LoginBase",

  data(){
    return{
      username:"",
      password:"",
       user:null
      
    }

  },
  methods: {
       async login() {

        
      const response =await axios.post('',{
        username:this.username,
        password:this.password
      });
      
      console.log(response);

      localStorage.setItem('token',response.data.token);
       
      this.$router.push('/api'); 
      },
      // async created(){
      //   const response = await axios.get('user');
      //   this.user=response.data;

      // }
      

    },
  }

</script>

<style scoped>
.login {
  width: 382px;
  overflow: hidden;
  margin: auto;
  padding: 80px;
  background: #111111;
  border-radius: 15px;
  top: 0px;
  box-shadow: 0px 0px 5px lightblue;
}

h1 {
  text-align: center;
  padding: 20px;
}

label {
  opacity: 0.8;
  font-size: 17px;
  padding-bottom: 20px;
}
#Username {
  width: 300px;
  height: 30px;
  border-color: lightblue;
  border-radius: 10px;
  padding-left: 8px;
  color: white;
  background: transparent;
  outline: none;
}
#Password {
  width: 300px;
  height: 30px;
  border-radius: 3px;
  padding-left: 8px;
  border-color: lightblue;
  border-radius: 10px;
  padding-left: 8px;
  color: white;
  background: transparent;
  outline: none;
}
#log_button {
  width: 300px;
  height: 30px;
  border: none;
  border-radius: 17px;
  padding-left: 7px;
  color: #000000;
}
span {
  color: white;
  font-size: 17px;
}
</style>


