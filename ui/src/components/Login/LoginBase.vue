<template>
    <div class="main">
      <div class="nav">
        <div class="title">AI ALGO TRADER</div>
        <router-link to="/">
        <div class="home">
            Home
        </div>
        </router-link>
      </div>
      <div class="header">
        <div class="login-wrapper">
            <div class="login-content">
                <h3 class="signin-title">
                    Sign In
                </h3>
                <div class="alert">
                  <v-alert v-if="alert" dense outlined type="error"><b>Wrong Username or Password</b></v-alert>
                 
                  </div>
                <form action="#" v-on:submit.prevent="login" >
                  
                    <input type="text" name="login-username" placeholder="Username" class="login-username" v-model="username">
                    <input type="password" name="login-password" placeholder="Password" class="login-password" v-model="password">
                    <!-- <router-link to="/allstrategies"><button>Go</button></router-link> -->
                    <button>Go</button>
                </form>
                <router-link to="/">
                <a href="#" class="signin-back"> ←Back</a>
                </router-link>
            </div>
            <div class="login-vector"></div>
        </div>
        <div class="footer">Made with ♡ from VSDH</div> 
      </div>
    </div>
</template>
<script>
 
export default {
  
    name: 'LoginBase',
    data(){
        return{
          username:"",
          password:"",
          alert:false,
        
        }
    },
    methods:{
       login(){
        this.$store.dispatch('retrieveToken',{
          username:this.username,
          password:this.password,
        })
        
      .then(response => {
        console.log(response)
        console.log(response.status)
        
        this.$router.push({name:'AllStrategies'})
         
        })
      
      .catch(error => {
        
        console.log(error)
        this.alert=true
        
      })
        
      },
      loggedIn(){
        return this.$store.getters.getloggedIn

      }
     

    }
    
};
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap');
.nav {
    background-color: #fff;
    margin-top: 0px;
    padding-top: 0px;
    margin-bottom: 0px;
    margin-left: 0px;
    position: fixed;
    z-index: 100;
    width: 100%;
    top: 0px;
    height: 80px;
    filter: drop-shadow(0px 10px 10px rgba(0, 0, 0, 0.50));
    background-image: url("~@/assets/v1s.jpg");
    background-repeat: repeat;
    background-size:cover;
    background-position: center right;
    /*background-image: url("~@/assets/logo.jpg");
    background-size:100%;*/
}
.alert{
  position:absolute;
  color:red;
  text-align:center;
  
  top:93px;
  left:0px;
  width:395px;
  
}
.title {
    position: absolute;
    font-family: Poppins;
    font-size: 40px;
    top:10px;
    left: 120px;
    margin-top: 0px;
    color:#fff;
    transform: 0.4s;
    
}

.home {
    position: absolute;
    width: 150px;
    height: 50px;
    right: 40px;
    top: 16px;
    background-color: transparent;
    border:1px solid #FFFFFF;
    box-shadow: 0px 0px 0px #FFFFFF;
    box-sizing: border-box;
    border-radius: 50px;
    text-align: center;
    line-height: 50px;
    transition: 0.2s;
    color: #FFFFFF;
    font-size: 20px;
}
.home:hover {
    box-shadow: 0px 0px 5px #FFFFFF;
    
}
.header {
  background:url('~@/assets/v10s.jpeg');
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0px;
  top: 0px;
  background-size:cover;
  margin: 0;
  
}
.footer {
    text-align: center;
    font-family: Poppins;
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
    color: #FFFFFF;
    margin-top: 12%;
    
}

/*
.login-wrapper {
    width: 788px;
    height: 400px;
    margin: 0 auto;
    border: 1px solid transparent;
    filter: drop-shadow(10px 10px 100px rgba(0, 0, 0, 0.7));
 
}
*/
.login-content {
    position: relative;
    width: 394px;
    height: 400px;
    margin: 0 auto;
    margin-top:14%;
    background-color: transparent;
    border:1px solid #FFFFFF;
    box-shadow: 0px 0px 8px #FFFFFF;
    transition: 0.2s;
}
.login-content:hover {
    box-shadow: 0px 0px 15px #FFFFFF;
}
/*
.login-vector {
    position: absolute;
    width: 394px;
    height: 400px;
    right: 0px;
    top: 0px;
    background-image: url('~@/assets/v14.jpeg');
    background-size: cover;
    background-position: center;
    margin: 0px; 
    background-color: transparent;

}
*/
.signin-title {
    position: absolute;
    width: 271px;
    height: 42px;
    left: 60px;
    top: 30px;
    font-family: Poppins;
    font-style: normal;
    font-weight: bolder;
    font-size: 24px;
    line-height: 36px;
    text-align: center;
    color: #FFFFFF;
}

input {
    width: 298px;
    height: 44px;
    border: 1px solid rgba(196, 196, 196, 0.2);
    text-align: center;
    font-family: Poppins;
    font-size: 15px;
    border-radius: 30px;
   
}
input:focus {
    border-radius: 0px;
    border:none;
    background-color: transparent;
    color: #FFFFFF;
    opacity: 90%;

}
.login-username {
    position: absolute;
    left: 45px;
    top: 120px;
}
.login-password {
    position: absolute;
    left: 45px;
    top: 190px;
}
button {
    position: absolute;
    text-align: center;
    font-size: 20px;
    margin-left:10px;
    margin-top:10px;
    padding: 4px 70px;
    font-family: Poppins;
    border-radius: 50px;
    background-image: linear-gradient(270deg, dodgerblue,blue);
    color: #fff;
    opacity: 0.9;
    transition: 0.4s;
    border: 1px solid transparent;
    width: auto;
    top: 260px;
    left: 25%;
}
button:hover{
    opacity: 1;
    background-image: linear-gradient(200deg, dodgerblue,blue);
    font-weight: bold;
    box-shadow: 0px 0px 5px #fff;
    border-color: #fff;
}
.signin-back {
    position: absolute;
    width: 78px;
    height: 27px;
    left: 300px;
    top: 360px;
    font-family: Poppins;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 24px;
    text-align: center;
    color: #FFFFFF;
    text-decoration: none;
    transition: 0.2s;
}
.signin-back:hover {
  font-size: 19px;
}
</style>

<!--Old Code-->
<!--
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
      this.$router.push("/backtestreport");
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
-->
