// import { authHeader } from '../helpers/auth-header';
// import { getApiOrigin } from '../helpers/api-origin';

export const userService = {
    login,
    logout
};

function handleResponse(response) {
    return response.text().then(text => {
        console.log(response);
        const data = text && JSON.parse(text);

        if (!response.ok) {
            if (response.status === 401) {
                logout();
            }
            return Promise.reject(data, response.status);
        }
        return data;
    });
}

function login(name, password) {
    console.log(`login attempt`);
    const requestOptions = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + window.btoa(name + ':' + password)
        },
    };

    return fetch(`http://localhost:8000/login/`, requestOptions)
        .then(handleResponse)
        .then(user => {
            if (user) {
                user.authdata = window.btoa(name + ':' + password);
                localStorage.setItem('user', JSON.stringify(user));
            }
            return user;
        });
}

function logout() {
    console.log('logout')
    localStorage.removeItem('user');
}