<template>
<body>
    <div class="login"> 
    <h1>Login Form</h1> 
    <br><br>
    <form id="login" method="get" action="">    
        <label><b>User Name</b></label>       
        <input type="text" name="Username" id="Username" >    
        <br><br>    
        <label><b>Password</b></label>        
        <input type="Password" name="Password" id="Password" >    
        <br><br>    
        <input type="button" name="log_button" id="log_button" value="Log In">       
        <br><br>    
        <input type="checkbox" id="check"><span>Remember me</span>     
    </form>     
    </div>
</body>    
</template> 



<style scoped> 
.login{  
        width: 382px;  
        overflow: hidden;
        
        padding: 80px;  
        background: #000000;  
        border-radius: 15px ; 
        top: 0px;
          
}  
h2{  
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
body  
{  
    margin: 0;  
    padding-top: 180px;
    padding-left:650px;
    background-color:#6abadeba;  
    font-family: 'Arial';  
}  

</style>



