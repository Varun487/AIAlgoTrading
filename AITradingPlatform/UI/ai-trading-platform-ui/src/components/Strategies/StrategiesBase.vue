<template>
  <div>
    
    <h1><center>Strategies</center></h1>
    <p><center>Description: </center></p>
    <hr class="separator" />
    <h2>BackTested Strategies</h2>
    <h3>Simple Bollinger Bands Strategy</h3>
    <p> Description: </p>
    <hr class="separator" />
    

    <ul>
    <li class="dropdown">
      <a href="javascript:void(0)" class="dropbtn">Company:TCS BSE, Strategy: "Simple Bollinger Bands Strategy", Column: "Close", Indicator_time_period: 5, Sigma: 1</a>
      <div class="dropdown-content">
        <a href="/backtest">Start_date_time: "2021-05-1 00:00:00", End_date_time: "2021-05-20 00:00:00", Risk_ratio: "10:10", Max_risk : 2, Initial_acc: 1000000</a>
        <a href="/backtest">Link 2</a>
        <a href="/backtest">Link 3</a>
      </div>
    </li>
    </ul>

    <ul>
    <li class="dropdown">
      <a href="javascript:void(0)" class="dropbtn">Company:TCS NSE, Strategy: "Simple Bollinger Bands Strategy", Column: "Close", Indicator_time_period: 5, Sigma: 1</a>
      <div class="dropdown-content">
        <a href="/backtest">Start_date_time: "2021-05-1 00:00:00", End_date_time: "2021-05-20 00:00:00", Risk_ratio: "10:10", Max_risk : 2, Initial_acc: 1000000</a>
        <a href="/backtest">Link 2</a>
        <a href="/backtest">Link 3</a>
      </div>
    </li>
    </ul>
    
    <br><br><br><br><br>
    <hr class="separator" />
    <h2>PaperTraded Strategies</h2>
    <h3>Simple Bollinger Bands Strategy</h3>
    <p> Description: </p>
    <hr class="separator" />
    <ul>
    <li class="dropdown">
      <a href="javascript:void(0)" class="dropbtn">Company:TCS BSE, Strategy: "Simple Bollinger Bands Strategy", Column: "Close", Time_period: 5, Sigma: 1, Name: "tcs bse bb close 5 1"</a>
      <div class="dropdown-content">
        <a href="#">Company:TCS BSE, Strategy: "Simple Bollinger Bands Strategy", Column: "Close", Time_period: 5, Sigma: 1, Name: "tcs bse bb close 5 1"</a>
      </div>
    </li>
    </ul>

    
  </div>
</template>


<script>
export default {
  name: 'StrategiesBase',
}
</script>

<style scoped>
.separator {
  opacity: 1.0;
}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a, .dropbtn {
  display: inline-block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover, .dropdown:hover .dropbtn {
  background-color: #228B22;
}

li.dropdown {
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {background-color: #f1f1f1;}

.dropdown:hover .dropdown-content {
  display: block;
}

</style>
