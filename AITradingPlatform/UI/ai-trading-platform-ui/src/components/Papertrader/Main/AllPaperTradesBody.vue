<template>
    <div class="all-trades-wrapper">
        <h2 class="at-title">All Paper Traded Orders</h2>
        <div class="card c1">
        </div>
        <div class="card c2">
            
        </div>
        <div class="card c3">
            
        </div>
    </div>
</template>

<script>
export default {
    name: 'AllPaperTradesBody',
}
</script>
<style scoped>
.all-trades-wrapper {
    text-align: center;
    margin-top:0%;
    /*margin-bottom: 5%;*/
    /*margin-left:5%;*/
    padding: 50px 0px 10px 0px;
    /*width: 1225px;*/
    width:100%;
    /*border-radius: .5em;*/
    box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 /20%), 0 0 0 1px rgb(10 10 10 / 2%);
    background-color: #fff;
    transition: 0.6s;
    color:#000;
}

.at-title{
    font-family: Poppins;
    font-size: 70px;
    padding-bottom:15px;
    text-decoration: underline;
    text-decoration-thickness: 2px;
    text-underline-offset: 10px;
}

.card {
    margin: 20px 20px;
    width:350px;
    border: 1px solid #fff;
    padding: 250px 50px;
    border-radius: 20px;
    box-shadow: 0 0.2em 1em -0.125em rgb(10 10 10 /20%), 0 0 0 1px rgb(10 10 10 / 2%);
    transition: 0.6s;
}

.card:hover {
    box-shadow: 0 0.5em 4em -0.125em rgb(10 10 10 /20%), 0 0 0 1px rgb(10 10 10 / 2%);
}

.c1 {
    position: absolute;
    left:3%;

}

.c2 {
    position: relative;
    top: 7px;
    left: 36%;
}

.c3 {
    position: relative;
    top: -520px;
    left:70%;
}
</style>