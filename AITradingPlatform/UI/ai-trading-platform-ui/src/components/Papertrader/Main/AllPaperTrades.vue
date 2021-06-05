<template>    
    <body>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
        <button type="button" class="btn btn-outline-primary">
            View Orders
        </button>
    </body>
    
</template>

<script>

export default {
    name: 'AllPaperTrades',
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap');

button {
    position:relative;
    text-align: center;
    /*color: dodgerblue;*/
    font-size: 20px;
    margin-left: 52%;
    margin-top: -3.8%;
    padding: 4px 70px;
    font-family: Poppins;
    width:auto;
    border-radius: 50px;
    background-image: linear-gradient(270deg, dodgerblue,blue);
    color: wheat;
    opacity: 0.9;
    transition: 0.6s;
    border: 1px solid #b3aeb5;
}

button:hover{
    opacity: 1;
    font-size: 21px;
    background-image: linear-gradient(200deg, dodgerblue,blue);
    font-weight: bold;
}

</style>
