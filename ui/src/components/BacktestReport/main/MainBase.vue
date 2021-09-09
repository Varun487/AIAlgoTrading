<template>
    <div class="strategy">
        <br>
        <About />
        <br><br><br><br><br><br><br><br>
        <MainLanding />
    </div>
</template>

<script>
import MainLanding from "./graph.vue"
import About from "./data.vue"

export default {
    name: "StrategyPageMain",
    components: {
        
        About,
        MainLanding,
    },
};
</script>

<style scoped>
.strategy {
    margin:0px;
    color: rgb(255, 255, 255);
    background-color: rgb(255, 255, 255);
}
h1{
    text-align: center;
    padding: 20px;
    color:black;
    background-color: rgb(255, 255, 255);
    font-family: Poppins;
    font-size: 55px;
    line-height: 82px;
    
}
/* p{
    text-align: center;
    padding: 20px;
    color:black;
    background-color: rgb(255, 255, 255);
} */
p{
    text-align: center;
    padding: 20px;
	top: 485px;
	left: 1000px;
	width: 688.2px;
	height: 69.64px;
	overflow: hidden;
	font-family: Poppins;
	font-size: 25px;
	font-weight: bold;
	color:#000000;
} 
.line1 {
    position: absolute;
    width: 675px;
    height: 0px;
    left: 0px;
    top: 1200px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
.title {
    position: absolute;
    width: 1000px;
    height: 78px;
    left: 750px;
    top: 1165px;
    font-family: Poppins;
    font-style: normal;
    font-weight: normal;
    font-size: 55px;
    line-height: 82px;
    display: flex;
    align-items: center;
    text-align: center;
    color: #000000;
}

.line2 {
    position: absolute;
    width: 735px;
    height: 0px;
    left: 1100px;
    top: 1200px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
table {
  font-family: arial, sans-serif;
  border: 1px solid rgb(255, 255, 255);
  /* border-collapse: collapse; */
  width: 75%;
  color: black;
  font-size: 23px;
  border-radius: 25px;
}

th{
    border: 1px solid #ffffff;
    text-align: center;
    padding: 25px;
    width: 750px;
    height: 0px;
    left: 1100px;
    top: 1200px;
}
td{
    border: 1px solid #941dcb;
    text-align: center;
    padding: 25px;
    width: 750px;
    height: 0px;
    left: 1100px;
    top: 1200px;
    border-radius: 25px; 
}
.hover1:hover {
    background-color: #941dcb;
    color: white;
}
table.center {
  margin-left: auto; 
  margin-right: auto;
}

/* th:hover {
    background-color: #ffffff;
} */

/* tr:nth-child(even) {
  background-color: #dddddd;
} */
</style>