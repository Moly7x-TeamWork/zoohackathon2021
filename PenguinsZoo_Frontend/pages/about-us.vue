<template>
    <div>
        <Navbar></Navbar>
        <AboutUsDetail></AboutUsDetail>
        <Footer></Footer>
    </div>
</template>

<script>
import Navbar from '~/components/layouts/NavBar'
import Footer from '~/components/layouts/Footer'
import AboutUsDetail from '~/components/AboutUsDetail'
export default {
    components: { AboutUsDetail, Footer, Navbar },
    data() {
        return {
            title: 'About us',
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
}
</script>
