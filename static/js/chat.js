console.log("Hello World");

window.onload = function () {
  document.querySelector("#btnMessage").addEventListener("click", sendMessage);
  document
    .querySelector("#inputMessage")
    .addEventListener("keyup", function (event) {
      if (event.keyCode === 13) {
        sendMessage();
      }
    });
  function sendMessage() {
    var messageInput = document.querySelector("#inputMessage");
    var message = messageInput.value.trim(); // Obtener el valor del mensaje

    // Definir una expresión regular para restringir caracteres no permitidos
    var regex = /^[a-zA-Z0-9\s.,!?]+$/; // Permitir solo letras, números y algunos caracteres

    // Validar el mensaje con la expresión regular
    if (!regex.test(message)) {
        alert("El mensaje contiene caracteres no permitidos.");
        return; // Salir de la función si hay caracteres no permitidos
    }

    // Cargar el mensaje en el DOM si es válido
    loadMessagesDOM(message); // Llama a la función para cargar el mensaje
    if (message !== "") {
        messageInput.value = ""; // Limpiar el campo de entrada
    }
  }
  function loadMessagesDOM(m) {
    const now = new Date();
    const date = now.toLocaleDateString(); // Formato de fecha
    const time = now.toLocaleTimeString(); // Formato de hora
    // Usar user como se define en home.html
    var displayName = user === user ? "Me" : user;

    document.querySelector("#boxMessages").innerHTML += `
    <div class="alert alert-dark" role="alert">
          ${m}
          <div>
            <small class="fst-italic fw-bold">${displayName}</small>
            <small class="float-end">${date} ${time}</small>
          </div>
        </div>`;
  }
};
