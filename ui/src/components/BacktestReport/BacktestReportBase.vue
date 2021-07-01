<template> 
  
  <div id="main_frame">
    <h1 id="header">Backtester Report</h1>
    <div id="base">
      <div id="attributes" >
        Start Date Time :
				<input type="text" name="Username" id="textbox" />
       </div>
      <div id="attributes" >
        End Date Time :
				<input type="text" name="Username" id="textbox" />
      </div>
      <div id="attributes" >
        Strategy Type : 
				<input type="text" name="Username" id="textbox" />
      </div>
      <div id="attributes" >
        Strategy Config : 
				<input type="text" name="Username" id="textbox" />
      </div>
      <div id="attributes" >
        Total return % : 
				<input type="text" name="Username" id="textbox" />
      </div>
      <div id="attributes" >
        Total Number of Trades:
				<input type="text" name="Username" id="textbox" />  
      </div>
      <div id="attributes" >
        Profit Trades: 
				<input type="text" name="Username" id="textbox" />
      </div>
      <div id="attributes" >
        Loss Trades: 
				<input type="text" name="Username" id="textbox" />
      </div>
      <div id="attributes" >
        Profit Trades % : 
				<input type="text" name="Username" id="textbox" />
      </div>
      <div id="attributes" >
        Loss Trades % : 
				<input type="text" name="Username" id="textbox" />
      </div>
      <div id="attributes" >
        Company : 
				<input type="text" name="Username" id="textbox" />
      </div>
            
    </div>
        
    <div id="title"  >
      <div id="__p__trades" >
        Trades Visulaization
      </div>
      <div id="line_1"  ></div>
      <div id="line_2"  ></div> 
    </div>
		<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
		
    <div id="title"  >
      <div id="__p__trades" >
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
          <td><input type="text" name="Signal" id="textboxx" /></td>
          <td><input type="text" name="Return %" id="textboxx" /></td>
          <td><input type="text" name="Return" id="textboxx" /></td>
        </tr>
         <tr>
          <td><input type="text" name="Signal" id="textboxx" /></td>
          <td><input type="text" name="Return %" id="textboxx" /></td>
          <td><input type="text" name="Return" id="textboxx" /></td>
        </tr>
         <tr>
          <td><input type="text" name="Signal" id="textboxx" /></td>
          <td><input type="text" name="Return %" id="textboxx" /></td>
          <td><input type="text" name="Return" id="textboxx" /></td>
        </tr>
         <tr>
          <td><input type="text" name="Signal" id="textboxx" /></td>
          <td><input type="text" name="Return %" id="textboxx" /></td>
          <td><input type="text" name="Return" id="textboxx" /></td>
        </tr>
      </table>

			
		</div>
		
    </div>     
</template>


<script>
export default {
  name: "LoginBase",

  data() {
    return {
      
    };
  },
  methods: {
    
}
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
	
	margin: 100px 500px 75px 0px;  ;
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
	background:rgb(245, 245, 245);
}



</style>

