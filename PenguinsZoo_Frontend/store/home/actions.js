import axios from 'axios'

/**
 *
 * @param { function } commit
 * @param params
 * @param { string } data
 */

export function addLinkGroup({ commit, state }, data) {
    return axios.post(`/addLinkGroup`, data)
}

export function login({ commit, state }, data) {
    return axios.post(`/login`, data)
}
