<template>
 
<div>
  <Navbar />
  <div id ="main_frame">
    <h1 id="header">Trades</h1>
      <div id="base">
        <div id="attributes" >
          <b>Id</b> : {{$store.getters.getTradesData.id}}
        </div>

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

          Close Price:  {{$store.getters.getTradesData.trade.entry_order.ticker_data.time_stamp}}  <br><br>
          Time Stamp: {{$store.getters.getTradesData.trade.entry_order.ticker_data.time_stamp}} <br>
        </div>

        <div id="attributess">
          <b>Exit Order</b> <br><br>

          
          Close Price:  {{$store.getters.getTradesData.trade.exit_order.ticker_data.time_stamp}}  <br><br>
          Time Stamp: {{$store.getters.getTradesData.trade.exit_order.ticker_data.time_stamp}} <br>
        </div>

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
    // this.$store.dispatch("setTradesData",21);
  },
 
}
</script>

<style scoped>
#header{
  text-align: center;
  padding: 20px;
  color:black;
  font-family: Poppins;
  font-size: 20px;
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

</style>

