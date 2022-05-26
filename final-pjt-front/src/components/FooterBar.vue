<template>
  <div class="footer-basic">
        <footer>
            <div class="social"><a href="https://www.instagram.com/qqqqqkr/"><i class="fa-brands fa-instagram"></i></a><a href="https://www.instagram.com/nogusdn/"><i class="fa-brands fa-facebook-f"></i></a>
            <a href="https://www.instagram.com/nogusdn/"><i class="fa-brands fa-github"></i></a>
            <a href="https://www.instagram.com/nogusdn/"><i class="fa-brands fa-snapchat"></i></a>
            </div>
            <ul class="list-inline">
                <li class="list-inline-item"><a href="https://www.instagram.com/nogusdn/">Home</a></li>
                <li class="list-inline-item"><a href="https://www.instagram.com/nogusdn/">Services</a></li>
                <li class="list-inline-item"><a href="https://www.instagram.com/qqqqqkr/">About</a></li>
                <li class="list-inline-item"><a href="https://www.instagram.com/ssafy/">Terms</a></li>
                <li class="list-inline-item"><a href="https://www.instagram.com/ssafy/">Privacy Policy</a></li>
            </ul>
            <p class="copyright">made by 노현우 박주현 © 2022</p>
        </footer>
    </div>
</template>

<script>
export default {
  name:'FooterBar'
}
</script>

<style>
.footer-basic {
  padding:40px 0;
  background-color:rgb(2,3, 16);
  color: white;
}

.footer-basic ul {
  padding:0;
  list-style:none;
  text-align:center;
  font-size:18px;
  line-height:1.6;
  margin-bottom:0;
}

.footer-basic li {
  padding:0 10px;
}

.footer-basic ul a {
  color:inherit;
  text-decoration:none;
  opacity:0.8;
}

.footer-basic ul a:hover {
  opacity:1;
}

.footer-basic .social {
  text-align:center;
  padding-bottom:25px;
}

.footer-basic .social > a {
  font-size:24px;
  width:40px;
  height:40px;
  line-height:40px;
  display:inline-block;
  text-align:center;
  border-radius:50%;
  border:1px solid #ccc;
  margin:0 8px;
  color:inherit;
  opacity:0.75;
}

.footer-basic .social > a:hover {
  opacity:0.9;
}

.footer-basic .copyright {
  margin-top:15px;
  text-align:center;
  font-size:13px;
  color:#aaa;
  margin-bottom:0;
}

</style>