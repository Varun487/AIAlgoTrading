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
            v-for="report in $store.getters.getAllBacktests.slice(0, 5)"
      v-bind:key="report.id">
            
      <!-- <tr class="hover1" v-for="report in computedObj" :key="report.id"> -->
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
            
            <!-- <button @click="report in $store.getters.getAllBacktests">Show more</button> -->
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
            <div class="card text-center m-3">
        <h1 class="card-header">Vue.js Pagination Tutorial  Example</h1>
        <div class="card-body">
            <div v-for="item in pageOfItems" :key="item.id">
                <p>{{item.name}}</p></div>
        </div>
        <div class="card-footer pb-0 pt-3">
            <p><jw-pagination :items="exampleItems" @changePage="onChangePage" :labels="customLabels"></jw-pagination></p>
        </div>
    </div>
        <!-- </div> -->
    
</div>
    
</template>

<script>
const exampleItems = [...Array(150).keys()].map(i => ({ id: (i+1), name: 'Item ' + (i+1) }));
const customLabels = {
    first: '<<',
    last: '>>',
    previous: '<',
    next: '>'
};

export default {
    name: 'MainLanding',
//     mounted() {
//         return {
//     object:this.$store.dispatch("setAllBacktests",2), // your original data
//     limit: 5 // or any number you wish to limit to
//   }
//     // this.$store.dispatch("setAllBacktests",2);
//   },
//   data(){
//   return {
//     object:this.$store.dispatch("setAllBacktests",2), // your original data
//     limit: 5 // or any number you wish to limit to
//   }
// },
//   computed:{
//   computedObj(){
//     return this.limit ? this.object.slice(0,this.limit) : this.object
//   }
// }
data() {
        return {
            exampleItems,
            customLabels,
            pageOfItems: [],
        };
    },
    methods: {
        onChangePage(pageOfItems) {
            // update page of items
            this.pageOfItems = pageOfItems;
        }
    }
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
    top: 1570px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
.title {
    position: absolute;
    width: 1000px;
    height: 78px;
    left: 750px;
    top: 1530px;
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
    top: 1570px;
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

.hover1:hover td {
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
