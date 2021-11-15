<template>
    <div>
        <Navbar></Navbar>
        <div class="w-full flex justify-end">
            <p class="mt-2 mr-5 font-semibold">
                Total: {{ $store.state.review.completedTotal }}
            </p>
        </div>
        <div
            class="pt-2 pb-5"
            v-for="completed in $store.state.review.completedReports"
        >
            <CompletedDetail
                :completed="completed"
                :key="completed.id"
            ></CompletedDetail>
        </div>
        <Footer></Footer>
    </div>
</template>
<script>
import Navbar from '~/components/layouts/NavBar'
import Footer from '~/components/layouts/Footer'
import CompletedDetail from '~/components/CompletedDetail'
export default {
    components: { CompletedDetail, Footer, Navbar },
    data() {
        return {
            title: 'Completed reports',
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
                .dispatch('review/getCompleted')
                .then((response) => {
                    console.log(response)
                    self.$store.state.loading = false
                    if (response.data.record.length) {
                        self.$store.commit(
                            'review/ADD_COMPLETED',
                            response.data.record
                        )
                        self.$store.commit(
                            'review/ADD_COUNT',
                            response.data.count
                        )
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
