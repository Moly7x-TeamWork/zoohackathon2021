<template>
    <div>
        <Navbar></Navbar>
        <div
            class="pt-2 pb-5 my-5 h-full"
            v-for="report in $store.state.review.reports"
        >
            <ReviewDetail :report="report" :key="report.id"></ReviewDetail>
        </div>
        <Footer></Footer>
    </div>
</template>

<script>
import Navbar from '~/components/layouts/NavBar'
import Footer from '~/components/layouts/Footer'
import ReviewDetail from '~/components/ReviewDetail'
import Swal from 'sweetalert2'
export default {
    components: { ReviewDetail, Footer, Navbar },
    data() {
        return {
            title: 'Review reports',
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
                .dispatch('review/getPending')
                .then((response) => {
                    self.$store.state.loading = false
                    if (response.data.record.length) {
                        self.$store.commit(
                            'review/ADD_REPORT',
                            response.data.record
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
