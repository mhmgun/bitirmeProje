window.onload = function() {
    setTimeout(function() {
        var merhaba = document.getElementById('merhaba');
        merhaba.style.opacity = 1;  // "Merhaba"yı görünür yapıyoruz
    }, 2000);  // 2 saniye sonra çalışacak
    setTimeout(function() {
        var aciklama = document.getElementById('aciklama');
        aciklama.style.opacity = 1;  // "Merhaba"yı görünür yapıyoruz
    }, 3000);  // 2 saniye sonra çalışacak

    setTimeout(function() {
        var buton = document.getElementById('butonEvet');
        
        buton.style.opacity = 1;  // "Merhaba"yı görünür yapıyoruz
    }, 4000);  // 2 saniye sonra çalışacak
        // Butona tıklanıldığında yeni yazıyı ekranda göster

    
    setTimeout(function() {
        var buton = document.getElementById('butonHayir');
            
        buton.style.opacity = 1;  // "Merhaba"yı görünür yapıyoruz
    }, 4000);  // 2 saniye sonra çalışacak
        // Butona tıklanıldığında yeni yazıyı ekranda göster
                 

};
