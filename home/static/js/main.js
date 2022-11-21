// let body = document.body
// let toggle = document.querySelector('.toggle')
// let icon = document.querySelector('.fa-moon')
 


// function checkIcon(){
//   if(body.classList.contains('dark')){
//     icon.classList.add('fa-moon')
//     icon.classList.remove('fa-sun')
//   }else{
//     icon.classList.replace('fa-sun')
//     icon.classList.remove('fa-moon')
//   } 
// }

// checkIcon()

// toggle.onclick = () =>{
//   body.classList.toggle('dark')
//   setTimeout(()=>{
//     checkIcon()
//   },100)
// }

let body = document.body
let toggle = document.querySelector('.toggle')
let icon = document.querySelector('.fa-sun')
let icon2 = document.querySelector('.fa-moon')

toggle.onclick = () =>{
  body.classList.toggle('dark')
  if(body.classList.contains('dark')){
  icon.classList.replace('fa-sun', 'fa-moon')

  }else{
    icon.classList.replace('fa-moon', 'fa-sun')
  }
}