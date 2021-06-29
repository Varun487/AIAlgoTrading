<template>
    <div class="container">
        <div class="logo"></div>
        <div class="title">AI ALGO TRADER</div> 
        <!--
        <div class="phone"> ☏ xxxxxxxxxx</div>
        <div class="email">✉️ aialgotrader@gmail.com</div>
        -->
        <div class="sitemap-title">Sitemap</div>
        <a href="#" class="sitemap-home">Home</a>
        <a href="#" class="sitemap-about">About</a>
        <a href="#" class="sitemap-logout">Logout</a>
        <!-- Contact Form -->
        <h3 class="contact-form-title">Tell us what you think!</h3>
        <form action="#">
            <input type="text" class="contact-form-name" placeholder="Name">
            <input type="text" class="contact-form-email" placeholder="Email">
            <input type="text" class="contact-form-message" placeholder="Message">
            <button>Submit</button>
        </form>
    </div>
</template>
<script>
export default {
    name: 'FooterBase'
}
</script>
<style scoped>
.container {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 500px;
    /* top: 2270px; */
    
    background-image: url('~@/assets/v10s.jpeg');
    background-size: cover;
    background-position: center left;
}
.logo {
    position: absolute;
    width: 75px;
    height: 65px;
    left: 50px;
    /* top: 160px;*/
    top: 70px;
    background: #FFFFFF;
    border: 1px solid transparent;
    box-sizing: border-box;
    border-radius: 50%;
}
.title {
    position: absolute;
    font-family: Poppins;
    font-size: 40px;
    /* top:163px; */
    top:73px;
    left: 128px;
    margin-top: 0px;
    color:#fff;
    transform: 0.4s;
    text-decoration: underline overline;
    text-underline-offset: 10px;
    text-shadow: 0px 0px 10px #FFFFFF;
}
/*
.phone {
    position: absolute;
    width: 273px;
    height: 37px;
    left: 120px;
    top: 200px;
    font-family: Poppins;
    font-style: normal;
    font-weight: normal;
    font-size: 30px;
    line-height: 45px;
    display: flex;
    align-items: center;
    text-align: center;
    color: #FFFFFF;

}
.email {
    position: absolute;
    width: 500px;
    height: 69px;
    left: 120px;
    top: 220px;

    font-family: Poppins;
    font-style: normal;
    font-weight: normal;
    font-size: 30px;
    line-height: 45px;
    display: flex;
    align-items: center;
    text-align: center;

    color: #FFFFFF;
}
*/
a {
    text-decoration: none;
}
.sitemap-title {
    position: absolute;
    width: 280px;
    height: 27px;
    left: 620px;
    top: 90px;
    font-family: Poppins;
    font-style: normal;
    font-weight: bold;
    font-size: 36px;
    line-height: 54px;
    display: flex;
    align-items: center;
    text-align: center;
    text-decoration-line: none;
    color: #FFFFFF;

}
.sitemap-home {
    position: absolute;
    width: 142px;
    height: 43px;
    left: 650px;
    top: 150px;
    font-family: Poppins;
    font-style: normal;
    font-weight: 500;
    font-size: 30px;
    line-height: 54px;
    display: flex;
    align-items: center;
    text-align: center;
    color: #FFFFFF;
    transition: 0.4s;
}
.sitemap-home:hover {
    color: black;
}
.sitemap-about {
    position: absolute;
    width: 158px;
    height: 40px;
    left: 650px;
    top: 200px;
    font-family: Poppins;
    font-style: normal;
    font-weight: 500;
    font-size: 30px;
    line-height: 54px;
    display: flex;
    align-items: center;
    text-align: center;
    color: #FFFFFF;
    transition: 0.4s;
}
.sitemap-about:hover {
    color: black;
}
.sitemap-logout {
    position: absolute;
    width: 138px;
    height: 40px;
    left: 645px;
    top: 250px;
    font-family: Poppins;
    font-style: normal;
    font-weight: 500;
    font-size: 30px;
    line-height: 54px;
    display: flex;
    align-items: center;
    text-align: center;
    color: #FFFFFF;
    transition: 0.4s;
}
.sitemap-logout:hover {
    color: black;
}
.contact-form-title {
    position: absolute;
    width: 424px;
    height: 27px;
    left: 980px;
    top: 55px;

    font-family: Poppins;
    font-style: normal;
    font-weight: bold;
    font-size: 36px;
    line-height: 54px;
    display: flex;
    align-items: center;
    text-align: center;
    text-decoration-line:none;

    color: #FFFFFF;
}
input {
    position: absolute;
    width: 340px;
    height: 45px;
    font-size: 20px;
    font-family: Poppins;
    background-color: #FFFFFF;
    border: none;
    padding: 0px;
}
input:focus {
    background-color: transparent;
    color: #FFFFFF;

}
.contact-form-name {
    left: 1000px;
    top: 160px;
}
.contact-form-email {
    left:1000px;
    top:220px;
}
.contact-form-message {
    left:1000px;
    top:280px;    
}
button {
    position: absolute;
    width: 120px;
    height: 50px;
    left: 1110px;
    top: 350px;
    background-color: transparent;
    border-radius: 10px;
    border:1px solid #FFFFFF;
    color:#FFFFFF;
    font-size: 20px;
    font-family: Poppins;
    transition: 0.s;
}
button:hover{
    background-color: #000;
    border:1px solid transparent;
}
</style>