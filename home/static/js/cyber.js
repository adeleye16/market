let signup = document.form
let username = document.form.username
let fname = document.form.firstname
let lname = document.form.lastname
let email = document.form.email
let state = document.form.state
let phone = document.form.phone
let address = document.form.address
let password = document.form.password

console.log(fname)
let validate = () =>{
  if(username.value.length <=0){
    alert('Please,supply Username');
    username.focus()
    return form;
  }

  if(fname.value.length <=0){
    alert('Please,supply First name');
    fname.focus()
    return form;
  }

  if(lname.value.length <=0){
    alert('Please,supply last name');
    lname.focus()
    return form;
  }

  if(email.value.length <=0){
    alert('Please,supply email');
    email.focus()
    return form;
  }

  if(state.value.length <=0){
    alert('Please,supply state');
    state.focus()
    return form;
  }

  if(phone.value.length <=0){
    alert('Please,supply Phone Number');
    phone.focus()
    return form;
  }

  if(address.value.length <=0){
    alert('Please,supply Home Address');
    address.focus()
    return form;
  }

  if(password.value.length <=0){
    alert('Please,supply password');
    username.focus()
    return form;
  }
}
