<template>
    <div class="topbanner-container">
        <div class="topbanner-title">
            Strategies
        </div>
        <div class="topbanner-description">
           <!--
            It is a long established fact that a reader will be distracted by the readable 
            content of a page when looking at its layout. The point of using Lorem Ipsum is 
            that it has a more-or-less normal distribution of letters, as opposed to using 
            'Content here, content here', making it look like readable English. 
             -->
            A strategy is a set of rules on when to make an order <br>to buy or sell an instrument 
            in the stock market. Strategies read data from the database and can <br>use multiple 
            indicators, machine learning models, <br>or a combination of both to generate orders <br>
            according to the rules mentioned in the strategy. 
        </div>
        <div class="topbanner-bg-vector">

        </div>
    </div>

</template>

<script>
export default {
    name: 'Topbanner',
};
</script>

<style scoped>
.topbanner-container {
    margin-top:80px;
}
.topbanner-title {
    position: absolute;
    width: 344px;
    height: 74px;
    left: 130px;
    top: 150px;
    font-family: Poppins;
    font-style: normal;
    font-weight: bolder;
    font-size: 64px;
    line-height: 96px;
    display: flex;
    align-items: center;
    text-align: center;
    color: #000000;
    
}
.topbanner-description {
    position: absolute;
    width: 553px;
    height: 273px;
    left: 130px;
    top: 200px;
    font-family: Poppins;
    font-style: normal;
    font-weight: normal;
    font-size: 20px;
    line-height: 30px;
    display: flex;
    align-items: center;
    
    color: #000000;
}
.topbanner-bg-vector {
    position: absolute;
    width: 626px;
    height: 352px;
    left: 710px;
    top: 120px;
    background-image: url('~@/assets/v3.jpg');
    background-size: cover;
}
</style>