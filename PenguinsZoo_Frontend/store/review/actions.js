import axios from 'axios'

/**
 *
 * @param { function } commit
 * @param params
 * @param { string } data
 */

export function getPending({ commit, state }, params) {
    return axios.get(`/review`, { params })
}

export function getCompleted({ commit, state }, params) {
    return axios.get(`/completed`, { params })
}

export function changeStatus({ commit, state }, params) {
    return axios.post(`/changeStatus`, { params })
}
