<template>
 
<div>
  <Navbar />
  <div id ="main_frame">
    <h1 id="header">Trades</h1>
      <div id="base">
        <!-- <div id="attributes" >
          <b>Id</b> : {{$store.getters.getTradesData.id}}
        </div> -->

        <div id="attributes" >
          <b>Duration</b>: {{$store.getters.getTradesData.trade.duration}}
        </div>

        <div id="attributes">
          <b>Net Return</b> : {{$store.getters.getTradesData.trade.net_return}}
        </div>

        <div id="attributes">
          <b>Return Percentage</b> : {{$store.getters.getTradesData.trade.return_percent}}
        </div>

        <div id="attributess">
          <b>Entry Order</b> <br><br>

          Close Price:  {{$store.getters.getTradesData.trade.entry_order.ticker_data.close}}  <br><br>
          Time Stamp: {{$store.getters.getTradesData.trade.entry_order.ticker_data.time_stamp}} <br>
        </div>

        <div id="attributess">
          <b>Exit Order</b> <br><br>

          
          Close Price:  {{$store.getters.getTradesData.trade.exit_order.ticker_data.close}}  <br><br>
          Time Stamp: {{$store.getters.getTradesData.trade.exit_order.ticker_data.time_stamp}} <br>
        </div>

      </div>
    
  </div>
  <div id="title"  >
      <div id="line_1"  ></div>
      <div id="__p__trades" >
        Trades Visualization
      </div>
     <div id="line_2"  ></div> 
      <div id="image">
          <v-zoomer style="width: 1800px; height: 1000px; border: solid 1px silver;">
          <img v-bind:src="'data:image/png;base64,'+$store.getters.getTradespageVisualization.img" />
        
           </v-zoomer>
           <br /><br /><br /><br /><br /><br /><br /><br />
      </div>
    </div>
    
		

</div>

    
</template>


<script>
import Navbar from "../TopNavbar/NavPostLogin.vue"
export default {
  name: "TradesBase",
  components: {
    Navbar,
  },
  mounted (){
    this.$store.dispatch("setTradesData",this.$store.getters.getBacktestsId);
    this.$store.dispatch("setTradespageVisualization",this.$store.getters.getBacktestsId);
   
  },
 
}
</script>

<style scoped>
#header{
  text-align: center;
  padding: 20px;
  color:black;
  font-family: Poppins;
  font-size: 50px;
  background-color: rgb(255, 255, 255);
}
#main_frame {
  position:relative;
	margin: 100px auto;
	width: 100%;
	height: 100%;
	background:rgb(255, 255, 255);
}
#base{
	
	margin: 100px 50px 75px 400px;  
	
	width: 800px;
	height: 800px;
	background:rgb(255, 255, 255)
}
#attributes{
	top: 485px;
	left: 213px;
	width: 1200.2px;
	height: 150.64px;
	overflow: hidden;
	/* font-family: Poppins; */
	font-size: 25px;
	/* font-weight: bold; */
	text-align: left;
	color:#000000;
} 
#attributess{
	top: 485px;
	left: 213px;
	width: 1200.2px;
	height: 250.64px;
	overflow: hidden;
	/* font-family: Poppins; */
	font-size: 25px;
	/* font-weight: bold; */
	text-align: left;
	color:#000000;
} 
#textbox {
  width: 300px;
  height: 30px;
  border-color: lightblue;
  border-radius: 10px;
  padding-left: 8px;
  color:black;
  background: transparent;
  outline: none;
}
  
#title {
	margin: 100px 1000px 75px 630px;
	width: 440px;
	height: 104px;
	background:rgb(255, 255, 255);
}
.title2 {
    position: absolute;
    width: 1000px;
    height: 78px;
    left: 750px;
    top: 2260px;
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

#__p__trades {
	
	margin: 320px 50px 75px 0px;  ;
	width: 572px;
	height: 144.5px;
	overflow: hidden;
	font-family: Poppins;
	font-size: 55px;
	text-align: center;
	-webkit-text-stroke-width: 1px;
	-webkit-text-stroke-color: #ffffff;
	text-shadow: 0 0 2px #ffffff;
	color:#000000;
	background:rgb(255, 255, 255);
}
#line_1 {
    position: absolute;
    width: 645px;
    height: 0px;
    left: 0px;
    top: 1500px;
     border: 1px solid rgba(0, 0, 0, 0.1);
    
}
#line_2 {
    position: absolute;
    width: 660px;
    height: 0px;
    left: 1190px;
    top: 1500px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#line_3 {
    position: absolute;
    width: 775px;
    height: 0px;
    left: 0px;
    top: 3690px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#line_4 {
    position: absolute;
    width: 900px;
    height: 0px;
    left: 1000px;
    top: 3690px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#trades_group {
	margin: auto;
	width: 1305px;
	height: 800px;
	background:rgb(255, 255, 255);
}

#textboxx {
  margin:auto;
  left:20px;
  width: 250px;
  height: 30px;
  border-color: lightblue;
  border-radius: 10px;
  padding-left: 8px;
  color:black;
  background: transparent;
  outline: none;
  
}
#th{
  color:#000000;
  
  border-radius: 50px;
  padding:20px;
  
    font-style: normal;
    font-weight: bolder;
    font-size: 30px;
}
table{
  height:300px;
  width:100%;
  margin: 0px auto;
  padding:5px;
  color: black;
  /* border:2px solid black; */
  border-radius: 25px;
  text-align:center;
  border-spacing: 0 30px;
  /* -ms-box-shadow:10px 10px 10px 10px rgba(0,0,0,0.25);
	-o-box-shadow:10px 10px 10px 10px rgba(0,0,0,0.25);
	-webkit-box-shadow:10px 10px 10px 10px rgba(0,0,0,0.25);
	-moz-box-shadow:10px 10px 10px 10px rgba(0,0,0,0.25);
	box-shadow:4px 10px 10px 10px rgba(0,0,0,0.25); */
  

}
.red{
  width:750px;
}
.green{
  width:750px;
}
.black{
  width:750px;
}
.ded{
  width:1500px;
}


td{
   border: 2px solid #941dcb;
    text-align: center;
    padding: 10px;
    width: 750px;
    height: 0px;
    left: 1100px;
    top: 1200px;
    border-radius: 50px; 
    font-size:30px;
}



.green{
  padding: 10px;
  color:green;
   
 border-radius: 50px;
  border-collapse: collapse;
  border: 2px solid #941dcb;
}

.red{
  padding: 10px;
  color:rgb(255, 0, 0);
   
 border-radius: 50px;
  border-collapse: collapse;
  border: 2px solid #941dcb;
}
.red:hover{
  color:white;
}

.black{
  padding: 10px;
  color:rgb(0, 0, 0);
   
 border-radius: 50px;
  border-collapse: collapse;
  border: 2px solid #941dcb;
}


#image{
  position:absolute;
  width: 100px;
	height: 100px;
  left:50px;
  top:1750px;
	

	
  background-color: rgb(255, 255, 255);
}

img{
  
  width:1750px;
  height:1000px
}

h1{
  font-size:50px;
}
p{
  font-weight:bold;
}

.hover1:hover td {
   color: white;
    background-color:  #941dcb;
}

</style>

