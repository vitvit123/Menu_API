let cart = document.querySelector('.cart');
$("#cart-icon").on("clcik",()=>{
  alert("hii");
})
document.querySelector('#cart-icon').onclick = () =>{

  cart.classList.add('active');
}
document.querySelector('#close-icon').onclick = () =>{
  cart.classList.remove('active');
}
function notificationlength(){
  $.ajax({
      url: '{% url "myapp:get_notification_count" %}',
      data: obj,
      type: 'GET',
      success: function(response) {
          console.log("The length of notification is : ", response);
          console.log('Order placed successfully:', response);
      },
      error: function(xhr, status, error) {
          console.error('Error placing order:', error);
          // Handle error response as needed
      }
  });
}
notificationlength();