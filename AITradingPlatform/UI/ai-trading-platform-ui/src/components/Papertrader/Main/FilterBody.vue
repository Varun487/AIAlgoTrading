<template>
    <div class="filter-wrapper">
        <h2 class="filter-title">Filter Orders</h2>
        <h3 class="filter-desc">Orders can be filtered according to the following criteria</h3>
        <div class="filter-section">
            <label for="sd">Start Date</label>
            <input type="date" name="sd">
        </div>
        <div class="filter-section">
            <label for="ed">End Date</label>
            <input type="date" name="ed">
        </div>
        <div class="filter-section">
            <label for="ord-type">Order Type</label>
            <select name="ord-type">
                <option value="B">Buy</option>
                <option value="S">Short</option>
                <option value="G">GTFO</option>
            </select>
        </div>
        <div class="filter-section">
            <label for="company">Company</label>
            <select name="company">
                <option value="select">Select</option>
            </select>
        </div>
        <div class="filter-section">
            <label for="strategy">Strategy</label>
            <select name="strategy">
                <option value="select">Select</option>
            </select>
        </div>
        <button>Go</button>
    </div>
</template>

<script>
export default {
    name: "FilterBody"
};
</script>

<style scoped>
.filter-wrapper {
    text-align: center;
    margin-top:10%;
    /*margin-bottom: 5%;*/
    /*margin-left:5%;*/
    padding: 120px 0px 130px 0px;
    /*width: 1225px;*/
    width:100%;
    /*border-radius: .5em;*/
    box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 /20%), 0 0 0 1px rgb(10 10 10 / 2%);
    background-color: #000;
    transition: 0.6s;
    color:#fff;
}
/*
.filter-wrapper:hover{
    box-shadow: 0 2.5em 1em 0.125em rgb(10 10 10 /20%), 0 0 0 1px rgb(10 10 10 / 2%);
    
}
*/
.filter-title{
    font-family: Poppins;
    font-size: 70px;
    padding-bottom:15px;
    text-decoration: underline;
    text-decoration-thickness: 2px;
    text-underline-offset: 10px;
}

.filter-section {
    font-family: Poppins;
    font-weight:bold;
}

label {
    font-size:25px;
    padding: 10px 10px;
}

option {
    font-weight: bold;
}

button {
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
    border: 1px solid #000;
    width: auto;
}

button:hover{
    opacity: 1;
    background-image: linear-gradient(200deg, dodgerblue,blue);
    font-weight: bold;
    box-shadow: 0px 0px 5px #fff;
    border-color: #fff;
}
</style>