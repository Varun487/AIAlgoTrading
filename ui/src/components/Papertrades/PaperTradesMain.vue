<template>
    <div>
        <div class="pt-title">PAPER TRADES</div>
        <div class="pt-type" v-if='$store.getters.getPaperTradeTopData.live== "True"'>LIVE</div>
        <div class="pt-type" v-else>HISTORICAL</div>
        <div class="pt-t-info">
            <h3>General Information</h3>
            <div class="t-company"><b>Company:</b> {{$store.getters.getPaperTradeTopData.company.name}}</div>
            <div class="t-last_updated"><b>Last Updated:</b> {{$store.getters.getPaperTradeTopData.last_updated}}</div>
            <div class="t-open"><b>Open: </b>{{$store.getters.getPaperTradeTopData.ticker_data.open}}</div>
            <div class="t-high"><b>High: </b>{{$store.getters.getPaperTradeTopData.ticker_data.high}}</div>
            <div class="t-close"><b>Close: </b>{{$store.getters.getPaperTradeTopData.ticker_data.close}}</div>
            <div class="t-low"><b>Low: </b>{{$store.getters.getPaperTradeTopData.ticker_data.low}}</div>
        </div> 
       <h4>TRADE DETAILS</h4>
       <div class="pt-m-info">
           <h3>Strategy Configuration</h3>
            <div class="m-sname"><b>Strategy Name: </b>{{$store.getters.getPaperTradeMidData.paper_traded_strategy.strategy_config.strategy_type.name}}</div>
            <div class="m-itp"><b>Indicator Time Period: </b>{{$store.getters.getPaperTradeMidData.paper_traded_strategy.strategy_config.indicator_time_period}}</div>
            <div class="m-mhp"><b>Maximum Holding Period: </b>{{$store.getters.getPaperTradeMidData.paper_traded_strategy.strategy_config.max_holding_period}}</div>
            <div class="m-tpf"><b>Take Profit Factor: </b>{{$store.getters.getPaperTradeMidData.paper_traded_strategy.strategy_config.take_profit_factor}}</div>
            <div class="m-slf"><b>Stop Loss Factor: </b>{{$store.getters.getPaperTradeMidData.paper_traded_strategy.strategy_config.stop_loss_factor}}</div>
            <div class="m-sigma"><b>Sigma: </b>{{$store.getters.getPaperTradeMidData.paper_traded_strategy.strategy_config.sigma}}</div>
            <h3>Trade</h3>
            <div class="m-entry-order"><b>Entry Order: </b>{{$store.getters.getPaperTradeMidData.trade.entry_order}}</div>
            <div class="m-exit-order"><b>Exit Order: </b>{{$store.getters.getPaperTradeMidData.trade.exit_order}}</div>
            <div class="m-duration"><b>Duration: </b>{{$store.getters.getPaperTradeMidData.trade.duration}}</div>
            <div class="m-net-returns"><b>Net Returns: </b>{{$store.getters.getPaperTradeMidData.trade.net_return}}</div>
            <div class="m-return-percentage"><b>Return Percentage: </b>{{$store.getters.getPaperTradeMidData.trade.return_percent}}</div>
       </div>
       <h4>TRADE VISUALIZATION</h4>
       <div class="pt-b-info"></div>
    </div>
</template>
<script>
//  import axios from "axios";
export default {
  name: "PapertradesMain",
  methods: {
    
  },
  mounted() {
    this.$store.dispatch("setPaperTradeTopData",this.$store.getters.getPapertradesId);
    this.$store.dispatch("setPaperTradeMidData",this.$store.getters.getPapertradesId);
    this.$store.dispatch("setPaperTradeBottomData",this.$store.getters.getPapertradesId);
  },
}
</script>
<style scoped>
.pt-title{
    margin-top: 70px;
    text-align: center;
    font-size: 50px;
    font-weight: bold;
}
.pt-type{
    text-align: center;
    font-size: 30px;
    font-weight: light;
    margin-bottom: 20px;
}
.pt-t-info{
    margin-top: 50px;
    margin-left: 15%;
    font-weight: lighter;
    font-size: 24px;
}
h3{
    text-decoration: underline;
}
h4 {
    display: flex;
    flex-direction: row;
    font-size: 40px;
    font-weight: lighter;
}
h4:before, h4:after {
    content: "";
    flex: 1 1;
    border-bottom: 1px solid #000;
    margin: auto;
}
.pt-m-info {
    margin-top: 50px;
    margin-left: 15%;
    font-weight: lighter;
    font-size: 24px;
}
</style>
