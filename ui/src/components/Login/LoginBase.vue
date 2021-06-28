<template>
  <div class="parent">
    <div class="login">
      <h1>Login</h1>
      <label><b>User Name</b></label>
      <br /><br />
      <input type="text" name="Username" id="Username" v-model="username" />
      <br /><br />
      <label><b>Password</b></label>
      <br /><br />
      <input type="Password" name="Password" id="Password" v-model="password" />
      <br /><br />
      <br /><br />
      <div class="login-button-div">
        <input
          type="button"
          name="log_button"
          id="log-button"
          value="LOGIN"
          @click="login"
        />
      </div>
      <br /><br />
    </div>
  </div>
</template> 

<script>
// import axios from "axios";
export default {
  name: "LoginBase",

  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async login() {
      this.$router.push("/strategies");
      // const data = {
      //   user_name: this.username,
      //   password: this.password,
      // };
      // //console.log(data)

      // const res = await axios.post(
      //   process.env.VUE_APP_BASE_URL + "api/auth/login/",
      //   data
      // );
      // console.log(res);
    },
  },
};
</script>



<style scoped>
.login {
  position: relative;
  top: 50%;
  left: 50%;
  margin: -25px 0 0 -25px;
  width: 382px;
  overflow: hidden;
  margin: auto;
  padding: 70px;
  background-color: #1111;
  border-radius: 15px;
  bottom: 0px;
  box-shadow: 0px 0px 5px lightblue;
}
.login:hover {
  /* box-shadow: 0px 0px 10px #fa8072; */
  box-shadow: 0px 0px 10px cyan;
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
#log-button {
  padding: 20px;
  border-radius: 17px;
  text-align: center;
  color: lightblue;
  background-color: transparent;
  border-color: #fa8072;
}
.login-button-div {
  text-align: center;
}
span {
  color: white;
  font-size: 17px;
}
.parent {
  height: 250px;
  width: 900px;
  position: relative;
  background-color: #1111;
}
</style>