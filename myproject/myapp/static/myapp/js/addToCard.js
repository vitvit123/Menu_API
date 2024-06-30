let cart = document.querySelector('.cart');

document.querySelector('#cart-icon').onclick = () =>{
  cart.classList.add('active');
}
document.querySelector('#close-icon').onclick = () =>{
  cart.classList.remove('active');
}
document.querySelector('.buy-btn').onclick = () =>{
  alert('Ordered');
}