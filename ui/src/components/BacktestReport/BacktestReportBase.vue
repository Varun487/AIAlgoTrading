<template> 
  
  <div id="main_frame">
    <h1 id="header">Backtester Report</h1>
    
    <!-- <div id="base"
    v-for="report in $store.getters.getBacktestReportData"
                :key="report.id"> -->
      <div id="base">         
      <p id="attributes" >
        <b>Start Date Time</b> : {{$store.getters.getBacktestReportData.start_date_time}}
				
       </p>
      <p id="attributes" >
        End Date Time : {{$store.getters.getBacktestReportData.end_date_time}}
			
      </p>
      <p id="attributess" >
        Strategy Type :  {{$store.getters.getBacktestReportData.strategy_type}}
				
      </p>
      <p id="attributes" >
        Strategy Config :  {{$store.getters.getBacktestReportData.strategy_config}}
				
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
        Loss Trades:  {{$store.getters.getBacktestReportData.total_trades}} - {{$store.getters.getBacktestReportData.profit_trades}}
				
      </p>
      <p id="attributes" >
        Profit Trades % :  {{$store.getters.getBacktestReportData.profit_trades_percent}}
			
      </p>
      <p id="attributes" >
        Loss Trades % : [{{$store.getters.getBacktestReportData.total_trades}} - {{$store.getters.getBacktestReportData.profit_trades}}] / {{$store.getters.getBacktestReportData.total_trades}} *100
				
      </p>
      <p id="attributes" >
        Company :  {{$store.getters.getBacktestReportData.company}}
				
      </p>
      
    </div>

         
   

    
        
    <div id="title"  >
      <div id="line_1"  ></div>
      <div id="__p__trades" >
        Trades Visualization
      </div>
     <div id="line_2"  ></div> 
      <div id="image">
     
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
        <tr>
          <td>drefdre</td>
          <td>drefdre</td>
          <td>drefdre</td>
        </tr>
        <tr>
          <td>drefdre</td>
          <td>drefdre</td>
          <td>drefdre</td>
        </tr>
        <tr>
          <td>drefdre</td>
          <td>drefdre</td>
          <td>drefdre</td>
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
	margin: 100px auto;
	width: 1500px;
	height: 3000px;
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
	width: 1200.2px;
	height:300.64px;
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
	
	margin: 900px 500px 75px 0px;
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
	
	margin: 1000px 500px 75px 0px;  ;
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
    top: 2050px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#line_2 {
    position: absolute;
    width: 670px;
    height: 0px;
    left: 1170px;
    top: 2050px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#line_3 {
    position: absolute;
    width: 775px;
    height: 0px;
    left: 0px;
    top: 3150px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#line_4 {
    position: absolute;
    width: 900px;
    height: 0px;
    left: 1000px;
    top: 3150px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#trades_group {
	margin: auto;
	width: 1305px;
	height: 800px;
	background:rgb(255, 255, 255);
}
/* #tr{
	margin:auto ;
	width: 800px;
	height: 75px;
	-ms-border-radius: 50px;
	-o-border-radius: 50px;
	-moz-border-radius: 50px;
	-webkit-border-radius: 50px;
	border-radius: 50px;
  border: 5px solid #941dcb;
	-ms-box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	-o-box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	-webkit-box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	-moz-box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	background:rgba(255,255,255,1);
} */
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
  font-family: Poppins;
    font-style: normal;
    font-weight: bolder;
    font-size: 24px;
}
table{
  height:300px;
  width:700px;
  margin: 200px auto;
  padding:10px;
  color: black;
  border:5px solid black;
  text-align:center;
  border-spacing: 0 30px;
  -ms-box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	-o-box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	-webkit-box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	-moz-box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
  

}
tr{
   border: 5px solid #941dcb;
}

td{
  padding: 10px;
   
 border-radius: 50px;
  border-collapse: collapse;
  border: 5px solid #941dcb;
}

#image{
  margin:auto;
	
	width: 800px;
	height: 800px;
	
  background-color: rgb(255, 255, 255);
}
#vector {
	top: 3165px;
	left: 263px;
	width: 50px;
	height: 71.05px;
}




</style>

