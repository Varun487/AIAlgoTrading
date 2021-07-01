<template>
    <div class="container">
        <div class="content">
            Made with ♥ from VSDH
        </div>
    </div>
</template>

<script>
export default {
    name : 'Footer',
};
</script>

<style scoped>
/*
.container {
    position: absolute;
    width: 100%;
    height: 400px;
    left: 0px;
    top: 2273px;
    background-image: url('~@/assets/v1.jpg');
    background-size: cover;
}
.logo {
    position: absolute;
    width: 75px;
    height: 65px;
    left: 50px;
    top: 70px;
    background: #FFFFFF;
    border: 1px solid transparent;
    box-sizing: border-box;
    border-radius: 50%;
}
*/
.container {
    position: absolute;
    width: 100%;
    height: 45px;
    left: 0px;
    top: 100%;
    background-color: #2876f9;
    background-image: linear-gradient(-90deg, #2876f9 0%, #6d17cb 74%);
    background-size: cover;
   
}
.content {
    text-align: center;
    position: absolute;
    width: 100%;
    height: 45px;
    left: 550px;
    top: 0px;
    margin-bottom: 0px;
    font-family: Poppins;
    font-style: normal;
    font-weight: 500;
    font-size: 25px;
    line-height: 37px;
    display: flex;
    align-items: center;
    text-align: center;
    color: #FFFFFF;
}
</style>