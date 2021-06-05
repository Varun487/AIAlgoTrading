<template>
  <div class="container">
    <div class="bg"></div>
    <div class="bg bg2"></div>
    <div class="bg bg3"></div>
    <div class="margin">
      <h1><center>Strategies</center></h1>
      <h4><center>Strategies read data from the database and can use multiple indicators, machine learning models, or a 
        combination to generate orders according to the rules mentioned in the strategy.</center></h4>
      <hr class="separator" />
      <h2>BackTested Strategies</h2><br>
      <div class="box">
        <p class="no-backtests" v-if="!$store.getters.getBacktestReports.length">
          NO BACKTESTS STRATEGIES AVAILABLE
        </p>
        <div >
          <h3 >Simple Bollinger Bands</h3>
          <p> Description:  Bollinger Bands consist of three bands—an upper, middle and lower band—that are used to spotlight extreme short-term prices in a security. 
            The upper band represents overbought territory, while the lower band can show you when a security is oversold. </p>
                
          
          <ul v-for="report in $store.getters.getBacktestReports" :key="report">
          <li class="dropdown" >
            <a href="javascript:void(0)" class="dropbtn">Column: {{ report.column }}, Indicator_time_period: {{ report.indicator_time_period }}, Sigma: {{ report.sigma }}</a>
            <div class="dropdown-content">
              <a href="/backtest">Company: {{ report.company.name }}, Start_date_time: {{
          report.start_date_time.split("T")[0] +
          "  " +
          report.start_date_time.split("T")[1].slice(0, -1)
        }}, End_date_time: {{
          report.end_date_time.split("T")[0] +
          "  " +
          report.end_date_time.split("T")[1].slice(0, -1)
        }}, Risk_ratio: {{ report.risk_ratio }}, Max_risk : {{ report.max_risk }}%, Initial_account_size: {{ report.initial_account_size }}, Final_account_size: {{ report.final_account_size }},
        Total profit: {{ Math.round(report.total_profit_loss) }}</a>
              <!-- <a href="/backtest">Company:TCS BSE, Start_date_time: "2021-04-1 00:00:00", End_date_time: "2021-04-20 00:00:00", Risk_ratio: "10:10", Max_risk : 2, Initial_acc: 10000</a>
              <a href="/backtest">Company:TCS BSE, Start_date_time: "2021-03-1 00:00:00", End_date_time: "2021-03-20 00:00:00", Risk_ratio: "10:10", Max_risk : 2, Initial_acc: 100000</a> -->
            </div>
          </li>
          </ul>
          <br>
          <!-- <ul>
          <li class="dropdown">
            <a href="javascript:void(0)" class="dropbtn">Column: "Open", Indicator_time_period: 5, Sigma: 1</a>
            <div class="dropdown-content" style="margin-top:50px;">
              <a href="/backtest">Company:TCS NSE, Start_date_time: "2021-05-1 00:00:00", End_date_time: "2021-05-20 00:00:00", Risk_ratio: "10:10", Max_risk : 2, Initial_acc: 1000000</a>
              <a href="/backtest">Company:TCS NSE, Start_date_time: "2021-04-1 00:00:00", End_date_time: "2021-04-20 00:00:00", Risk_ratio: "10:10", Max_risk : 2, Initial_acc: 10000</a>
              <a href="/backtest">Company:TCS NSE, Start_date_time: "2021-03-1 00:00:00", End_date_time: "2021-03-20 00:00:00", Risk_ratio: "10:10", Max_risk : 2, Initial_acc: 100000</a>
            </div>
          </li>
          </ul> -->
        </div>
      </div>
      
      <br><br><br>
      <h2>PaperTraded Strategies</h2><br>
      <div class="box">
        <p class="no-backtests" v-if="!$store.getters.getPapertradeReports.length">
          NO PAPERTRADE STRATEGIES AVAILABLE
        </p>
        <h3>Simple Bollinger Bands Strategy</h3>
        <p> Description: Bollinger Bands consist of three bands—an upper, middle and lower band—that are used to spotlight extreme short-term prices in a security.
          The upper band represents overbought territory, while the lower band can show you when a security is oversold.  </p>
        
        <!-- <ul v-for="report in $store.getters.getPapertradeReports" :key="report">
        <li class="dropdown">
          <a href="javascript:void(0)" class="dropbtn">Column: {{ report.column }}, Time_period: {{ report.time_period }}, Sigma: {{ report.sigma }}, 
            Name: {{ report.name }}</a>
          <div class="dropdown-content">
            <a href="#">Company:{{ report.company.name }},Column: {{ report.column }}, Time_period: {{ report.time_period }}, Sigma: {{ report.sigma }}, 
            Name: {{ report.name }}</a>
          </div>
        </li>
        </ul> -->
      </div>
      <br><br>
    
    </div>
    
  </div>
</template>


<script>
export default {
  name: 'StrategiesBase',
  mounted() {
    this.$store.dispatch("setBacktestReports");
    this.$store.dispatch("setPapertradeReports");
  },
}
</script>
<!--  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
-->

<style scoped>
.separator {
  opacity: 0.5;
}
.box {
  width: 92%;
  overflow: hidden;
  margin: auto;
  padding: 70px;
  background: #111111;
  border-radius: 15px;
  top: 90px;
  box-shadow: 0px 0px 5px rgb(201, 153, 150);
  
}

.box:hover {
	/* box-shadow: 0px 0px 10px #fa8072; */
	box-shadow: 0px 0px 10px rgb(221, 73, 36);
}
.margin {
  margin: auto;
  width: 90%;
  font-size: 18px;
  opacity: 0.9;
}
.bg {
  animation:slide 3s ease-in-out infinite alternate;
  background-image: linear-gradient(-60deg, rgb(15, 15, 15) 50%, rgb(34, 35, 36) 50%);
  bottom:0;
  left:-50%;
  opacity:.5;
  position:fixed;
  right:-50%;
  top:0;
  z-index:-1;
}

.bg2 {
  animation-direction:alternate-reverse;
  animation-duration:4s;
}

.bg3 {
  animation-duration:5s;
}

@keyframes slide {
  0% {
    transform:translateX(-25%);
  }
  100% {
    transform:translateX(25%);
  }
}
ul {
  list-style-type: none;
  margin: 0;
  padding: 2px;
  overflow: hidden;
  /* background-color: #333; */
  /* width: 100%; */
  text-align: left;
  /* padding: 20px; */
  
}

li {
  float: center;
}

li a, .dropbtn {
  display: inline-block;
  color: white;
  text-align: center;
  padding: 20px;
  text-decoration: none;
  border-radius: 17px;
  box-shadow: 0px 0px 5px rgb(201, 153, 150);
  /* width: 100%; */
}

li a:hover, .dropdown:hover .dropbtn {
  background-color: #86250c;
}

li.dropdown {
  display: inline-block;
}

.dropdown-content {
  display: none;
  /* position: absolute; */
  /* position: left; */
  /* background-color: #f9f9f9; */
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(228, 6, 6, 0.2);
  z-index: 1;
  padding: 20px;
  border-radius: 17px;
  background-color: transparent;
  border-color: #fa8072;
}

.dropdown-content a {
  color: white;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {background-color: #dd5e4dfd;}

.dropdown:hover .dropdown-content {
  display: block;
}

</style>
