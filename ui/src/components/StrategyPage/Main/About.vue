<template>

    <div class="strategy">
        <h1 >{{ $store.getters.getSelectedStrategy.name }}</h1>
        <!-- <div class= "attributes"
        v-for="strategy in $store.getters.getSelectedStrategy"
                :key="strategy.id"> -->
        <div class= "attributes">
        <center><p>Description: {{ $store.getters.getSelectedStrategy.description }}</p></center>
        <center><p>Stock Selection: {{ $store.getters.getSelectedStrategy.stock_selection }}</p></center>
        <center><p>Entry Criteria: {{ $store.getters.getSelectedStrategy.entry_criteria }}</p></center>
        <center><p>Exit Criteria: {{ $store.getters.getSelectedStrategy.exit_criteria }}</p></center>	
        <center><p>Stop Loss Method: {{ $store.getters.getSelectedStrategy.stop_loss_method }}</p></center>	
        <center><p>Take Profit Method: {{ $store.getters.getSelectedStrategy.take_profit_method }}</p></center><br><br>
        </div>
    
    
    </div>
    
    
</template>

<script>
export default {
    name: 'About',
    methods: {
        showPerStrategy(id) {
            this.$store.dispatch("setSelectedStrategyId", id);
            this.$store.dispatch("flipPerStrategiesMainPage");
        },
    },
};
</script>

<style scoped>
.strategy {
    margin:0px;
    color: rgb(255, 255, 255);
    background-color: rgb(255, 255, 255);
}

/* .about-wrapper {
    
    color:#fff;
    margin:70px 60px 40px 60px;
    padding: 100px 100px;
    background: rgb(255, 255, 255);
} */
h1{
    text-align: center;
    padding: 20px;
    color:black;
    background-color: rgb(255, 255, 255);
    font-family: Poppins;
    font-size: 55px;
    line-height: 82px;
    
}
p{
    text-align: center;
    padding: 50px;
	top: 485px;
	/* left: 1000px; */
	width: 688.2px;
	height: 69.64px;
	overflow: hidden;
	font-family: Poppins;
	font-size: 25px;
	font-weight: bold;
	color:#000000;
} 
h3 {
    text-align: center;
    color: #000;
    font-family: Poppins;
    font-size:60px;
	float: left;
    margin-left: 100px;
}

</style>
