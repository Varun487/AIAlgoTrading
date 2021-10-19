<template>
<div>
<div class="container">
    <!-- <img src="https://image.freepik.com/free-photo/stock-market-forex-trading-graph-graphic-concept_73426-171.jpg" alt="image"> -->
    <!-- <img src="https://www.tinkoff.ru/api/invest-gw/social/file/v1/cache/post/image/6aae5a84-37ae-473e-8611-41e66c4531b9?size=small&appName=invest&platform=web" alt="image"> -->
    <!-- <img src="https://t4.ftcdn.net/jpg/03/12/92/71/240_F_312927167_K2tJynI8TyU87rIeYMHWPWNZW5124MiF.jpg" alt="image"> -->
    <!-- <img src= "https://img.freepik.com/free-vector/technology-wire-mesh-network-connection-digital-background_1017-28407.jpg?size=338&ext=jpg" alt = "image"> -->
    <h1><div class="top-left1">AI ALGORITHMIC
    </div></h1>
    <h1><div class="top-left2">TRADING
    </div></h1>
    <h1><div class="top-left3">SYSTEM
    </div></h1>
    <!-- <p><i class="arrow down"></i></p> -->
    <!-- <a href="#section2">Click Me to Smooth Scroll to Section 2 Below</a> -->
    <!-- <h1><div class = "section2">hi</div></h1> -->
</div>
</div>    
</template>

<script>
export default {
    name: 'MainLanding',
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap');
html {
  scroll-behavior: smooth;
}

.container {
  position: relative;
  text-align: center;
  /* color: 8FB6EF; */
  width: 100%;
  height: 890px;
  background-image: url("~@/assets/landing.png");
  background-repeat: repeat;
  background-size:cover;
  background-position: center right;
  background-color: black;
}
img {
  
  width: 100%;
  height: 890px;
}
.top-left1 {
  position: absolute;
  top: 200px;
  left: 100px;
  color: rgb(51, 119, 184);
  font-size: 60px;
}
.top-left2 {
  position: absolute;
  top: 300px;
  left: 100px;
  color: rgb(51, 119, 184);
  font-size: 60px;
}
.top-left3 {
  position: absolute;
  top: 400px;
  left: 100px;
  color: rgb(51, 119, 184);
  font-size: 60px;
}
/* .arrow {
    position: absolute;
    bottom: 8px;
    border: solid rgb(51, 119, 184);
    border-width: 0 9px 9px 0;
    display: inline-block;
    padding: 3px;
}
.down {
  transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
} */
/* #section2 {
  text-align: center;
  color: 8FB6EF;
} */
</style>
