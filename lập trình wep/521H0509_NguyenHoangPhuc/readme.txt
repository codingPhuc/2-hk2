

### Task 1: HTML and CSS

1. Nội dung trang web bao gồm hình ảnh giơi thiệu  về mèo và nội dung liên quan tới méo với html 
2. Nút Show More để hiện thêm nội dung từ trang web
3. Phần chân trang (Footer) hiện thị các thông tin lần lượt về trang web, copyrights, và địa chỉ liên hệ cũng như các trang social media của hệ thống cửa hàng.

### Task 2: JavaScript
1. Ở trang Index.html, khi ấn vào nút "Show More" một đoạn thông tin mới sẽ được hiển thị trong trang. Sử dụng getElementByID để lấy được đối tượng và gán style.display = "none". Sau khi ấn nút set trạng thái thành "flex" để hiện thị nội dung và ngược lại. Điều này giúp đảm bảo thông tin được ẩn khi load trang web.
2. Ở trang about.html sử dụng     
    <scrip>
      window.addEventListener("beforeunload", function (event) {
        event.preventDefault();
        event.returnValue = "Do you really want to leave the page?";
      });
    </script>
3. Ở trang Index.html sử dụng  
    <script>
      function showMore() {
        var more = document.getElementById("more");
        more.style.display = "block";
        var button = document.getElementById("show-more");
        button.style.display = "none";
      }
    </script>
để phát hiện trang có ngừng load hay không và hiện thị ra cửa số thông báo người dùng, khi ấn leave là rời khỏi và cancel là ở lại. 