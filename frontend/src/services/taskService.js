import { authHeader } from '../helpers/auth-header';
import { userService } from '.';

export const taskService = {
    fetchTasks,
    updateTask,
    addTask
};

function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);

        if (!response.ok) {
            if (response.status === 401) {
                userService.logout();
                location.reload(true);
            }
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }
        return data;
    });
}

function handleAddResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);

        if (!response.ok) {
            if (response.status === 401) {
                userService.logout();
                location.reload(true);
            }
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }
        return response;
    });
}

function fetchTasks() {
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };
    return fetch(`http://localhost:8000/todos`, requestOptions).then(handleResponse);
}

function updateTask(id) {
    const requestOptions = {
        method: 'PUT',
        headers: authHeader()
    };
    return fetch(`http://localhost:8000/todos/${id}`, requestOptions).then(handleResponse);
}

function addTask(payload) {
    const requestOptions = {
        method: 'POST',
        headers: authHeader(),
        body: JSON.stringify(payload)
    };
    return fetch(`http://localhost:8000/todos`, requestOptions).then(handleAddResponse);
}