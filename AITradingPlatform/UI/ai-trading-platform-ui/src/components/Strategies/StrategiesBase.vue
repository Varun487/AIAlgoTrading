<template>
  <div>
    <h1><center>Strategies</center></h1>
    <hr class="separator" />
    <h2>BackTested Strategies</h2>
    <p> Description: </p>
    <hr class="separator" />
    

    <div class="dropdown">
    <button class="dropbtn">Company:TCS BSE, Strategy: "Simple Bollinger Bands Strategy", Column: "Close", Indicator_time_period: 5, Sigma: 1</button>
    <div class="dropdown-content">
    <a href="/backtest">Start_date_time: "2021-05-1 00:00:00", End_date_time: "2021-05-20 00:00:00", Risk_ratio: "10:10", Max_risk : 2, Initial_acc: 1000000</a>
    <a href="/backtest">Link 2</a>
    <a href="/backtest">Link 3</a>
    </div>
    </div>
    <br><br><br><br><br><br><br><br><br><br><br><br>
    <div class="dropdown">
    <button class="dropbtn">Company:TCS NSE, Strategy: "Simple Bollinger Bands Strategy", Column: "Close", Indicator_time_period: 5, Sigma: 1</button>
    <div class="dropdown-content">
    <a href="/backtest">Start_date_time: "2021-05-1 00:00:00", End_date_time: "2021-05-20 00:00:00", Risk_ratio: "10:10", Max_risk : 2, Initial_acc: 1000000</a>
    <a href="/backtest">Link 2</a>
    <a href="/backtest">Link 3</a>
    </div>
    </div>
    <br><br><br><br><br><br><br><br><br><br>
    <hr class="separator" />
    <h2>PaperTraded Strategies</h2>
    <p> Description: </p>
    <hr class="separator" />
    <div class="dropdown">
    <button class="dropbtn">Company:TCS BSE, Strategy: "Simple Bollinger Bands Strategy", Column: "Close", Time_period: 5, Sigma: 1, Name: "tcs bse bb close 5 1"</button>
    <div class="dropdown-content">
    <a href="#">Company:TCS BSE, Strategy: "Simple Bollinger Bands Strategy", Column: "Close", Time_period: 5, Sigma: 1, Name: "tcs bse bb close 5 1"</a>
    </div>
    </div>
    
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
.dropbtn {
  background-color: #4CAF50;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}

.dropdown {
  
  display: inline-block;
  position: fixed; /* or absolute */
  left: 25%;
  width: 50000px;
  height: 400px;
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
}

.dropdown-content a:hover {background-color: #f1f1f1}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropbtn {
  background-color: #3e8e41;
}

</style>
