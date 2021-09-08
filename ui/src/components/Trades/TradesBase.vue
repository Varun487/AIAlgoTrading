<template>
 
<div>
  <Navbar />
  <div id ="main_frame">
    <h1 id="header">Trades</h1>
      <div id="base">
        <div id="attributes" >
          <b>Id</b> : 
        </div>

        <div id="attributes" >
          <b>Trade</b>  <br><br>

          Name: {{$store.getters.getBacktestReportData.strategy_type.name}}<br>
          Description:    {{$store.getters.getBacktestReportData.strategy_type.description}}<br>
          Stock Selection: {{$store.getters.getBacktestReportData.strategy_type.stock_selection}}<br>
          Entry Criteria: {{$store.getters.getBacktestReportData.strategy_type.entry_criteria}}<br>
          Exit Criteria: {{$store.getters.getBacktestReportData.strategy_type.exit_criteria}}<br>
          Stop Loss Method: {{$store.getters.getBacktestReportData.strategy_type.stop_loss_method}}<br>
          Take Profit Method: {{$store.getters.getBacktestReportData.strategy_type.take_profit_method}}<br>
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
 
}
</script>

<style scoped>
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

</style>

