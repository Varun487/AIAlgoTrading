<template>
    <div>
        <div class="title">Paper Trades</div>
        <div class="stub">Historical</div>
        <div class="current-trade-update">
            <table>
                <tr>
                    <th>Company</th>
                    <th>Open</th>
                    <th>High</th>
                </tr>
            </table>
            <div id="historical">Historical:</div>
            <div id="company">Company:</div>
            <div id="open">Open:</div>
            <div id="high">High:</div>
            <div id="low">Low:</div>
            <div id="close">Close:</div>
            <div id="last_updated">Last Updated:</div>
        </div>
    </div>
</template>
<script>
//  import axios from "axios";
export default {
  name: "PapertradesMain",
  methods: {
    
  },
}
</script>
<style scoped>
.title {
    text-align: center;
    color: black;
    font-size: 40px;
    margin-top: 80px;
    font-family: Poppins;
}
.stub {
    height: 50px;
    width: 150px;
    border-radius: 30px;
    border: 1px solid black;
    line-height: 50px;
    text-align: center;
}
.current-trade-update{
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
