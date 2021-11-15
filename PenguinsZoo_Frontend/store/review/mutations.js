import {
    ADD_COMPLETED,
    ADD_REPORT,
    SET_REPORT,
    SET_COMPLETED,
    ADD_COUNT,
    DELETE_REPORT,
} from './mutation-types'
export default {
    /**
     *
     * @param state
     * @param { string } data
     */
    [SET_REPORT](state, { data }) {
        state.reports = data
    },

    [SET_COMPLETED](state, { data }) {
        state.completedReports = data
    },

    [ADD_REPORT](state, reports) {
        state.reports.push(...reports)
    },

    [ADD_COMPLETED](state, completed) {
        state.completedReports.push(...completed)
    },

    [ADD_COUNT](state, count) {
        state.completedTotal = count
    },

    [DELETE_REPORT](state, report_id) {
        state.reports = state.reports.filter((t) => t.reports.id !== report_id)
    },
}
