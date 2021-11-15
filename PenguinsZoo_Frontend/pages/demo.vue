<template>
    <div>
        <p class="text-lg text-red-500">Penguins Zoo hackathon 2021</p>
        <search-icon></search-icon>
    </div>
</template>

<script>
import SearchIcon from '~/static/searchIcon'
export default {
    components: { SearchIcon },
    data() {
        return {
            title: 'Penguins',
            infinite_key: '',
        }
    },
    head() {
        return {
            title: this.title,
            meta: [
                { hid: 'og-title', property: 'og:title', content: this.title },
            ],
        }
    },

    methods: {
        showData() {
            const self = this
            this.$store.state.loading = true
            this.$store
                .dispatch('demo/getTagList', self.$store.state.demo.query)
                .then((response) => {
                    self.$store.state.loading = false
                    if (response.data.data.length) {
                        // ++self.$store.state.demo.query.page
                        self.$store.commit('demo/ADD_DATA', response.data.data)
                    }
                })
                .catch((err) => {
                    this.$store.state.loading = false
                })
        },
    },

    mounted() {
        this.showData()
    },
}
</script>
