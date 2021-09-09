


<template> 
  <div>
    

    
        
    <div id="title"  >
      <div id="line_1"  ></div>
      <div id="__p__trades" >
        Signal Visualization
      </div>
     <div id="line_2"  ></div> 
      <div id="image">
          <v-zoomer style="width: 1800px; height: 1000px; border: solid 1px silver;">
          <img v-bind:src="'data:image/png;base64,'+$store.getters.getTradeVisualization.img" />
        
           </v-zoomer>
      </div>
    </div>
		

		
    <div id="title"  >
      <div id="line_3"  ></div>
      <div id="__p__tradess" >
        Trades 
      </div>
      <div id="line_4"  ></div> 
    </div>
		
    
    
    <div id="trades_group"  >
      <router-link to="/"></router-link>
			<table id="table">
        <tr>
          <th id="th">Signal </th>
          <th id="th">Return %</th>
          <th id="th">Return</th>
        </tr>
        <tr class="hover1"
          v-for="(trade) in $store.getters.getTrades.slice(0,5)" 
                :key="trade.id" @click="Trades(trade.id)">
          <td  calss= "ded" v-if='trade.trade_type=== "1"'>Buy</td>
          <td class="ded" v-else>Sell</td>
          
           
          <td class="red" v-if='trade.trade_return_percent < 0'>{{trade.trade_return_percent}}</td>
          <td  class="green" v-else-if='trade.trade_return_percent > 0'>{{trade.trade_return_percent}}</td>
          
          <td  class="black" v-else>{{trade.trade_return_percent}}</td>
          
         <td class="red" v-if='trade.trade_net_return < 0'>{{trade.trade_net_return}}</td>
         <td  class="green" v-else-if='trade.trade_net_return > 0'>{{trade.trade_net_return}}</td> 
         <td  class="black" v-else>{{trade.trade_net_return}}</td>
        
        </tr>
       
         </table>

			
		</div>
		
    </div>     
</template>


<script>
//  import axios from "axios";


export default {
  name: "Graph",
  methods: {
    // addRows(){
    //   this.$store.commit('incrementRows',5);
    // }
    Trades(){
      this.$router.push({name:'Trades'})
    }
    
  },
    mounted() {
    // this.$store.dispatch("setBacktestReportdata",21);
    // this.$store.dispatch("setTradeVisualization",21);
    // this.$store.dispatch("setTrades",21);
    // this.$store.dispatch("incrementRows",5);
    this.$store.dispatch("setAllBacktests",this.$store.getters.getStrategyId);
    this.$store.dispatch("setBacktestReportdata",this.$store.getters.getBacktestsId);
    this.$store.dispatch("setTradeVisualization",this.$store.getters.getBacktestsId);
    this.$store.dispatch("setTrades",this.$store.getters.getBacktestsId);
  },
}

</script>

<style>
#header{
  text-align: center;
  padding: 20px;
  color:black;
  font-family: Poppins;
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
	height: 100.64px;
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
	width: 1400.2px;
	height:420.64px;
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
	margin: 100px 1000px 75px 600px;
	width: 440px;
	height: 104px;
	background:rgb(0, 0, 0);
}
#__p__trades {
	
	margin: 1200px 500px 75px 0px;
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
#__p__tradess {
	
	margin: 1200px 500px 75px 0px;  ;
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
    width: 600px;
    height: 0px;
    left: 0px;
    top: 2380px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#line_2 {
    position: absolute;
    width: 670px;
    height: 0px;
    left: 1170px;
    top: 2380px;
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
  left:50px;
  top:2500px;
	
	width: 900px;
	height: 800px;
	
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

