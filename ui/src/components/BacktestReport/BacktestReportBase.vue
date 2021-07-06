<template> 
  
  <div id="main_frame">
    <h1 id="header">Backtester Report</h1>
    
    
      <div id="base">         
      <p id="attributes" >
        <strong>Start Date Time</strong> : {{$store.getters.getBacktestReportData.start_date_time}}
				
       </p>
      <p id="attributes" >
        End Date Time : {{$store.getters.getBacktestReportData.end_date_time}}
			
      </p>
      <p id="attributess" >
        Strategy Type  <br><br>
        
        Name: {{$store.getters.getBacktestReportData.strategy_type.name}}<br>
        Description:    {{$store.getters.getBacktestReportData.strategy_type.description}}<br>
        Stock Selection: {{$store.getters.getBacktestReportData.strategy_type.stock_selection}}<br>
        Entry Criteria: {{$store.getters.getBacktestReportData.strategy_type.entry_criteria}}<br>
        Exit Criteria: {{$store.getters.getBacktestReportData.strategy_type.exit_criteria}}<br>
        Stop Loss Method: {{$store.getters.getBacktestReportData.strategy_type.stop_loss_method}}<br>
        Take Profit Method: {{$store.getters.getBacktestReportData.strategy_type.take_profit_method}}<br>
				
      </p>
      <p id="attributess" 
      v-if='$store.getters.getBacktestReportData.strategy_config.strategy_type=== "1"'>
        Strategy Config   <br><br>

        Indicator Time Period :  {{$store.getters.getBacktestReportData.strategy_config.indicator_time_period}}<br>
        Max Holding  Period: {{$store.getters.getBacktestReportData.strategy_config.max_holding_period}}<br>
        Take Profit Factor: {{$store.getters.getBacktestReportData.strategy_config.take_profit_factor}}<br>
        Stop Loss Factor: {{$store.getters.getBacktestReportData.strategy_config.stop_loss_factor}}<br>
        Sigma:{{$store.getters.getBacktestReportData.strategy_config.sigma}}<br>
        Dimension:{{$store.getters.getBacktestReportData.strategy_config.dimension}}<br>
        Strategy_type: Buy<br>


				
      </p>
      <p id="attributess" 
      v-else>
        Strategy Config   <br><br>

        Indicator Time Period :  {{$store.getters.getBacktestReportData.strategy_config.indicator_time_period}}<br>
        Max Holding Time Period: {{$store.getters.getBacktestReportData.strategy_config.max_holding_period}}<br>
        Take Profit Factor: {{$store.getters.getBacktestReportData.strategy_config.take_profit_factor}}<br>
        Stop Loss Factor: {{$store.getters.getBacktestReportData.strategy_config.stop_loss_factor}}<br>
        Sigma:{{$store.getters.getBacktestReportData.strategy_config.sigma}}<br>
        Dimension:{{$store.getters.getBacktestReportData.strategy_config.dimension}}<br>
        Strategy Type: Sell<br>


				
      </p>
      <p id="attributes" >
        Total return % :  {{$store.getters.getBacktestReportData.total_returns_percent}}
				
      </p>
      <p id="attributes" >
        Total Number of Trades:  {{$store.getters.getBacktestReportData.total_trades}}
				
      </p>
      <p id="attributes" >
        Profit Trades:  {{$store.getters.getBacktestReportData.profit_trades}}
				
      </p>
      <p id="attributes" >
        Loss Trades:  {{$store.getters.getBacktestReportData.total_trades - $store.getters.getBacktestReportData.profit_trades}}
				
      </p>
      <p id="attributes" >
        Profit Trades % :  {{$store.getters.getBacktestReportData.profit_trades_percent}}
			
      </p>
      <p id="attributes" >
        Loss Trades % : {{100-$store.getters.getBacktestReportData.profit_trades_percent}}
				
      </p>
      <p id="attributess" >
        
        Company   <br><br>
        
              Name :{{$store.getters.getBacktestReportData.company.name}} <br>
              Ticker:{{$store.getters.getBacktestReportData.company.ticker}}<br>
        Description: {{$store.getters.getBacktestReportData.company.description}}<br>
				
      </p>
      
    </div>

         
   

    
        
    <div id="title"  >
      <div id="line_1"  ></div>
      <div id="__p__trades" >
        Trades Visualization
      </div>
     <div id="line_2"  ></div> 
      <div id="image">
        
          <img v-bind:src="'data:image/png;base64,'+$store.getters.getTradeVisualization.img" />
        <!-- {{$store.getters.getTradeVisualization.img}} -->
       
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
			
			<table id="table">
        <tr>
          <th id="th">Signal </th>
          <th id="th">Return %</th>
          <th id="th">Return</th>
        </tr>
        <tr class="hover1"
        v-for="trade in $store.getters. getTrades"
                :key="trade.id">
          <td v-if='trade.trade_type=== "1"'>Buy</td>
          <td v-else>Sell</td>
          
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
  name: "LoginBase",
  methods: {
    showBacktestReport(id){
      this.$store.dispatch("setBacktestId", id);
      
    }
  },
    mounted() {
    this.$store.dispatch("setBacktestReportdata",31);
    this.$store.dispatch("setTradeVisualization",31);
    this.$store.dispatch("setTrades",31);
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
	font-family: Poppins;
	font-size: 25px;
	font-weight: bold;
	text-align: left;
	color:#000000;
} 
#attributess{
	top: 485px;
	left: 213px;
	width: 1400.2px;
	height:500.64px;
	overflow: hidden;
	font-family: Poppins;
	font-size: 25px;
	font-weight: bold;
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
	
	margin: 1600px 500px 75px 0px;
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
    top: 2790px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#line_2 {
    position: absolute;
    width: 670px;
    height: 0px;
    left: 1170px;
    top: 2790px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#line_3 {
    position: absolute;
    width: 775px;
    height: 0px;
    left: 0px;
    top: 4090px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#line_4 {
    position: absolute;
    width: 900px;
    height: 0px;
    left: 1000px;
    top: 4090px;
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
  
    font-style: normal;
    font-weight: bolder;
    font-size: 24px;
}
table{
  height:300px;
  width:100%;
  margin: 100px auto;
  padding:25px;
  color: black;
  border:2px solid black;
  border-radius: 25px;
  text-align:center;
  border-spacing: 0 30px;
  -ms-box-shadow:10px 10px 10px 10px rgba(0,0,0,0.25);
	-o-box-shadow:10px 10px 10px 10px rgba(0,0,0,0.25);
	-webkit-box-shadow:10px 10px 10px 10px rgba(0,0,0,0.25);
	-moz-box-shadow:10px 10px 10px 10px rgba(0,0,0,0.25);
	box-shadow:4px 10px 10px 10px rgba(0,0,0,0.25);
  

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
    font-size:25px;
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
  top:2900px;
	
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

