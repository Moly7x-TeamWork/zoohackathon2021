import axios from 'axios'

/**
 *
 * @param { function } commit
 * @param params
 * @param { string } data
 */

export function getTagList({ commit, state }, params) {
  return axios.get(`/test`, { params })
}
