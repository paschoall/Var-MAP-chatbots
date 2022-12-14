const register = (name, username, password, email) => {
  const data = {
    name: name,
    username: username,
    password: password,
    email: email,
  }
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  }
  fetch('/user', requestOptions)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not OK');
      }
      console.log(response)
      return response.json()
    })
    .then(data => console.log(data))
    .catch((error) => {
      console.error('There has been a problem with your fetch operation:', error);
    });
};

const login = (token, user) => {
  localStorage.setItem('token', JSON.stringify(token))
  localStorage.setItem('user', JSON.stringify(user))
};

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
  };
  const AuthService = {
    register,
    login,
    logout,
  };

  export default AuthService;