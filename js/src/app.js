class User{
    constructor(name) {
        this.name = name
        this.password
    }

    welcome(){
        return `Welcome, ${this.name}`
    }
}

const user = new User("Kolozuz");

let welcome_msg = user.welcome()
let welcome_msg_dom = $("#welcome_msg")

welcome_msg_dom.replaceWith(welcome_msg);

// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
  
        form.classList.add('was-validated')
      }, false)
    })
  })()