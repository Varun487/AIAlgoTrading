<template>
    <div class="container">
        <div class="logo">
        </div>
        <div class="title">AI ALGO TRADER</div> 
        <!--<div class="logout">
        </div>
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
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap');
.container {
    background-color: #fff;
    position: absolute;
    width: 100%;
    height: 80px;
    left: 0px;
    top: 0px;
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

.logout {
    position: absolute;
    width: 150px;
    height: 50px;
    left: 1190px;
    top: 16px;
    background: #FFFFFF;
    border: 1px solid transparent;
    box-sizing: border-box;
    border-radius: 50px;
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

