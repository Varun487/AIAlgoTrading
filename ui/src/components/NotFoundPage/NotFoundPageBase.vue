<template>
    <div id=main>
        <center>
            <h1>404 not found</h1>
            <h3>THE PAGE YOU WERE LOOKING FOR DOES NOT EXIST</h3>
            <h6>YOU MAY HAVE MISTYPED THE ADDRESS OR THE PAGE MAY HAVE MOVED</h6>
            <div id=link>
                
             <a href="http://localhost:8080/">Take me back</a> 
             
             </div>
        </center>
    </div>
</template>

<script>
//  import axios from "axios";
export default {
  name: "NotFoundPageBase",
 
}
</script>
<style scoped>
#main{
    position:relative;
}
#link{
    position:absolute;
    top:200px;
    left:870px;
}
</style>
