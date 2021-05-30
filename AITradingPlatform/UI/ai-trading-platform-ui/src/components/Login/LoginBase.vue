<template>
<body>
    <div class="login"> 
    <h1>Login Form</h1> 
    <br><br>
    <form id="login" method="get" action="">    
        <label><b>User Name</b></label>       
        <input type="text" name="Username" id="Username" v-model='user_name' >    
        <br><br>    
        <label><b>Password</b></label>        
        <input type="Password" name="Password" id="Password" v-model='password' >    
        <br><br><br><br>   
        <input type="button" name="log_button" id="log_button" value="Log In" v-on:click="login"> 
        <br><br><br>
        <input type="checkbox" id="check"><span>Remember me</span>     
    </form>     
    </div>
</body>    
</template> 

<script>
//import axios from 'axios'

export default {
  name: "LoginBase",

  data(){
    return{
      user_name:"",
      password:""
    }

  },
  methods: {
      login() {
        const data = {
          user_name: this.user_name,
          password: this.password
        };
        console.log(data)
        
        this.$router.push('/api'); 
      },

    },
  }
  
</script>





<style scoped> 
.login{  
        width: 382px;  
        overflow: hidden;
        margin: auto;  
        margin: 20 300 300 450px;
        padding: 80px;  
        background: #000000;  
        border-radius: 15px ; 
        top: 0px;
          
}  
h1{  
    text-align: center;  
    color: #ffffff;  
    padding: 20px;  
}  
label{  
    color: yellow;  
    font-size: 17px;  
}  
#Username{  
    width: 300px;  
    height: 30px;  
    border: none;  
    border-radius: 3px;  
    padding-left: 8px;  
}  
#Password{  
    width: 300px;  
    height: 30px;  
    border: none;  
    border-radius: 3px;  
    padding-left: 8px;  
      
}  
#log_button{  
    width: 300px;  
    height: 30px;  
    border: none;  
    border-radius: 17px;  
    padding-left: 7px;  
    color: #000000; 
  
}

span{  
    color: white;  
    font-size: 17px;  
}
</style>


