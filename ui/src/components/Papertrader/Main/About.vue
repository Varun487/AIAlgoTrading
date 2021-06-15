<template>
    <div class="about-wrapper">
        <h3>The Paper Trader aids in evaluating the performance of a backtested strategy in real market conditions.
        <br>Strategies are run against real time data to generates orders. Detailed report indicating the 
        performance <br> of the stratedy are generated after evaluating these orders .
    </h3>
    </div>
    
</template>

<script>
export default {
    name: 'About',
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap');

.about-wrapper {
    box-shadow: 0 0.2em 1em -0.125em rgb(10 10 10 /20%), 0 0 0 1px rgb(10 10 10 / 2%);
    color:#fff;
    border:1px solid #fff;
    margin:70px 60px 40px 60px;
    padding: 100px 10px;
    border-radius: 40px;
    transition: 0.6s;
}
.about-wrapper:hover {
    box-shadow: 0 2.5em 8em -0.125em rgb(10 10 10 /20%), 0 0 0 1px rgb(10 10 10 / 2%);
    border-radius: 50px;
    
}
h3 {
    text-align: center;
    color: #000;
    font-family: Poppins;
    font-size:20px;
    
}

</style>
