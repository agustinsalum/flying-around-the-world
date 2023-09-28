// https://jsonplaceholder.typicode.com/

fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  .then(json => {
    const userDataDiv = document.getElementById('userData');

    for (let user of json) {
      const userName = document.createElement('h3');
      userName.textContent = user.name;
      userDataDiv.appendChild(userName);
    }
  })
  .catch(error => {
    console.error('Error al obtener datos:', error);
  });
