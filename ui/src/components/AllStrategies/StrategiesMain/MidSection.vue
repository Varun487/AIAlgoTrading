<template>
    <div class="container">
        
        <div class="title">
            All Strategies
        </div>
        
        <!--
        <div class="strat1">
            <div class="strat1-img"></div>
            <div class="strat1-content">
                <p class="strat-name">Strategy 1</p>
                <p class="strat-desc">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. </p>
                <button>Start</button>
            </div>
        </div>
        <div class="strat2">
            <div class="strat2-img"></div>
            <div class="strat2-content">
                <p class="strat-name">Strategy 2</p>
                <p class="strat-desc">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. </p>
                <button>Start</button>
            </div>
        </div>
        <div class="strat3">
            <div class="strat3-img"></div>
            <div class="strat3-content">
                <p class="strat-name">Strategy 3</p>
                <p class="strat-desc">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. </p>
                <button>Start</button>
            </div>
        </div>
        -->
        <!--
        <div class="strat1thissssss">
            <div class="strat1-img"></div>
            <div 
                class="strat1-content"
                v-for="strategy in $store.getters.getAllStrategies"
                :key="strategy.id"
            >
                <p class="strat-name">{{ strategy.name }}</p>
                <p class="strat-desc">{{ strategy.description }}</p>
                <button @click="showStrategy(strategy.id)">Go</button>
            </div>
        </div>
        -->
        <!--
        <div class="strat1-img"></div>
        <div class="strat2-img"></div>
        -->
        <div class="strat3-img"></div>
        <div class="strat2-img"></div>
        <div class="strat">
            <div 
                class="strat1-content"
                v-for="strategy in $store.getters.getAllStrategies"
                :key="strategy.id"
            >
            
                <div class="strat-name">{{ strategy.name }}</div>
                <div class="strat-desc">{{ strategy.description }}</div>
                
                <button @click="showStrategy(strategy.id)">Go</button>
                <router-link to="/">
                </router-link>>
            </div>
        </div>
        <!--
        <div class="strat2">
            <div class="strat2-img"></div>
            <div class="strat2-content">
                <p class="strat-name">Strategy 2</p>
                <p class="strat-desc">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. </p>
                <button>Start</button>
            </div>
        </div>
        <div class="strat3">
            <div class="strat3-img"></div>
            <div class="strat3-content">
                <p class="strat-name">Strategy 3</p>
                <p class="strat-desc">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. </p>
                <button>Start</button>
            </div>
        </div>
        -->
    </div>
</template>

<script>
export default {
    name: 'MidSection',
    methods: {
        showStrategy(id) {
            this.$store.dispatch("setStrategyId", id);
            // this.$store.dispatch("flipAllStrategiesMainPage");
            this.$router.push({name:'StrategyPage'});
    },
  },
    mounted() {
    this.$store.dispatch("setAllStrategies");
    
  },
};
</script>

<style scoped>
.container {
    background-color: #FFFFFF;
}
/*
.line1 {
    position: absolute;
    width: 521px;
    height: 0px;
    left: 0px;
    top: 691px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
*/
.title {
    margin-top: 40%;
    left: 530px;
    top: 652px;
    font-family: Poppins;
    font-style: normal;
    font-weight: normal;
    font-size: 55px;
    line-height: 82px;
    display: flex;
    align-items: center;
    text-align: center;
    color: #000000;
    display: flex;
    flex-direction: row;
    font-weight: lighter;
}
.title:before, .title:after {
    content: "";
    flex: 1 1;
    border-bottom: 1px solid #000;
    margin: auto;
}
/*
.line2 {
    position: absolute;
    width: 465px;
    height: 0px;
    left: 880px;
    top: 691px;
    border: 1px solid rgba(0, 0, 0, 0.1);
}
*/
.strat1-content {
    position: relative;
    width: 512px;
    height: 300px;
    left:760px;
    background: #FFFFFF;
    box-shadow: 4px 4px 50px rgba(0, 0, 0, 0.25);
    border-radius: 30px;
    text-align: center;
    margin: 40px;
    margin-top:180px;
}
.strat-name {
    font-family: Poppins;
    font-style: normal;
    font-weight: bold;
    font-size: 30px;
    color: #000000;
    text-align: center;
    padding: 20px;
    
}
.strat-desc {
    position: absolute;
    width: 376.42px;
    height: 159.71px;
    left: 15%;
    top: 40px;
    font-family: Poppins;
    font-style: normal;
    font-weight: normal;
    font-size: 20px;
    line-height: 30px;
    display: flex;
    align-items: center;
    text-align: center;
    color: #000000;
}
.strat1-img {
    position: absolute;
    width: 495px;
    height: 482px;
    left: 101px;
    top: 650px;
    background-image: url('~@/assets/v9.jpg');
    background-size: cover;
}

.strat2-img {
    position: absolute;
    width: 670px;
    height: 440px;
    /*left: 675px;*/
    left: 100px;
    top: 1250px;
    background-image: url('~@/assets/v5.jpeg');
    background-size: cover;
}

.strat2-content {
    position: absolute;
    width: 512px;
    height: 300px;
    left: 93px;
    top: 1250px;
    background: #FFFFFF;
    box-shadow: 4px 4px 50px rgba(0, 0, 0, 0.25);
    border-radius: 30px;
}

.strat3-img {
    position: absolute;
    width: 589px;
    height: 628px;
    /*
    left: 68px;
    top: 1650px;
    */
    left: 120px;
    top: 650px;
    background-image: url('~@/assets/v4.png');
    background-size: cover;
}

.strat3-content {
    position: absolute;
    width: 512px;
    height: 300px;
    left: 750px;
    top: 1850px;
    background: #FFFFFF;
    box-shadow: 4px 4px 50px rgba(0, 0, 0, 0.25);
    border-radius: 30px;
}


button {
    position: absolute;
    text-align: center;
    font-size: 20px;
    margin-left:10px;
    margin-top:10px;
    padding: 4px 70px;
    font-family: Poppins;
    border-radius: 50px;
    background-image: linear-gradient(270deg, dodgerblue,blue);
    color: #fff;
    opacity: 0.9;
    transition: 0.4s;
    border: 1px solid transparent;
    width: auto;
    top: 200px;
    left: 30%;
}
button:hover{
    opacity: 1;
    background-image: linear-gradient(200deg, dodgerblue,blue);
    font-weight: bold;
    box-shadow: 0px 0px 5px #fff;
    border-color: #fff;
}
</style>
