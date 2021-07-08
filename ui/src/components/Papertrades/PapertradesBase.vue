<template>
   <div id="main_frame">
        <h1 id="header">Paper Trades</h1>
        <div id="div1">
            <div id="historical">
                Historical:
            </div>

            <div id="company">
                Company:
            </div>
            
            <div id="open">
                Open:
            </div>

            <div id="high">
                High:
            </div>

             <div id="low">
                Low:
            </div>

             <div id="close">
                Close:
            </div>

             <div id="last_updated">
                Last Updated:
            </div>
        
        </div> 
        
        
        <div>
            <div id="line_1"  ></div>
            <div id="__p__trades" >
                Trades Details
            </div>
            <div id="line_2"  ></div> 
        </div>
        
        <div id="base"> 
            <div id="attributes1">
            <b>Strategy Config</b>   <br><br>

            Indicator Time Period :  <br><br>
            Max Holding  Period: <br><br>
            Take Profit Factor: <br><br>
            Stop Loss Factor: <br><br>
            Sigma:<br><br>
            Dimension:<br><br>
            Strategy_type: <br><br>
            
            </div>

            <div id="attributes2">
        
            <b>Trade</b>   <br><br>

            Entry Order : <br><br>
            Exit order: <br><br>
            Durations: <br><br>
            Net Returns: <br><br>
            Return Percentage:<br><br>
            
            </div>
        </div>

    <div id="title"  >
        <div id="line_3"  ></div>
        <div id="__p__tradess" >
            Trades Visualization
        </div>
        <div id="line_4"  ></div> 
    </div>

    <div id="image">
          <!-- <v-zoomer style="width: 500px; height: 500px; border: solid 1px silver;"> -->
          <!-- <img v-bind:src="'data:image/png;base64,'+$store.getters.getTradeVisualization.img" /> -->
        <!-- {{$store.getters.getTradeVisualization.img}} -->
          <!-- </v-zoomer> -->
      </div>

    </div>
</template>


<script>
//  import axios from "axios";
export default {
  name: "PapertradesBase",
  methods: {
    
  },
   
}

</script>

<style scoped>
#header{
  text-align: center;

  padding: 20px;
  color:black;
  /* font-family: Poppins; */
  background-color: rgb(255, 255, 255);
}
#main_frame {
  position:relative;
	margin: 100px auto;
	width: 100%;
	height: 100%;
	background:rgb(0, 0, 0);
}
#div1{
    position:relative;
    top:0px;
    left:0px;
    width: 1900px;
	height: 400px;
	background:rgb(255, 255, 255);
    border-radius: 25px;
}
#historical{
    position:absolute;
    top:10px;
    left:820px;
    width:200px;
    height:40px;
    font-size:25px;
    text-align: center;
    background-color:#E8BF2D;
    border: 2px solid #E8BF2D;
    border-radius:20px;
    
}
#company{
    position:absolute;
    top:120px;
    left:200px;
    width:200px;
    height:40px;
    font-size:25px;
    text-align: center;
    background-color:#C4C4C4;
    border: 2px solid #C4C4C4;
    border-radius:20px;

}
#open{
    position:absolute;
    top:120px;
    left:820px;
    width:150px;
    height:40px;
    font-size:25px;
    text-align: center;
    background-color:#C4C4C4;
    border: 2px solid #C4C4C4;
    border-radius:20px;

}
#high{
    position:absolute;
    top:120px;
    left:1350px;
    width:150px;
    height:40px;
    font-size:25px;
    text-align: center;
    background-color:#C4C4C4;
    border: 2px solid #C4C4C4;
    border-radius:20px;

}
#last_updated{
    position:absolute;
    top:300px;
    left:200px;
    width:200px;
    height:40px;
    font-size:25px;
    text-align: center;
    background-color:#C4C4C4;
    border: 2px solid #C4C4C4;
    border-radius:20px;

}
#close{
    position:absolute;
    top:300px;
    left:820px;
    width:150px;
    height:40px;
    font-size:25px;
    text-align: center;
    background-color:#C4C4C4;
    border: 2px solid #C4C4C4;
    border-radius:20px;

}
#low{
    position:absolute;
    top:300px;
    left:1350px;
    width:150px;
    height:40px;
    font-size:25px;
    text-align: center;
    background-color:#C4C4C4;
    border: 2px solid #C4C4C4;
    border-radius:20px;

}
#__p__trades {
	
	margin: 140px 900px 75px 610px;
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
#base{
	position:relative;
	margin: 100px 50px 75px 400px;  
	
	width: 800px;
	height: 800px;
	background:rgb(255, 255, 255)
}
#line_1 {
    position: absolute;
    width: 690px;
    height: 0px;
    left: 0px;
    top: 800px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#line_2 {
    position: absolute;
    width: 730px;
    height: 0px;
    left: 1100px;
    top: 802px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#attributes1{
    position:absolute;
	left:0px;
    top:0px;
	width: 1400.2px;
	height:500.64px;
	overflow: hidden;
	/* font-family: Poppins; */
	font-size: 25px;
	/* font-weight: bold; */
	text-align: left;
	color:#000000;
} 
#attributes2{
    position:absolute;
	top:600px;
    left:0px;
	width: 1400.2px;
	height:420.64px;
	overflow: hidden;
	/* font-family: Poppins; */
	font-size: 25px;
	/* font-weight: bold; */
	text-align: left;
	color:#000000;
} 
#__p__tradess {
	
	margin: 300px 900px 75px 610px;
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
#line_3 {
    position: absolute;
    width: 610px;
    height: 0px;
    left: 0px;
    top: 2145px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#line_4 {
    position: absolute;
    width: 670px;
    height: 0px;
    left: 1175px;
    top: 2145px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
#image{
  position:absolute;
  left:50px;
  top:2250px;
	
	width: 1750px;
	height: 800px;
	
  background-color: rgb(255, 255, 255);
}

</style>
