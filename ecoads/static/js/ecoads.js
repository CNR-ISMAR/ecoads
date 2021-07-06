function myFunction() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("btn1");

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btnText.innerHTML = "Read more";
        moreText.style.display = "none";
    } else {
        dots.style.display = "none";
        btnText.innerHTML = "Read less";
        moreText.style.display = "inline";
    }
}

var zoomImg = function () {
    // (A) CREATE EVIL IMAGE CLONE
    var clone = this.cloneNode();
    clone.classList.remove("zoomD");
  
    // (B) PUT EVIL CLONE INTO LIGHTBOX
    var lb = document.getElementById("lb-img");
    lb.innerHTML = "";
    lb.appendChild(clone);
  
    // (C) SHOW LIGHTBOX
    lb = document.getElementById("lb-back");
    lb.classList.add("show");
  };
  
  window.addEventListener("load", function(){
    // (D) ATTACH ON CLICK EVENTS TO ALL .ZOOMD IMAGES
    var images = document.getElementsByClassName("zoomD");
    if (images.length>0) {
      for (var img of images) {
        img.addEventListener("click", zoomImg);
      }
    }
  
    // (E) CLICK EVENT TO HIDE THE LIGHTBOX
    document.getElementById("lb-back").addEventListener("click", function(){
      this.classList.remove("show");
    })
  });