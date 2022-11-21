let change = document.querySelector('.grab')
let cyber = document.querySelector('.show')

change.addEventListener("click", () =>{
  change.classList.toggle('show')
  if(cyber.type === 'password'){
    cyber.type = 'text';
  }else{
    cyber.text = 'password';
  }

})