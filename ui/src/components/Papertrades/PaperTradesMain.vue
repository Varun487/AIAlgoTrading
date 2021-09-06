<template>
    <div>
        <div class="pt-title">PAPER TRADES</div>
        <div class="pt-type">Historical</div>
        <div class="pt-t-info">
            <h3>General Information</h3>
            <div class="t-company">Company:</div>
            <div class="t-last_updated">Last Updated:</div>
            <div class="t-open">Open:</div>
            <div class="t-high">High:</div>
            <div class="t-close">Close:</div>
            <div class="t-low">Low:</div>
        </div>
       <h4>TRADE DETAILS</h4>
       <div class="pt-m-info">
           <h3>Strategy Configuration</h3>
            <div class="m-sname">Strategy Name:</div>
            <div class="m-itp">Indicator Time Period:</div>
            <div class="m-mhp">Maximum Holding Period:</div>
            <div class="m-tpf">Take Profit Factor:</div>
            <div class="m-slf">Stop Loss Factor:</div>
            <div class="m-sigma">Sigma:</div>
            <h3>Trade</h3>
            <div class="m-entry-order">Entry Order:</div>
            <div class="m-exit-order">Exit Order:</div>
            <div class="m-duration">Duartion:</div>
            <div class="m-net-returns">Net Returns:</div>
            <div class="m-return-percentage">Return Percentage:</div>
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
