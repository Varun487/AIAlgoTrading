<template> 
  
  <div id="main_frame">
    <h1 id="header">Backtester Report</h1>
    
    <div id="base"
    v-for="report in $store.getters.getBacktestReportData"
                :key="report.id">
      <p id="attributes" >
        Start Date Time : {{report.start_date_time}}
				
       </p>
      <p id="attributes" >
        End Date Time :{{report.end_date_time}}
			
      </p>
      <p id="attributes" >
        Strategy Type : {{report.strategy_type}}
				
      </p>
      <p id="attributes" >
        Strategy Config : {{report.strategy_config}}
				
      </p>
      <p id="attributes" >
        Total return % : {{report.total_returns_percent}}
				
      </p>
      <p id="attributes" >
        Total Number of Trades: {{report.total_trades}}
				
      </p>
      <p id="attributes" >
        Profit Trades: {{report.profit_trades}}
				
      </p>
      <p id="attributes" >
        Loss Trades: {{report.total_returns_percent}} - {{report.profit_trades}}
				
      </p>
      <p id="attributes" >
        Profit Trades % : {{report.profit_trades_percent}}
			
      </p>
      <p id="attributes" >
        Loss Trades % :[{{report.total_returns_percent}} - {{report.profit_trades}}] / {{report.total_trades}} *100
				
      </p>
      <p id="attributes" >
        Company : {{report.company}}
				
      </p>
    </div>

    <div id="base">
    
      <p id="attributes" >
        Start Date Time : 
       </p>
      <p id="attributes" >
        End Date Time :
			
      </p>
      <p id="attributes" >
        Strategy Type : 
				
      </p>
      <p id="attributes" >
        Strategy Config : 
				
      </p>
      <p id="attributes" >
        Total return % : 
				
      </p>
      <p id="attributes" >
        Total Number of Trades: 
				
      </p>
      <p id="attributes" >
        Profit Trades: 
				
      </p>
      <p id="attributes" >
        Loss Trades: 
				
      </p>
      <p id="attributes" >
        Profit Trades % : 
			
      </p>
      <p id="attributes" >
        Loss Trades % : 
				
      </p>
      <p id="attributes" >
        Company : 
				
      </p>
    </div>             
   

    
        
    <div id="title"  >
      <div id="__p__trades" >
        Trades Visulaization
      </div>
      <div id="line_1"  ></div>
      <div id="line_2"  ></div> 
      <div id="image">
      v-for="image in $store.getters."
                :key="report.id">
      </div>
    </div>
		

		
    <div id="title"  >
      <div id="__p__tradess" >
        Trades 
      </div>
      <div id="line_1"  ></div>
      <div id="line_2"  ></div> 
    </div>
		
    
    
    <div id="trades_group"  >
			
			<table id="table">
        <tr bordercolor="red">
          <th id="th">Signal</th>
          <th id="th">Return %</th>
          <th id="th">Return</th>
        </tr>
        <tr>
          
        </tr>
         <tr>
          
        </tr>
         <tr>
          
        </tr>
         <tr>
         
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
    this.$store.dispatch("setBacktestsReports");
  },
}

</script>

<style>
#header{
  text-align: center;
  padding: 20px;
  color:black;
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
	width: 688.2px;
	height: 69.64px;
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
	width: 688.2px;
	height: 69.64px;
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
	
	margin: 500px 500px 75px 0px;  ;
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
/* #line_1 {
	margin:10px 1000px 75px 500px;
	width: 472px;
	height: 10px;
	background:#ee0808;
}
#line_2 {
	margin:0px 0px 0px 0px;
	width: 434px;
	height: 10px;
	background:#ffffff;
} */
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
}
#table{
  margin: 100px auto;
  color: black;

}
tr{
  margin:auto ;
	width: 800px;
	height: 75px;
	-ms-border-radius: 50px;
	-o-border-radius: 50px;
	-moz-border-radius: 50px;
	-webkit-border-radius: 50px;
	border-radius: 50000px;
  border: 5px solid #941dcb;
	-ms-box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	-o-box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	-webkit-box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	-moz-box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	box-shadow:4px 10px 10px 1px rgba(0,0,0,0.25);
	background:white;
}
#image{
  margin:auto;
	
	width: 800px;
	height: 800px;
	
  background-color: black;
}



</style>

