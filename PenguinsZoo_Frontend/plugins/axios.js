import axios from 'axios'

axios.interceptors.request.use(
    function (config) {
        config.baseURL = process.env.NUXT_ENV_QC_BACKEND_URL
        return config
    },
    function (error) {
        return Promise.reject(error)
    }
)
