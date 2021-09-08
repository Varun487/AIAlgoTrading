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

          Id: <br>
          Duration:   <br>
          Net Return:<br>
          Return percentage:<br>
          Entry order
          <div id="attributess">
            Id : <br>
            Signal
            <div id="attributesss">
              Id : <br>
              Type: <br>
              Ticker data : <br>
              Strategy config : <br>
            </div>
            Ticker data :
            <div id="attributesss">
              Id : <br>
              Open : <br>
              High : <br>
              Low : <br>
              Close : <br>
              Volume : <br>
              Time Stamp : <br>
              Time period : <br>
              Company: <br>
            </div>
          </div>  
          Stop Loss Method: <br>
          Take Profit Method: <br>
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

