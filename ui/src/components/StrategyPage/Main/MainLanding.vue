<template>
<div class="strategy">
    <div class="line1">
        </div>
        <div class="title">
            BACKTESTS
        </div>
        <div class="line2">
        </div>
        <!-- <div id="tab"> -->
            <table class="center">
            <tr>
                <th>Company Ticker</th>
                <th>Return %</th>
                <th>Returns</th>
            </tr>
            <br><br>
            
            <tr class="hover1"
            v-for="report in $store.getters.getAllBacktests"
      :key="report.id">
                <td><a href="/backtestreport">
                    {{ report.company_ticker }}</a></td>

                <td class="red" v-if='report.total_returns_percent < 0'>{{ report.total_returns_percent }}</td>
                <td class="green" v-else-if='report.total_returns_percent > 0'>{{ report.total_returns_percent }}</td>
                <td class="black" v-else>{{ report.total_returns_percent }}</td>

                <td class="red" v-if='report.total_returns < 0'>{{ report.total_returns }}</td>
                <td class="green" v-else-if='report.total_returns > 0'>{{ report.total_returns }}</td>
                <td class="black" v-else>{{ report.total_returns }}</td>
            </tr>
            <br><br>
            <!-- <tr class="hover1">
                <td>Apple</td>
                <td>- 5</td>
                <td>-90.0</td>
            </tr>
            <br><br>
            <tr class="hover1">
                <td>Apple</td>
                <td>0.0</td>
                <td>0.0</td>
            </tr> -->
            
            
            </table>
            <br><br><br><br>
        <!-- </div> -->
    
</div>
    
</template>

<script>
export default {
    name: 'MainLanding',
    mounted() {
    this.$store.dispatch("setAllBacktests",2);
  },
};
</script>

<style scoped>
.strategy {
    margin:0px;
    color: rgb(255, 255, 255);
    background-color: rgb(255, 255, 255);
}
h1{
    text-align: center;
    padding: 20px;
    color:black;
    background-color: rgb(255, 255, 255);
    font-family: Poppins;
    font-size: 55px;
    line-height: 82px;
    
}
/* p{
    text-align: center;
    padding: 20px;
    color:black;
    background-color: rgb(255, 255, 255);
} */
p{
    text-align: center;
    padding: 20px;
	top: 485px;
	left: 1000px;
	width: 688.2px;
	height: 69.64px;
	overflow: hidden;
	font-family: Poppins;
	font-size: 25px;
	font-weight: bold;
	color:#000000;
} 
.line1 {
    position: absolute;
    width: 675px;
    height: 0px;
    left: 0px;
    top: 1750px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
.title {
    position: absolute;
    width: 1000px;
    height: 78px;
    left: 750px;
    top: 1710px;
    font-family: Poppins;
    font-style: normal;
    font-weight: normal;
    font-size: 55px;
    line-height: 82px;
    display: flex;
    align-items: center;
    text-align: center;
    color: #000000;
}

.line2 {
    position: absolute;
    width: 735px;
    height: 0px;
    left: 1100px;
    top: 1750px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
table {
  font-family: arial, sans-serif;
  border: 1px solid rgb(255, 255, 255);
  /* border-collapse: collapse; */
  width: 75%;
  color: black;
  font-size: 23px;
  border-radius: 25px;
}

th{
    border: 1px solid #ffffff;
    text-align: center;
    padding: 25px;
    width: 750px;
    height: 0px;
    left: 1100px;
    top: 1200px;
}
td{
    border: 1px solid #941dcb;
    text-align: center;
    padding: 25px;
    width: 750px;
    height: 0px;
    left: 1100px;
    top: 1200px;
    border-radius: 25px; 
}
.hover1:hover {
    background-color: #941dcb;
    color: white;
}
table.center {
  margin-left: auto; 
  margin-right: auto;
}
a{
    color: black;
    text-decoration: none;
}
a:hover {
    background-color: #941dcb;
    color: white;
}
.green{
  padding: 10px;
  color:green;
   
 /* border-radius: 50px;
  border-collapse: collapse;
  border: 2px solid #941dcb; */
}
.red{
  padding: 10px;
  color:rgb(255, 0, 0);
   
 /* border-radius: 50px;
  border-collapse: collapse;
  border: 2px solid #941dcb; */
}

.black{
  padding: 10px;
  color:rgb(0, 0, 0);
   
 /* border-radius: 50px;
  border-collapse: collapse;
  border: 2px solid #941dcb; */
}

/* th:hover {
    background-color: #ffffff;
} */

/* tr:nth-child(even) {
  background-color: #dddddd;
} */
</style>
