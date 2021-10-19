<template>
    <div>
        
        <!-- <div v-for="strategy in $store.getters.getAllStrategies"
                :key="strategy.id"
            >
            <h1>{{ strategy.id }}</h1>
            <div @onload="showStrategy(strategy.id)">Go</div>
        </div> -->
        <div class="container">
        <!-- <div class="logo">
        </div> -->
        <router-link to="/strategy">
        <div class="back">
            BACK
            </div>
        </router-link>

        <div class="title">AI ALGO TRADER</div>
        
        <router-link to="/login">
        <div class="logout">
            Logout
        </div>
        </router-link>
        <!--
        <div class="list">
            <ul>
                <li><a href="#">Strategy 1 </a>|</li>
                <li><a href="#">Strategy 2 </a>|</li>
                <li><a href="#">Strategy 3</a></li>
            </ul>
        </div>-->
    </div>
        <BacktesterMain />
    </div>
</template>

<script>
import BacktesterMain from "./Main/MainBase.vue"


export default {
  name: "BacktestReportBase",
  components: {
    // Navbar,
    BacktesterMain,
  },
  methods: {
    // addRows(){
    //   this.$store.commit('incrementRows',5);
    // }
  },
    mounted() {
    // this.$store.dispatch("setBacktestReportdata",21);
    // this.$store.dispatch("setTradeVisualization",21);
    // this.$store.dispatch("setTrades",21);
    // this.$store.dispatch("incrementRows",5);
    this.$store.dispatch("setAllBacktests",this.$store.getters.getStrategyId);
    this.$store.dispatch("setBacktestReportdata",this.$store.getters.getBacktestsId);
    this.$store.dispatch("setTradeVisualization",this.$store.getters.getBacktestsId);
    this.$store.dispatch("setTrades",this.$store.getters.getBacktestsId);
  },
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap');
.container {
    background-color: #fff;
    margin-top: 0px;
    padding-top: 0px;
    margin-bottom: 0px;
    margin-left: 0px;
    position: fixed;
    z-index: 100;
    width: 100%;
    top: 0px;
    height: 80px;
    filter: drop-shadow(0px 10px 10px rgba(0, 0, 0, 0.50));
    background-image: url("~@/assets/v1s.jpg");
    background-repeat: repeat;
    background-size:cover;
    background-position: center right;
    /*background-image: url("~@/assets/logo.jpg");
    background-size:100%;*/
}
.logo {
    position: absolute;
    width: 75px;
    height: 65px;
    left: 41px;
    top: 7px;
    background: #FFFFFF;
    border: 1px solid transparent;
    box-sizing: border-box;
    border-radius: 50%;
    
}

.title {
    position: absolute;
    font-family: Poppins;
    font-size: 40px;
    top:10px;
    left: 140px;
    margin-top: 0px;
    color:#fff;
    transform: 0.4s;
    
}

.logout {
    position: absolute;
    width: 150px;
    height: 50px;
    right: 40px;
    top: 16px;
    background-color: transparent;
    border:1px solid #FFFFFF;
    box-shadow: 0px 0px 5px #FFFFFF;
    box-sizing: border-box;
    border-radius: 50px;
    text-align: center;
    line-height: 50px;
    transition: 0.5s;
    color: #FFFFFF;
    font-size: 20px;
}
.logout:hover {
    box-shadow: 0px 0px 1px #FFFFFF;
    color: black;
    background-color: whitesmoke;
}

.back {
    position: absolute;
    width: 100px;
    height: 50px;
    /* right: 40px; */
    font-family: Poppins;
    top:10px;
    left: 15px;
    margin-top: 0px;
    background-color: transparent;
    border:1px solid #FFFFFF;
    box-shadow: 0px 0px 5px #FFFFFF;
    box-sizing: border-box;
    border-radius: 50px;
    text-align: center;
    line-height: 50px;
    transition: 0.5s;
    color: #FFFFFF;
    font-size: 20px;
}
.back:hover {
    box-shadow: 0px 0px 1px #FFFFFF;
    color: black;
    background-color: whitesmoke;
}

ul {

    list-style: none;
    display: flex;
    justify-content: flex-end;
    margin-top:23px;
    margin-right:50px;
}
li {

    margin-right:10px;
    font-family: Poppins;
    font-size: 20px;
    color:#FFFFFF;
    
}
a {
    text-decoration: none;
    color: #FFFFFF;
    transform: 0.9s;
}
a:hover {
   font-weight: bold;
}

</style>