<template>
    <div class="container">
        <!-- <div class="logo">
        </div> -->
        <div class="title">AI ALGO TRADER</div>
        <router-link to="/login">
        <div class="login">
            Login
        </div>
        </router-link>
        <!--
        <div class="list">
            <ul>
                <li><a href="#">Strategy 1 </a>|</li>
                <li><a href="#">Strategy 2 </a>|</li>
                <li><a href="#">Strategy 3</a></li>
            </ul>
        </div>-->
    </div>
</template>

<script>
export default {
    name: 'Navbar',
    methods: {
        login(){
            this.$store.dispatch("flipLoginPage");
            this.$store.dispatch("flipLandingPage");
        }
    },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap');
.container {
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
.logo {
    position: absolute;
    width: 75px;
    height: 65px;
    left: 41px;
    top: 7px;
    background: #FFFFFF;
    border: 1px solid transparent;
    box-sizing: border-box;
    border-radius: 50%;
    
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

.login {
    position: absolute;
    width: 150px;
    height: 50px;
    right: 40px;
    top: 16px;
    background-color: transparent;
    border:1px solid #FFFFFF;
    box-shadow: 0px 0px 5px #FFFFFF;
    box-sizing: border-box;
    border-radius: 50px;
    text-align: center;
    line-height: 50px;
    transition: 0.5s;
    color: #FFFFFF;
    font-size: 20px;
}
.login:hover {
    box-shadow: 0px 0px 1px #FFFFFF;
    color: black;
    background-color: whitesmoke;
}

ul {

    list-style: none;
    display: flex;
    justify-content: flex-end;
    margin-top:23px;
    margin-right:50px;
}
li {

    margin-right:10px;
    font-family: Poppins;
    font-size: 20px;
    color:#FFFFFF;
    
}
a {
    text-decoration: none;
    color: #FFFFFF;
    transform: 0.9s;
}
a:hover {
   font-weight: bold;
}

</style>

