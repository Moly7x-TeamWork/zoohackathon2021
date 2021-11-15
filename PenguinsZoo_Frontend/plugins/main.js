import Vue from 'vue'
import VueTailwind from 'vue-tailwind'
Vue.use(VueTailwind)

import {
    TDatepicker,
    TSelect,
    TModal,
    TTextarea,
    TInput,
    TDropdown,
    TRichSelect,
} from 'vue-tailwind/dist/components'

Vue.component('t-datepicker', TDatepicker)
Vue.component('t-select', TSelect)
Vue.component('t-input', TInput)
Vue.component('t-modal', TModal)
Vue.component('t-textarea', TTextarea)
Vue.component('t-dropdown', TDropdown)
Vue.component('t-rich-select', TRichSelect)
