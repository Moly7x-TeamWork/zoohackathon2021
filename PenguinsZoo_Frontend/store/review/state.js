/** @var { demo } */
const STATE = {
    reports: [],
    completedReports: [],
    completedTotal: 0,
    waitingTotal: 0,
    query: {
        // page: 1,
    },
    statusReport: [
        { id: 0, label: 'Processing' },
        { id: 1, label: 'Waiting for review' },
        { id: 2, label: 'Accepted' },
        { id: 3, label: 'Denied' },
    ],

    stats: [
        { id: 1, label: '1B' },
        { id: 2, label: '2B' },
        { id: 2, label: 'Others' },
    ],
}

export default STATE
